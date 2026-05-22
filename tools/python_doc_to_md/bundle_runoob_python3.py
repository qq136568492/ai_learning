"""
聚合菜鸟教程 Python3 频道：从种子页侧边栏 #leftcolumn 收集 /python3/*.html，
逐页抓取正文并写入单一 Markdown（与 Sphinx bundle 不同，站点 DOM 独立实现）。

用法:
  python bundle_runoob_python3.py --seed https://www.runoob.com/python3/python3-tutorial.html \\
    -o ../../obsidian-vault/LLM_Learning/raw/runoob-python3-bundle.md --delay 1.0

注意: 请遵守 runoob.com robots.txt 与版权；仅作个人学习归档，控制频率。
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse

from bs4 import BeautifulSoup

from fetch_python_doc import DEFAULT_UA, fetch_html, html_to_md


def normalize_url(u: str) -> str:
    p = urlparse(u)
    return urlunparse(p._replace(fragment="", query=""))


def is_python3_page(u: str) -> bool:
    p = urlparse(u)
    if p.scheme not in ("http", "https"):
        return False
    host = p.netloc.lower()
    if host not in ("www.runoob.com", "runoob.com"):
        return False
    path = p.path.lower()
    if not path.startswith("/python3/"):
        return False
    if not path.endswith(".html"):
        return False
    return True


def discover_from_leftcolumn(seed_url: str, timeout: float) -> list[str]:
    html = fetch_html(seed_url, timeout=timeout)
    soup = BeautifulSoup(html, "html.parser")
    col = soup.select_one("#leftcolumn, [id=leftcolumn]")
    if col is None:
        raise SystemExit("未找到侧边栏 #leftcolumn，页面结构可能已变更")
    base = normalize_url(seed_url)
    ordered: list[str] = []
    seen: set[str] = set()
    for a in col.find_all("a", href=True):
        raw = a["href"].strip()
        if not raw or raw.startswith("#") or raw.lower().startswith("javascript:"):
            continue
        full = normalize_url(urljoin(base, raw))
        if not is_python3_page(full):
            continue
        if full in seen:
            continue
        seen.add(full)
        ordered.append(full)
    if not ordered:
        raise SystemExit("侧边栏未发现任何 /python3/*.html 链接")
    return ordered


def find_article_root(soup: BeautifulSoup):
    for sel in ("#content", ".article-body", "[role=main]", "article"):
        n = soup.select_one(sel)
        if n:
            return n
    return soup.body


def extract_article_html(soup: BeautifulSoup) -> str:
    root = find_article_root(soup)
    frag = BeautifulSoup(str(root), "html.parser")
    for bad in frag.select("script, style, iframe, .google-auto-placed, ins.adsbygoogle"):
        bad.decompose()
    return str(frag)


def bundle(seed_url: str, output: Path, delay: float, timeout: float, max_pages: int) -> None:
    seed_norm = normalize_url(seed_url)
    if not is_python3_page(seed_norm):
        raise SystemExit("种子须为 https://www.runoob.com/python3/ 下的 .html")

    urls = discover_from_leftcolumn(seed_norm, timeout=timeout)
    if seed_norm not in urls:
        urls.insert(0, seed_norm)
    else:
        urls.remove(seed_norm)
        urls.insert(0, seed_norm)

    if len(urls) > max_pages:
        urls = urls[:max_pages]

    parts: list[str] = []
    quoted = lambda u: '"' + u.replace('"', '\\"') + '"'
    head_urls = "\n".join(f"  - {quoted(u)}" for u in urls)
    parts.append(
        "---\n"
        f'title: "Runoob Python3 教程（聚合）"\n'
        f"seed_url: {quoted(seed_norm)}\n"
        f"page_count: {len(urls)}\n"
        f"source_site: https://www.runoob.com\n"
        f"urls:\n{head_urls}\n"
        "---\n\n"
    )
    parts.append(
        f"# Runoob Python3 教程聚合\n\n"
        f"**Seed:** `{seed_norm}`  \n"
        f"**Pages:** {len(urls)}（来自左侧导航）\n\n---\n\n"
    )

    for i, url in enumerate(urls):
        if i > 0 and delay > 0:
            time.sleep(delay)
        body = fetch_html(url, timeout=timeout)
        soup = BeautifulSoup(body, "html.parser")
        title_txt = ""
        if soup.title and soup.title.string:
            title_txt = soup.title.string.replace("¶", "").strip()
            for sep in (" | ", " — ", " - "):
                if sep in title_txt:
                    title_txt = title_txt.split(sep)[0].strip()
                    break
        md = html_to_md(extract_article_html(soup))
        h = title_txt or url
        parts.append(f"## {h}\n\n**Source:** [{url}]({url})\n\n{md}\n\n---\n\n")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {len(urls)} pages -> {output.resolve()}")
    print("User-Agent:", DEFAULT_UA)


def main():
    ap = argparse.ArgumentParser(description="Runoob Python3 多页聚合为 Markdown")
    ap.add_argument("--seed", required=True, help="例如 https://www.runoob.com/python3/python3-tutorial.html")
    ap.add_argument("-o", "--output", default="runoob_python3_bundle.md")
    ap.add_argument("--delay", type=float, default=1.0)
    ap.add_argument("--timeout", type=float, default=45.0)
    ap.add_argument("--max-pages", type=int, default=120)
    args = ap.parse_args()
    bundle(args.seed, Path(args.output), args.delay, args.timeout, args.max_pages)


if __name__ == "__main__":
    main()
