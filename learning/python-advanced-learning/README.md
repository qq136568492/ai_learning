# Python 进阶学习项目

学习入口：`learning/python-advanced-learning/`（**无**单独的 `python进阶/` 二级目录）。

目标：对照本机 Obsidian 知识库里「Python 进阶 → AI 应用」分层大纲，形成 **四层 notebooks** 结构与可运行练习闭环。实战与大项目写在仓库根的 [`../../practical/`](../../practical/)。

## 一、四层知识地图与目录

对应 Obsidian：`LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`、`raw/Python进阶到AI应用_完整学习地图.md`。

| 层级 | `notebooks/` 目录 | 内容纲要 |
|------|-------------------|-----------|
| 基础层｜语言巩固 | `01_基础层_语言巩固/` | 类型与可变性、`match`、字符串与 IO、函数与作用域、异常、对象模型、模块与 venv |
| 进阶层｜语法与工程 | `02_进阶层_语法与工程/` | 推导式、迭代器/生成器、OOP、装饰器、上下文、魔术方法、类型提示、`asyncio`、`pytest`、`logging` |
| 接轨层｜数据与 API | `03_接轨层_数据与API/` | NumPy、Pandas、Matplotlib/Seaborn、FastAPI、Pydantic、Streamlit、部署与可观测 |
| AI 核心层｜应用工程 | `04_AI核心层_应用工程/` | LLM/Prompt（stub）、LangChain/Agent（stub）、RAG/向量库（stub）、微调与推理（stub）、企业工程（stub）；附概念练习 |

各层根目录下有 `*_summary.md`；小节目录内为 `{知识点}_note.md` 与拆分 `*.py` 练习脚本。

早期结构已归档：**`notebooks/_legacy_pre-2026-05-14/`**（仍可查阅旧 `_note`/练习）。

### Obsidian

见同目录 [`obsidian_bridge.md`](obsidian_bridge.md)。

## 二、环境与依赖

在项目根：

```powershell
cd d:\Python_WorkSpace\Learning_Project\learning\python-advanced-learning
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev,learning]"
```

- `learning` extras：NumPy、Pandas、Matplotlib、Seaborn、FastAPI、`uvicorn[standard]`、`httpx`、`pydantic`、`streamlit`（仅练习需要）。

## 三、推荐阅读顺序

1. `01_基础层_语言巩固` → `02_进阶层_语法与工程` → `03_接轨层_数据与API` → `04_AI核心层_应用工程`。  
2. 每小节：`*_note.md` → 同名前缀 `NN_*.py` 两个练习（可删实现自练）→ 费曼复述。  

## 四、自检（示例）

任选练习文件：

```powershell
python .\notebooks\01_基础层_语言巩固\01_数据类型与可变性\数据类型与可变性01_mutable_default_none.py
```

---

根仓库约定见 [../../README.md](../../README.md)。
