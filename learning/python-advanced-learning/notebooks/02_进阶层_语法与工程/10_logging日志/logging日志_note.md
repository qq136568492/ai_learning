# logging 日志｜从小白到能用的系统讲义

<参考资料>

- https://docs.python.org/3/library/logging.html ：`logging` 标准库
- https://docs.python.org/3/howto/logging.html ：Logging HOWTO
- https://docs.python.org/3/howto/logging-cookbook.html ：Logging Cookbook
- https://docs.python.org/3/library/logging.config.html ：`dictConfig` 配置
- https://docs.pytest.org/en/stable/how-to/logging.html ：pytest 中测试日志与 `caplog`

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/standard-library.md`：标准库精选与 `logging.warning` / `logging.info`
- `obsidian-vault/LLM_Learning/wiki/concepts/deployment-strategy.md`：部署与可观测，日志、指标、追踪
- `obsidian-vault/LLM_Learning/wiki/concepts/string-formatting.md`：字符串格式化，帮助理解日志消息格式
- `obsidian-vault/LLM_Learning/wiki/concepts/decorators.md`：日志装饰器与横切能力
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md` 与 `raw/Python进阶到AI应用_完整学习地图.md`：F3/I 工程化与可观测
- `obsidian-vault/LLM_Learning/wiki/topics/fastapi-api-engineering.md`：API 服务中的测试、部署、监控与日志

---

## 小白视角：原文教学漏洞与本版修复

| 教学漏洞 | 小白会卡在哪里 | 本版修复 |
|---|---|---|
| 直接讲 `getLogger(__name__)` | 不知道为什么不用 `print` | 新增 print 的限制和 logging 的价值 |
| Logger/Handler/Formatter 关系太抽象 | 不知道谁负责过滤、谁负责输出、谁负责格式 | 新增职责表和广播类比 |
| 层级传播没讲透 | 一行日志重复多次不知道原因 | 新增 logger 层级、propagate、重复 Handler 陷阱 |
| `basicConfig` 与生产配置边界不足 | 可能在库代码里乱配全局日志 | 新增脚本/库/应用配置边界 |
| 日志级别缺少团队语义 | DEBUG/INFO/WARNING/ERROR 用混 | 新增级别使用规范 |
| 异常日志不足 | 只打印错误字符串，丢 traceback | 新增 `logger.exception` 和 `exc_info` |
| 敏感信息风险不足 | token、手机号、用户隐私进日志 | 新增脱敏红线 |
| 缺少测试日志 | 不知道如何断言关键日志 | 新增 pytest `caplog` 示例 |

---

## 上一章核心收获回顾（衔接「pytest」）

- 你已经知道测试能把行为预期写成机器可重复执行的检查。
- 你已经知道失败信息越清楚，定位问题越快。
- 你已经见过 `caplog` 可以在测试中捕获日志。
- 你已经知道线上系统不是只靠断点调试，必须有可查询的运行记录。
- 本章要学的 logging，就是生产排障和可观测链路的基础。

但是，我们遇到了一个新问题……

开发时用 `print()` 很快，但生产环境里你需要按级别过滤、按模块定位、输出到文件/控制台/日志系统、记录 traceback、携带 request_id，并避免泄露敏感信息。`print()` 做不到这些。

因此本章需要：学习标准库 `logging`，掌握 Logger、Level、Handler、Formatter、Filter、层级传播和 `dictConfig`，建立可用于脚本、库和服务的日志习惯。

---

## 本章学习目标

学完本章，你应该能做到：

1. 说清楚 `logging` 相比 `print` 的优势。
2. 用 `logging.basicConfig` 写最小可运行日志。
3. 理解 Logger、Handler、Formatter、Filter 的职责。
4. 使用 `logging.getLogger(__name__)` 创建模块级 logger。
5. 正确选择 DEBUG、INFO、WARNING、ERROR、CRITICAL。
6. 用 `logger.exception()` 记录异常 traceback。
7. 避免重复日志、敏感信息泄露和库代码乱配置。
8. 用 `dictConfig` 理解生产配置结构。
9. 用 pytest `caplog` 测试关键日志。

---

## 前置知识极速补齐

### 1. `print` 为什么不够

```python
print("user login failed")
```

问题：

- 没有级别，分不清调试信息和错误。
- 没有模块名，不知道谁打印的。
- 很难统一输出到文件、控制台、日志平台。
- 很难按环境调整输出。
- 不适合记录异常 traceback 和结构化上下文。

### 2. 最小 logging 示例

```python
import logging


logging.basicConfig(level=logging.INFO)
logging.info("service started")
logging.debug("debug detail")
```

`INFO` 会显示，`DEBUG` 默认不会显示，因为当前级别是 `INFO`。

---

## 动机：日志是线上系统的行车记录仪

程序出错时，你不一定能复现现场。日志记录了发生了什么、什么时候发生、哪个模块发生、是否有 request_id、异常堆栈是什么。

没有日志，排障靠猜。日志混乱，排障像翻垃圾桶。好的日志能帮助你快速定位问题。

---

## 类比：广播系统

把 logging 想成一套广播系统：

- Logger：决定谁在播、播什么级别。
- Handler：决定播到哪里，例如控制台、文件、远程平台。
- Formatter：决定播报格式，例如是否带时间、模块名、级别。
- Filter：决定哪些消息被允许通过。

---

## 核心定义：logging 是什么

`logging` 是 Python 标准库中的日志系统，用于记录程序运行过程中的事件。它支持级别、模块层级、多个输出目标、格式化、异常堆栈、配置化和过滤。

标准用法：

```python
import logging


log = logging.getLogger(__name__)


def do_work() -> None:
    log.info("work started")
```

库代码通常只获取 logger，不主动配置全局 logging。应用入口负责配置。

---

## 精讲一：最小闭环 `basicConfig`

```python
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

log = logging.getLogger(__name__)

log.debug("debug detail")
log.info("service started")
log.warning("cache missed")
```

解释：

- `level=logging.INFO`：显示 INFO 及以上级别。
- `format=...`：定义输出格式。
- `%(name)s`：logger 名称。
- `%(levelname)s`：日志级别。
- `%(message)s`：日志消息。

---

## 精讲二：为什么用 `getLogger(__name__)`

```python
log = logging.getLogger(__name__)
```

`__name__` 是当前模块名。例如：

- `app.service.user`
- `app.repository.order`
- `app.api.health`

好处：

- 日志能定位到模块。
- 可以按模块调整级别。
- logger 名称天然形成层级。
- 库代码不会都挤到 root logger。

---

## 精讲三：日志级别怎么用

| 级别 | 含义 | 示例 |
|---|---|---|
| DEBUG | 开发排查细节 | SQL 参数、分支细节、缓存 key |
| INFO | 正常业务节奏 | 服务启动、任务完成、订单创建 |
| WARNING | 可恢复但异常的情况 | 重试、降级、配置缺省 |
| ERROR | 当前操作失败，需要关注 | 外部 API 失败、任务失败 |
| CRITICAL | 系统级严重问题 | 服务不可用、数据损坏风险 |

团队原则：

- 不要把正常流程写成 ERROR。
- 不要把高频循环细节写成 INFO。
- WARNING 应该表示“值得看，但系统还能继续”。

---

## 精讲四：Logger、Handler、Formatter、Filter

```python
import logging


logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s %(name)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("hello")
```

职责：

- Logger 创建日志事件，并做第一层级别判断。
- Handler 决定输出到哪里，并可再次过滤级别。
- Formatter 决定日志长什么样。
- Filter 决定日志是否允许通过。

---

## 精讲五：层级传播与重复日志

logger 名称有层级：

```text
app
app.service
app.service.user
```

子 logger 默认会把日志向父 logger 传播。若你给父子 logger 都加 Handler，可能出现重复输出。

常见原因：

- 多次调用配置函数。
- root logger 和业务 logger 都挂了控制台 Handler。
- 第三方库和应用都配置了输出。

解决方向：

- 应用入口统一配置一次。
- 库代码不要调用 `basicConfig()`。
- 必要时设置 `logger.propagate = False`。
- 添加 Handler 前检查是否已经存在。

---

## 精讲六：异常日志要保留 traceback

不推荐：

```python
try:
    1 / 0
except ZeroDivisionError as exc:
    log.error(f"failed: {exc}")
```

这样通常只有错误文本，没有完整堆栈。

推荐：

```python
try:
    1 / 0
except ZeroDivisionError:
    log.exception("calculation failed")
```

`logger.exception()` 只能在 `except` 块里使用，等价于 `logger.error(..., exc_info=True)`。

---

## 精讲七：日志消息格式，优先延迟格式化

推荐：

```python
log.info("user %s logged in", user_id)
```

不推荐在高频 DEBUG 中直接 f-string：

```python
log.debug(f"expensive data: {build_debug_payload()}")
```

原因：即使 DEBUG 不输出，f-string 里的表达式也已经执行。logging 的 `%s` 参数会延迟到真正需要格式化时处理。

注意：如果表达式本身已经很便宜，f-string 在业务日志中也不是绝对禁用；关键是理解性能和求值时机。

---

## 精讲八：生产配置用 `dictConfig`

```python
import logging
import logging.config


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s %(name)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
        }
    },
    "loggers": {
        "app": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        }
    },
}


logging.config.dictConfig(LOGGING)
log = logging.getLogger("app")
log.info("configured")
```

适合生产：配置集中、环境可调整、方便切换 JSON formatter 或不同 handler。

---

## 精讲九：结构化上下文与 request_id

日志最好能关联到一次请求或任务。

```python
import logging


log = logging.getLogger(__name__)


def handle_request(request_id: str, user_id: str) -> None:
    log.info(
        "request handled",
        extra={"request_id": request_id, "user_id": user_id},
    )
```

标准库 formatter 默认不会自动显示 `extra` 字段，你需要在 formatter 中声明字段，或使用 JSON 日志方案。生产中常见做法是输出 JSON 到 stdout，再由日志平台收集。

---

## 精讲十：用 caplog 测日志

```python
import logging


log = logging.getLogger(__name__)


def risky(ok: bool) -> None:
    if not ok:
        log.warning("fallback used")


def test_risky_logs_warning(caplog) -> None:
    with caplog.at_level(logging.WARNING):
        risky(False)
    assert "fallback used" in caplog.text
```

适合测试：关键降级、审计日志、安全告警是否出现。

---

## 辨析：容易混淆的概念

### 1. print vs logging

| 对比项 | print | logging |
|---|---|---|
| 级别 | 无 | DEBUG/INFO/WARNING/ERROR |
| 输出目标 | 标准输出 | 控制台、文件、远程系统等 |
| 模块定位 | 手写 | logger 名称 |
| 生产适用 | 弱 | 强 |

### 2. 应用代码 vs 库代码

| 代码类型 | 应该做什么 | 不应该做什么 |
|---|---|---|
| 应用入口 | 配置 logging | 重复配置多次 |
| 库模块 | `getLogger(__name__)` 打日志 | 擅自 `basicConfig()` |

### 3. ERROR vs exception

| 方法 | 用途 |
|---|---|
| `log.error(...)` | 记录错误事件 |
| `log.exception(...)` | 在 except 中记录错误并附带 traceback |

---

## 陷阱：高频错误与改法

### 陷阱 1：到处用 `print`

改法：脚本调试可以短期用 `print`，项目代码使用 `logging`。

### 陷阱 2：库代码调用 `basicConfig`

问题：库不应该替应用决定日志格式和输出位置。

改法：库只写：

```python
log = logging.getLogger(__name__)
```

配置放在应用入口。

### 陷阱 3：重复 Handler 导致一行日志输出多遍

改法：统一配置一次；必要时检查 `logger.handlers` 或设置 `propagate=False`。

### 陷阱 4：日志泄露敏感信息

不要记录：

- token、API key、密码。
- 身份证、手机号、邮箱全量。
- Cookie、Authorization header。
- 完整用户输入中的隐私内容。

改法：脱敏、哈希、截断、白名单字段。

### 陷阱 5：异常只记录字符串

改法：在 `except` 中用 `log.exception()` 保留 traceback。

### 陷阱 6：日志过多

高频循环里打 INFO 会压垮日志系统。

改法：降到 DEBUG、采样、聚合指标、限频。

---

## 双重示例 A：极简入门 Demo

```python
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s",
)

log = logging.getLogger(__name__)

log.debug("debug detail")
log.info("service started")
log.warning("cache missed")
```

运行：

```bash
python logging_demo.py
```

预期：显示 INFO 和 WARNING，不显示 DEBUG。

---

## 双重示例 B：工程最小切片，模块 logger + 异常日志

```python
import logging


log = logging.getLogger(__name__)


def parse_int(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        log.exception("parse_int failed for input=%r", text)
        return None


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    parse_int("abc")
```

工程边界：真实系统里不要把可能含敏感信息的完整输入直接打入日志，必要时截断或脱敏。

---

## 适用范围与边界

适合写日志：

- 服务启动、停止、配置摘要。
- 关键业务事件。
- 外部依赖失败、重试、降级。
- 异常 traceback。
- 安全审计与关键状态变化。

不适合写日志：

- 高频循环里的每条细节。
- 敏感信息原文。
- 可用指标表达的大量计数。
- 没有行动价值的噪音。

---

## 练习

### 基础题：配置控制台日志

```python
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)
log.info("hello")
```

### 进阶题：记录异常 traceback

```python
import logging


log = logging.getLogger(__name__)


def divide(a: int, b: int) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        log.exception("divide failed")
        return None
```

### 开放题：团队日志规范

参考方向：

- 规定各级别含义。
- 禁止记录 token、密码、完整隐私字段。
- 每条请求日志携带 request_id。
- 应用入口统一配置 logging。
- 库代码只 `getLogger(__name__)`。

---

## 费曼反问

1. 为什么项目代码里不建议长期用 `print` 当日志？
2. Logger、Handler、Formatter 分别负责什么？
3. 为什么库代码不应该调用 `basicConfig()`？
4. 为什么一行日志会重复出现多次？
5. 什么时候应该用 `log.exception()`？

---

## 本章闭环

不看资料，尝试口述：

> logging 是 Python 标准库日志系统，比 print 更适合工程场景，因为它支持级别、模块名、多个输出目标、格式化、异常堆栈和集中配置。模块里通常写 `log = logging.getLogger(__name__)`，应用入口统一配置。Logger 产生日志，Handler 决定输出到哪里，Formatter 决定格式，Filter 决定是否放行。生产日志要避免重复 Handler、敏感信息泄露和高频噪音。

---

## 来源分层

本地知识库文件：

- `obsidian-vault/LLM_Learning/wiki/concepts/standard-library.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/deployment-strategy.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/string-formatting.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/decorators.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md`
- `obsidian-vault/LLM_Learning/wiki/topics/fastapi-api-engineering.md`

外部补充：

- https://docs.python.org/3/library/logging.html
- https://docs.python.org/3/howto/logging.html
- https://docs.python.org/3/howto/logging-cookbook.html
- https://docs.python.org/3/library/logging.config.html
- https://docs.pytest.org/en/stable/how-to/logging.html
