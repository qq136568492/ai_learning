---
type: source
created: 2026-05-14
updated: 2026-05-14
tags: [python, ai, roadmap, engineering]
source_url:
source_path: LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md
---

# Python 进阶到 AI 应用｜完整学习地图

## 摘要
该文档把“Python 基础→Python 进阶→AI 工程化落地”串成一条完整主线，覆盖语言能力、数据处理、API 服务、LLM 应用、RAG、微调部署与企业级运维，并与本 vault 现有页面建立了详细映射关系。

## 核心论点
- 学习路径应从语法能力平滑过渡到工程化与 AI 应用，而非割裂学习。
- Python 进阶层的关键是：装饰器/生成器/上下文管理器/魔术方法 + 类型系统 + 异步 + 测试规范。
- AI 接轨的底座是数据处理（NumPy/Pandas）与 API 工程（FastAPI/Pydantic/安全/部署）。
- LLM 应用核心链路是：模型调用 + Prompt 工程 + Tool Use + RAG + 可观测。
- 企业级落地需要 CI/CD、监控、安全、成本治理等非模型能力共同支撑。

## 关键结构
- A～C：Python 基础层（语言/数据模型/模块环境）
- D～F：Python 进阶层（语法、类型异步、工程化）
- G～I：AI 接轨准备层（数据处理、API、部署观测）
- J～N：AI 应用核心层（LLM、Agent、RAG、微调、企业化）

## 与现有 wiki 的连接
- 强化并串联了 [[topics/python-fundamentals]]、[[topics/numpy-numerical-foundations]]、[[topics/fastapi-api-engineering]]。
- 与 [[topics/enterprise-llm-engineering-roadmap]] 形成“总纲 + 分层细化”关系。
- 明确指出了知识库待补页（如装饰器、contextmanager、LangGraph、Pydantic v2 等）。

## 待深化的问题
- 各阶段 DoD 需要量化（交付标准/测试标准/性能目标）。
- 对 LangChain vs LlamaIndex、向量库选型可单独做对比专题。
- 可补充“周计划→日计划”执行模板与验收清单。
