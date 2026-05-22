---
type: source
created: 2026-05-14
updated: 2026-05-14
tags: [roadmap, ai-learning, java]
source_url:
source_path: LLM_Learning/raw/学习地图.md
---

# Java工程师转型企业级AI应用开发学习地图

## 摘要
这份路线图面向“有 Python 基础的 Java 工程师”，目标不是深入算法理论，而是以工程化视角快速构建并落地 LLM 应用：从 Python 工程基础、数据处理、API 服务，到 RAG、Agent、向量数据库、微调部署、企业级运维。

## 核心论点
- 学习顺序应按“工程落地链路”推进，而不是按传统 ML 理论顺序。
- Python 阶段强调工程能力：类型、测试、异步、包管理、代码规范。
- LLM 应用核心能力是：模型调用 + 检索增强（RAG）+ 工具调用（Agent）。
- 从原型到生产的关键跃迁在于：容器化、CI/CD、监控、安全限流。
- 对 Java 工程师而言，可迁移能力（分层架构、DI、服务治理）远大于语法迁移成本。

## 关键结构（8阶段）
1. Python 工程化基础
2. 数据处理（NumPy/Pandas/可视化）
3. API 服务开发（FastAPI + Pydantic）
4. LLM 调用与 Prompt 工程
5. 复杂应用（LangChain/LlamaIndex/Agent）
6. 向量数据库与检索
7. 微调与推理部署（LoRA/vLLM/Ollama）
8. 企业级工程化（Docker/CI/CD/监控/安全）

## 实战路线（5个项目）
- 大规模 CSV 清洗 + FastAPI 查询服务
- Ollama 本地聊天服务（流式）
- LangChain + Chroma 的 PDF RAG 问答
- Agent 工具调用（天气查询总结）
- Docker + Actions + Prometheus 的生产化改造

## 与现有 wiki 的连接
- 工程基础部分延伸了 [[topics/python-fundamentals]] 与 [[concepts/virtual-environment]]。
- API 层与 [[concepts/modules-and-packages]] 关联（服务组织与依赖管理）。
- 该 source 将学习主题从“Python 语言学习”扩展到“企业级 LLM 应用工程化”。

## 待深化的问题
- 每个阶段的“完成定义（DoD）”与评估标准尚未细化。
- 各技术栈的选型边界（如 LangChain vs LlamaIndex）需要补充对比。
- 生产落地中的成本、延迟、稳定性指标需要加入量化目标。
