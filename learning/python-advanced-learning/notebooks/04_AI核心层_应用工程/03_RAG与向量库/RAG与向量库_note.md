# RAG 与向量库｜讲义笔记（阶段精读）

<参考资料>

- LangChain Retrieval：**https://python.langchain.com/docs/modules/data_connection/**（外部）
- `obsidian-vault/LLM_Learning/wiki/concepts/retrieval-augmented-generation.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/vector-storage.md`

**可选向量库：**`chromadb`、`qdrant-client`、`pinecone`、`faiss-cpu`（跟随各自 README 安装）。  
**向量模型：**OpenAI Embedding、`sentence-transformers` 等（注意 **许可证与隐私**）。

</参考资料>

## 本地知识库命中（与本节对齐）

- 上文两篇 concept wiki
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **L**

---

## 上一章核心收获回顾（衔接「Agent / LangChain」）

你能用 **链路图**表达 router / memory。

你已理解：**工具调用**需要 **可读描述 + schema**。

你已准备：**把专有知识接上模型**——当 prompt 上下文塞不下整本手册时。

---

## 但是，我们遇到了一个新的问题……

只靠预训练：**公司条例、工单库、周报**都无法「逐字背进参数」。**RAG：** **切块 → 嵌入 → 建索引 → 召回 Top‑K → 拼进上下文 → 要求引用**。**因此本章需要：**理解 **overlap、hybrid retrieval、评测 hit@k、metadata filter、抑制胡编**（与 citations 对齐）。 

---

## 动机

**可控时效性**：知识更新换索引分段，不等于整模重训；**可追溯**：给用户可点开出处。

---

## 类比（非编程）

开卷考试：**先翻索引贴纸 → 翻到原文引用 → 再组织语言作答**——不是闭眼默写百科全书。

---

## 精讲（由浅入深）

1. **Chunk**：长度 ~几百 token，`overlap` 缓解 **截断断句**。  
2. **Embedding**：领域文本 vs 结构化表格要选 **匹配的嵌入族**；不匹配会「搜回无关段落」。  
3. **Retriever**：向量相似度 + （可选）**BM25 混合**；**MMR** 提高多样性；**cross-encoder 重排**提高精度-cost。  
4. **拼装 Prompt**：`context + instruction + 要求标注出处`。  
5. **评测**：**hit@k、nDCG、人工相关性**组合拳，别只靠「感觉好点」。  

---

## 陷阱（≥2）：成因 → 改法

1. **过小 chunk**丢跨段语义。**改：**overlap、层级摘要、父子块。  
2. **上下文胡拼**。 — **相关性阈值、rerank、citation_loss 约束**。  

---

## 适用范围 · 延伸

离线批处理入库；实时变更需 **流式入库与版本**。合规场景注意 **租户隔离**。 

---

## 双重示例

### A. 伪：**建索引骨架**

```python
def build_index(docs: list[str]) -> dict:
    """真实实现：嵌入模型 + 向量库客户端。"""
    return {"chunks": docs, "embedding_model": "<name>"}


def retrieve(q: str, k: int = 5):
    ...
```

### B. **Prompt 壳**（示意）

```
<context>
{citations}
</context>
请仅用 context 作答；如无依据请显式说不确定。
```

---

## 练习

- **基础**：口述 **四层 RAG 数据流**。  

- **进阶**：画出 **hybrid（向量 + 关键词）**流程。  

- **开放：**设计 **hit@k**评测表头与采样策略。

---

## 费曼反问

1. **overlap** 增加的代价是什么？  
2. **embedding model 与语种/领域不匹配**会发生什么？  
3. 你如何给终端用户 **「可跳转出处」**？

---

> **闭环**：不看资料复述 **四层 RAG 流水线**用语义完整句。 
