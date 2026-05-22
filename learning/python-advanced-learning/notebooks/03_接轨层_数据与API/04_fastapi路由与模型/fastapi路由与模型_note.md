# FastAPI 路由与模型｜讲义笔记

<参考资料>

- https://fastapi.tiangolo.com/tutorial/first-steps/
- https://fastapi.tiangolo.com/tutorial/body/
- `obsidian-vault/LLM_Learning/wiki/topics/fastapi-api-engineering.md`

```bash
pip install fastapi uvicorn[standard]
```

启动：**`uvicorn 模块路径:app --reload`**。**常见报错：**`ModuleNotFoundError` — 检查 venv；端口占用加 **`--port`**。

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/topics/fastapi-api-engineering.md`
- `obsidian-vault/LLM_Learning/wiki/entities/fastapi.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/dependency-injection.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **H**

---

## 上一章核心收获回顾（衔接「可视化 → HTTP 对外出口」）

你能用 **pandas 聚合、画图**把诊断摆上桌面。

你已理解：**键对齐 `merge`** 是业务表里最常见的翻车点。

你已准备：**把可被调用的行为**暴露在 **HTTP**，而不只是离线脚本。

你已具备阅读 **`async def` 路由**的背景（可先全写同步 **`def`**，再渐进迁移）。

你已知道 **REST 动词与 URL**：**GET 取资源、POST 提交体**的日常分工。

---

## 但是，我们遇到了一个新的问题……

手写 WSGI/Flask 拼装 **校验 + OpenAPI** 很贵；团队在 Postman / 前端/SDK 上对不齐契约。**FastAPI + Pydantic（下一节可加细）把 JSON 校验与 typing 前移**。**因此本章需要：**会写 **`FastAPI`、`APIRouter`、路径/查询/请求体分层、Depends 钩子、自动 `/docs`。  
**异步纪律：** **`async def` 里不要用阻塞式 `requests`/`time.sleep` 卡住 loop**——用异步客户端或 **`to_thread`**。

---

## 动机

**坏输入早一点红、好文档自动生成** ⇒ 更少 **500** 埋在最深处才被用户踩到。

---

## 类比（非编程）

机场安检：**票务与证件先行核对（模型）**，再进候机厅做托运等重体力活（handler）。

---

## 精讲（由浅入深）

```python
from fastapi import Depends, FastAPI, Query


app = FastAPI()


async def tenant(x_tenant: str | None = Query(default=None)):
    return x_tenant or "default"


@app.get("/items/{item_id}")
async def read_item(item_id: int, tenant_id: str = Depends(tenant)):
    return {"id": item_id, "tenant": tenant_id}


# 启动示例： uvicorn YOUR_FILE:app --reload
```

- **路径参数：**`{item_id:int}` …  
- **查询参数：**`Query`、`Header`、`Cookie`。  
- **请求体：**Pydantic `BaseModel`（见下一笔记）。  

**OpenAPI**：**`/openapi.json`**、Swagger **`/docs`、Redoc`。  
**Depends**：可把「解析租户」「打开 DB」「鉴权」拆成 **可组合依赖**，详见 **`dependency-injection`** wiki。

---

## 辨析

| | **路径参数** | **Query `?`** | **Body JSON** |
|--|----------------|----------------|---------------|
| 心智 | `/users/123` | 过滤分页 | 提交的整张记录 |

---

## 陷阱（≥2）：成因 → 改法

1. **`async def` + 阻塞 I/O**。 — **异步 HTTP / DB** 库或 **`to_thread`**。  
2. **`Optional` 语义误读**。 — **查 FastAPI**：缺省与必填由 **`...`、`default=None`、`Field`** 共同决定。

---

## 适用范围 · 延伸

**JWT、`HTTPBearer`、`middleware`、`lifespan`、流式 `StreamingResponse`。** **安全：**`api-security` wiki。LLM 路由见核心层讲义。

---

## 双重示例

### A. 极简｜再挂一个 **`POST /echo`**

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/echo")
def echo(payload: dict):
    return {"you_sent": payload}
```

### B. **APIRouter** 子路由挂载

```python
from fastapi import APIRouter, FastAPI

api_v1 = APIRouter(prefix="/v1")

@api_v1.get("/ping")
def ping():
    return {"ping": True}

root = FastAPI()
root.include_router(api_v1)
```

---

## 练习

- **基础**：导出 **OpenAPI YAML**，标出仍需手写的安全配置。  

- **进阶**：用 **`Depends`** 链路伪实现 **JWT 解析**（不真实连 IdP）。  

- **开放**：对比 **ASGI / WSGI** 与你的部署拓扑一句结论。

---

## 费曼反问

1. **Depends** 给单测与复用带来什么？  
2. 自动 **`/docs` 可信度**边界何在？  
3. 何种 handler 你仍会坚持写 **`def` 不写 `async def`**？

---

> **闭环**：口述 **path / query / body** 各放哪种信息。
