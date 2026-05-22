# Python 进阶

本目录为学习项目 `learning/python-advanced-learning/` 下的 **「Python 进阶」子工程**（目录中文名 `python进阶`）。可编辑安装时发行名为 **`python-jinjie`（pip / pyproject 字段）**；import 包名为 `python_jinjie`。

**实战类 demo** 与小型项目请放在**仓库根**与 `learning/` 同级的 [`practical/`](../../../practical/)。

全栈学习地图与阶段验收见下文。仓库根总说明见 [../../../README.md](../../../README.md)。

## Obsidian 知识库联动

- 关联知识库（Vault）：`D:/Obsidian/repository/Obsidian Vault`
- 索引笔记：`D:/Obsidian/repository/Obsidian Vault/llm-wiki/index.md`
- 总日志：`D:/Obsidian/repository/Obsidian Vault/llm-wiki/log.md`
- 问答记录文件：`D:/Obsidian/repository/Obsidian Vault/llm-wiki/qa-records.md`

联动约定：

1. 本子工程内发起「要讲解 / 刷题 / 费曼」类请求时，优先检索 Vault 的本地笔记，再补充外部资料。
2. 每次问答在 Obsidian 中追加记录（问题、命中文件、答案摘要、参考链接），用于后续复盘。
3. 生成的 `notebooks/` 内容与 Obsidian 问答日志保持主题一致，便于双向跳转检索。

## 学习地图（摘要）

**约 20% 核心覆盖约 80% 实用场景**：能写出可维护的库级代码、可观测的服务与可复现的数据工作流。

| 块 | 核心抓手 |
|----|----------|
| 语言 | 一等函数与 `itertools`/`functools`、MRO/描述符/数据类/协议、可组合装饰器、`yield`/`send` 与 `yield from`、`__enter__`/`__exit__` 与 `contextlib` |
| 数据 | `ndarray` 轴与广播、向量化与 `ufunc`；`DataFrame` 清洗/合并/组聚合；一图一故事（`matplotlib` 底层 + `seaborn` 统计图） |
| Web | `FastAPI` 路由/依赖/校验/Async；`Gradio`/`Streamlit` 分钟级界面 |
| 工程 | `pytest` 夹具/参数化/标记；`logging` 分层与结构化；可预期错误边界与自定义异常体系 |

**建议路径**（可并行小步）：语言深化 → 数据清洗与可视化小项目 → 一个带测试与日志的 `FastAPI` 服务；原型用 `Streamlit`/`Gradio` 做演示。整合多阶段时可在仓库根 `practical/` 中另建实战目录。

## 分阶段目标与阶段验收

### 阶段 1：语言进阶

- **目标**：能独立用装饰器/生成器/上下文管理器写小工具；函数式与 OOP 能按场景选型。
- **验收**（任一项可证明达标）：
  - 实现一个**带参数的装饰器**并用于缓存或计时；写配套 `pytest`。
  - 用**生成器**处理大文件行流或分页迭代，附简短说明「为何比一次性列表省内存」。
  - 用 `contextlib.contextmanager` 或类协议实现**可嵌套的上下文管理器**，并在测试中验证异常时资源释放。

### 阶段 2：NumPy + Pandas

- **目标**：会轴与广播；会典型清洗（缺值、类型、去重、合并、分组聚合）。
- **验收**：
  - `notebooks/` 或脚本：从 CSV 完成清洗到一张汇总表，步骤可复现。
  - 至少 3 个有业务含义的**聚合/透视**；单元测试可测纯函数部分。

### 阶段 3：Matplotlib + Seaborn

- **目标**：会选图型、调轴与图例、导出 publication-friendly 图。
- **验收**：同一数据至少两种视图（如分布 + 关系/时间），图题与轴标签完整。

### 阶段 4：FastAPI

- **目标**：理解依赖注入、Pydantic 模型、可测试分层（路由薄、业务可单测）。
- **验收**：一个最小**资源 CRUD 或只读 API** + `pytest`（`TestClient`）覆盖主路径与 4xx/5xx 边界；文档可从 OpenAPI 访问。也可在仓库根 `practical/` 中建独立可运行服务目录。

### 阶段 5：Gradio / Streamlit

- **目标**：把阶段 2–4 的能力接到 UI，做演示或内部工具。
- **验收**：单页可运行，输入/输出明确，有基本错误提示。

### 阶段 6：工程化

- **目标**：`pytest` 为默认反馈环；`logging` 有模块名与级别策略；异常分层清晰。
- **验收**：`pytest` 在 CI 或本地可一键通过；服务或脚本启动时**可配置**日志；自定义异常有文档说明何时抛出。

## 本目录约定

- 练习代码放在 `src/python_jinjie/` 与 `tests/`；探索性分析放在 `notebooks/`。触发 **「要讲解：…」**（见 `.cursor/skills/ai-precision-learning/SKILL.md`）时，在 `notebooks/<知识块>/` 下生成 `*_summary.md`、按序号分节的 `*_note.md` 与 `*_practice.py`；函数式已有包：`notebooks/函数式/`。单文件 `函数式_note.py` 仅为跳转说明。
- 每阶段结束在本文「阶段验收」下打勾或补一句**如何验证**（可检查产出），便于续学。

## 初装（PowerShell）

从仓库根进入：

```powershell
cd learning\python-advanced-learning\python进阶
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

需要数据/Web 依赖时，在 `pyproject.toml` 的 `dependencies` 中按需增加（如 `pandas`、`fastapi[standard]` 等）后再 `pip install -e ".[dev]"`。

## 可复制的下一句（精准指令，见主 Skill）

- 要地图：`我要快速掌握【领域】，给我核心知识点、学习路径、阶段性目标。`
- 要讲解：`用最简单的比喻，零基础解释【知识点》。`
- 要刷题：`我练习【技能】，出 5 道题，我答完后帮我纠错并讲解。`
- 要费曼：`你当小白，我讲【内容】，你一直提问，直到我讲明白。`
