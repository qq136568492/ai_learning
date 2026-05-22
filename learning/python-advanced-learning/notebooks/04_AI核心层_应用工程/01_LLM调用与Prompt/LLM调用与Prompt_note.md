# LLM 调用与 Prompt 工程｜讲义笔记（阶段精读）

<参考资料>

- OpenAI：**https://platform.openai.com/docs/guides/text-generation**（外部）
- Prompt 指南：**https://platform.openai.com/docs/guides/prompt-engineering**（外部）
- 兼容：**Ollama**、**LiteLLM**（外部）；**密钥仅环境变量**：`OPENAI_API_KEY`，**勿写入仓库**

```bash
pip install httpx pydantic python-dotenv
```

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **核心层 J**
- `obsidian-vault/LLM_Learning/wiki/topics/enterprise-llm-engineering-roadmap.md`
- （安全：`obsidian-vault/LLM_Learning/wiki/concepts/api-security.md`）

---

## 上一章核心收获回顾（衔接「FastAPI / 部署 / 异步」）

你已能把 **HTTP 契约 + Pydantic**摆在服务入口处，提早暴露坏输入。

你已理解：**`async`/流式**对延迟与网关扇出的工程含义。

你已坚持：**密钥走在环境变量与密钥管理服务里**，不写进源码与镜像。

你已准备：**用结构化 `messages=[...]` 表达对话**，而非整段无章法的裸字符串拼接。

你已具备 **超时、重试、退避** 的基础网络语义。

---

## 但是，我们遇到了一个新的问题……

「控制力」如果只写在散落在各脚本里的自然语言：**不可回放、难以版本比对、无法用同一套题库回归**。**因此本章需要：**厘清 **`system/user/assistant` 分工**，掌握 **`temperature`、`top_p`、流式 `SSE`/`chunk`** 的工程取舍；**JSON mode / Schema + Pydantic 校验结果**；**工具调用 JSON** 与安全边界。**安全**：prompt injection / RBAC 见 **api-security**。

---

## 动机

把 Prompt 当作 **可被审查、可被 diff、可被灰度的配置**：产品迭代才能 **可预期**而非「玄学改一句」。

---

## 类比（非编程）

- **`system`**：厨房总则与安全红线。  
- **`user`**：这一桌客人的具体需求。  
- **few-shot 示例**：墙上样菜（少而精好过一堆噪声）。  
- **tool calling**：允许写传票让小工（函数）冷库取货——**须有审批与白名单**。 

---

## 精讲（由浅入深）

1. **`messages`** 装配顺序与角色边界。  
2. **采样参数**：温度高创意强、漂移大；要低方差推理则降温 + 收窄 top-p。  
3. **吞吐路径**：一次性 `completion` vs **chunk 消费**——中间层需背压与取消。  
4. **计费与 429**：退避 **`backoff jitter`**、`max_retries`、指标记账。  
5. **结构化输出**：先 **schema**（Pydantic）再 **`model_validate`**，不要只靠 Prompt 口述。

```python
def chat(messages: list[dict]) -> str:
    """此处接官方 SDK / httpx；勿在讲义中硬编码密钥。"""
    raise NotImplementedError

MESSAGES = [
    {"role": "system", "content": "You are a terse assistant."},
    {"role": "user", "content": "用不超过 50 个汉字简述 asyncio。"},
]
```

---

## 辨析

| | **system** | **user / assistant** |
|--|-------------|-----------------------|
| 更新频率 | 相对稳定 | **随请求轮动** |

---

## 陷阱（≥2）：成因 → 改法

1. **密钥、token、PII** 钻进日志与报错栈。**改：**结构化脱敏、`logging.Filter`。  
2. **没有权威 schema**，只靠 Prompt **承诺金额/权限**。**改：**服务端双检。

---

## 适用范围 · 延伸

下一节 **RAG**、**LangChain/Agent**。企业治理见 **enterprise-llm-engineering-roadmap**。 

---

## 双重示例

### A. 纯函数：**构造消息列表**（不外呼网络）

上文 **`MESSAGES`**：单测可对 **dict shape**断言。

### B. 「伪链路」：**JSON-string → pydantic**

```python
import json

from pydantic import BaseModel


class Capsule(BaseModel):
    zh: str
    en: str


raw = '{"zh":"协程","en":"coroutine"}'
capsule = Capsule.model_validate_json(raw)
```

真实场景再加 **超时、校验失败文案、fallback**。 

---

## 练习

- **基础**：为同一 **`user`** 写两版 **`system`**，对比 **漂移**。  

- **进阶**：手写 **retry+退避** 伪代码包裹 HTTP 429。  

- **开放：**读一页 **Structured Outputs / JSON Schema**官方更新摘要。

---

## 费曼反问

1. 为何 **「messages 可追溯」对产品团队**是好事？  
2. **流式**主要改善的是 **体感延迟**还是 **服务端算力账单**？  
3. **`tool_calls` 与白名单 RBAC**应如何配对？

---

> **闭环**：三句话说清 **temperature / schema / backoff**各自解决哪类顾虑。
