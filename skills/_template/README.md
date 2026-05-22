# 技能子工程模板

复制本文件夹到 `skills/<新技能名>` 后：

1. 重命名 `src/skill_template` 为实际包名（如 `python_basics`）。
2. 修改本目录下 `pyproject.toml` 的 `name`、`description`。
3. `python -m venv .venv` 并 `pip install -e ".[dev]"`。
4. 在 `notebooks/` 做实验，在 `src/` 写可复用代码，在 `tests/` 写小测验。
