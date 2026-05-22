---
type: concept
created: 2026-05-19
updated: 2026-05-19
tags: [llm, rag]
source_count: 1
---

# retrieval-augmented-generation

RAG（Retrieval Augmented Generation）通过检索外部知识并把相关上下文交给 LLM，提升回答准确性、可追溯性与知识新鲜度，而不需要微调模型。

## 基本链路
用户问题 → 查询改写/embedding → 检索 top-k 文档 → 可选重排 → Prompt 拼装 → LLM 生成 → 引用与评估

## 评估维度
- 检索：context precision / recall
- 生成：faithfulness / answer relevancy
- 工具：Ragas、DeepEval

## 来源
- [[sources/2026-05-19-mlabonne-llm-course]]
