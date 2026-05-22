---
type: concept
created: 2026-05-19
updated: 2026-05-19
tags: [llm, rag, vector-store]
source_count: 1
---

# vector-storage

向量存储是 RAG 的基础设施：把文档切分后转换为 embedding 向量并存入向量数据库，以便查询时按相似度检索相关片段。

## 核心流程
1. Ingest documents：加载 PDF/Markdown/HTML/JSON/数据库/API 数据
2. Split documents：按标题、语义或递归策略切分 chunk
3. Embedding：用 embedding 模型把 chunk 转成向量
4. Vector DB：存储向量与 metadata，支持相似度检索和过滤

## 常见工具
- Chroma / FAISS：原型与本地
- Milvus / Pinecone / Qdrant：生产级向量检索
- Sentence Transformers / OpenAI embeddings / BGE 系列：常见 embedding 模型

## 来源
- [[sources/2026-05-19-mlabonne-llm-course]]
