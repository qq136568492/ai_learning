"""
FastAPI 官方文档 Material/MkDocs 中文版「学习」区聚合：
从 https://fastapi.tiangolo.com/zh/learn/ 侧边栏解析链接，
选取学习相关路径（tutorial / advanced / deployment / how-to 等），排除 Reference 与站点其他一级栏目。

用法:
  python bundle_fastapi_zh_learn.py --seed https://fastapi.tiangolo.com/zh/learn/ \\
    -o obsidian-vault/LLM_Learning/raw/fastapi-learn-zh-bundle.md --delay 0.8
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path
from urllib.parse import urlparse, urljoin, urlunparse

from bs4 import BeautifulSoup

from fetch_python_doc import DEFAULT_UA, fetch_html, html_to_md


HOST = "fastapi.tiangolo.com"


def normalize_url(u: str) -> str:
    p = urlparse(u)
    return urlunparse(p._replace(fragment="", query=""))


def normalize_mkdocs_section(u: str) -> str:
    u = normalize_url(u).rstrip("/")
    p = urlparse(u)
    if not p.path or p.path.endswith("/"):
        return u + "/"
    last = p.path.rsplit("/", 1)[-1]
    if "." in last:
        return u
    return u + "/"


def path_in_learn_scope(path: str) -> bool:
    """与「学习」栏目一致：排除首页、特性、Reference、资源/关于等。"""
    p = "/" + path.strip("/").rstrip("/")
    if p == "/zh":
        return False
    prefixes = (
        "/zh/learn",
        "/zh/python-types",
        "/zh/async",
        "/zh/environment-variables",
        "/zh/virtual-environments",
        "/zh/tutorial",
        "/zh/advanced",
        "/zh/deployment",
        "/zh/how-to",
        "/zh/fastapi-cli",
        "/zh/editor-support",
    )
    for pre in prefixes:
        if p == pre or p.startswith(pre + "/"):
            return True
    return False


def discover_ordered_urls(seed_url: str, timeout: float) -> list[str]:
    seed = normalize_mkdocs_section(seed_url)
    sp = urlparse(seed).path.rstrip("/")
    if not sp.endswith("/learn") and not sp.endswith("/learn/index"):
        raise SystemExit("种子应为 FastAPI 中文「学习」入口，例如 …/zh/learn/")

    html = fetch_html(seed, timeout=timeout)
    soup = BeautifulSoup(html, "html.parser")
    nav = soup.select_one("nav.md-nav--primary")
    if nav is None:
        raise SystemExit("未找到 nav.md-nav--primary")

    ordered: list[str] = []
    seen: set[str] = set()
    for a in nav.find_all("a", href=True):
        fragment = a["href"].split("#")[0].strip()
        if not fragment or fragment.startswith(("mailto:", "javascript:")):
            continue
        full = normalize_mkdocs_section(urljoin(seed, fragment))
        pu = urlparse(full)
        if pu.scheme not in ("http", "https") or not pu.netloc.endswith(HOST):
            continue
        path_only = pu.path.rstrip("/") or "/"
        if not path_in_learn_scope(path_only):
            continue
        if full in seen:
            continue
        seen.add(full)
        ordered.append(full)

    if not ordered:
        raise SystemExit("未发现学习区链接，DOM 可能已变更")

    seed_norm = normalize_mkdocs_section(seed_url)
    if seed_norm in ordered:
        ordered.remove(seed_norm)
    ordered.insert(0, seed_norm)
    return ordered


def extract_main_html(soup: BeautifulSoup) -> str:
    inner = soup.select_one("[data-md-component=content] .md-typeset")
    if inner:
        frag = BeautifulSoup(str(inner), "html.parser")
    else:
        frag = BeautifulSoup(str(soup.select_one(".md-content__inner") or soup.body), "html.parser")
    for bad in frag.select("script, style, iframe, .md-source__repository"):
        bad.decompose()
    return str(frag)


def bundle(seed_url: str, output: Path, delay: float, timeout: float, max_pages: int) -> None:
    urls = discover_ordered_urls(seed_url, timeout=timeout)
    if len(urls) > max_pages:
        urls = urls[:max_pages]

    parts: list[str] = []
    q = lambda u: '"' + u.replace('"', '\\"') + '"'
    parts.append(
        "---\n"
        f'title: "FastAPI 中文学习区（聚合）"\n'
        f"seed_url: {q(normalize_url(seed_url))}\n"
        f"page_count: {len(urls)}\n"
        f"source_site: https://{HOST}\n"
        "urls:\n"
        + "\n".join(f"  - {q(u)}" for u in urls)
        + "\n"
        'generator_note: "mkdocs-material bundle (urllib + html2text)"\n'
        "---\n\n"
    )
    parts.append(
        "# FastAPI 中文「学习」聚合\n\n"
        f"**Seed:** `{normalize_url(seed_url)}`  \n"
        f"**Pages:** {len(urls)}\n\n"
        "（含教程、高级用户指南、部署、诀窍等；不含 Reference 整树。）\n\n---\n\n"
    )

    for i, url in enumerate(urls):
        if i > 0 and delay > 0:
            time.sleep(delay)
        html = fetch_html(url, timeout=timeout)
        soup = BeautifulSoup(html, "html.parser")
        title = ""
        if soup.title and soup.title.string:
            title = soup.title.string.replace("¶", "").strip()
            for sep in (" - ", " | ", " — "):
                if sep in title:
                    title = title.split(sep)[0].strip()
        md = html_to_md(extract_main_html(soup))
        h = title or url
        parts.append(f"## {h}\n\n**Source:** [{url}]({url})\n\n{md}\n\n---\n\n")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {len(urls)} pages -> {output.resolve()}")
    print("User-Agent:", DEFAULT_UA)


def main():
    ap = argparse.ArgumentParser(description="FastAPI zh learn section -> one Markdown")
    ap.add_argument("--seed", default="https://fastapi.tiangolo.com/zh/learn/")
    ap.add_argument("-o", "--output", default="fastapi_learn_zh_bundle.md")
    ap.add_argument("--delay", type=float, default=0.8)
    ap.add_argument("--timeout", type=float, default=45.0)
    ap.add_argument("--max-pages", type=int, default=200)
    args = ap.parse_args()
    bundle(args.seed, Path(args.output), args.delay, args.timeout, args.max_pages)


if __name__ == "__main__":
    main()
