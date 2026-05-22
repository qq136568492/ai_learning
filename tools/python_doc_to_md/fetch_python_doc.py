"""
从 Python 官方文档（Sphinx HTML）给定 URL 拉取正文并保存为 Markdown。

用法:
  pip install -r requirements.txt
  python fetch_python_doc.py "https://docs.python.org/zh-cn/3.11/tutorial/controlflow.html#documentation-strings" -o doc_section.md

说明:
  - 无锚点时导出整页主内容区域；有 #fragment 时尽量只导出对应 id（通常为 <section id="...">） subtree。
"""

from __future__ import annotations

import argparse
import re
import time
from html import unescape
from urllib.error import HTTPError, URLError
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import html2text
from bs4 import BeautifulSoup


DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36"
)


def fetch_html(url: str, timeout: float = 30.0) -> str:
    """抓取 HTML。优先使用 requests（对大页面/chunked 更稳），否则 urllib 带重试。"""
    headers = {"User-Agent": DEFAULT_UA, "Accept-Language": "en-US,en;q=0.9"}
    read_timeout = max(float(timeout), 300.0)
    connect_timeout = min(30.0, read_timeout)

    try:
        import requests
        from requests.exceptions import (
            ChunkedEncodingError,
            ConnectionError as RequestsConnectionError,
            ReadTimeout,
            Timeout as RequestsTimeout,
        )
    except ImportError:
        requests = None

    if requests is not None:
        retryable = (ReadTimeout, RequestsTimeout, RequestsConnectionError, ChunkedEncodingError)
        last_exc: BaseException | None = None
        for attempt in range(6):
            try:
                r = requests.get(
                    url,
                    headers=headers,
                    timeout=(connect_timeout, read_timeout),
                )
                r.raise_for_status()
                if r.encoding is None:
                    r.encoding = r.apparent_encoding or "utf-8"
                return r.text
            except retryable as e:
                last_exc = e
                time.sleep(2.0 * (attempt + 1))
        assert last_exc is not None
        raise last_exc

    last_err: BaseException | None = None
    for attempt in range(3):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=read_timeout) as resp:
                charset = resp.headers.get_content_charset() or "utf-8"
                return resp.read().decode(charset, errors="replace")
        except (TimeoutError, OSError, HTTPError, URLError) as e:
            last_err = e
            time.sleep(1.0 * (attempt + 1))
    assert last_err is not None
    raise last_err


def find_main_fragment(soup: BeautifulSoup):
    selectors = (
        '[role="main"]',
        "article.bd-article",
        "div.document",
        "div.body",
    )
    for sel in selectors:
        node = soup.select_one(sel)
        if node:
            return node
    return soup.body or soup


def subtree_for_anchor(main, fragment: str):
    fragment = fragment.strip()
    if not fragment:
        return None
    # Sphinx: id 常为 section；少数在 dl/dt/h2 的子节点上
    target = main.find(id=fragment)
    if target is None:
        return None
    sec = target.name == "section" and target or target.find_parent("section")
    return sec if sec is not None else target


def html_to_md(html: str) -> str:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0
    h.unicode_snob = True
    h.skip_internal_links = False
    md = h.handle(html).strip()
    # 去掉 Sphinx 残留的 ¶（段落跳转符）常见后缀
    md = re.sub(r"\s*¶\s*$", "", md, flags=re.MULTILINE)
    return md


def slug_title_from_fragment(fragment: str) -> str:
    return fragment.replace("-", " ").replace("_", " ")


def build_markdown(title: str, source_url: str, body_md: str) -> str:
    display_title = title or "Untitled"
    meta_title = escape_yaml_scalar(display_title)
    meta_source = escape_yaml_scalar(source_url)
    return (
        f"---\n"
        f'title: "{meta_title}"\n'
        f'source: "{meta_source}"\n'
        f"created: auto-export\n"
        f"---\n\n"
        f"# {display_title}\n\n"
        f"**Source:** [{source_url}]({source_url})\n\n"
        f"{body_md}\n"
    )


def escape_yaml_scalar(value: str) -> str:
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return value


def run(url: str, output: str, timeout: float) -> None:
    raw_url = url
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise SystemExit("请提供完整的 http(s) URL")

    strip_fragment_url = parsed._replace(fragment="").geturl()
    fragment = unescape(parsed.fragment or "")

    try:
        html = fetch_html(strip_fragment_url, timeout=timeout)
    except HTTPError as e:
        raise SystemExit(f"HTTP 错误 {e.code}: {e.reason}") from e
    except URLError as e:
        raise SystemExit(f"请求失败: {e.reason}") from e

    soup = BeautifulSoup(html, "html.parser")
    doc_title = ""
    title_tag = soup.title
    if title_tag and title_tag.string:
        doc_title = title_tag.string.strip()

    main = find_main_fragment(soup)
    subtree = subtree_for_anchor(main, fragment) if fragment else None
    slice_root = subtree if subtree is not None else main

    title = doc_title
    if fragment:
        # 小节标题可能比整页标题更贴切
        h = subtree.find(["h2", "h3", "h4"]) if subtree else None
        heading_text = h.get_text(" ", strip=True) if h else ""
        heading_text = re.sub(r"\s*¶.*$", "", heading_text).strip()
        title = heading_text or slug_title_from_fragment(fragment) or doc_title

    body_md = html_to_md(str(slice_root))
    mk = build_markdown(title or "Python Docs", raw_url, body_md)

    outp = Path(output)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(mk, encoding="utf-8")
    anchored = bool(fragment and subtree)
    scope = "锚点小节" if anchored else ("整页正文（未命中锚点，已导出主页区域）" if fragment else "整页正文")
    print(f"已写入 {outp.resolve()} （{scope}）")


def main():
    parser = argparse.ArgumentParser(description="Python 官方文档 HTML → Markdown")
    parser.add_argument("url", help="文档页面 URL（可含 #小节锚点）")
    parser.add_argument("-o", "--output", default="python_doc_export.md", help="输出 .md 路径")
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()
    run(args.url, args.output, args.timeout)


if __name__ == "__main__":
    main()
