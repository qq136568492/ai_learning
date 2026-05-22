#!/usr/bin/env python3
"""Small local helper for searching and recording Obsidian Q&A context."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


MAIN_VAULT = Path("D:/Obsidian/repository/Obsidian Vault")
SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".obsidian",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
}


@dataclass
class Hit:
    path: Path
    title: str
    score: float
    snippets: list[str]


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
        except OSError:
            return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def unique_paths(paths: Iterable[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []
    for path in paths:
        try:
            resolved = path.expanduser().resolve()
        except OSError:
            resolved = path.expanduser().absolute()
        key = str(resolved).lower()
        if key not in seen and resolved.exists():
            seen.add(key)
            result.append(resolved)
    return result


def workspace_candidates(workspace: str | None) -> list[Path]:
    starts: list[Path] = []
    if workspace:
        starts.append(Path(workspace))
    starts.append(Path.cwd())

    candidates: list[Path] = []
    for start in starts:
        try:
            current = start.expanduser().resolve()
        except OSError:
            current = start.expanduser().absolute()
        for parent in (current, *current.parents):
            portable = parent / "obsidian-vault" / "LLM_Learning"
            candidates.extend([portable / "wiki", portable / "raw"])
    return candidates


def search_roots(workspace: str | None, extra_roots: list[str] | None = None) -> list[Path]:
    roots: list[Path] = []
    if os.environ.get("OBSIDIAN_VAULT"):
        roots.append(Path(os.environ["OBSIDIAN_VAULT"]))
    roots.extend(
        [
            MAIN_VAULT / "llm-wiki",
            MAIN_VAULT / "LLM_Learning" / "wiki",
            MAIN_VAULT / "LLM_Learning" / "raw",
        ]
    )
    roots.extend(workspace_candidates(workspace))
    if extra_roots:
        roots.extend(Path(root) for root in extra_roots)
    return unique_paths(roots)


def markdown_files(roots: Iterable[Path], max_files: int) -> Iterable[Path]:
    count = 0
    for root in roots:
        if root.is_file() and root.suffix.lower() == ".md":
            yield root
            count += 1
            continue
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
            for filename in filenames:
                if not filename.lower().endswith(".md"):
                    continue
                yield Path(dirpath) / filename
                count += 1
                if count >= max_files:
                    return


def query_terms(query: str) -> list[str]:
    lowered = query.lower()
    terms: list[str] = []
    terms.extend(re.findall(r"[a-z0-9_][a-z0-9_.-]{1,}", lowered))
    for chunk in re.findall(r"[\u4e00-\u9fff]{2,}", query):
        terms.append(chunk)
        terms.extend(chunk[i : i + 2] for i in range(len(chunk) - 1))
    if not terms:
        terms.extend(token for token in re.split(r"\s+", lowered) if token)

    seen: set[str] = set()
    result: list[str] = []
    for term in terms:
        if term not in seen:
            seen.add(term)
            result.append(term)
    return result


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines()[:40]:
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback
    return fallback


def score_file(path: Path, text: str, terms: list[str]) -> float:
    haystack = text.lower()
    path_text = str(path).lower()
    name_text = path.stem.lower()
    score = 0.0
    for term in terms:
        count = haystack.count(term.lower())
        if count:
            score += min(count, 20)
        if term.lower() in name_text:
            score += 12
        if term.lower() in path_text:
            score += 6
    return score


def make_snippets(text: str, terms: list[str], max_snippets: int = 2) -> list[str]:
    lines = text.splitlines()
    matches: list[int] = []
    lowered_lines = [line.lower() for line in lines]
    for index, line in enumerate(lowered_lines):
        if any(term.lower() in line for term in terms):
            matches.append(index)
        if len(matches) >= max_snippets:
            break

    snippets: list[str] = []
    for index in matches:
        start = max(0, index - 1)
        end = min(len(lines), index + 2)
        snippet = "\n".join(line.strip() for line in lines[start:end] if line.strip())
        if len(snippet) > 700:
            snippet = snippet[:697] + "..."
        snippets.append(snippet)
    return snippets


def search(query: str, roots: list[Path], limit: int, max_files: int) -> list[Hit]:
    terms = query_terms(query)
    hits: list[Hit] = []
    for path in markdown_files(roots, max_files=max_files):
        text = read_text(path)
        if not text:
            continue
        score = score_file(path, text, terms)
        if score <= 0:
            continue
        hits.append(
            Hit(
                path=path,
                title=first_heading(text, path.stem),
                score=score,
                snippets=make_snippets(text, terms),
            )
        )
    hits.sort(key=lambda hit: (-hit.score, str(hit.path).lower()))
    return hits[:limit]


def print_search_markdown(query: str, roots: list[Path], hits: list[Hit]) -> None:
    print("# Obsidian Search Results")
    print(f"Query: {query}")
    print("\nRoots searched:")
    for root in roots:
        print(f"- {root}")
    if not hits:
        print("\nNo relevant Markdown hits found.")
        return
    for index, hit in enumerate(hits, start=1):
        print(f"\n## {index}. {hit.title}")
        print(f"- Path: {hit.path}")
        print(f"- Score: {hit.score:.1f}")
        if hit.snippets:
            print("- Snippets:")
            for snippet in hit.snippets:
                print("  - " + snippet.replace("\n", "\n    "))


def writable_wiki_dir(workspace: str | None, preferred: str | None = None) -> Path:
    candidates: list[Path] = []
    if preferred:
        candidates.append(Path(preferred))
    if os.environ.get("OBSIDIAN_WIKI_DIR"):
        candidates.append(Path(os.environ["OBSIDIAN_WIKI_DIR"]))
    candidates.append(MAIN_VAULT / "llm-wiki")
    for candidate in workspace_candidates(workspace):
        if candidate.name.lower() == "wiki" and candidate.parent.name == "LLM_Learning":
            candidates.append(candidate)

    for candidate in unique_or_new_paths(candidates):
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            test = candidate / ".codex_write_test"
            test.write_text("ok", encoding="utf-8")
            test.unlink(missing_ok=True)
            return candidate
        except OSError:
            continue
    raise RuntimeError("No writable Obsidian wiki directory found.")


def unique_or_new_paths(paths: Iterable[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []
    for path in paths:
        try:
            resolved = path.expanduser().resolve(strict=False)
        except OSError:
            resolved = path.expanduser().absolute()
        key = str(resolved).lower()
        if key not in seen:
            seen.add(key)
            result.append(resolved)
    return result


def bullet_list(items: list[str]) -> str:
    if not items:
        return "  - None"
    return "\n".join(f"  - {item}" for item in items)


def append_record(
    wiki_dir: Path,
    question: str,
    summary: str,
    context: str,
    hits: list[str],
    references: list[str],
) -> tuple[Path, Path]:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    qa_path = wiki_dir / "qa-records.md"
    log_path = wiki_dir / "log.md"
    qa_record = (
        f"\n## [{timestamp}] Q: {question}\n"
        f"- Context: {context}\n"
        "- Hits:\n"
        f"{bullet_list(hits)}\n"
        f"- Answer-Summary: {summary}\n"
        "- References:\n"
        f"{bullet_list(references)}\n"
    )
    log_summary = " ".join(summary.split())
    if len(log_summary) > 240:
        log_summary = log_summary[:237] + "..."
    log_record = f"- [{timestamp}] {context}: {question} -> {log_summary}\n"

    if not qa_path.exists():
        qa_path.write_text("# Q&A Records\n", encoding="utf-8")
    if not log_path.exists():
        log_path.write_text("# LLM Wiki Log\n", encoding="utf-8")
    with qa_path.open("a", encoding="utf-8") as handle:
        handle.write(qa_record)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(log_record)
    return qa_path, log_path


def cmd_search(args: argparse.Namespace) -> int:
    roots = search_roots(args.workspace, args.root)
    hits = search(args.query, roots, limit=args.limit, max_files=args.max_files)
    if args.json:
        payload = {
            "query": args.query,
            "roots": [str(root) for root in roots],
            "hits": [
                {
                    "path": str(hit.path),
                    "title": hit.title,
                    "score": hit.score,
                    "snippets": hit.snippets,
                }
                for hit in hits
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_search_markdown(args.query, roots, hits)
    return 0


def cmd_record(args: argparse.Namespace) -> int:
    wiki_dir = writable_wiki_dir(args.workspace, args.wiki_dir)
    qa_path, log_path = append_record(
        wiki_dir=wiki_dir,
        question=args.question,
        summary=args.summary,
        context=args.context,
        hits=args.hits or [],
        references=args.references or [],
    )
    print(f"Recorded Q&A to: {qa_path}")
    print(f"Recorded log to: {log_path}")
    return 0


def cmd_paths(args: argparse.Namespace) -> int:
    print("Search roots:")
    for root in search_roots(args.workspace, args.root):
        print(f"- {root}")
    try:
        print(f"Writable wiki dir: {writable_wiki_dir(args.workspace, args.wiki_dir)}")
    except RuntimeError as exc:
        print(f"Writable wiki dir: unavailable ({exc})")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search and record Obsidian knowledge-base context.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    search_parser = subparsers.add_parser("search", help="Search local Obsidian Markdown notes.")
    search_parser.add_argument("--query", required=True)
    search_parser.add_argument("--limit", type=int, default=8)
    search_parser.add_argument("--workspace", default=None)
    search_parser.add_argument("--root", action="append", default=[])
    search_parser.add_argument("--max-files", type=int, default=5000)
    search_parser.add_argument("--json", action="store_true")
    search_parser.set_defaults(func=cmd_search)

    record_parser = subparsers.add_parser("record", help="Append a Q&A record and log entry.")
    record_parser.add_argument("--question", required=True)
    record_parser.add_argument("--summary", required=True)
    record_parser.add_argument("--context", default="Obsidian knowledge bridge")
    record_parser.add_argument("--hits", action="append", default=[])
    record_parser.add_argument("--references", action="append", default=[])
    record_parser.add_argument("--workspace", default=None)
    record_parser.add_argument("--wiki-dir", default=None)
    record_parser.set_defaults(func=cmd_record)

    paths_parser = subparsers.add_parser("paths", help="Show resolved search and write-back paths.")
    paths_parser.add_argument("--workspace", default=None)
    paths_parser.add_argument("--root", action="append", default=[])
    paths_parser.add_argument("--wiki-dir", default=None)
    paths_parser.set_defaults(func=cmd_paths)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:  # noqa: BLE001 - command-line helper should report compact failures.
        print(f"obsidian_bridge.py: error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
