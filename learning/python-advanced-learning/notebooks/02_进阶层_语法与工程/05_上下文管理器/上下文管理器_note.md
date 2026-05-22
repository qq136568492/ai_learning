# 上下文管理器｜从小白到能用的系统讲义

<参考资料>

- https://docs.python.org/3/reference/datamodel.html#context-managers ：`__enter__` / `__exit__` 协议
- https://docs.python.org/3/reference/compound_stmts.html#the-with-statement ：`with` 语句执行语义
- https://docs.python.org/3/library/contextlib.html ：`contextmanager`、`closing`、`suppress`、`ExitStack`
- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files ：`with open(...)` 文件读写
- https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager ：异步上下文管理器

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/context-managers.md`：资源生命周期、`__enter__` / `__exit__`、`async with`
- `obsidian-vault/LLM_Learning/wiki/concepts/file-io.md`：文件读写与 `with open(...)`
- `obsidian-vault/LLM_Learning/wiki/concepts/dependency-injection.md`：FastAPI `yield` 依赖中的清理逻辑
- `obsidian-vault/LLM_Learning/wiki/concepts/decorators.md`：装饰器负责“函数调用环绕”，用于和上下文管理器区分
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md` 与 `raw/Python进阶到AI应用_完整学习地图.md`：本章属于 D4 进阶语法，连接装饰器、魔术方法与 asyncio

---

## 小白视角：原文教学漏洞与本版修复

| 教学漏洞 | 小白会卡在哪里 | 本版修复 |
|---|---|---|
| 默认已经理解 `try/finally` | 不知道 `with` 解决的到底是什么痛点 | 从手写资源释放开始讲 |
| `__enter__` / `__exit__` 过早出现 | 容易把协议名当成要背的魔法词 | 先用 `with open` 建立直觉，再解释协议 |
| `as` 绑定对象讲得不够清楚 | 误以为 `as` 一定绑定构造出来的对象本身 | 明确 `as` 绑定的是 `__enter__` 返回值 |
| `__exit__` 返回值边界不足 | 不知道 `return True` 会吞异常 | 新增异常路径和吞异常反例 |
| `@contextmanager` 的 `yield` 风险不够落地 | 容易忘记 `try/finally`，异常时不清理 | 新增错误写法与正确模板 |
| 缺少工程取舍 | 不知道什么时候用类、什么时候用 `contextmanager` | 新增对比表和场景边界 |
| 缺少练习答案 | 写完无法自检 | 新增三档练习与参考答案 |

---

## 上一章核心收获回顾（衔接「装饰器」）

- 装饰器适合围绕“一次函数调用”增加日志、计时、缓存、权限等外壳逻辑。
- `@decorator` 本质是 `func = decorator(func)`，会把函数名重新绑定到包装后的函数。
- `functools.wraps` 能保留原函数的名字、文档和注解，方便调试。
- 装饰器主要处理“调用前后”，但有些问题不是一次函数调用，而是一段代码区域的资源生命周期。
- 你已经见过 `try/finally`：无论中间是否出错，最后都要执行收尾逻辑。

但是，我们遇到了一个新问题……

打开文件、申请锁、建立数据库连接、临时切换目录，都有共同特点：进入时要获取资源，离开时必须释放资源。如果中间发生异常，释放动作也不能丢。

因此本章需要：学习上下文管理器，用 `with` 明确一段代码的资源边界，让“进入”和“退出”变成统一协议，而不是到处手写容易遗漏的 `try/finally`。

---

## 本章学习目标

学完本章，你应该能做到：

1. 解释 `with` 相比手写 `try/finally` 的价值。
2. 说清楚 `with expr as target:` 的执行顺序。
3. 手写一个实现 `__enter__` / `__exit__` 的上下文管理器。
4. 理解 `__exit__` 的三个异常参数和返回值含义。
5. 用 `contextlib.contextmanager` 快速编写小型上下文管理器。
6. 区分装饰器和上下文管理器的适用场景。
7. 了解 `closing`、`suppress`、`ExitStack`、`async with` 的入口。

---

## 前置知识极速补齐

### 1. 为什么 `finally` 很重要

```python
f = open("demo.txt", "w", encoding="utf-8")
try:
    f.write("hello")
finally:
    f.close()
```

`finally` 的含义：不管 `try` 里面正常结束、`return`、还是抛异常，都会执行收尾代码。

上下文管理器就是把这类“必须收尾”的模式收成标准写法。

### 2. 最熟悉的上下文管理器：`with open`

```python
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

这段代码的核心意思：

- 进入 `with` 时打开文件。
- `as f` 拿到可用的文件对象。
- 离开 `with` 时自动关闭文件。
- 即使写文件时出错，也会尝试关闭文件。

---

## 动机：资源泄漏比代码重复更危险

手写资源管理容易漏掉异常路径。

```python
lock.acquire()
do_work()
lock.release()
```

如果 `do_work()` 抛异常，`lock.release()` 就不会执行，可能导致死锁。

正确写法要用 `try/finally`：

```python
lock.acquire()
try:
    do_work()
finally:
    lock.release()
```

但如果每个地方都手写，样板多、容易漏。上下文管理器把它变成：

```python
with lock:
    do_work()
```

---

## 类比：借钥匙进仓库

你进入仓库前要借钥匙，离开时必须还钥匙。不管你在里面正常工作、发现问题提前出来，还是中途摔倒被扶出来，钥匙都必须还。

上下文管理器就是仓库门口的制度：进门登记，出门归还。`with` 画出“钥匙有效”的代码区域。

---

## 核心定义：什么是上下文管理器

上下文管理器是支持 `with` 语句的对象。它需要实现两个特殊方法：

- `__enter__`：进入 `with` 代码块前调用。
- `__exit__`：离开 `with` 代码块时调用，无论是否发生异常。

最小模型：

```python
class MyContext:
    def __enter__(self):
        print("进入")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("退出")
        return False


with MyContext() as ctx:
    print("处理中")
```

输出：

```text
进入
处理中
退出
```

---

## 精讲一：`with expr as target` 的执行顺序

```python
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

大致执行过程：

1. 计算 `open(...)`，得到一个上下文管理器对象。
2. 调用这个对象的 `__enter__()`。
3. 把 `__enter__()` 的返回值绑定给 `f`。
4. 执行缩进代码块。
5. 离开代码块时调用 `__exit__(exc_type, exc, tb)`。

重点：`as f` 绑定的是 `__enter__` 的返回值，不一定是构造出来的对象本身。

---

## 精讲二：`__exit__` 的异常参数

```python
class Watch:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("exit")
        print(exc_type)
        print(exc)
        return False


with Watch():
    print("ok")
```

正常结束时，`exc_type`、`exc`、`tb` 都是 `None`。

如果代码块中发生异常：

```python
with Watch():
    raise ValueError("bad")
```

`__exit__` 仍会执行，并收到异常类型、异常对象和 traceback。

---

## 精讲三：`__exit__` 返回值决定是否吞异常

默认推荐：返回 `False` 或 `None`，表示异常继续向外抛。

```python
class SafeLog:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc is not None:
            print(f"记录异常: {exc}")
        return False
```

谨慎写法：返回 `True` 会吞掉异常。

```python
class SuppressValueError:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return exc_type is ValueError


with SuppressValueError():
    raise ValueError("被吞掉")

print("程序继续")
```

工程建议：除非这个上下文管理器的职责就是“明确忽略某类异常”，否则不要随便 `return True`。

---

## 精讲四：类写法，适合有状态的上下文

```python
import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.cost = (time.perf_counter() - self.start) * 1000
        print(f"cost: {self.cost:.2f}ms")
        return False


with Timer() as timer:
    sum(range(10000))
```

适合用类的情况：

- 进入和退出之间要保存状态。
- 上下文对象还有其他方法。
- 逻辑较复杂，需要多个辅助函数。

---

## 精讲五：`@contextmanager`，适合小型上下文

标准库 `contextlib.contextmanager` 可以用生成器快速写上下文管理器。

```python
from contextlib import contextmanager


@contextmanager
def tag(name: str):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")


with tag("job"):
    print("working")
```

输出：

```text
<job>
working
</job>
```

理解方式：

- `yield` 前面的代码相当于 `__enter__`。
- `yield` 后面的清理代码相当于 `__exit__`。
- `yield` 的值会绑定给 `as` 后面的变量。
- 清理逻辑建议放在 `finally` 中，保证异常路径也能执行。

---

## 精讲六：`contextlib` 常用工具

| 工具 | 用途 | 适合场景 |
|---|---|---|
| `contextmanager` | 用生成器快速写上下文 | 小型资源边界 |
| `closing(obj)` | 离开时调用 `obj.close()` | 第三方对象只有 `.close()` |
| `suppress(*exceptions)` | 忽略指定异常 | 明确允许失败的清理动作 |
| `ExitStack` | 动态管理多个上下文 | 资源数量运行时才知道 |
| `asynccontextmanager` | 写异步上下文管理器 | 异步连接、异步会话 |

示例：忽略文件不存在。

```python
from contextlib import suppress
from pathlib import Path


with suppress(FileNotFoundError):
    Path("missing.txt").unlink()
```

---

## 辨析：容易混淆的概念

### 1. 装饰器 vs 上下文管理器

| 对比项 | 装饰器 | 上下文管理器 |
|---|---|---|
| 语法 | `@timed` | `with timer:` |
| 关注点 | 一次函数调用 | 一段代码区域 |
| 常见用途 | 日志、计时、权限、缓存 | 文件、锁、连接、事务、临时状态 |

### 2. 类写法 vs `@contextmanager`

| 写法 | 适合 | 风险 |
|---|---|---|
| 类实现 `__enter__` / `__exit__` | 状态多、逻辑复杂 | 方法签名写错 |
| `@contextmanager` | 十几行以内的小工具 | 忘记 `try/finally` 或写多个 `yield` |

### 3. `as` 后面的变量是什么

| 写法 | `as` 绑定 |
|---|---|
| `with open(...) as f:` | `open(...)` 对象的 `__enter__()` 返回值 |
| `with Timer() as t:` | `Timer.__enter__()` 返回值 |

---

## 陷阱：高频错误与改法

### 陷阱 1：以为 `as` 一定绑定原对象

错误理解：`as x` 一定是 `with` 后面表达式的结果。

正确理解：`as x` 绑定的是 `__enter__` 的返回值。

### 陷阱 2：`__exit__` 随便返回 `True`

问题：异常会被吞掉，调用方可能完全不知道出错。

推荐：默认返回 `False`。

### 陷阱 3：`@contextmanager` 不写 `finally`

错误写法：

```python
@contextmanager
def bad():
    acquire()
    yield
    release()
```

如果 `yield` 所在的代码块抛异常，`release()` 的可靠性会变差。推荐：

```python
@contextmanager
def good():
    acquire()
    try:
        yield
    finally:
        release()
```

### 陷阱 4：把纯计算硬套成 `with`

如果没有明确“进入/退出”义务，`with` 只会增加理解负担。

---

## 双重示例 A：极简入门 Demo，计时上下文

```python
import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.cost_ms = (time.perf_counter() - self.start) * 1000
        print(f"cost {self.cost_ms:.2f}ms")
        return False


with Timer() as timer:
    time.sleep(0.01)

print(timer.cost_ms > 0)
```

运行方式：

```bash
python timer_demo.py
```

---

## 双重示例 B：工程最小切片，临时环境变量

```python
import os
from contextlib import contextmanager


@contextmanager
def push_env(key: str, value: str):
    old_value = os.environ.get(key)
    existed = key in os.environ
    os.environ[key] = value
    try:
        yield
    finally:
        if existed:
            os.environ[key] = old_value or ""
        else:
            os.environ.pop(key, None)


print(os.environ.get("APP_MODE"))
with push_env("APP_MODE", "test"):
    print(os.environ["APP_MODE"])
print(os.environ.get("APP_MODE"))
```

这个例子适合测试场景：临时修改环境变量，退出后恢复，不污染其他测试。

---

## 适用范围与边界

适合使用上下文管理器：

- 文件打开与关闭。
- 锁的获取与释放。
- 数据库连接、事务、会话。
- 临时切换目录、环境变量、配置。
- 测试中的临时补丁和资源清理。

不适合使用上下文管理器：

- 没有明确清理动作的纯计算。
- 核心业务流程本身。
- 只是为了让代码看起来高级。

---

## 练习

### 基础题：手写 `Timer`

要求：进入时记录开始时间，退出时打印耗时。

参考答案见“双重示例 A”。

### 进阶题：实现 `push_env`

要求：临时设置环境变量，退出后恢复原值；如果原本不存在，退出后删除。

参考答案见“双重示例 B”。

### 开放题：什么时候需要 `ExitStack`

参考方向：当资源数量不是写代码时固定的，而是运行时才知道，例如用户传入多个文件路径，需要打开所有文件并保证最后全部关闭。

---

## 费曼反问

1. `with open(...) as f` 中，`f` 是谁返回的？
2. `__exit__` 返回 `True` 和返回 `False` 有什么区别？
3. `@contextmanager` 中 `yield` 前后分别对应什么阶段？
4. 什么时候你会选择上下文管理器，而不是装饰器？
5. 你的项目里哪个资源最应该用 `with` 管理？

---

## 本章闭环

不看资料，尝试口述：

> 上下文管理器用 `with` 画出一段资源有效期。进入时调用 `__enter__`，退出时调用 `__exit__`，即使中间发生异常也会执行退出逻辑。`as` 绑定的是 `__enter__` 的返回值。默认不要让 `__exit__` 返回 `True`，否则会吞掉异常。小型上下文可以用 `@contextmanager`，但清理逻辑要放在 `finally` 中。

---

## 来源分层

本地知识库文件：

- `obsidian-vault/LLM_Learning/wiki/concepts/context-managers.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/file-io.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/dependency-injection.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/decorators.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md`

外部补充：

- https://docs.python.org/3/reference/datamodel.html#context-managers
- https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
- https://docs.python.org/3/library/contextlib.html
