# 类型提示｜从小白到能用的系统讲义

<参考资料>

- https://docs.python.org/3/library/typing.html ：标准库 `typing`
- https://docs.python.org/3/tutorial/controlflow.html#function-annotations ：函数注解
- https://docs.python.org/3/library/typing.html#typing.Protocol ：`Protocol`
- https://docs.python.org/3/library/typing.html#typing.TypedDict ：`TypedDict`
- https://docs.python.org/3/library/typing.html#typing.Annotated ：`Annotated`
- https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html ：mypy 类型速查表
- https://microsoft.github.io/pyright/ ：pyright 类型检查器

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/functions.md`：函数注解、参数、返回值、`*args/**kwargs`
- `obsidian-vault/LLM_Learning/wiki/topics/python-fundamentals.md`：一切皆对象、动态类型、基础学习路径
- `obsidian-vault/LLM_Learning/wiki/topics/python-data-model.md`：对象的身份、类型和值，可变性与字典键
- `obsidian-vault/LLM_Learning/wiki/concepts/classes-and-oop.md`：类作为类型、鸭子类型、组合优于继承
- `obsidian-vault/LLM_Learning/raw/FastAPI_官方文档.md`：类型提示在 FastAPI 中驱动请求解析、校验与文档生成
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md` 与 `raw/Python进阶到AI应用_完整学习地图.md`：类型系统属于 Python 进阶层 E1，连接 FastAPI/Pydantic/API 工程

---

## 小白视角：原文教学漏洞与本版修复

| 教学漏洞 | 小白会卡在哪里 | 本版修复 |
|---|---|---|
| 直接进入 `Protocol` / `TypedDict` | 不知道普通变量、函数、列表、字典怎么标注 | 新增基础类型提示语法路线 |
| “注解不运行时强制”讲得不够具体 | 以为写了 `x: int` 就不会传入字符串 | 新增运行时反例与工具边界 |
| 缺少类型检查工具闭环 | 不知道 mypy/pyright 怎么参与开发 | 新增本地检查命令和最小配置思路 |
| `Any` 风险不够突出 | 用 `Any` 后类型检查形同关闭 | 新增 `Any` vs `object` 辨析 |
| `Protocol` 抽象 | 不知道它和继承、ABC、鸭子类型有什么关系 | 新增生活类比和最小可运行例子 |
| `TypedDict` / `Annotated` 缺少场景 | 不知道什么时候该用，什么时候该上 Pydantic | 新增 JSON/API 场景边界 |
| 缺少练习答案 | 自学无法确认写法 | 新增基础/进阶/开放题答案 |

---

## 上一章核心收获回顾（衔接「魔术方法」）

- 你已经知道对象的类型决定它支持哪些操作，例如 `len(obj)`、`obj + other`。
- 你已经知道 Python 是动态类型语言，变量本身不需要提前声明类型。
- 你已经写过函数参数和返回值，也见过 `def add(a: int, b: int) -> int` 这种写法。
- 你已经知道 `is` 和 `==` 不同，类型、值、身份是对象的不同维度。
- 你即将学习一种“不改变运行时逻辑，但提升可读性、补全、检查能力”的工具：类型提示。

但是，我们遇到了一个新问题……

项目变大后，函数之间传来传去的对象越来越多。如果不写类型，读代码的人要猜：这个参数是 `str` 还是 `Path`？这个函数会不会返回 `None`？这个字典里到底有哪些键？这些问题经常要运行到出错时才暴露。

因此本章需要：学习类型提示，用清晰的注解表达代码契约，让 IDE、mypy、pyright 和团队成员能更早发现不匹配，而不是等线上报错。

---

## 本章学习目标

学完本章，你应该能做到：

1. 给变量、函数参数、返回值、列表、字典写基础类型提示。
2. 解释“类型提示默认不做运行时校验”。
3. 使用 `T | None`、`Literal`、`TypedDict`、`Protocol`、`Callable` 表达常见结构。
4. 知道 `Any`、`object`、具体类型的区别。
5. 理解 `Annotated` 的用途：类型本身 + 额外元数据。
6. 用 mypy 或 pyright 做一次静态类型检查。
7. 判断什么时候类型提示够用，什么时候需要 Pydantic 或手写校验。

---

## 前置知识极速补齐

### 1. Python 是动态类型，但对象仍然有类型

```python
x = "hello"
print(type(x))  # <class 'str'>

x = 123
print(type(x))  # <class 'int'>
```

Python 允许同一个变量名先后绑定不同类型的对象。类型提示不会改变这个机制，它只是给人和工具看的“说明书”。

### 2. 函数注解的最小写法

```python
def add(a: int, b: int) -> int:
    return a + b
```

含义：

- `a: int` 表示希望 `a` 是整数。
- `b: int` 表示希望 `b` 是整数。
- `-> int` 表示函数应该返回整数。

### 3. 类型提示默认不阻止运行

```python
def add(a: int, b: int) -> int:
    return a + b


print(add("x", "y"))  # xy，Python 运行时默认不会因为注解报错
```

结论：类型提示主要服务于 IDE、静态检查器和团队阅读。外部输入仍然需要运行时校验。

---

## 动机：越早发现类型错，修复成本越低

没有类型提示：

```python
def send_email(user, retry):
    ...
```

读者要猜：

- `user` 是字符串、字典、还是对象？
- `retry` 是布尔值、次数、还是重试策略？
- 函数返回什么？

有类型提示：

```python
class User:
    def __init__(self, email: str) -> None:
        self.email = email


def send_email(user: User, retry: int = 3) -> bool:
    ...
```

读者和工具都更容易理解接口。

---

## 类比：食品包装上的成分表

类型提示像食品包装上的成分表。它不改变食物本身，但能让购买者和检查员更快判断：里面有什么、适不适合你、有没有明显不匹配。

如果你真的要保证食物安全，还需要检测流程。对应到程序里，就是 Pydantic、表单校验、手写校验、数据库约束等运行时机制。

---

## 核心定义：什么是类型提示

类型提示是 Python 代码中的注解，用来描述变量、函数参数、返回值、类属性等期望的类型。它默认不改变运行时行为，但能帮助 IDE 补全、静态检查、文档生成和框架校验。

最常见位置：

```python
name: str = "Ada"
age: int = 18
scores: list[int] = [90, 95]


def greet(name: str) -> str:
    return f"Hello, {name}"
```

---

## 精讲一：基础类型与容器类型

```python
name: str = "Ada"
age: int = 18
price: float = 9.9
active: bool = True

names: list[str] = ["Ada", "Bob"]
scores: dict[str, int] = {"Ada": 95, "Bob": 88}
point: tuple[int, int] = (1, 2)
tags: set[str] = {"python", "typing"}
```

常见写法：

- `list[str]`：字符串列表。
- `dict[str, int]`：键是字符串，值是整数的字典。
- `tuple[int, int]`：两个整数组成的元组。
- `set[str]`：字符串集合。

---

## 精讲二：可选值与联合类型

如果一个值可能是字符串，也可能是 `None`：

```python
def normalize_name(name: str | None) -> str:
    if name is None:
        return "anonymous"
    return name.strip().title()
```

`str | None` 的意思是：这个值可以是 `str`，也可以是 `None`。

老写法：

```python
from typing import Optional


def normalize_name(name: Optional[str]) -> str:
    ...
```

在 Python 3.10+ 中，优先使用 `str | None`。

---

## 精讲三：`Any`、`object`、具体类型

| 类型 | 含义 | 检查强度 |
|---|---|---|
| `Any` | 什么都行，工具基本不检查 | 最弱 |
| `object` | 可以传任何对象，但使用前要收窄 | 中等 |
| `str` / `int` / 自定义类 | 明确类型 | 最强 |

`Any` 示例：

```python
from typing import Any


def handle(value: Any) -> None:
    value.not_exist_method()  # 类型检查器通常不会拦
```

`object` 示例：

```python
def handle(value: object) -> None:
    if isinstance(value, str):
        print(value.upper())
```

工程建议：不要把 `Any` 当万能胶。能写具体类型就写具体类型，不确定时优先用 `object` 再收窄。

---

## 精讲四：`Literal` 表达固定可选值

```python
from typing import Literal


Mode = Literal["read", "write", "append"]


def open_resource(mode: Mode) -> None:
    print(mode)


open_resource("read")
# open_resource("delete")  # 类型检查器会提示不匹配
```

适合：状态、模式、少量固定字符串选项。

---

## 精讲五：`TypedDict` 描述字典形状

普通字典类型只能描述键和值的大类：

```python
user: dict[str, str] = {"name": "Ada", "email": "a@example.com"}
```

如果你想描述固定字段，可以用 `TypedDict`。

```python
from typing import TypedDict


class UserPayload(TypedDict):
    name: str
    email: str
    age: int


def send_welcome(user: UserPayload) -> str:
    return f"hello {user['name']}"
```

适合：小型 JSON、配置、API payload 的静态形状说明。

边界：如果要运行时校验、类型转换、错误消息，使用 Pydantic 或手写校验更合适。

---

## 精讲六：`Protocol` 描述“只要会做某事”

白话：不关心对象属于哪个类，只关心它有没有某个方法。

```python
from typing import Protocol


class Readable(Protocol):
    def read(self) -> str:
        ...


class FileLike:
    def read(self) -> str:
        return "data"


def load(reader: Readable) -> str:
    return reader.read()


print(load(FileLike()))
```

`FileLike` 没有继承 `Readable`，但它有 `read()` 方法，所以在静态类型意义上符合协议。

适合：插件、适配器、依赖注入、只关心行为不关心具体类的场景。

---

## 精讲七：`Callable` 描述函数形状

```python
from collections.abc import Callable


Processor = Callable[[str], str]


def apply(text: str, processor: Processor) -> str:
    return processor(text)


def strip_text(text: str) -> str:
    return text.strip()


print(apply(" hello ", strip_text))
```

含义：`Processor` 是一个函数类型，接收一个 `str`，返回一个 `str`。

---

## 精讲八：`Annotated` 表达“类型 + 元数据”

```python
from typing import Annotated


UserId = Annotated[int, "must be positive"]


def get_user(user_id: UserId) -> str:
    return f"user-{user_id}"
```

Python 本身不会因为 `"must be positive"` 自动校验。`Annotated` 的价值在于：框架或工具可以读取这些额外信息。

FastAPI/Pydantic 中常见用途：给参数增加校验规则、描述、示例、OpenAPI 元数据。

---

## 精讲九：类型检查工具怎么用

可选安装：

```bash
pip install mypy pyright
```

运行：

```bash
mypy path/to/file.py
pyright path/to/file.py
```

建议团队策略：

- 新代码尽量补齐函数入参和返回值。
- 公共 API 必须写类型。
- 边界数据不要用裸 `dict` 到处传。
- 逐步减少 `Any`，不要追求一天全项目清零。

---

## 辨析：容易混淆的概念

### 1. 类型提示 vs 运行时校验

| 对比项 | 类型提示 | 运行时校验 |
|---|---|---|
| 何时发生 | 写代码、静态检查、CI | 程序运行时 |
| 工具 | IDE、mypy、pyright | Pydantic、手写 if、数据库约束 |
| 能否拦住真实用户输入 | 不能直接拦 | 可以 |

### 2. `TypedDict` vs Pydantic

| 工具 | 作用 | 适合 |
|---|---|---|
| `TypedDict` | 静态描述 dict 结构 | 内部小型 payload |
| Pydantic | 运行时校验、转换、错误消息 | API 请求体、配置、外部输入 |

### 3. `Protocol` vs 继承

| 方式 | 关注点 | 适合 |
|---|---|---|
| 继承 | “它是谁的子类” | 共享实现、明确层级 |
| `Protocol` | “它会做什么” | 插件、适配器、鸭子类型 |

---

## 陷阱：高频错误与改法

### 陷阱 1：以为注解会自动校验

```python
def double(x: int) -> int:
    return x * 2


print(double("ha"))  # hahaha，不会自动报类型错
```

改法：对外部输入使用运行时校验。

### 陷阱 2：滥用 `Any`

```python
from typing import Any


def process(data: Any) -> Any:
    return data["missing"].do_something()
```

改法：用 `TypedDict`、具体类、`Protocol` 或 `object + isinstance` 替代。

### 陷阱 3：返回值漏写 `None`

```python
def find_user(name: str) -> str:
    if name == "Ada":
        return "Ada"
    return None  # 类型不匹配
```

改法：

```python
def find_user(name: str) -> str | None:
    if name == "Ada":
        return "Ada"
    return None
```

### 陷阱 4：用 `dict[str, Any]` 传遍全项目

问题：短期省事，长期每个调用点都要猜字段。

改法：内部结构用 `TypedDict` 或 dataclass，外部输入用 Pydantic。

---

## 双重示例 A：极简入门 Demo，用户格式化

```python
def format_user(name: str, age: int | None = None) -> str:
    if age is None:
        return name.title()
    return f"{name.title()} ({age})"


assert format_user("ada") == "Ada"
assert format_user("ada", 18) == "Ada (18)"
```

---

## 双重示例 B：工程最小切片，API payload

```python
from typing import Literal, TypedDict


class CreateUserPayload(TypedDict):
    name: str
    email: str
    role: Literal["admin", "member"]


def build_welcome(payload: CreateUserPayload) -> str:
    return f"Welcome {payload['name']} as {payload['role']}"


user: CreateUserPayload = {
    "name": "Ada",
    "email": "ada@example.com",
    "role": "member",
}

print(build_welcome(user))
```

工程边界：这个例子只做静态说明；如果 payload 来自 HTTP 请求，还需要运行时校验。

---

## 适用范围与边界

适合类型提示：

- 公共函数、服务方法、库 API。
- 数据结构复杂的参数和返回值。
- 团队协作频繁修改的模块。
- IDE 补全和重构收益明显的代码。

不能只靠类型提示：

- 用户输入。
- 网络请求体。
- 配置文件。
- 数据库返回值。
- LLM 输出或第三方 API 响应。

这些场景需要运行时校验。

---

## 练习

### 基础题：给函数补类型

```python
def total(prices: list[float]) -> float:
    return sum(prices)


assert total([1.0, 2.5]) == 3.5
```

### 进阶题：写 `Protocol`

要求：描述一个带 `.close()` 方法的资源。

参考答案：

```python
from typing import Protocol


class SupportsClose(Protocol):
    def close(self) -> None:
        ...


def close_all(resources: list[SupportsClose]) -> None:
    for resource in resources:
        resource.close()
```

### 开放题：何时用 `TypedDict`，何时用 Pydantic

参考方向：内部静态结构用 `TypedDict`；外部输入、需要校验和转换时用 Pydantic。

---

## 费曼反问

1. 为什么说类型提示默认不负责运行时安全？
2. `Any` 和 `object` 的区别是什么？
3. `str | None` 想表达什么？
4. `Protocol` 为什么适合鸭子类型？
5. API 请求体为什么不能只靠 `TypedDict`？

---

## 本章闭环

不看资料，尝试口述：

> 类型提示是写给人、IDE 和静态检查器看的契约。它能提升补全、重构和提前发现错误的能力，但默认不会在运行时拦截错误输入。基础写法包括 `str`、`list[str]`、`dict[str, int]`、`T | None`。复杂结构可以用 `TypedDict`、`Protocol`、`Literal`、`Annotated`。外部输入仍要靠 Pydantic 或手写校验。

---

## 来源分层

本地知识库文件：

- `obsidian-vault/LLM_Learning/wiki/concepts/functions.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-fundamentals.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-data-model.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/classes-and-oop.md`
- `obsidian-vault/LLM_Learning/raw/FastAPI_官方文档.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md`

外部补充：

- https://docs.python.org/3/library/typing.html
- https://docs.python.org/3/tutorial/controlflow.html#function-annotations
- https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
- https://microsoft.github.io/pyright/
