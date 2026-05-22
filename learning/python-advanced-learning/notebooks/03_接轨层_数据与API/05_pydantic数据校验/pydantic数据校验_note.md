# Pydantic 数据校验｜讲义笔记

<参考资料>

- https://docs.pydantic.dev/latest/ — **Pydantic v2**

```bash
pip install pydantic
```

与 FastAPI **Body / Query** 共用生态；最小服务启动见 **`fastapi` 讲义**。

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/entities/fastapi.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **H**

---

## 上一章核心收获回顾（衔接「FastAPI 路由」）

你已能挂载 **路由**，并预览 **OpenAPI `/docs`**。

你已看到：**typing / 默认值**会直接驱动生成的 schema（框架层）。

你已准备：**把不规则 JSON** 关在门口，不要让 **`KeyError`** 渗进核心业务。

你已理解：**HTTP handler** 应保持瘦——校验与规整尽量 **声明式下沉到模型层**。

---

## 但是，我们遇到了一个新的问题……

散装 **`dict`**：缺键、类型乱、空格未 strip —— **`if`** 守门代码爆炸。**因此本章需要：**会用 **`BaseModel`、`Field`、`ValidationError`、`model_validate` / `model_dump`**；按需了解 **`model_validator`、`field_validator`**（命名以你所用 Pydantic 主版本文档为准）。

---

## 动机

坏输入在服务入口就变 **结构化错误**：返给前端/调用方可预期，也方便记录审计。

---

## 类比（非编程）

报税表：**缺必填格**当场退回，不靠办事员脑补。

---

## 精讲（由浅入深）

```python
from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(gt=0, le=140)


try:
    User(name="", age=200)
except ValidationError as e:
    err = e.errors()[0]
    assert "loc" in err and "type" in err
```

常用：**`model_dump()`**、**`model_validate(...)`** 校验外部 **`dict`**、嵌套模型、**`| None`** 表达可选字段。  
进阶：**`computed_field`、`model_config` strict** 等——对照官方 changelog / migration。  
金额慎用 **`float` 表示货币**——需 **Decimal / 自建类型**的业务约束。

---

## 辨析

| | **Pydantic** | **手写 `if`** |
|--|-----------------|---------------|
| 可读 | 字段即规格 | `if` 树难维护 |

---

## 陷阱（≥2）：成因 → 改法

1. **默认 `float64` JSON 漂移** — 金融业务改 **Decimal**。  
2. **自引用 / 前向模型** — **`from __future__ import annotations`** 与按需 **`model_rebuild`**。

---

## 适用范围 · 延伸

配置管理 **`pydantic-settings`**、ORM/DTO。**LLM** JSON-mode：解析后 **`model_validate`**。

---

## 双重示例

### A. **嵌套模型**

```python
from pydantic import BaseModel


class Addr(BaseModel):
    city: str


class Profile(BaseModel):
    user: str
    addr: Addr


p = Profile.model_validate({"user": "Ada", "addr": {"city": "BJ"}})
```

### B. **`field_validator` 清洗邮箱（示意思路）**

在 **`mode='before'`** 下 **strip + lower**；详见官方 **validators** 章节。

---

## 练习

- **基础**：写一个 **可选字段默认值**示例。  

- **进阶：**把 **`ValidationError`** 转成对用户友好的统一错误码 JSON。  

- **开放：**读 **`model_config`** 里 **`strict`** / **`extra`** 的差异。

---

## 费曼反问

1. 为何 **单靠 prompt**不能保证 JSON 完全符合业务？  
2. **`ValidationError`** 与 Python 原生 **`ValueError`** 分工？  
3. 何时拆分 **DTO** 模型与 **持久化实体**？

---

> **闭环**：口述 **`model_validate` 与 「手工 `User(**dict)`」**各有哪些工程风险差异。
