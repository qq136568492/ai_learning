# 装饰器｜从小白到能用的系统讲义

<参考资料>

- https://docs.python.org/3/glossary.html#term-decorator ：Python 官方术语表，decorator 定义
- https://docs.python.org/3/reference/compound_stmts.html#function-definitions ：函数定义与装饰器语法
- https://docs.python.org/3/library/functools.html#functools.wraps ：`functools.wraps` 与元数据保留
- https://docs.python.org/3/library/functools.html#functools.lru_cache ：标准库缓存装饰器示例
- https://docs.python.org/3/tutorial/controlflow.html#defining-functions ：函数定义、默认参数、文档字符串
- https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes ：方法、对象与可调用对象基础

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/decorators.md`：装饰器本质、语法糖、带参装饰器、`functools.wraps`
- `obsidian-vault/LLM_Learning/wiki/concepts/functions.md`：函数定义、函数是一等对象、`*args/**kwargs`、LEGB 与闭包、函数注解、docstring
- `obsidian-vault/LLM_Learning/wiki/topics/python-fundamentals.md`：Python 基础路径，一切皆对象，函数是基础能力
- `obsidian-vault/LLM_Learning/wiki/topics/python-data-model.md`：赋值是绑定引用，对象有身份、类型和值
- `obsidian-vault/LLM_Learning/wiki/concepts/classes-and-oop.md`：方法、`self`、对象与行为封装，衔接上一章
- `obsidian-vault/LLM_Learning/wiki/concepts/context-managers.md`：上下文管理器与资源生命周期，帮助区分装饰器和 `with`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md` 与 `raw/Python进阶到AI应用_完整学习地图.md`：本章位于 Python 进阶层 D4，典型场景是计时、缓存、日志、权限

---

## 小白视角：原文教学漏洞与本版修复

原文已经覆盖装饰器的核心点，但更像给有经验读者看的速览。对刚学完函数和类的学习者来说，主要漏洞如下。

| 教学漏洞 | 小白会卡在哪里 | 本版修复 |
|---|---|---|
| 默认读者已经懂“函数是一等对象” | 不明白函数为什么能当参数传入、还能被返回 | 新增函数对象前置知识和可运行示例 |
| 过早使用“高阶函数”“闭包”等术语 | 能背定义，但看不懂 `fn` 为什么还活着 | 新增闭包白话解释、生活类比和最小例子 |
| `@` 语法糖讲得偏快 | 不知道装饰器是在“定义函数时”执行，不是在每次调用时才装上 | 新增定义阶段 vs 调用阶段的打印验证 |
| `*args/**kwargs` 没有铺垫 | 不知道 wrapper 为什么要这样写 | 新增“为什么包装函数要接住所有参数” |
| 带参数装饰器三层嵌套跳跃大 | 分不清 `retry`、`decorator`、`wrapper` 三层分别干什么 | 新增三层职责表、调用链拆解和错误写法 |
| 缺少装饰器链顺序的运行观察 | 多个 `@` 叠放时不知道先执行谁、先调用谁 | 新增定义顺序和调用顺序示例 |
| `wraps` 的价值不够落地 | 知道要写，但不知道不写会影响调试、文档、测试 | 新增无 `wraps` 反例和 `__wrapped__` 说明 |
| 工程边界不够清楚 | 容易把业务分支、状态修改、异常吞掉都塞进装饰器 | 新增适用范围、禁忌边界、反例与改法 |
| 缺少练习答案 | 自学后无法判断自己实现是否正确 | 新增基础/进阶/开放题与参考答案 |

---

## 上一章核心收获回顾（衔接「类与面向对象」）

- 你已经知道函数可以封装一段可复用逻辑，调用时传入参数，最后返回结果。
- 你已经知道函数名本质上也是一个变量名，它指向一个函数对象。
- 你已经学过类和对象，知道对象可以把“状态 + 行为”放在一起。
- 你已经见过 `self`，知道方法调用时对象会参与进来。
- 你已经知道重复代码会降低可维护性，尤其是日志、校验、计时这类到处出现的样板逻辑。

但是，我们遇到了一个新问题……

很多函数都需要同一类“外壳逻辑”：进入前打印日志、执行后统计耗时、出错时重试、调用前检查权限。如果把这些逻辑复制到每个函数体里，业务代码会被包围，修改规则时也要到处改。

因此本章需要：学习装饰器，用统一的外层函数给原函数“套壳”，在不改原函数主体的前提下增加日志、计时、重试、权限、缓存等横切能力，并且知道这层壳什么时候执行、怎么保留原函数信息、什么时候不该滥用。

---

## 本章学习目标

学完本章，你应该能做到：

1. 用一句话解释装饰器：它接收函数，返回一个新函数。
2. 看懂 `@decorator` 与 `func = decorator(func)` 的等价关系。
3. 手写无参装饰器，并正确使用 `*args/**kwargs` 和 `functools.wraps`。
4. 理解闭包：内层函数为什么能记住外层函数里的 `fn`。
5. 手写带参数装饰器，例如 `@retry(times=3)`、`@threshold(ms=100)`。
6. 说清楚多个装饰器叠放时的定义顺序和调用顺序。
7. 判断装饰器适合处理哪些横切逻辑，哪些业务逻辑不应该藏进装饰器。

---

## 前置知识极速补齐

### 1. 函数名也是变量名

一句话：函数定义完成后，函数名会指向一个函数对象。

```python
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))      # 3
print(add.__name__)   # add
print(type(add))      # <class 'function'>
```

这意味着你可以把函数赋值给另一个变量。

```python
def add(a: int, b: int) -> int:
    return a + b


other_name = add
print(other_name(1, 2))  # 3
```

理解这个点后，装饰器就不神秘了：装饰器本质上会把原来的函数名重新绑定到另一个函数上。

### 2. 函数可以作为参数传入另一个函数

```python
def add(a: int, b: int) -> int:
    return a + b


def run_twice(fn, x: int, y: int) -> int:
    return fn(x, y) + fn(x, y)


print(run_twice(add, 1, 2))  # 6
```

这里的 `fn` 只是一个普通参数名，只不过它接收到的是函数对象。

### 3. 函数可以返回另一个函数

```python
def make_greeter(prefix: str):
    def greet(name: str) -> str:
        return f"{prefix}, {name}"

    return greet


hello = make_greeter("你好")
print(hello("小明"))  # 你好, 小明
```

这段代码里，`greet` 是 `make_greeter` 里面定义的函数。`make_greeter` 执行结束后，`greet` 仍然记得 `prefix` 的值。

### 4. 闭包是什么

白话解释：闭包就是“内层函数带着外层函数的变量一起被返回”。

生活类比：你在奶茶店点了一杯“少冰、三分糖”的饮品。店员离开收银台去制作时，仍然带着你的配置。内层函数就像店员，`prefix`、`fn`、`times` 这些外层变量就是被带走的配置。

最小例子：

```python
def outer(message: str):
    def inner() -> None:
        print(message)

    return inner


say_hi = outer("hi")
say_hi()  # hi
```

装饰器大量依赖这个能力：包装函数 `wrapper` 会记住原函数 `fn`。

### 5. `*args` 和 `**kwargs` 为什么常出现在装饰器里

装饰器通常不知道原函数到底有几个参数，所以包装函数要尽量“原样接住、原样转交”。

```python
def wrapper(*args, **kwargs):
    return fn(*args, **kwargs)
```

含义：

- `*args` 接住额外的位置参数。
- `**kwargs` 接住额外的关键字参数。
- 调用 `fn(*args, **kwargs)` 时，再把这些参数原样交给原函数。

---

## 动机：为什么要学装饰器

先看一个重复代码问题。

```python
import time


def create_order(user_id: int) -> str:
    start = time.perf_counter()
    print("开始 create_order")

    result = f"order for user {user_id}"

    cost = (time.perf_counter() - start) * 1000
    print(f"结束 create_order，耗时 {cost:.2f}ms")
    return result


def cancel_order(order_id: int) -> str:
    start = time.perf_counter()
    print("开始 cancel_order")

    result = f"cancel order {order_id}"

    cost = (time.perf_counter() - start) * 1000
    print(f"结束 cancel_order，耗时 {cost:.2f}ms")
    return result
```

问题：

- 计时代码复制了两份。
- 以后想改日志格式，要改很多地方。
- 业务逻辑被样板代码夹住，可读性下降。
- 有人可能忘记某一处日志或异常处理。

装饰器的目标：把“计时这种外壳逻辑”抽出去，业务函数只写业务。

```python
@timed
def create_order(user_id: int) -> str:
    return f"order for user {user_id}"
```

---

## 类比：给快递盒贴统一标签

函数像一个快递盒，里面装的是业务逻辑。装饰器像贴在盒子外面的统一标签或保护膜。

- 盒子里的东西没有变。
- 外面多了一层统一处理：扫码、称重、记录、检查。
- 同一种外壳可以贴到很多盒子上。
- 外壳不能代替盒子里的东西，否则别人就不知道真正的货物在哪里。

这就是装饰器的边界：适合做统一外层处理，不适合隐藏核心业务逻辑。

---

## 核心定义：什么是装饰器

装饰器是一个可调用对象，常见形式是函数。它接收一个函数作为参数，返回一个新的函数。这个新函数通常会在调用原函数前后增加额外行为。

最常见模型：

```python
def decorator(fn):
    def wrapper(*args, **kwargs):
        # 调用前的额外逻辑
        result = fn(*args, **kwargs)
        # 调用后的额外逻辑
        return result

    return wrapper
```

一句话版本：装饰器就是“拿到原函数，包一层，再把包好的函数还回去”。

---

## 精讲一：先不写 `@`，理解重新赋值

先看没有 `@` 的版本。

```python
def trace(fn):
    def wrapper(*args, **kwargs):
        print(f"准备调用 {fn.__name__}")
        result = fn(*args, **kwargs)
        print(f"调用结束 {fn.__name__}")
        return result

    return wrapper


def add(a: int, b: int) -> int:
    return a + b


add = trace(add)

print(add(1, 2))
```

输出类似：

```text
准备调用 add
调用结束 add
3
```

关键拆解：

1. 原来的 `add` 指向真正的加法函数。
2. `trace(add)` 返回 `wrapper`。
3. `add = trace(add)` 让名字 `add` 改为指向 `wrapper`。
4. 以后调用 `add(1, 2)`，实际先进入 `wrapper`。
5. `wrapper` 里面通过闭包记住了原始函数 `fn`，所以还能调用真正的加法。

这就是装饰器的底层骨架。

---

## 精讲二：`@decorator` 只是语法糖

下面两段代码等价。

写法 A：手动赋值。

```python
def work() -> str:
    return "done"


work = trace(work)
```

写法 B：使用 `@`。

```python
@trace
def work() -> str:
    return "done"
```

等价关系：

```python
@trace
def work():
    return "done"

# 等价于：

def work():
    return "done"

work = trace(work)
```

重点：`@trace` 发生在函数定义完成之后，函数名绑定完成之前。它不是每次调用函数时才临时装上。

---

## 精讲三：定义阶段 vs 调用阶段

这是小白最容易混的点：装饰器什么时候执行？包装函数什么时候执行？

```python
def trace(fn):
    print("1. 正在装饰", fn.__name__)

    def wrapper(*args, **kwargs):
        print("3. 正在调用 wrapper")
        return fn(*args, **kwargs)

    return wrapper


@trace
def hello() -> None:
    print("4. 正在执行 hello")


print("2. 函数定义已经结束")
hello()
```

输出：

```text
1. 正在装饰 hello
2. 函数定义已经结束
3. 正在调用 wrapper
4. 正在执行 hello
```

结论：

- `trace(hello)` 在定义函数时执行一次。
- `wrapper()` 在每次调用 `hello()` 时执行。
- 原函数 `hello()` 是在 `wrapper` 内部被调用的。

---

## 精讲四：写一个标准无参装饰器

一个实用装饰器模板如下。

```python
import functools


def trace(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"进入 {fn.__name__}")
        result = fn(*args, **kwargs)
        print(f"退出 {fn.__name__}，返回 {result!r}")
        return result

    return wrapper


@trace
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


print(add(1, 2))
print(add.__name__)
print(add.__doc__)
```

输出：

```text
进入 add
退出 add，返回 3
3
add
Add two numbers.
```

这个模板包含 4 个关键点：

- `trace(fn)` 接收原函数。
- `wrapper(*args, **kwargs)` 接收任意参数。
- `fn(*args, **kwargs)` 调用原函数。
- `@functools.wraps(fn)` 保留原函数名字、文档等元数据。

---

## 精讲五：为什么必须重视 `functools.wraps`

先看不加 `wraps` 的问题。

```python
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


@trace
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


print(add.__name__)  # wrapper
print(add.__doc__)   # None
```

问题：

- 日志里看到的函数名会变成 `wrapper`。
- `help(add)` 看不到原函数文档。
- 测试、调试、框架自省可能拿不到正确信息。

加上 `functools.wraps`：

```python
import functools


def trace(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper
```

它会帮你保留常用元数据，例如：

- `__name__`
- `__doc__`
- `__module__`
- `__annotations__`
- `__wrapped__`

工程规则：自己写函数装饰器时，默认加 `@functools.wraps(fn)`。

---

## 精讲六：带参数装饰器，三层函数怎么理解

### 目标写法

我们希望写出：

```python
@repeat(times=3)
def say_hi() -> None:
    print("hi")
```

这里的 `times=3` 是装饰器自己的配置，不是 `say_hi` 的参数。

### 等价关系

```python
@repeat(times=3)
def say_hi():
    print("hi")

# 等价于：

def say_hi():
    print("hi")

say_hi = repeat(times=3)(say_hi)
```

所以 `repeat(times=3)` 必须先返回一个真正的装饰器，然后这个装饰器再接收 `say_hi`。

### 三层职责表

| 层级 | 常见名字 | 接收什么 | 返回什么 | 作用 |
|---|---|---|---|---|
| 第 1 层 | `repeat(times)` | 装饰器配置 | `decorator` | 先保存配置 |
| 第 2 层 | `decorator(fn)` | 原函数 | `wrapper` | 接收要被装饰的函数 |
| 第 3 层 | `wrapper(*args, **kwargs)` | 原函数调用参数 | 原函数结果 | 每次调用时执行外壳逻辑 |

### 完整代码

```python
import functools


def repeat(times: int):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(times=3)
def say_hi() -> None:
    print("hi")


say_hi()
```

输出：

```text
hi
hi
hi
```

常见错误：忘记返回 `decorator`。

```python
def repeat(times: int):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)

        return wrapper

    # 错误：这里忘了 return decorator
```

后果通常是：

```text
TypeError: 'NoneType' object is not callable
```

---

## 精讲七：多个装饰器叠放的顺序

看代码：

```python
def deco_a(fn):
    print("装饰 A", fn.__name__)

    def wrapper(*args, **kwargs):
        print("进入 A")
        result = fn(*args, **kwargs)
        print("退出 A")
        return result

    return wrapper


def deco_b(fn):
    print("装饰 B", fn.__name__)

    def wrapper(*args, **kwargs):
        print("进入 B")
        result = fn(*args, **kwargs)
        print("退出 B")
        return result

    return wrapper


@deco_a
@deco_b
def work() -> None:
    print("执行 work")


work()
```

等价于：

```python
work = deco_a(deco_b(work))
```

规则：

- 装饰时：离函数最近的先装，也就是 `deco_b` 先接收原函数。
- 调用时：最外层先进入，也就是 `deco_a` 的 `wrapper` 先执行。

可以理解为穿衣服：先穿内衣，再穿外套；出门时别人先看到外套。

---

## 精讲八：类也能当装饰器，先认识即可

只要一个对象能被调用，它就可以当装饰器。类实例可以通过 `__call__` 实现“像函数一样调用”。

```python
import functools


class PrefixLogger:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"{self.prefix}: {fn.__name__}")
            return fn(*args, **kwargs)

        return wrapper


@PrefixLogger("LOG")
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
```

初学阶段重点不是背类装饰器，而是理解：装饰器需要“可调用”。函数可以，带 `__call__` 的对象也可以。

---

## 精讲九：常见内置与框架装饰器

你会在真实项目里经常看到这些装饰器。

| 装饰器 | 来源 | 作用 |
|---|---|---|
| `@functools.lru_cache` | 标准库 | 缓存函数结果 |
| `@property` | 内置 | 把方法包装成属性访问 |
| `@classmethod` | 内置 | 让方法第一个参数接收类 |
| `@staticmethod` | 内置 | 放在类里的普通函数 |
| `@pytest.mark.parametrize` | pytest | 参数化测试 |
| `@app.get(...)` | FastAPI | 注册路由 |

示例：标准库缓存。

```python
import functools


@functools.lru_cache(maxsize=128)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(30))
print(fib.cache_info())
```

注意：框架装饰器不一定只是“包一层函数”。例如 FastAPI 的 `@app.get()` 还会把函数注册到路由表中。初学阶段先掌握函数装饰器，再看框架源码会更稳。

---

## 精讲十：异步函数装饰器的边界

如果原函数是 `async def`，普通同步 wrapper 会出问题，因为它返回的是协程对象，可能没有被 `await`。

异步装饰器模板：

```python
import functools
import time


def async_timed(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await fn(*args, **kwargs)
        cost = (time.perf_counter() - start) * 1000
        print(f"{fn.__name__} {cost:.2f}ms")
        return result

    return wrapper
```

边界规则：

- 装饰普通函数，`wrapper` 通常用普通 `def`。
- 装饰异步函数，`wrapper` 通常用 `async def`，内部 `await fn(...)`。
- 想同时兼容同步和异步函数，需要额外判断，初学阶段不要急着封装成万能装饰器。

---

## 辨析：容易混淆的概念

### 1. 普通函数调用 vs 装饰器执行

| 问题 | 普通函数调用 | 装饰器 |
|---|---|---|
| 何时发生 | 你写 `func()` 时 | 函数定义完成时先执行装饰器 |
| 输入 | 调用参数 | 原函数对象 |
| 输出 | 函数返回值 | 新函数或可调用对象 |

### 2. 无参装饰器 vs 带参装饰器

| 类型 | 写法 | 等价式 | 层数 |
|---|---|---|---|
| 无参装饰器 | `@trace` | `func = trace(func)` | 两层：`trace` + `wrapper` |
| 带参装饰器 | `@retry(times=3)` | `func = retry(times=3)(func)` | 三层：`retry` + `decorator` + `wrapper` |

### 3. 装饰器 vs 上下文管理器

| 对比项 | 装饰器 | 上下文管理器 |
|---|---|---|
| 典型语法 | `@trace` | `with open(...) as f:` |
| 主要用途 | 包住一次函数调用 | 管理一段代码块的进入和退出 |
| 适合场景 | 日志、计时、权限、缓存、重试 | 文件、连接、锁、事务等资源生命周期 |

### 4. 装饰器 vs 直接改函数体

| 方式 | 优点 | 风险 |
|---|---|---|
| 装饰器 | 统一复用横切逻辑 | 过度叠加后调用链变隐蔽 |
| 直接改函数体 | 逻辑直观 | 重复代码多，难统一修改 |

---

## 陷阱：高频错误与改法

### 陷阱 1：忘记 `return wrapper`

错误写法：

```python
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    # 忘了 return wrapper
```

后果：

```text
TypeError: 'NoneType' object is not callable
```

改法：

```python
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper
```

### 陷阱 2：wrapper 不返回原函数结果

错误写法：

```python
def trace(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)

    return wrapper
```

问题：原函数明明返回值，但被装饰后变成 `None`。

改法：

```python
def trace(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result

    return wrapper
```

### 陷阱 3：忘记 `functools.wraps`

错误后果：函数名、文档、注解可能都变成 wrapper 的信息。

改法：

```python
import functools


def trace(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper
```

### 陷阱 4：带参数装饰器少写一层

错误写法：

```python
def repeat(times: int, fn):
    def wrapper(*args, **kwargs):
        for _ in range(times):
            fn(*args, **kwargs)

    return wrapper
```

这不能直接支持 `@repeat(times=3)`，因为 Python 会先调用 `repeat(times=3)`，此时还没有把原函数传进去。

改法：使用三层结构。

```python
def repeat(times: int):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result

        return wrapper

    return decorator
```

### 陷阱 5：把核心业务逻辑藏进装饰器

不推荐：

```python
@change_order_status
@charge_user
@send_coupon
def submit_order(order_id: int):
    return "ok"
```

问题：读 `submit_order` 的人看不到关键业务步骤，测试也很难定位是哪一层改了状态。

推荐：核心业务显式写出来，装饰器只做外围能力。

```python
@timed
@audit_log
def submit_order(order_id: int):
    order = load_order(order_id)
    charge_user(order)
    change_order_status(order, "paid")
    send_coupon(order.user_id)
    return order
```

### 陷阱 6：装饰异步函数却忘记 `await`

错误方向：

```python
def timed(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)  # 如果 fn 是 async def，这里返回协程对象

    return wrapper
```

改法：异步函数用 `async def wrapper` 和 `await fn(...)`。

---

## 双重示例 A：极简入门 Demo，计时装饰器

依赖：只需要标准库 `functools` 和 `time`。

保存为 `timed_demo.py` 后运行：

```bash
python timed_demo.py
```

代码：

```python
import functools
import time


def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        cost = (time.perf_counter() - start) * 1000
        print(f"{fn.__name__} cost {cost:.2f}ms")
        return result

    return wrapper


@timed
def slow_add(a: int, b: int) -> int:
    time.sleep(0.01)
    return a + b


print(slow_add(1, 2))
print(slow_add.__name__)
```

预期输出类似：

```text
slow_add cost 10.00ms
3
slow_add
```

这个例子对应最常见的无参装饰器结构：`decorator(fn) -> wrapper`。

---

## 双重示例 B：工程最小切片，有限重试装饰器

场景：调用外部接口时，偶发 `RuntimeError` 可以重试几次。但不是所有异常都应该重试，所以示例只捕获指定异常。

```python
import functools
import time


def retry(times: int = 3, delay: float = 0.0):
    if times < 1:
        raise ValueError("times 必须 >= 1")

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except RuntimeError as error:
                    last_error = error
                    print(f"第 {attempt} 次失败: {error}")
                    if attempt < times:
                        time.sleep(delay)
            raise last_error

        return wrapper

    return decorator


counter = {"value": 0}


@retry(times=3, delay=0.01)
def unstable_api() -> str:
    counter["value"] += 1
    if counter["value"] < 3:
        raise RuntimeError("temporary failure")
    return "success"


print(unstable_api())
```

预期输出：

```text
第 1 次失败: temporary failure
第 2 次失败: temporary failure
success
```

工程边界：

- 重试要限定异常类型，不要裸 `except Exception`。
- 上线前要加日志、指标、退避策略和最大耗时控制。
- 如果需求复杂，优先使用成熟库，例如 `tenacity`，不要手写大型重试框架。

---

## 什么时候该用装饰器，什么时候别用

### 适合使用

- 日志、审计、计时、指标上报。
- 权限校验、参数校验这类统一守卫逻辑。
- 缓存、简单重试、限流。
- 框架注册，例如路由、任务、测试参数化。
- 多个函数都需要同一类前后缀逻辑。

### 不适合使用

- 关键业务流程，例如扣款、发货、改订单状态。
- 需要读者明确看到的分支决策。
- 会偷偷改变返回值类型的逻辑。
- 会吞掉异常但没有记录的逻辑。
- 叠加太多层导致调试困难的逻辑。

一句工程原则：装饰器适合做“外围横切能力”，不适合藏“核心业务真相”。

---

## 与类型提示的关系（进阶认识）

简单装饰器如果只写 `*args, **kwargs`，类型检查器很难知道被装饰函数的参数和返回值。

进阶写法可以用 `ParamSpec` 和 `TypeVar` 保留函数签名信息。

```python
import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")


def trace(fn: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"调用 {fn.__name__}")
        return fn(*args, **kwargs)

    return wrapper
```

初学阶段不要求马上掌握这段类型写法，但要知道：装饰器会影响类型推断，工程项目中需要更严谨的标注。

---

## 练习

### 基础题：手写 `@trace`

要求：

- 调用前打印函数名和参数。
- 调用后打印返回值。
- 使用 `functools.wraps`。
- 不改变原函数返回值。

参考答案：

```python
import functools


def trace(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"调用 {fn.__name__}, args={args!r}, kwargs={kwargs!r}")
        result = fn(*args, **kwargs)
        print(f"返回 {result!r}")
        return result

    return wrapper


@trace
def add(a: int, b: int) -> int:
    return a + b


assert add(1, 2) == 3
assert add.__name__ == "add"
```

### 进阶题：手写 `@threshold(ms)`

要求：函数耗时超过阈值时打印告警。

参考答案：

```python
import functools
import time


def threshold(ms: float):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            cost = (time.perf_counter() - start) * 1000
            if cost > ms:
                print(f"警告: {fn.__name__} 耗时 {cost:.2f}ms，超过 {ms:.2f}ms")
            return result

        return wrapper

    return decorator


@threshold(ms=5)
def slow_work() -> str:
    time.sleep(0.01)
    return "done"


assert slow_work() == "done"
```

### 开放题：判断是否应该用装饰器

判断下面场景是否适合装饰器，并说明理由。

1. 每个接口都要打印请求耗时。
2. 用户提交订单时，要扣库存、扣款、发优惠券。
3. 某个纯函数计算很慢，输入相同时结果也相同。
4. 每个后台任务执行前都要检查权限。

参考方向：

- 1 适合，属于统一观测逻辑。
- 2 不适合全部藏进装饰器，核心业务流程应该显式写在函数体或服务类里。
- 3 适合，可以考虑缓存装饰器。
- 4 适合，但失败时要明确抛出异常并记录日志。

---

## 费曼反问

1. 你能不能不用 `@`，只用 `func = decorator(func)` 解释装饰器？
2. 为什么 `wrapper` 里面还能调用已经“被替换”的原函数？
3. 带参数装饰器为什么通常需要三层函数？
4. 为什么工程里写装饰器默认要加 `functools.wraps`？
5. 哪些业务逻辑你会拒绝藏进装饰器？

---

## 本章闭环

不看资料，尝试口述下面这段话：

> 装饰器本质上是一个接收函数并返回新函数的可调用对象。`@trace` 等价于 `func = trace(func)`，这件事发生在函数定义完成时。返回的新函数通常叫 `wrapper`，它通过闭包记住原函数 `fn`，所以能在调用前后加日志、计时、权限、缓存、重试等外围逻辑。写装饰器时要用 `*args/**kwargs` 原样转发参数，用 `functools.wraps` 保留原函数元数据，并避免把核心业务流程藏进过深的装饰链。

---

## 来源分层

本地知识库文件：

- `obsidian-vault/LLM_Learning/wiki/concepts/decorators.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/functions.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-fundamentals.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-data-model.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/classes-and-oop.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/context-managers.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md`

外部补充：

- https://docs.python.org/3/glossary.html#term-decorator
- https://docs.python.org/3/reference/compound_stmts.html#function-definitions
- https://docs.python.org/3/library/functools.html#functools.wraps
- https://docs.python.org/3/library/functools.html#functools.lru_cache
- https://docs.python.org/3/tutorial/controlflow.html#defining-functions
