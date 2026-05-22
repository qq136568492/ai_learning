# asyncio 异步编程｜从小白到能用的系统讲义

<参考资料>

- https://docs.python.org/3/library/asyncio.html ：`asyncio` 标准库入口
- https://docs.python.org/3/library/asyncio-task.html ：协程、Task、`gather`、`wait_for`、`to_thread`
- https://docs.python.org/3/glossary.html#term-coroutine ：协程术语
- https://docs.python.org/3/library/asyncio-sync.html ：异步锁、事件、信号量、队列
- https://fastapi.tiangolo.com/async/ ：FastAPI 对 `async def` 与 I/O 等待的解释

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/asyncio-in-practice.md`：`asyncio.run`、`create_task`、`gather`、`wait_for`、`to_thread`、Queue
- `obsidian-vault/LLM_Learning/raw/FastAPI_官方文档.md`：异步代码、协程、`async def`、`await`、FastAPI 中同步/异步函数行为
- `obsidian-vault/LLM_Learning/wiki/topics/fastapi-api-engineering.md`：FastAPI 异步优先、测试与部署
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md` 与 `raw/Python进阶到AI应用_完整学习地图.md`：E2 类型与异步，服务于 HTTP、数据库、LLM 流式输出等 I/O 场景
- `obsidian-vault/LLM_Learning/wiki/concepts/context-managers.md`：`async with` 与资源清理的平行关系

---

## 小白视角：原文教学漏洞与本版修复

| 教学漏洞 | 小白会卡在哪里 | 本版修复 |
|---|---|---|
| 直接讲 `gather`，缺少同步/异步对比 | 不知道为什么要异步 | 从“等待”场景和同步耗时开始讲 |
| 协程对象讲得不够具体 | 调用 `async def` 后不知道为什么没执行 | 新增协程对象与 `asyncio.run` 入口示例 |
| `await` 的意义偏抽象 | 不知道它是“让出控制权”，不是开新线程 | 新增事件循环类比和打印顺序 |
| `create_task` / `gather` 边界不清 | 以为写了 `async` 就自动并发 | 新增顺序 await 与并发 gather 对比 |
| 阻塞调用风险不足 | 会在 `async def` 里写 `time.sleep` / `requests.get` | 新增错误写法与 `to_thread` / 异步库替代 |
| 缺少取消、超时、并发限制 | 工程里容易无限等待或打爆对端 | 新增 `wait_for`、`Semaphore`、取消意识 |
| 缺少适用边界 | 以为 asyncio 能加速 CPU 密集计算 | 新增 I/O-bound vs CPU-bound 辨析 |
| 缺少练习答案 | 自学无法闭环 | 新增三档练习与参考答案 |

---

## 上一章核心收获回顾（衔接「类型提示」）

- 你已经知道类型提示主要帮助人、IDE 和静态检查器，不等于运行时校验。
- 你已经能看懂 `async def fetch() -> str` 这种带返回值注解的函数签名。
- 你已经知道外部 I/O 边界，例如 HTTP、数据库、文件、LLM API，需要额外关注错误、超时和类型转换。
- 你已经见过 `async with` 这个名字，它和上下文管理器一样强调资源进入与退出，只是发生在异步世界里。
- 本章开始，`async` / `await` 不再只是签名，而是真正影响运行时调度。

但是，我们遇到了一个新问题……

程序经常不是在算，而是在等：等网络、等数据库、等文件、等大模型返回 token。如果每个等待都把整个程序卡住，吞吐会很差。我们希望一个任务在等待外部响应时，程序能先去推进其他任务。

因此本章需要：学习 asyncio 的协作式并发模型，理解 `async def`、协程对象、事件循环、`await`、Task、`gather`、超时、阻塞调用处理和适用边界。

---

## 本章学习目标

学完本章，你应该能做到：

1. 解释同步、异步、并发、并行的区别。
2. 说明调用 `async def` 得到的是协程对象，不会自动执行。
3. 用 `asyncio.run()` 运行顶层协程。
4. 用 `await` 等待异步操作，并理解它会把控制权交回事件循环。
5. 用 `asyncio.gather()` 并发等待多个 I/O 任务。
6. 用 `asyncio.wait_for()` 设置超时。
7. 用 `asyncio.to_thread()` 兼容暂时无法改造的阻塞函数。
8. 判断 asyncio 适合 I/O 密集，不适合直接加速 CPU 密集计算。

---

## 前置知识极速补齐

### 1. 同步代码：一步等完再下一步

```python
import time


def fetch(name: str, delay: float) -> str:
    time.sleep(delay)
    return f"{name} done"


start = time.perf_counter()
print(fetch("a", 1))
print(fetch("b", 1))
print(f"cost {time.perf_counter() - start:.2f}s")
```

两个任务各等 1 秒，总时间大约 2 秒。

### 2. 异步代码：等待时让别人先跑

```python
import asyncio
import time


async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} done"


async def main() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(fetch("a", 1), fetch("b", 1))
    print(results)
    print(f"cost {time.perf_counter() - start:.2f}s")


asyncio.run(main())
```

两个任务都在等待时可以交替推进，总时间大约 1 秒。

---

## 动机：大量 I/O 等待时，别让一个等待卡住全场

适合 asyncio 的典型场景：

- 同时请求多个 HTTP API。
- 等数据库异步驱动返回结果。
- 处理 WebSocket 或流式响应。
- LLM 流式输出。
- 大量短连接或高并发 I/O。

不适合直接用 asyncio 提速的场景：

- 大量 CPU 计算。
- 图片/视频编码。
- 大矩阵计算。
- Python for 循环里的纯计算热点。

这些更可能需要多进程、C 扩展、NumPy、任务队列或更合适的算法。

---

## 类比：一个店员管理多杯奶茶

同步模式：店员接到 A 的订单后，站在封口机前等 30 秒，什么也不做。A 完成后才处理 B。

异步模式：A 放到封口机等待时，店员去给 B 加糖；B 等待时，再去处理 C。店员不是同时用三只手工作，而是在“等待外部设备”时切换任务。

这就是 asyncio：不是多线程抢着跑，而是任务在 `await` 点主动让出控制权。

---

## 核心定义：asyncio 是什么

`asyncio` 是 Python 标准库中的异步 I/O 框架。它用事件循环调度协程，让多个 I/O 等待型任务在一个线程中协作推进。

核心词：

- `async def`：定义协程函数。
- 协程对象：调用协程函数后得到的对象，需要事件循环驱动。
- `await`：等待一个可等待对象，并把控制权交回事件循环。
- 事件循环：负责调度协程和任务。
- Task：被事件循环调度的协程包装对象。

---

## 精讲一：`async def` 调用后不会立刻执行

```python
async def hello() -> str:
    print("running")
    return "hello"


coro = hello()
print(coro)
```

你会看到类似：

```text
<coroutine object hello at ...>
```

`running` 不会打印，因为协程还没有被事件循环驱动。

正确运行：

```python
import asyncio


async def hello() -> str:
    print("running")
    return "hello"


result = asyncio.run(hello())
print(result)
```

---

## 精讲二：`await` 是“等一下，我先让别人跑”

```python
import asyncio


async def job(name: str) -> None:
    print(f"{name} start")
    await asyncio.sleep(1)
    print(f"{name} end")


async def main() -> None:
    await job("a")
    await job("b")


asyncio.run(main())
```

这里是顺序执行，总耗时约 2 秒。`await` 会等待当前任务完成，才继续下一行。

如果要并发等待多个任务，用 `gather` 或 `create_task`。

---

## 精讲三：`asyncio.gather` 并发等待多个任务

```python
import asyncio
import time


async def job(name: str) -> str:
    await asyncio.sleep(1)
    return f"{name} done"


async def main() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(job("a"), job("b"), job("c"))
    print(results)
    print(f"cost {time.perf_counter() - start:.2f}s")


asyncio.run(main())
```

总耗时约 1 秒，而不是 3 秒。

适合：一组互不依赖的 I/O 请求。

---

## 精讲四：`create_task` 先启动，后等待

```python
import asyncio


async def job(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} done"


async def main() -> None:
    task = asyncio.create_task(job("a", 1))
    print("task created")
    result = await task
    print(result)


asyncio.run(main())
```

`create_task` 会把协程包装成 Task，并交给事件循环调度。

常见用法：先启动后台任务，中间做别的事，最后再 `await task`。

---

## 精讲五：超时，避免无限等待

```python
import asyncio


async def slow() -> str:
    await asyncio.sleep(10)
    return "done"


async def main() -> None:
    try:
        result = await asyncio.wait_for(slow(), timeout=0.1)
        print(result)
    except TimeoutError:
        print("timeout")


asyncio.run(main())
```

工程建议：网络、数据库、外部 API 调用都应该有超时策略。

---

## 精讲六：不要在 `async def` 里阻塞事件循环

错误写法：

```python
import asyncio
import time


async def bad() -> None:
    time.sleep(1)  # 阻塞整个事件循环


asyncio.run(bad())
```

正确方向：

```python
import asyncio


async def good() -> None:
    await asyncio.sleep(1)


asyncio.run(good())
```

如果必须调用阻塞函数，可以临时用 `to_thread`。

```python
import asyncio
import time


def blocking_work() -> str:
    time.sleep(1)
    return "done"


async def main() -> None:
    result = await asyncio.to_thread(blocking_work)
    print(result)


asyncio.run(main())
```

---

## 精讲七：限制并发，别打爆对端

```python
import asyncio


async def fetch(i: int, sem: asyncio.Semaphore) -> str:
    async with sem:
        await asyncio.sleep(0.1)
        return f"ok-{i}"


async def main() -> None:
    sem = asyncio.Semaphore(3)
    results = await asyncio.gather(*(fetch(i, sem) for i in range(10)))
    print(results)


asyncio.run(main())
```

`Semaphore(3)` 表示最多同时跑 3 个受保护任务。真实请求外部 API 时很常用。

---

## 精讲八：取消任务要有清理意识

```python
import asyncio


async def worker() -> None:
    try:
        while True:
            print("working")
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        print("cleanup before cancel")
        raise


async def main() -> None:
    task = asyncio.create_task(worker())
    await asyncio.sleep(0.3)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("cancelled")


asyncio.run(main())
```

工程建议：取消不是失败噪音，而是异步系统中的正常控制流之一。被取消时要释放资源，然后重新抛出 `CancelledError`。

---

## 辨析：容易混淆的概念

### 1. 并发 vs 并行

| 概念 | 含义 | 类比 |
|---|---|---|
| 并发 | 多个任务交替推进 | 一个店员处理多杯等待中的奶茶 |
| 并行 | 多个任务真的同时运行 | 多个店员同时制作 |

asyncio 主要提供并发，不等于多核并行计算。

### 2. 协程 vs Task

| 名称 | 含义 |
|---|---|
| 协程对象 | 调用 `async def` 后得到，尚未必被调度 |
| Task | 被事件循环调度的协程包装对象 |

### 3. `gather` vs `create_task`

| 工具 | 适合 |
|---|---|
| `gather` | 一组任务一起开始，一起等待结果 |
| `create_task` | 先启动任务，稍后再等待或取消 |

### 4. `asyncio` vs 线程池

| 工具 | 适合 | 不适合 |
|---|---|---|
| asyncio | 异步 I/O 库、网络并发 | 直接跑 CPU 密集任务 |
| 线程池 | 包装无法改造的阻塞 I/O | 高强度 CPU 计算 |

---

## 陷阱：高频错误与改法

### 陷阱 1：调用协程但不 await

```python
async def hello() -> None:
    print("hello")


hello()  # 错误：只是创建协程对象
```

改法：

```python
asyncio.run(hello())
```

或在异步函数中：

```python
await hello()
```

### 陷阱 2：在 `async def` 里用 `time.sleep`

改法：用 `await asyncio.sleep()`，或者把阻塞调用放到 `asyncio.to_thread()`。

### 陷阱 3：以为 `async` 自动并发

```python
await job("a")
await job("b")
```

这是顺序等待。并发等待要用 `gather` 或 `create_task`。

### 陷阱 4：没有超时

外部 API 永远可能慢或卡住。给 I/O 加 `wait_for` 或客户端级 timeout。

### 陷阱 5：并发无上限

一口气 `gather` 一万个请求可能打爆自己或对端。用 `Semaphore` 限制并发。

---

## 双重示例 A：极简入门 Demo，并发 sleep

```python
import asyncio
import time


async def fake_request(name: str) -> str:
    await asyncio.sleep(1)
    return f"{name} ok"


async def main() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(
        fake_request("a"),
        fake_request("b"),
        fake_request("c"),
    )
    print(results)
    print(f"cost {time.perf_counter() - start:.2f}s")


asyncio.run(main())
```

预期：总耗时约 1 秒。

---

## 双重示例 B：工程最小切片，带超时和并发限制

```python
import asyncio


async def call_api(i: int, sem: asyncio.Semaphore) -> str:
    async with sem:
        await asyncio.sleep(0.2)
        return f"result-{i}"


async def main() -> None:
    sem = asyncio.Semaphore(2)
    tasks = [call_api(i, sem) for i in range(5)]
    try:
        results = await asyncio.wait_for(asyncio.gather(*tasks), timeout=2)
        print(results)
    except TimeoutError:
        print("api timeout")


asyncio.run(main())
```

工程边界：真实 HTTP 调用要使用异步客户端，例如 `httpx.AsyncClient` 或 `aiohttp`，不要在热路径里直接调用同步 `requests.get()`。

---

## 适用范围与边界

适合 asyncio：

- 高并发 HTTP 请求。
- WebSocket、流式响应。
- 异步数据库驱动。
- LLM 流式输出。
- 多个 I/O 任务编排。

不适合直接用 asyncio：

- CPU 密集型计算。
- 已经全是同步阻塞库且短期无法替换的大型代码。
- 只执行一两个简单步骤的小脚本。

---

## 练习

### 基础题：三个假请求并发执行

参考答案见“双重示例 A”。

### 进阶题：用 `to_thread` 包装阻塞函数

```python
import asyncio
import time


def blocking_fetch() -> str:
    time.sleep(0.5)
    return "ok"


async def main() -> None:
    result = await asyncio.to_thread(blocking_fetch)
    print(result)


asyncio.run(main())
```

### 开放题：判断场景

哪些适合 asyncio？

- 同时请求 100 个网页：适合。
- 计算 10 亿次哈希：不适合直接用 asyncio。
- FastAPI 中调用异步数据库驱动：适合。
- 只有一个本地小文件读取：通常没必要。

---

## 费曼反问

1. 为什么调用 `async def` 不等于执行函数体？
2. `await` 到底把控制权交给了谁？
3. 为什么 `time.sleep()` 会卡住整个事件循环？
4. `gather` 和 `create_task` 的差别是什么？
5. 为什么 asyncio 不适合直接加速 CPU 密集计算？

---

## 本章闭环

不看资料，尝试口述：

> asyncio 适合 I/O 密集型并发。`async def` 调用后得到协程对象，需要事件循环驱动。`await` 表示等待一个异步操作，同时把控制权交回事件循环，让其他任务有机会运行。`gather` 可以并发等待多个任务，`create_task` 可以先启动任务，`wait_for` 用于超时，`to_thread` 用于临时兼容阻塞函数。不要在 async 热路径里写 `time.sleep` 或同步网络请求。

---

## 来源分层

本地知识库文件：

- `obsidian-vault/LLM_Learning/wiki/concepts/asyncio-in-practice.md`
- `obsidian-vault/LLM_Learning/raw/FastAPI_官方文档.md`
- `obsidian-vault/LLM_Learning/wiki/topics/fastapi-api-engineering.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/context-managers.md`

外部补充：

- https://docs.python.org/3/library/asyncio.html
- https://docs.python.org/3/library/asyncio-task.html
- https://docs.python.org/3/glossary.html#term-coroutine
- https://fastapi.tiangolo.com/async/
