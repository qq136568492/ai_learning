#!/usr/bin/env python3
"""Strip notebook *.py implementations: skeleton + `pass` (or trivial yield stubs); keeps __main__ asserts."""

from __future__ import annotations

import ast
import sys
from pathlib import Path


def _doc_or_empty(body: list[ast.stmt]) -> tuple[list[ast.stmt], list[ast.stmt]]:
    if body and isinstance(body[0], ast.Expr):
        ev = body[0].value
        if isinstance(ev, ast.Constant) and isinstance(ev.value, str):
            return body[:1], body[1:]
    return [], body


def _is_expr_string(stmt: ast.stmt) -> bool:
    """Module/class/function standalone string literal stmt (typically docstring)."""
    return bool(_doc_or_empty([stmt])[0])


def _has_yield(body: list[ast.stmt]) -> bool:
    class V(ast.NodeVisitor):
        """Ignore nested defs while scanning yields (those are stubs below)."""

        def __init__(self) -> None:
            self.found = False

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            return

        visit_AsyncFunctionDef = (
            lambda self, node: None
        )  # noqa: ARG005
        visit_ClassDef = lambda self, node: None

        visit_Lambda = lambda self, node: None

        def visit_Yield(self, _node: ast.Yield) -> None:
            self.found = True

        def visit_YieldFrom(self, _node: ast.YieldFrom) -> None:
            self.found = True

    v = V()
    v.visit(ast.Module(body=list(body), type_ignores=[]))
    return v.found


def _stub_leaf(sync: bool, body: list[ast.stmt], doc_prefix: list[ast.stmt]) -> list[ast.stmt]:
    if _has_yield(body):
        if sync:
            return doc_prefix + [
                ast.Expr(value=ast.YieldFrom(value=ast.Tuple(elts=[], ctx=ast.Load()))),
            ]
        return doc_prefix + [
            ast.If(
                test=ast.Constant(value=False),
                body=[
                    ast.Expr(value=ast.Yield(value=ast.Constant(value=None))),
                ],
                orelse=[],
            ),
        ]
    return doc_prefix + [ast.Pass()]


def stub_function_like(f: ast.FunctionDef) -> None:
    doc_prefix, sans_doc = _doc_or_empty(f.body)
    defs_here = (
        isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) for s in sans_doc
    )
    if not any(defs_here):
        f.body = _stub_leaf(True, sans_doc, doc_prefix)
        return
    nb: list[ast.stmt] = []
    for stmt in sans_doc:
        if isinstance(stmt, ast.FunctionDef):
            stub_function_like(stmt)
            nb.append(stmt)
        elif isinstance(stmt, ast.AsyncFunctionDef):
            stub_async_like(stmt)
            nb.append(stmt)
        elif isinstance(stmt, ast.ClassDef):
            stub_class_like(stmt)
            nb.append(stmt)
        else:
            nb.append(ast.Pass())
    f.body = doc_prefix + nb


def stub_async_like(f: ast.AsyncFunctionDef) -> None:
    doc_prefix, sans_doc = _doc_or_empty(f.body)
    if not any(isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) for s in sans_doc):
        f.body = _stub_leaf(False, sans_doc, doc_prefix)
        return
    nb: list[ast.stmt] = []
    for stmt in sans_doc:
        if isinstance(stmt, ast.FunctionDef):
            stub_function_like(stmt)
            nb.append(stmt)
        elif isinstance(stmt, ast.AsyncFunctionDef):
            stub_async_like(stmt)
            nb.append(stmt)
        elif isinstance(stmt, ast.ClassDef):
            stub_class_like(stmt)
            nb.append(stmt)
        else:
            nb.append(ast.Pass())
    f.body = doc_prefix + nb


def stub_class_like(c: ast.ClassDef) -> None:
    nb: list[ast.stmt] = []
    for stmt in c.body:
        if isinstance(stmt, ast.FunctionDef):
            stub_function_like(stmt)
            nb.append(stmt)
        elif isinstance(stmt, ast.AsyncFunctionDef):
            stub_async_like(stmt)
            nb.append(stmt)
        elif isinstance(stmt, (ast.AnnAssign, ast.Assign, ast.Pass)):
            nb.append(stmt)
        elif _is_expr_string(stmt):
            nb.append(stmt)
        else:
            nb.append(ast.Pass())
    c.body = nb


def stub_block(body: list[ast.stmt]) -> None:
    for stmt in body:
        if isinstance(stmt, ast.FunctionDef):
            stub_function_like(stmt)
        elif isinstance(stmt, ast.AsyncFunctionDef):
            stub_async_like(stmt)
        elif isinstance(stmt, ast.ClassDef):
            stub_class_like(stmt)
        elif isinstance(stmt, ast.If):
            stub_block(stmt.body)
            stub_block(stmt.orelse)
        elif isinstance(stmt, ast.With):
            stub_block(stmt.body)
        elif isinstance(stmt, ast.For):
            stub_block(stmt.body)
            stub_block(stmt.orelse)
        elif isinstance(stmt, ast.AsyncFor):
            stub_block(stmt.body)
            stub_block(stmt.orelse)
        elif isinstance(stmt, ast.While):
            stub_block(stmt.body)
            stub_block(stmt.orelse)
        elif isinstance(stmt, ast.Try):
            stub_block(stmt.body)
            for h in stmt.handlers:
                stub_block(h.body)
            stub_block(stmt.orelse)
            stub_block(stmt.finalbody)
        elif isinstance(stmt, ast.Match):
            for case in stmt.cases:
                stub_block(case.body)


def main() -> None:
    root = Path(__file__).resolve().parents[1] / "notebooks"
    if not root.is_dir():
        sys.exit(f"missing notebooks: {root}")
    targets = sorted(root.rglob("*.py"))
    for path in targets:
        src = path.read_text(encoding="utf-8")
        nl = "\r\n" if "\r\n" in src else "\n"
        tree = ast.parse(src)
        stub_block(tree.body)
        ast.fix_missing_locations(tree)
        out = ast.unparse(tree)
        if not out.endswith("\n"):
            out += "\n"
        pre = "# 练习时可先遮住实现自行编写。\n"
        if not out.startswith("# 练习时可先遮住"):
            out = pre + out
        path.write_text(out.replace("\n", nl), encoding="utf-8")
    print(f"stubbed {len(targets)} files under {root}")


if __name__ == "__main__":
    main()
