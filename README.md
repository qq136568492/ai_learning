# Learning Project

按**技能 / 主题**划分子工程，每个子工程独立虚拟环境与依赖，避免不同课程互相污染。

**Cursor Skill（精准学习闭环）**：`.cursor/skills/ai-precision-learning/SKILL.md`。在聊天里发送**触发语**：`/精学流程 …`（快速）或 `/精学分步 …`（分步一问一答后再建 `skills/<名称>/`）。

## 目录约定

| 路径 | 说明 |
|------|------|
| `skills/_template/` | 新建技能时复制此文件夹 |
| `skills/<技能名>/` | 具体学习子工程（如 `python-basics`、`langchain`） |
| `learning/<学习项目名>/` | 可选：按「**学习项目**」组织的目录，内放**中文或英文子目录名**的进阶子工程（带 `pyproject`，独立 `venv`）。示例见 `learning/python-advanced-learning/`（子工程目录 `python进阶/`）。 |
| `practical/` | **仓库根**下与 `learning/` 同级，存放**实战 demo** 与小型项目。 |

## 新建一个技能子工程

1. 复制模板：`skills/_template` → `skills/<你的技能名>`
2. 在 `skills/<你的技能名>/` 内修改 `pyproject.toml` 里的 `name`、`description`
3. 将包目录 `src/skill_template/` 重命名为你的包名，并同步修改 `pyproject.toml` 中 `[tool.setuptools.packages.find]` 若需要
4. 进入该目录创建虚拟环境并安装：

```powershell
cd skills\<你的技能名>
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

5. 在该技能目录内写代码、`tests/`、`notebooks/` 等。

若你希望「**学习项目** + **实战区** + **可编辑子工程**」分栏存放，可新建 `learning/<学习项目名>/`（子工程仍用上述步骤），并在**仓库根**的 `practical/` 中放可运行的实战 demo 目录（与 `learning/` 同级）。

## 根目录（可选）

`src/learning_meta/` 是仅占位的轻量包，方便在根目录执行 `pip install -e ".[dev]"` 以安装 `pytest`、`ruff`。  
在仓库根目录建 `.venv`，仅用于统一跑检查工具；**练习与项目代码以各 `skills/*` 内环境为准**。

```powershell
cd D:\Python_WorkSpace\Learning_Project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```
