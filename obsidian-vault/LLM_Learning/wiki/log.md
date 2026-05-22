## [2026-05-14] ingest | NumPy 开发文档（用户指南聚合）
- 新增 [[sources/2026-05-14-numpy-devdocs]]
- 新增 [[entities/numpy]]
- 新增 [[topics/numpy-numerical-foundations]]
- 更新 [[overview]]：补齐数据处理层的向量化与数组语义基础
- 更新 [[index.md]]

---
---
type: log
created: 2026-05-13
---

# Log

时间倒序（最新在顶）。由 LLM 自动追加。

---


## [2026-05-19] learning | 批量重生：魔术方法 → 企业工程化 共 17 份 `_note.md`（persona + vault + 顺稿）
- wiki：[[qa-records]] `23:55`

## [2026-05-19] learning | `上下文管理器_note.md` 对齐 persona + vault（with / yield / ExitStack）
- wiki：[[qa-records]] `22:10` 条目

## [2026-05-19] learning | `装饰器_note.md` 按 persona 分层重写（衔接 OO / wraps / 工厂）
- wiki：[[qa-records]] `21:30` 条目

## [2026-05-19] learning | 答疑：可变默认参数与 dataclass「共用一只桶」
- 说明默认求值时机、`default_factory`、`None` 哨兵；见 [[qa-records]] `20:15` 条目

## [2026-05-19] learning | OO 讲义 `类与面向对象_note.md` 与同层「装饰器」等板块标题对齐
- 调整：精讲/辨析/陷阱/适用范围 · 延伸/练习/费曼小节命名与分隔线；措辞与进阶练习微调
- wiki：[[qa-records]] 同日 `19:05` 条目

## [2026-05-19] learning | python-advanced-learning：29 份 `_note.md` 统一讲义收口 + injector 无害化 + 小问题修补
- 全节含 `｜讲义笔记` 与 `## 双重示例`；`inject_python_advanced_note_scaffold.py` 对统一稿跳过；补 `部署与可观测_note.md` 双重示例；修 `上下文管理器_note.md` 回顾句
- wiki：[[qa-records]] 同日 `18:35` 条目

## [2026-05-19] learning | 「类与面向对象」讲义按 python-teaching-persona 单列重写 + QA 存档
- 文件：`Learning_Project/learning/python-advanced-learning/notebooks/02_进阶层_语法与工程/03_类与面向对象/类与面向对象_note.md`
- wiki：[[qa-records]] 同日 `12:30` 条目

## [2026-05-19] learning | python-advanced-learning：`_note.md` 按知识地图与教学规则注入讲义骨架 + vault 路径回退
- 29 份 `*_note.md`：`teaching-scaffold-head/tail:v1` 标记、衔接/动机/类比/练习/费曼；知识库指针改为仓库 `obsidian-vault/LLM_Learning/...`
- 工具：`Learning_Project/tools/inject_python_advanced_note_scaffold.py`（幂等）
- wiki：同日 [[qa-records]] 条目

## [2026-05-18] learning | 答疑补记：open() 默认编码与 UTF-8 模式 / 封装
- 更新 `Learning_Project/.../字符串与文件IO_note.md` §4.4；[[qa-records]] 同日条目

## [2026-05-18] learning | notebooks 四层结构重建（Python→AI roadmap）
- 产出：`learning/python-advanced-learning/notebooks/01_*`〜`04_*`，旧版归入 `_legacy_pre-2026-05-14/`
- 细节：进阶层补足 note；接轨层 7 小节 + `.py` 练习拆解；AI 核心 5 stub + 占位练习；`pyproject.toml` 增加 `[project.optional-dependencies] learning`

---

## [2026-05-13] learning | python-advanced-learning 笔记按 Obsidian 命中重生
- SKILL：补充 `obsidian-vault` 回退与「本地知识库命中」必选
- 产出：`learning/python-advanced-learning/notebooks/**` 全部 `*_note.md` + 各模块 `*_summary.md` 更新
- 详见 [[qa-records]] 同日条目

- 将误插入到 frontmatter 之前的两条 ingest 记录移回正文日志区
- 恢复 frontmatter 顶部位置与统一分隔格式

---

## [2026-05-14] ingest | FastAPI 文档二次结构化（概念拆分）
- 新增 [[concepts/dependency-injection]]
- 新增 [[concepts/api-security]]
- 新增 [[concepts/deployment-strategy]]
- 更新 [[topics/fastapi-api-engineering]]
- 更新 [[index.md]]

---

## [2026-05-14] ingest | FastAPI 官方文档（中文学习区聚合）
- 新增 [[sources/2026-05-14-fastapi-official-docs]]
- 新增 [[entities/fastapi]]
- 新增 [[topics/fastapi-api-engineering]]
- 更新 [[overview]]：补齐 API 服务层主线
- 更新 [[index.md]]

---

## [2026-05-14] ingest | Java工程师转型企业级AI应用开发学习地图
- 新增 [[sources/2026-05-14-java-ai-learning-roadmap]]
- 新增 [[topics/enterprise-llm-engineering-roadmap]]
- 更新 [[overview]]：研究主题扩展为企业级 LLM 应用工程化学习
- 更新 [[index.md]]

---

## [2026-05-13] ingest | Python 3.11 官方教程
- 新增 [[sources/2026-05-13-python311-tutorial]]
- 新增 [[entities/python]]
- 新增 concepts（10 个）：data-types、control-flow、functions、list-comprehension、modules-and-packages、classes-and-oop、iterators-and-generators、exception-handling、string-formatting、file-io、standard-library、virtual-environment
- 新增 topics（3 个）：python-fundamentals、python-data-model、python-module-system
- 更新 [[overview]]：确定研究主题为 Python 编程语言学习
- 更新 [[index.md]]

---

## [2026-05-13] schema | wiki 初始化
- 建立三层架构：raw/、wiki/（sources/concepts/entities/topics/questions）
- 编写 CLAUDE.md（schema）
- 创建 index.md、log.md、overview.md
- 学习主题尚未确定，待用户首次 ingest 时填写

---

## [2026-05-22 11:54:36] qa | 批量重写进阶层后续 note
- 基于 Obsidian context-managers、functions、python-data-model、asyncio-in-practice、standard-library、deployment-strategy、FastAPI 官方快照与学习地图，重写 5 篇后续笔记：05_上下文管理器、07_类型提示、08_asyncio异步、09_pytest测试、10_logging日志。
- 每篇补齐小白视角教学漏洞分析、前置铺垫、动机类比、系统精讲、辨析、陷阱、双重示例、练习答案、费曼反问和来源分层；跳过已重写的 06_魔术方法。
- 校验结果：结构关键章节存在；无乱码/TODO/FIXME 命中；99 个 Python 代码块 AST 语法校验通过。
