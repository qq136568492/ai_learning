# LangChain / Agent 编排｜讲义笔记（阶段精读）

<参考资料>

- LangChain 文档：**https://python.langchain.com/docs/get_started/**（外部）
- （对照）**LlamaIndex** 等（外部）
- 工程取舍：**纯 pydantic + jsonschema 手写链路 vs 编排框架**

```bash
pip install langchain langchain-openai langgraph   # 以官方当期文档为准调整包名
```

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **K**
- `obsidian-vault/LLM_Learning/wiki/topics/enterprise-llm-engineering-roadmap.md`

---

## 上一章核心收获回顾（衔接「直连 LLM + Prompt」）

你能区分 **`system/user`**，理解 **温控与结构化输出**。

你已认识 **SSE/分块**：产品体验和网络栈要一起算账。

你已准备：**把链路从「单次补全」拉成路由、记忆、工具的有机组合**。 

你已理解：**JSON schema ⇒ function calling** 是工具的「海关申报单」心智。

你已警惕：**不可重复步骤**会破坏测试与离线评估。

---

## 但是，我们遇到了一个新的问题……

手写 **`while True: llm(...); if tool:`**：**状态散落在全局变量**，难测、难看、难以多人协作。**因此本章需要：**把链路想成 **DAG / 明确状态机**：**`Runnable`/链式组合**，或 **LangGraph 节点-边图**；为 **checkpoint、memory** 划出隔离边界。**术语：**ReAct、Plan-and-execute——精读可各选一篇论文。 

---

## 动机：**子步骤可单测**，失败时能 **对准节点**回放。

---

## 类比（非编程）

旅行团：**导游（Planner）**定路线；**中巴（Retriever）**装资料；游客偏好贴纸是 **会话记忆**。 

---

## 精讲（由浅入深）

1. **LCEL**：用 **管道运算符**拼装 **可组合的 Runnable**。  
2. **LangGraph（或同类）**：节点显式声明 **读写状态**，更易画 **可视化与断点**。  
3. **工具层**：每条工具都要有 **可读描述 + 参数 schema**。  
4. **评估**：为关键节点保留 **离线 golden**：否则线上只能「玄学调 prompt」。  

---

## 辨析

| | **手写循环** | **编排框架图** |
|--|----------------|----------------|
| 控制力 | 任意复杂 | 开箱快 |
| 可维护 | 看人 | 需团队对齐「图方言」|

---

## 陷阱（≥2）：成因 → 改法

1. **会话级可变 memory**在 **多租户**混淆。**改：**每请求独立存储键、或显式 TTL。  
2. **直接把 LLM 输出当布尔控制流而不校验**。**改：**schema / 判别函数 / 熔断。  

---

## 适用范围 · 延伸

与 **向量检索、RAG** 拼；与 **观测 trace**、`OpenTelemetry` 挂钩见部署专题。

---

## 双重示例

### A. 文本链：**`route → retrieve → summarize`**

练习：用箭头与方框在白板或 Markdown 手写一版 ASCII DAG。

### B. 最小 **tool 清单头**（伪）

```python
TOOLS = [
    {"name": "search", "description": "search kb", "parameters": {"type": "object"}},
]
```

---

## 练习

- **基础**：手绘 **三路 router**（何时走知识库 / 计算器 /拒答）。  

- **进阶**：列出 **三类 memory 污染源**与规避。  

- **开放：**对比 LangGraph 与一个 **手写 80 行 state dict**的工程性价比。

---

## 费曼反问

1. **DAG vs 环图**：何时必须有环？  
2. 框架在什么规模开始 **边际收益变负**？  
3. 你如何 **离线断言** 「某节点输出 schema」？

---

> **闭环**：口述 **链路可观测**：你最希望在日志里并排出现的 **三类字段**。 
