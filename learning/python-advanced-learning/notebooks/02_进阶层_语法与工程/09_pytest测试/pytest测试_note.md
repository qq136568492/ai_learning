# pytest 测试｜从小白到能用的系统讲义

<参考资料>

- https://docs.pytest.org/en/stable/getting-started.html ：pytest 入门与测试发现
- https://docs.pytest.org/en/stable/how-to/assert.html ：断言与失败解释
- https://docs.pytest.org/en/stable/how-to/fixtures.html ：fixtures
- https://docs.pytest.org/en/stable/how-to/parametrize.html ：参数化测试
- https://docs.pytest.org/en/stable/how-to/monkeypatch.html ：monkeypatch
- https://pytest-asyncio.readthedocs.io/ ：异步测试插件
- https://pytest-cov.readthedocs.io/ ：覆盖率插件

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/standard-library.md`：`doctest`、`unittest`、标准库工程基线
- `obsidian-vault/LLM_Learning/wiki/concepts/functions.md`：函数、断言对象、参数化输入输出
- `obsidian-vault/LLM_Learning/wiki/concepts/exception-handling.md`：异常断言与错误路径
- `obsidian-vault/LLM_Learning/wiki/concepts/asyncio-in-practice.md`：异步测试的前置知识
- `obsidian-vault/LLM_Learning/wiki/topics/fastapi-api-engineering.md` 与 `raw/FastAPI_官方文档.md`：API 工程中的测试、依赖覆盖、异步测试
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md` 与 `raw/Python进阶到AI应用_完整学习地图.md`：F1 工程化基础，pytest、覆盖率、mock、异步测试

---

## 小白视角：原文教学漏洞与本版修复

| 教学漏洞 | 小白会卡在哪里 | 本版修复 |
|---|---|---|
| 直接讲 pytest 功能点 | 不知道为什么要测试、测什么、怎么组织 | 新增测试动机、AAA 模式和目录结构 |
| 发现规则过短 | 用例不运行却不知道原因 | 新增文件名/函数名/命令/常见不发现问题 |
| fixture 抽象 | 不知道它和普通 helper 有什么区别 | 新增 setup/teardown 生命周期图和例子 |
| 参数化缺少场景 | 不知道什么时候用表驱动 | 新增输入输出表格式测试 |
| 异常测试不够完整 | 只测正常路径，错误路径漏掉 | 新增 `pytest.raises` 和 `match` |
| 临时文件、环境变量、日志测试缺失 | 工程里仍然污染真实环境 | 新增 `tmp_path`、`monkeypatch`、`caplog` |
| mock 边界不清 | 容易 mock 到只测试自己的假实现 | 新增 mock/monkeypatch 适用边界 |
| 缺少练习答案 | 自学无法判断测试是否靠谱 | 新增三档练习与参考答案 |

---

## 上一章核心收获回顾（衔接「asyncio」）

- 你已经知道异步函数需要事件循环驱动，`async def` 调用后得到协程对象。
- 你已经知道 I/O 调用要设置超时，不能让任务无限等待。
- 你已经知道错误路径、取消路径和阻塞调用都需要被显式考虑。
- 这些边界如果只靠人工记忆，很容易在重构时被破坏。
- 测试就是把这些“应该一直成立”的规则写成机器可重复执行的检查。

但是，我们遇到了一个新问题……

代码现在能跑，但以后改一行会不会破坏旧行为？异常路径有没有测？异步超时有没有测？手动点几下程序不可靠，也不适合团队协作。

因此本章需要：学习 pytest，把函数行为、异常路径、文件副作用、环境变量、日志、异步任务等变成可自动执行的测试网。

---

## 本章学习目标

学完本章，你应该能做到：

1. 创建 `tests/` 目录并让 pytest 自动发现测试。
2. 用普通 `assert` 写清楚预期结果。
3. 用 AAA 结构组织测试：Arrange、Act、Assert。
4. 用 `@pytest.mark.parametrize` 测多组输入输出。
5. 用 fixture 管理准备和清理逻辑。
6. 用 `pytest.raises` 测异常路径。
7. 用 `tmp_path`、`monkeypatch`、`caplog` 测文件、环境变量和日志。
8. 了解异步测试、覆盖率和 CI 中的基本用法。

---

## 前置知识极速补齐

### 1. 什么是测试

测试就是用代码表达预期行为。

```python
def add(a: int, b: int) -> int:
    return a + b


def test_add() -> None:
    assert add(1, 2) == 3
```

如果以后有人把 `add` 写错，测试会失败。

### 2. AAA 结构

一条测试通常分三段：

- Arrange：准备数据。
- Act：执行被测行为。
- Assert：断言结果。

```python
def test_discount() -> None:
    price = 100  # Arrange
    result = price * 0.8  # Act
    assert result == 80  # Assert
```

---

## 动机：有回归网，才敢重构

没有测试时，重构靠感觉。你改了实现，只能手动试几个路径，容易漏掉边界。

有测试时，旧行为被写成一组可重复执行的检查。你可以更快发现：哪条规则被破坏了，破坏发生在哪里。

---

## 类比：出厂质检

测试像工厂里的质检量具。每个产品出厂前都过同一套检查。不是等客户投诉才知道尺寸不对，而是在生产线上立刻发现。

pytest 就是把这些量具组织起来并批量运行的工具。

---

## 核心定义：pytest 是什么

pytest 是 Python 测试框架。它能自动发现测试文件和测试函数，运行其中的断言，并给出清晰的失败信息。它也提供 fixture、参数化、临时目录、monkeypatch、插件生态等工程能力。

最小运行：

```bash
pip install pytest
pytest -q
```

---

## 精讲一：测试发现规则

推荐目录结构：

```text
project/
  src/
    calculator.py
  tests/
    test_calculator.py
```

pytest 默认会发现：

- 文件名形如 `test_*.py` 或 `*_test.py`。
- 函数名以 `test_` 开头。
- 类名以 `Test` 开头，且方法名以 `test_` 开头。

最小例子：

```python
# tests/test_calculator.py


def add(a: int, b: int) -> int:
    return a + b


def test_add() -> None:
    assert add(1, 2) == 3
```

运行：

```bash
pytest -q
```

---

## 精讲二：普通 assert 就够用

```python
def test_list_append() -> None:
    items = []
    items.append("a")
    assert items == ["a"]
```

pytest 会增强 `assert` 的失败输出，让你看到实际值和期望值差异。

不要写成：

```python
def test_something() -> None:
    assert True
```

这种测试没有检查真实行为。

---

## 精讲三：参数化，避免复制多条类似测试

```python
import pytest


@pytest.mark.parametrize(
    "text, expected",
    [
        (" ada ", "Ada"),
        ("BOB", "Bob"),
        ("", ""),
    ],
)
def test_title(text: str, expected: str) -> None:
    assert text.strip().title() == expected
```

适合：同一逻辑，多组输入输出。

---

## 精讲四：fixture 管理准备和清理

fixture 是测试的“准备材料”。

```python
import pytest


@pytest.fixture
def user() -> dict[str, str]:
    return {"name": "Ada", "email": "ada@example.com"}


def test_user_name(user: dict[str, str]) -> None:
    assert user["name"] == "Ada"
```

带清理逻辑的 fixture：

```python
import pytest


@pytest.fixture
def fake_db():
    db = {"users": []}
    yield db
    db["users"].clear()


def test_add_user(fake_db) -> None:
    fake_db["users"].append("Ada")
    assert fake_db["users"] == ["Ada"]
```

`yield` 前是 setup，`yield` 后是 teardown。

---

## 精讲五：测试异常路径

```python
import pytest


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="zero"):
        divide(1, 0)
```

错误路径和正常路径一样重要。只测 happy path，覆盖不了真实系统。

---

## 精讲六：`tmp_path` 测文件，不污染项目目录

```python
def test_write_file(tmp_path) -> None:
    file = tmp_path / "hello.txt"
    file.write_text("hello", encoding="utf-8")
    assert file.read_text(encoding="utf-8") == "hello"
```

`tmp_path` 是 pytest 内置 fixture，会给每条测试提供临时目录。

---

## 精讲七：`monkeypatch` 临时改环境变量或函数

```python
import os


def get_mode() -> str:
    return os.environ.get("APP_MODE", "dev")


def test_get_mode(monkeypatch) -> None:
    monkeypatch.setenv("APP_MODE", "test")
    assert get_mode() == "test"
```

测试结束后，pytest 会帮你恢复 monkeypatch 做过的修改。

适合：环境变量、当前目录、临时替换函数、隔离外部依赖。

---

## 精讲八：`caplog` 测日志

```python
import logging


log = logging.getLogger(__name__)


def do_work() -> None:
    log.warning("slow path")


def test_log_warning(caplog) -> None:
    with caplog.at_level(logging.WARNING):
        do_work()
    assert "slow path" in caplog.text
```

适合：确认关键异常、降级、审计日志确实出现。

---

## 精讲九：异步测试

安装：

```bash
pip install pytest-asyncio
```

示例：

```python
import asyncio
import pytest


async def async_add(a: int, b: int) -> int:
    await asyncio.sleep(0)
    return a + b


@pytest.mark.asyncio
async def test_async_add() -> None:
    assert await async_add(1, 2) == 3
```

团队要统一插件和配置，不要每个项目各写一套异步测试入口。

---

## 辨析：容易混淆的概念

### 1. helper 函数 vs fixture

| 对比项 | helper 函数 | fixture |
|---|---|---|
| 调用方式 | 手动调用 | 作为测试参数自动注入 |
| 适合 | 普通计算、构造小对象 | 共享准备、清理、临时资源 |
| 清理 | 自己写 | 可用 `yield` teardown |

### 2. 单元测试 vs 集成测试

| 类型 | 关注点 | 例子 |
|---|---|---|
| 单元测试 | 一个函数/类的局部行为 | `discount(price)` |
| 集成测试 | 多个组件协作 | API + DB + 配置 |

### 3. mock/monkeypatch 何时用

| 适合 mock | 不适合 mock |
|---|---|
| 外部 HTTP、时间、随机、环境变量 | 被测核心业务本身 |

---

## 陷阱：高频错误与改法

### 陷阱 1：测试文件或函数命名不对

问题：pytest 找不到测试。

改法：文件用 `test_xxx.py`，函数用 `test_xxx()`。

### 陷阱 2：测试没有断言

```python
def test_add() -> None:
    add(1, 2)
```

这只证明“没报错”，没有证明结果正确。

### 陷阱 3：fixture 作用域过大导致状态污染

如果 `scope="session"` 的 fixture 返回可变对象，多条测试可能互相影响。

改法：默认用 function 作用域；需要共享时返回工厂函数或每次复制数据。

### 陷阱 4：过度 mock

如果把核心逻辑都 mock 掉，测试只是在验证 mock 的返回值。

改法：mock 外部边界，不 mock 被测核心。

### 陷阱 5：只测正常路径

改法：补充异常、空输入、边界值、超时、权限失败等路径。

---

## 双重示例 A：极简入门 Demo，参数化测试

```python
import pytest


def normalize(text: str) -> str:
    return text.strip().lower()


@pytest.mark.parametrize(
    "text, expected",
    [
        (" Hello ", "hello"),
        ("PYTHON", "python"),
        ("", ""),
    ],
)
def test_normalize(text: str, expected: str) -> None:
    assert normalize(text) == expected
```

运行：

```bash
pytest -q
```

---

## 双重示例 B：工程最小切片，配置读取测试

```python
import os
from pathlib import Path


def load_config(path: Path) -> dict[str, str]:
    content = path.read_text(encoding="utf-8")
    items = {}
    for line in content.splitlines():
        key, value = line.split("=", 1)
        items[key] = value
    items["mode"] = os.environ.get("APP_MODE", "dev")
    return items


def test_load_config(tmp_path, monkeypatch) -> None:
    config = tmp_path / "app.env"
    config.write_text("host=127.0.0.1\nport=8000", encoding="utf-8")
    monkeypatch.setenv("APP_MODE", "test")

    result = load_config(config)

    assert result == {
        "host": "127.0.0.1",
        "port": "8000",
        "mode": "test",
    }
```

这个例子同时使用了 `tmp_path` 和 `monkeypatch`，避免污染真实文件和真实环境变量。

---

## 适用范围与边界

适合优先测试：

- 纯函数和核心规则。
- 容易出错的边界条件。
- 异常路径。
- 文件、环境变量、配置解析。
- API 输入输出和权限边界。

不建议一开始就追求：

- 100% 覆盖率数字。
- 大量脆弱快照。
- 对内部实现细节过度断言。
- 把所有外部依赖都真实调用一遍。

---

## 练习

### 基础题：写参数化测试

```python
import pytest


def clamp(x: int, lo: int, hi: int) -> int:
    return max(lo, min(x, hi))


@pytest.mark.parametrize(
    "x, lo, hi, expected",
    [
        (5, 1, 10, 5),
        (-1, 0, 10, 0),
        (20, 0, 10, 10),
    ],
)
def test_clamp(x: int, lo: int, hi: int, expected: int) -> None:
    assert clamp(x, lo, hi) == expected
```

### 进阶题：fixture + 异常断言

```python
import pytest


@pytest.fixture
def users() -> dict[str, int]:
    return {"Ada": 18}


def get_age(users: dict[str, int], name: str) -> int:
    if name not in users:
        raise KeyError(name)
    return users[name]


def test_get_age(users: dict[str, int]) -> None:
    assert get_age(users, "Ada") == 18


def test_get_age_missing(users: dict[str, int]) -> None:
    with pytest.raises(KeyError):
        get_age(users, "Bob")
```

### 开放题：为项目加测试策略

参考方向：

- 每个核心纯函数至少有正常值、边界值、异常值。
- 外部 HTTP 用 mock 或测试替身。
- 文件和环境变量用 `tmp_path` / `monkeypatch`。
- CI 中运行 `pytest -q`，必要时加 `pytest --cov`。

---

## 费曼反问

1. pytest 为什么能自动找到你的测试？
2. fixture 和普通 helper 函数有什么区别？
3. 为什么异常路径也应该写测试？
4. 什么情况下应该用 `monkeypatch`？
5. 覆盖率高是否等于测试质量高？

---

## 本章闭环

不看资料，尝试口述：

> pytest 是 Python 测试框架，会自动发现 `test_*.py` 和 `test_` 函数。测试用普通 `assert` 表达预期，常用 AAA 结构组织。参数化适合同一逻辑多组输入输出，fixture 适合准备和清理资源，`pytest.raises` 用于异常路径，`tmp_path` 和 `monkeypatch` 用于隔离文件和环境变量。测试要关注行为和边界，不要过度 mock 核心逻辑。

---

## 来源分层

本地知识库文件：

- `obsidian-vault/LLM_Learning/wiki/concepts/standard-library.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/functions.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/exception-handling.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/asyncio-in-practice.md`
- `obsidian-vault/LLM_Learning/wiki/topics/fastapi-api-engineering.md`
- `obsidian-vault/LLM_Learning/raw/FastAPI_官方文档.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md`

外部补充：

- https://docs.pytest.org/en/stable/getting-started.html
- https://docs.pytest.org/en/stable/how-to/fixtures.html
- https://docs.pytest.org/en/stable/how-to/parametrize.html
- https://docs.pytest.org/en/stable/how-to/monkeypatch.html
- https://pytest-asyncio.readthedocs.io/
- https://pytest-cov.readthedocs.io/
