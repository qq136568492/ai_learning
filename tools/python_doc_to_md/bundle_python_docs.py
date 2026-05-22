"""
从 Sphinx 索引页（如 Python 教程 index.html）发现同目录下子页面，
逐页抓取主内容并合并为一个 Markdown。

与 fetch_python_doc.py 共用 HTML→Markdown 管道；可直接由 Agent / Skill 调用。

用法:
  python bundle_python_docs.py --seed https://docs.python.org/zh-cn/3.11/tutorial/index.html \\
    -o ./python-tutorial-zh-311.md --delay 0.8 --recurse
"""

from __future__ import annotations

import argparse
import posixpath
import time
from pathlib import Path
from urllib.parse import urlparse, urljoin, urlunparse

from bs4 import BeautifulSoup

# 同目录下作为脚本运行
from fetch_python_doc import (
    DEFAULT_UA,
    fetch_html,
    find_main_fragment,
    html_to_md,
)


def normalize_page_url(page_url: str) -> str:
    p = urlparse(page_url)
    return urlunparse(p._replace(fragment="", query=""))


def path_dir_and_prefix(seed_url: str) -> tuple[urlparse, str]:
    p = urlparse(normalize_page_url(seed_url))
    path = p.path.rstrip("/")
    if posixpath.basename(path).endswith(".html"):
        dirpath = posixpath.dirname(path)
    elif path.endswith("tutorial"):  # 罕见：无文件名
        dirpath = path
    else:
        dirpath = path
    prefix = dirpath.rstrip("/") + "/"
    return p, prefix


def in_scope(candidate: urlparse, netloc: str, prefix: str) -> bool:
    if candidate.netloc != netloc:
        return False
    if not candidate.path.startswith(prefix):
        return False
    if not candidate.path.endswith(".html"):
        return False
    return True


def discover_urls_from_html(main_html_fragment: BeautifulSoup, base_url: str, netloc: str, prefix: str) -> list[str]:
    ordered: list[str] = []
    seen: set[str] = set()
    for a in main_html_fragment.find_all("a", href=True):
        full = normalize_page_url(urljoin(base_url, a["href"]))
        pu = urlparse(full)
        if not in_scope(pu, netloc, prefix):
            continue
        if full in seen:
            continue
        seen.add(full)
        ordered.append(full)
    return ordered


def clone_main_strip_index_toc(main_tag) -> BeautifulSoup:
    """索引页克隆后去掉 Sphinx toctree，避免与子页全文重复。"""
    frag = BeautifulSoup(str(main_tag), "html.parser")
    for sel in (".toctree-wrapper", ".toctree", '[class*="toctree"]'):
        for el in frag.select(sel):
            el.decompose()
    return frag


def clean_doc_title(raw: str | None) -> str:
    if not raw:
        return ""
    t = raw.replace("¶", "").strip()
    for sep in (" — ", " - ", " – "):
        if sep in t:
            return t.split(sep)[0].strip()
    return t


def harvest_links_from_network_page(url: str, netloc: str, prefix: str, timeout: float) -> list[str]:
    try:
        html = fetch_html(url, timeout=timeout)
    except Exception as e:
        print(f"[warn] link discovery skipped {url}: {e}")
        return []
    soup = BeautifulSoup(html, "html.parser")
    main = find_main_fragment(soup)
    base = normalize_page_url(url)
    return discover_urls_from_html(main, base, netloc, prefix)


def bundle(
    seed_url: str,
    output: str,
    delay: float,
    recurse: bool,
    timeout: float,
    max_pages: int,
) -> None:
    seed_norm = normalize_page_url(seed_url)
    pu_seed, prefix = path_dir_and_prefix(seed_norm)

    collected: list[str] = []

    seed_main_html = fetch_html(seed_norm, timeout=timeout)
    seed_soup = BeautifulSoup(seed_main_html, "html.parser")
    seed_main = find_main_fragment(seed_soup)
    discovered = discover_urls_from_html(seed_main, seed_norm, pu_seed.netloc, prefix)

    if recurse:
        seen: set[str] = set(discovered + [seed_norm])
        frontier = list(discovered)
        while frontier and len(seen) < max_pages:
            u = frontier.pop(0)
            new_links = harvest_links_from_network_page(u, pu_seed.netloc, prefix, timeout)
            time.sleep(delay)
            for ln in new_links:
                if ln not in seen:
                    seen.add(ln)
                    discovered.append(ln)
                    frontier.append(ln)
                    if len(seen) >= max_pages:
                        break

    # seed 永远排首位
    if seed_norm not in discovered:
        collected = [seed_norm] + [u for u in discovered if u != seed_norm]
    else:
        collected = [seed_norm] + [u for u in discovered if u != seed_norm]

    # 裁剪 max_pages（保留 seed）
    extra = collected[1 : max_pages] if len(collected) > max_pages else collected[1:]
    collected = [collected[0]] + extra

    parts: list[str] = []

    quoted = lambda u: '"' + u.replace('"', '\\"') + '"'
    yaml_urls = "\n".join(f"  - {quoted(u)}" for u in collected)
    meta_seed = quoted(seed_norm)
    header = (
        "---\n"
        f'title: "Aggregated docs (bundle)"\n'
        f"seed_url: {meta_seed}\n"
        f"page_count: {len(collected)}\n"
        f"urls:\n{yaml_urls}\n"
        f'generator_note: "sphinx-html-bundle (urllib + html2text)"\n'
        "---\n\n"
    )
    parts.append(header)
    parts.append(f"# Aggregated bundle\n\n**Seed:** `{seed_norm}`  \n**Pages merged:** {len(collected)}\n\n---\n\n")

    for i, url in enumerate(collected):
        if i > 0 and delay > 0:
            time.sleep(delay)
        try:
            html = fetch_html(url, timeout=timeout)
        except Exception as e:
            print(f"[warn] fetch failed {url}: {e}")
            parts.append(
                f"## （抓取失败）\n\n"
                f"**Source:** [{url}]({url})\n\n"
                f"```text\n{e!r}\n```\n\n---\n\n"
            )
            continue
        soup = BeautifulSoup(html, "html.parser")
        raw_title = soup.title.string.strip() if soup.title and soup.title.string else ""
        title = clean_doc_title(raw_title) or url
        main = find_main_fragment(soup)
        if normalize_page_url(url) == seed_norm and urlparse(url).path.lower().endswith("index.html"):
            fragment = clone_main_strip_index_toc(main)
        else:
            fragment = BeautifulSoup(str(main), "html.parser")

        md_body = html_to_md(str(fragment))
        parts.append(f"## {title}\n\n**Source:** [{url}]({url})\n\n{md_body}\n\n---\n\n")

    outp = Path(output)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {len(collected)} pages -> {outp.resolve()}")
    print("User-Agent:", DEFAULT_UA)


def main():
    ap = argparse.ArgumentParser(description="Bundle Sphinx sibling .html pages into one Markdown.")
    ap.add_argument("--seed", required=True, help="索引页或教程起始 URL（如 .../tutorial/index.html）")
    ap.add_argument("-o", "--output", default="python_docs_bundle.md", help="输出 Markdown 路径")
    ap.add_argument("--delay", type=float, default=0.75, help="请求间隔秒数（礼貌爬虫）")
    ap.add_argument(
        "--recurse",
        action="store_true",
        help="在子页主内容区内继续发现并合并同前缀页面（较慢，覆盖侧栏中出现的链接页面）",
    )
    ap.add_argument("--timeout", type=float, default=45.0)
    ap.add_argument("--max-pages", type=int, default=80, help="上限页数（含首页）以防失控")
    args = ap.parse_args()
    bundle(args.seed, args.output, args.delay, args.recurse, args.timeout, args.max_pages)


if __name__ == "__main__":
    main()
