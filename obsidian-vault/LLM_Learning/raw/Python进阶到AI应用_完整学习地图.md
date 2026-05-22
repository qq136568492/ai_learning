# Python 进阶到 AI 应用｜完整学习地图

> 在 `Python 基础语法 / 数据结构` 已掌握的前提下，将「Python 进阶」与「AI 大模型应用工程化」串成一条完整链路。
> 本文与本 vault 已有内容联动：
>
> - 基础与进阶语法：`obsidian-vault/LLM_Learning/wiki/topics/python-fundamentals.md` 及 `concepts/*`
> - 数据处理：`topics/numpy-numerical-foundations.md`、`concepts/broadcasting-rules.md` 等
> - API 工程：`topics/fastapi-api-engineering.md`、`concepts/dependency-injection.md` 等
> - 总路线：`topics/enterprise-llm-engineering-roadmap.md`、`raw/学习地图.md`

---

## 一、地图总览

```
Python 基础（已掌握）
   ↓
A. 语言基础巩固           ┐
B. 数据模型               │ → Python 基础层（A～C）
C. 模块与环境             ┘
   ↓
D. 进阶语法（装饰器/生成器/上下文/魔术方法）
E. 类型与异步
F. 工程化基础（pytest / ruff / 标准库）   → Python 进阶层（D～F）
   ↓
G. 数据处理三板斧（NumPy / Pandas / 可视化）
H. API 服务开发（FastAPI + Pydantic）       → AI 接轨准备层（G～H）
I. 部署与可观测（Docker / 反代 / 日志指标）
   ↓
J. LLM 调用与 Prompt 工程
K. 复杂应用：LangChain / LlamaIndex / Agent
L. 向量数据库与检索（RAG）                  → AI 应用核心层（J～M）
M. 模型微调与推理部署（LoRA / vLLM / Ollama）
   ↓
N. 企业级工程化落地（Docker / CI-CD / 监控 / 安全）
```

每节都给出：**子节点**、**必学要点**、**典型工具/产出**、**对应的 vault 文件或外部链接**。

---

## 二、Python 基础层（巩固）

### A. 语言基础

依据：`obsidian-vault/LLM_Learning/wiki/topics/python-fundamentals.md`

- **A1 数据类型**：可变 / 不可变；`list / tuple / set / dict / str / bytes`；切片；可变默认值陷阱（`concepts/data-types.md`）
- **A2 控制流**：`if/elif/else`、`for`、`while`、`break/continue/else`、3.10+ `match`（`concepts/control-flow.md`）
- **A3 字符串格式化**：f-string、`str.format`、`%`；`str()` vs `repr()`（`concepts/string-formatting.md`）
- **A4 文件 I/O**：`with open(..., encoding='utf-8')`、迭代行；`json.dump/load`（`concepts/file-io.md`）
- **A5 函数（入门段）**：位置/关键字、`*args/**kwargs`、`/` 与 `*` 分隔、`lambda`、LEGB 作用域（`concepts/functions.md`）
- **A6 异常处理**：`try/except/else/finally`、`raise … from …`、自定义异常、3.11+ `ExceptionGroup`（`concepts/exception-handling.md`）

### B. 数据模型

依据：`topics/python-data-model.md`

- **B1** 一切皆对象：`id / type / value`、`is` vs `==`
- **B2** 可变性的影响：赋值不复制、函数参数语义、字典键、默认参数陷阱、`copy/deepcopy`
- **B3** 序列协议：索引/切片/`+`/`*`/`in`/`len`
- **B4** 映射协议（dict）：可哈希键、3.7+ 插入顺序
- **B5** 迭代协议（衔接进阶 D2）

### C. 模块与环境

依据：`topics/python-module-system.md`、`concepts/modules-and-packages.md`、`concepts/virtual-environment.md`

- **C1** 模块与包；`__init__.py`、`__all__`
- **C2** 绝对 / 相对导入；`sys.path` 搜索；编译缓存
- **C3** `if __name__ == "__main__":` 入口点
- **C4** 虚拟环境：`venv`、`pip`、`requirements.txt`；进阶 `poetry`、`uv`

---

## 三、Python 进阶层

### D. 进阶语法

#### D1 推导式
依据：`concepts/list-comprehension.md`

- 列表 / 字典 / 集合 / 生成器表达式
- 多重 `for`、嵌套、条件
- 何时退回普通 `for`（复杂逻辑、有副作用）

#### D2 迭代器与生成器
依据：`concepts/iterators-and-generators.md`

- 迭代器协议：`__iter__` + `__next__` + `StopIteration`
- `for` 的本质：`iter()` → 循环 `next()` → 捕获 `StopIteration`
- 生成器函数 `yield`、生成器表达式
- 内置工具：`range / enumerate / zip / map / filter / reversed / sorted`
- 工程价值：**惰性读大文件**、流式分页、内存友好

#### D3 类与面向对象
依据：`concepts/classes-and-oop.md`

- 类变量 vs 实例变量；`self`、`__init__`
- 继承、`super()`、MRO（C3 线性化）、多重继承
- 私有约定：`_var`（约定）、`__var`（name mangling）
- 特殊方法：`__str__`、`__repr__`、`__iter__`、`__call__`、`__eq__/__hash__`、`__enter__/__exit__`
- duck typing、组合优于继承

#### D4 进阶魔法（学习地图必学，wiki 待补）
依据：`raw/学习地图.md` 阶段一

- **装饰器**：函数装饰器、带参装饰器、类装饰器、`functools.wraps`；典型——计时 / 缓存 / 日志 / 权限
- **上下文管理器**：`__enter__/__exit__` 协议、`contextlib.contextmanager`、`@asynccontextmanager`、资源安全
- **魔术方法**：运算符重载（`__add__`/`__lt__`/`__eq__`）、容器协议（`__len__`/`__getitem__`/`__contains__`）、可调用对象（`__call__`）
- **`yield` 惰性读取大文件**：分块/分页迭代器；与 `itertools.islice / chain` 串联

### E. 类型与异步

依据：`raw/学习地图.md` 阶段一

#### E1 类型提示与静态检查
- `typing`：`Optional / Union / Callable / Tuple`；3.9+ 用 `list[int]`；3.10+ `X | Y`
- 进阶：`TypeVar`、`Generic`、`Protocol`、`TypedDict`、`Literal`、`Annotated`、`ParamSpec`
- 工具链：`mypy`、`pyright`、`ruff` 的部分规则
- `from __future__ import annotations` 延迟求值

#### E2 异步编程
- `async def` / `await`、事件循环 `asyncio`
- 常用 API：`asyncio.run / gather / create_task / wait_for / sleep / Queue`
- 适用场景：**I/O 密集**（HTTP 抓取、数据库异步驱动、LLM 流式输出）
- 异步上下文与异步迭代器：`async with` / `async for`
- 与同步代码桥接：`asyncio.to_thread`、`run_in_executor`

### F. 工程化基础

#### F1 测试
- `pytest`：函数发现、断言重写、`-k`/`-m` 过滤
- **fixture**（夹具）：函数/类/模块/会话级；`yield` 风格清理
- **参数化**：`@pytest.mark.parametrize`
- mock：`unittest.mock`、`pytest-mock`、`monkeypatch`
- 异常断言：`pytest.raises`
- 覆盖率：`coverage.py` / `pytest-cov`
- 异步测试：`pytest-asyncio` / `anyio`

#### F2 代码规范
- `ruff`：一体化 lint + format（替代 `flake8/isort` 与部分 `black`）
- `black`：格式化（团队偏好二选一）
- PEP 8 摘要（见 `topics/python-fundamentals.md`）

#### F3 标准库速通
依据：`concepts/standard-library.md`

- OS / 路径：`os` / `pathlib` / `shutil` / `glob`
- 文本：`re` / `string`
- 数学：`math` / `random` / `statistics`
- 时间：`datetime` / `time` / `zoneinfo`
- 压缩 / 归档：`zlib` / `gzip` / `zipfile` / `tarfile`
- 并发：`threading`（受 GIL 限制）/ `multiprocessing` / `concurrent.futures`
- 日志：`logging`（级别、Handler、Formatter）；进阶 `loguru`、`structlog`
- 集合：`collections.deque / Counter / defaultdict / namedtuple`
- 函数式：`functools.partial / reduce / lru_cache / wraps`、`itertools.count / cycle / islice / chain / groupby`
- 数据类：`dataclasses.dataclass`、`enum`
- 配置：`configparser` / 推荐 `pydantic-settings`

---

## 四、AI 接轨准备层

### G. 数据处理三板斧

依据：`topics/numpy-numerical-foundations.md`、`raw/学习地图.md` 阶段二

#### G1 NumPy
依据：`entities/numpy.md`、`concepts/broadcasting-rules.md`、`concepts/view-vs-copy.md`、`concepts/dtype-and-memory.md`

- **ndarray 心智模型**：`shape / ndim / dtype / axis / size / itemsize`
- **向量化**：逐元素 ufunc、`np.sin/exp/log`、`+ - * /`
- **聚合**：`sum / mean / std / max / argmax` + `axis` / `keepdims`
- **广播规则**：尾维对齐、相等或 1 即兼容；典型——批量归一化、外积、注意力打分前 reshape
- **视图 vs 拷贝**：切片 → view；花式索引 → copy；`.base`、`.copy()`
- **dtype 与内存**：`float32` vs `float64`、`int8/16/32/64`、upcasting、字节序
- **矩阵运算**：`@` / `np.matmul` / `np.linalg`；高阶 `np.einsum`
- **形状变换**：`reshape / transpose / squeeze / expand_dims / stack / concatenate / split`
- **AI 价值**：与 **PyTorch / TensorFlow 张量语义高度相似**；嵌入向量本质就是 `ndarray[float32]`

#### G2 Pandas
- `Series` / `DataFrame`：带标签的 NumPy
- 读写：`read_csv / read_excel / read_json / read_parquet`；`to_*`
- 索引：`loc / iloc`；注意 `SettingWithCopyWarning`
- 清洗：`isna / dropna / fillna / astype / drop_duplicates / replace`
- 合并：`merge / join / concat`，`validate=` 防膨胀
- 分组聚合：`groupby + agg / transform / apply`（split-apply-combine）
- 透视：`pivot_table / crosstab`
- 时间序列：`to_datetime / resample / rolling`

#### G3 可视化（Matplotlib / Seaborn）
- Matplotlib 对象模型：`Figure` / `Axes`；`plt.plot / scatter / bar / hist`
- 坐标、图例、刻度、标题、`savefig` 导出
- Seaborn：`relplot / catplot / displot / heatmap / pairplot`
- 一图一故事原则；调色板与对色盲友好的配色

### H. API 服务开发

依据：`topics/fastapi-api-engineering.md`、`entities/fastapi.md`

#### H1 FastAPI 路由与模型
- `@app.get/post/put/delete`、路径参数、查询参数、请求体
- `response_model=` 过滤字段；`HTTPException`、`status_code`

#### H2 Pydantic 数据契约
- `BaseModel`、`Field(...)` 约束（`min_length / ge / le / regex`）
- 验证器：`field_validator` / `model_validator`
- 嵌套模型、`Optional` / `| None`
- 配置加载：`pydantic-settings`、`.env` + 环境变量

#### H3 依赖注入
依据：`concepts/dependency-injection.md`

- `Depends(...)`：鉴权、DB session、配置、限流上下文
- 子依赖、全局依赖、`yield` 依赖（清理资源）
- 测试 override：`app.dependency_overrides[dep] = fake`

#### H4 安全
依据：`concepts/api-security.md`

- OAuth2 Password Flow + Bearer Token；JWT 签发 / 校验 / 过期
- CORS、TrustedHost、HTTPSRedirect
- 认证 vs 授权分层、网关 + 应用双重防护、速率限制、审计日志

#### H5 异步 & 中间件
- `async def` 路由 + `httpx.AsyncClient` 等异步客户端
- `@app.middleware("http")`；`BackgroundTasks`；`lifespan`（启动 / 关闭钩子）

#### H6 测试
- `TestClient`（同步）/ `AsyncClient` + `pytest-asyncio`（异步）
- 覆盖主路径 + 4xx/5xx 边界

### I. 部署与可观测

依据：`concepts/deployment-strategy.md`

- 运行：`uvicorn` 多 worker；或 `gunicorn -k uvicorn.workers.UvicornWorker`
- 容器化：`Dockerfile` 多阶段构建、`.dockerignore`、`docker-compose`
- 反代 + HTTPS：Nginx / Traefik 终止 TLS；健康检查 + 优雅停机（`SIGTERM`）
- 配置：环境变量 + `pydantic-settings`；`.env` 不入 git
- 可观测三件套：
  - **日志**：`logging` / `loguru` / `structlog`（结构化 JSON）
  - **指标**：Prometheus（`prometheus-fastapi-instrumentator`）+ Grafana
  - **追踪**：OpenTelemetry（trace_id 贯穿）

---

## 五、AI 应用核心层

### J. LLM 调用与 Prompt 工程

依据：`raw/学习地图.md` 阶段四

#### J1 模型调用
- **OpenAI 兼容 API**：行业事实标准
  - `chat.completions.create`：messages、`temperature`、`top_p`、`max_tokens`、`stop`、`response_format`、`seed`
  - **流式输出** `stream=True`：服务端推送 token，前端边收边渲染
  - **函数调用 / Tool Use**：定义 JSON Schema → 模型决定调用哪个工具 → 业务再次回填消息再请求
- **国产兼容端点**：DeepSeek / 通义 / 月之暗面 / 智谱 等多数兼容 OpenAI 协议
- **本地模型 Ollama**：拉取模型 → REST API；适合调试与私密部署
- 客户端：`openai-python`、`httpx`、`anthropic`、`zhipuai`、`dashscope` 等

#### J2 Prompt 工程
- **结构化提示词**：System / Developer / User / Assistant 角色
- **少样本（Few-shot）**：给模型示例对照
- **思维链（CoT）**：分步推理、Self-Consistency、Tree-of-Thought
- **格式约束**：要求返回 JSON、用 `response_format={"type": "json_object"}` 或 JSON Schema
- **角色设定**：领域专家、严格审稿人、自我审视
- **温度策略**：确定性任务低温（0–0.3），创造性任务高温（0.7+）

#### J3 推理参数与成本
- token 计费（输入 / 输出 / 缓存 / 推理）；估算工具：`tiktoken`、`anthropic` tokenizer
- 上下文窗口与"针入草垛"实验
- **缓存命中**：提示词前缀稳定、用 prompt caching 降本
- 速率限制：RPS、TPM 双约束；客户端侧退避重试

### K. 复杂应用：LangChain / LlamaIndex / Agent

依据：`raw/学习地图.md` 阶段五

#### K1 LangChain
- 核心抽象：`Runnable` / `RunnableLambda` / `RunnableParallel` / `RunnablePassthrough`
- `PromptTemplate` / `ChatPromptTemplate` / `MessagesPlaceholder`
- Chain：LCEL（`prompt | model | parser`）
- `OutputParser`：Str / JSON / Pydantic / Structured
- Memory：`ConversationBufferMemory` / `Summary` / `Window`
- 文档处理：`Document Loader` → `TextSplitter` → `Embedding` → `VectorStore` → `Retriever`
- LangServe / LangGraph：分别为 FastAPI 化与图式流程编排

#### K2 LlamaIndex
- 偏 **数据索引 / RAG** 的框架
- 文档加载器、`Node`、`Index`（VectorStoreIndex、KnowledgeGraphIndex…）
- `QueryEngine` / `ChatEngine` / `Router`
- 与 LangChain 的边界：LlamaIndex 在"检索 + 数据"上 API 更专；LangChain 在通用 orchestration / Agent 上更全

#### K3 Function Calling / Tool Use
- 工具描述：JSON Schema（参数、类型、必填、说明）
- 调用解析：模型返回 `tool_calls[].arguments` → 业务执行 → 把结果作为 `tool` 角色回填 → 继续推理
- 安全：参数校验、白名单、超时、幂等、可观测（trace_id + 入参 / 出参日志）

#### K4 Agent 开发
- ReAct：Reason → Act → Observe → Reason ……
- AgentExecutor / **LangGraph** 状态图：节点 = 函数 / 工具，边 = 条件路由
- 模式：单 Agent + 工具集 / 多 Agent 协作（planner-executor、Hub-Spoke、Network）
- 反思与回滚（Reflection / Self-Critique）
- 终止条件、最大步数、人工介入（HITL）

### L. 向量数据库与检索（RAG）

依据：`raw/学习地图.md` 阶段六

#### L1 嵌入（Embedding）
- 文本 → 高维向量；常用 OpenAI `text-embedding-3-small/large`、`bge-m3`、`gte-large`
- 选型参考：MTEB 排行榜
- 维度（768 / 1024 / 3072 …）影响精度与存储
- **归一化** vs 原始向量；余弦相似度对归一化更稳定

#### L2 向量数据库
- **Chroma**：零配置，原型 / 本地单机
- **Milvus**：分布式，亿级以上向量
- **Qdrant**：Rust，性能优秀，**支持元数据过滤**
- **PgVector**：复用 Postgres，事务一致性
- **FAISS**：库不是服务，纯内存索引；适合嵌入到应用进程

#### L3 索引与检索
- 距离度量：cosine / inner product / L2
- 索引算法：HNSW / IVF / IVF+PQ；权衡 **召回率 vs 延迟 vs 内存**
- 检索：top-k + 阈值；**MMR（最大边际相关性）** 提升多样性
- 过滤：metadata where 子句 + 向量重排
- 重排序（Re-ranking）：交叉编码器 `bge-reranker`、Cohere Rerank

#### L4 RAG 全链路
```
原始文档 → Loader → Splitter（chunk + overlap）→ Embedding
   → VectorStore（含 metadata）
   → 用户问题 → Embedding → 检索 top-k → 可选 Re-rank
   → Prompt 拼装（system + context + question）→ LLM → 答案
   → 引用与可观测（trace + 命中片段）
```
- **常见坑**：切片粒度、表格 / 代码片段丢失、答非所问、引用幻觉、敏感词
- **进阶**：**Hybrid Search**（向量 + BM25）、**HyDE**、**Query Rewrite**、**Self-RAG**

### M. 模型微调与推理部署

依据：`raw/学习地图.md` 阶段七

#### M1 何时微调
- 优先级：**Prompt > RAG > Function Calling > 微调**
- 微调适合：稳定风格、领域术语、特定 JSON 输出格式、降本（小模型微调替代大模型）

#### M2 微调技术
- **LoRA / QLoRA**：低秩适配，少参数高效微调；显存友好
- **SFT 指令微调**：构造 `instruction / input / output` 数据集
- **DPO / RLHF**：偏好数据训练（进阶）
- 工具：HuggingFace **PEFT** + **transformers** Trainer；**LLaMA-Factory**（图形 / CLI 一站式）

#### M3 推理部署
- **vLLM**：工业级推理引擎；PagedAttention、连续 batching、高吞吐低延迟；OpenAI 兼容 API
- **Ollama**：私有化分发、`Modelfile` 自定义模型
- **TGI（Text Generation Inference）**：HuggingFace 出品
- 关键指标：**TTFT**（首 token 时延）、**TPS**（每秒 token）、**P99 延迟**、显存占用

### N. 企业级工程化落地

依据：`raw/学习地图.md` 阶段八

- **容器化**：Dockerfile 多阶段、小镜像（distroless / `python:3.11-slim`）
- **CI/CD**：GitHub Actions / GitLab CI；流程 = lint → test → build → push → deploy
- **日志**：`logging` + `loguru` 结构化输出；接 Loki / ELK
- **指标**：Prometheus + Grafana；LLM 关键指标——**调用量 / token 用量 / 命中率 / 失败率 / 延迟分布**
- **追踪**：OpenTelemetry；为 RAG / Agent 步骤记录跨度（span）
- **项目结构**：`router / service / repository` 分层（与 Java 经验一致）
- **安全**：JWT、速率限制（`slowapi`）、内容过滤、提示词注入防护、密钥管理（Vault / KMS）
- **成本与配额**：用户级 / 接口级 token quota、降级模型策略

---

## 六、推荐学习节奏

```
周 1－2  ：A～C 巩固 + D1/D2 推导式与生成器
周 3－4  ：D3/D4 OOP & 装饰器/上下文/魔术方法
周 5     ：E 类型 & 异步
周 6     ：F 工程化（pytest + ruff + 标准库）
周 7－8  ：G NumPy & Pandas（动手清洗一份 ≥10 万行 CSV）
周 9－10 ：H FastAPI（CRUD + JWT + TestClient 全绿）
周 11    ：I 容器化 + 反向代理 + 日志指标
周 12    ：J LLM 调用（含流式与 Function Calling）
周 13－14：K LangChain + Agent 入门（LangGraph 小流程）
周 15    ：L 嵌入 + 向量库 + 一个完整 RAG
周 16    ：M 推理部署（vLLM / Ollama）+ 可选微调
周 17+   ：N 企业级（CI/CD + 监控 + 安全）
```

---

## 七、五个递进式实战项目（建议按序）

依据：`raw/学习地图.md` 章节末尾

1. **数据 + API 服务**：Pandas 清洗 10 万行 CSV → FastAPI 提供查询 API → pytest 全覆盖
2. **本地聊天机器人**：Ollama 部署模型（如 `qwen3`） → FastAPI 包装 → 前端 SSE 流式渲染
3. **RAG 知识库问答**：LangChain + Chroma → PDF 上传 → 多轮对话 + 引用片段
4. **Agent 工具调用**：让模型查询天气 API 并总结成日报；要求带工具白名单与 trace
5. **企业级部署**：任一上述项目 → Docker → GitHub Actions（lint/test/build/push）→ 接 Prometheus 指标 + Grafana 大盘

---

## 八、与本 vault 现有笔记的对应表

| 本文章节 | vault 中现有依据 |
|----------|------------------|
| A1～A6  | `wiki/concepts/data-types.md`、`control-flow.md`、`string-formatting.md`、`file-io.md`、`functions.md`、`exception-handling.md` |
| B       | `wiki/topics/python-data-model.md` |
| C       | `wiki/topics/python-module-system.md`、`concepts/modules-and-packages.md`、`virtual-environment.md` |
| D1      | `wiki/concepts/list-comprehension.md` |
| D2      | `wiki/concepts/iterators-and-generators.md` |
| D3      | `wiki/concepts/classes-and-oop.md` |
| F3      | `wiki/concepts/standard-library.md` |
| G1      | `wiki/topics/numpy-numerical-foundations.md`、`concepts/broadcasting-rules.md`、`view-vs-copy.md`、`dtype-and-memory.md`、`entities/numpy.md`、`raw/Numpy_开发文档.md` |
| H1～H6  | `wiki/topics/fastapi-api-engineering.md`、`entities/fastapi.md`、`concepts/dependency-injection.md`、`api-security.md` |
| I       | `wiki/concepts/deployment-strategy.md` |
| J～N    | `wiki/topics/enterprise-llm-engineering-roadmap.md`、`raw/学习地图.md` |

---

## 九、知识库尚未单独立页的"待写清单"

下面这些条目本文给了纲要，但本 vault 暂未对应独立 wiki 笔记；建议后续按 `要讲解：【XX】` 流程逐一沉淀：

- 装饰器 / `functools.wraps` / 带参装饰器
- 上下文管理器 / `contextlib.contextmanager` / `@asynccontextmanager`
- 魔术方法（运算符 / 容器 / 可调用 / 上下文）
- 类型提示进阶（`Protocol`、`TypedDict`、泛型、`Annotated`）
- `asyncio` 与异步 I/O 实战
- Pandas / Matplotlib / Seaborn 详细页
- Pydantic v2 详细页
- OpenAI 兼容 API 调用与流式输出
- LangChain LCEL / LangGraph
- 向量库选型对比（Chroma / Milvus / Qdrant / PgVector）
- LoRA / vLLM / Ollama 实操
- OpenTelemetry + Prometheus + Grafana for LLM

---

## 十、参考来源

- 本仓库：`raw/学习地图.md`（Java→AI 8 阶段路线）
- 本仓库：`wiki/topics/python-fundamentals.md`、`python-data-model.md`、`python-module-system.md`
- 本仓库：`wiki/topics/numpy-numerical-foundations.md`、`fastapi-api-engineering.md`
- 本仓库：`wiki/topics/enterprise-llm-engineering-roadmap.md`
- 外部权威：
  - Python Tutorial：https://docs.python.org/3/tutorial/
  - NumPy User Guide：https://numpy.org/doc/stable/user/
  - Pandas User Guide：https://pandas.pydata.org/docs/user_guide/
  - FastAPI Tutorial：https://fastapi.tiangolo.com/tutorial/
  - Pydantic：https://docs.pydantic.dev/latest/
  - LangChain：https://python.langchain.com/docs/
  - LlamaIndex：https://docs.llamaindex.ai/
  - Chroma：https://docs.trychroma.com/
  - Milvus：https://milvus.io/docs
  - Qdrant：https://qdrant.tech/documentation/
  - Ollama：https://docs.ollama.com/
  - vLLM：https://docs.vllm.ai/
  - HuggingFace PEFT：https://huggingface.co/docs/peft/index
  - LLaMA-Factory：https://github.com/hiyouga/LLaMA-Factory
  - MTEB Leaderboard：https://huggingface.co/spaces/mteb/leaderboard
  - Full Stack FastAPI 模板：https://github.com/tiangolo/full-stack-fastapi-template
