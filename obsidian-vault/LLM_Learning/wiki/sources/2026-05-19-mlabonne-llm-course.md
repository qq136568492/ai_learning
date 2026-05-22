---
type: source
created: 2026-05-19
updated: 2026-05-19
tags: [llm, roadmap, llm-engineering, llm-scientist]
source_url: https://github.com/mlabonne/llm-course
source_path: LLM_Learning/raw/mlabonnellm-course Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks.md
---

# mlabonne/llm-course：Large Language Models 课程路线

## 摘要
`mlabonne/llm-course` 是一个面向 LLM 入门到实践的开放课程仓库，包含 roadmaps、Colab notebooks 与文章资源。课程分为三部分：LLM Fundamentals、LLM Scientist、LLM Engineer，分别对应基础知识、模型构建/训练优化、LLM 应用开发与生产部署。

## 核心论点
- LLM 学习应拆成三条路线：基础补齐、模型科学家、应用工程师。
- LLM Engineer 更贴近生产应用：运行 LLM、向量存储、RAG、高级 RAG、Agent、推理优化、部署、安全。
- LLM Scientist 更偏模型侧：Transformer 架构、预训练、后训练数据、微调、偏好对齐、量化、评估、模型合并、多模态与可解释性。
- 对应用开发者而言，RAG、Agent、部署与安全是最值得优先沉淀的工程能力。

## 关键结构
1. LLM Fundamentals：数学、Python/ML、神经网络、NLP
2. The LLM Scientist：架构、预训练、后训练数据、SFT/偏好优化、量化、评估、模型合并与多模态等
3. The LLM Engineer：运行 LLM、向量库、RAG、高级 RAG、Agent、推理优化、部署、安全

## 与现有 wiki 的连接
- 与 [[topics/python-advanced-to-ai-roadmap]] 的 AI 核心层高度重合。
- 与 [[topics/enterprise-llm-engineering-roadmap]] 的阶段四到阶段八互补。
- 与 [[topics/machine-learning-foundations]]、[[topics/numpy-numerical-foundations]] 构成 LLM Fundamentals 的前置基础。

## 待深化的问题
- 需要拆出 LLM Engineer 路线的生产化 DoD：RAG、Agent、部署、安全各自验收标准。
- 需要整理 LLM Scientist 路线中微调/量化/评估的最低可实践路径。
- 可生成“LLM 工程师 8 周路线”作为执行型 question 页面。
