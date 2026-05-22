# 异常处理｜讲义笔记

<参考资料>

- https://docs.python.org/3/tutorial/errors.html
- https://docs.python.org/3/library/exceptions.html
- PEP 654 — `ExceptionGroup`（「一组异常」，3.11+）；PEP 678 — Exception notes

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/exception-handling.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **A6**

---

## 上一章核心收获回顾（衔接「函数与作用域」）

你能读懂 **关键字 / 可变参数 / 仅限位置**，并口述 **可变默认参数的坑**。

你了解 **赋值建立局部绑定**的规则，不会轻易把外层状态「以为改成功了」却没 `nonlocal`。

你已能拆分 **可读的小函数**，开始面对「 callee 报错后 **调用栈怎么回溯**？」的问题。

你即将把 **`return (ok,val)`地狱**换一种「集中处理错误」的语义。

你已具备写 **健壮输入校验雏形**的时机（例如在 `parse_int`）。

---

## 但是，我们遇到了一个新的问题……

- 每层函数都 **`if not ok: return`** 让主流程面目全非。  
- 丢失 **异常因果链**：包装后忘了 **`raise … from`**。  
- 裸 **`except:`** 吞 Trace，只剩「静默失败」。  
（`ExceptionGroup` 属进阶：批量校验 / asyncio task group 时再抠。）

**因此本章需要：**学会 **`try / except / else / finally`、`raise`、`raise … from`** 与小型 **自定义异常层级**——把「走错路」与「怎么走回」说清楚。

---

## 动机：`None`/`False`/`0` 混作错误码迟早撞车

返回值约定 **无法表达堆栈上下文**，也会在泛型返回值里与合法 `None` 打架。

---

## 类比（非编程）

异常像电梯 **停运报警**：每层（函数）先试能否处理；解决不了就 **鸣笛上行**直达物业中心；`**from**` 像报警单上的 **根本原因附件**——方便事后查证。

---

## 精讲

### 骨架

```python
def parse_int(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        raise ValueError(f"非法整数: {s!r}") from e
```

顺序心智：**try → 命中 except → （无异常才）else → 不论如何 finally**。`return`/`break`穿行时 **`finally` 仍会跑**——别在 finally 抛新异常盖住原异常除非你非常清楚代价。

### 自定义异常 — 业务域信号

```python
class DomainError(Exception):
    """稳定业务语义，勿滥用裸 Exception。"""


class NegativeBalance(DomainError):
    pass
```

### **`ExceptionGroup`（简述）**

**一句话**：把「单次循环里多起子错误」打成一个 **`ExceptionGroup` 信封**再给上层。**最小阅读**：[`docs.python.org/3/library/exceptions.html#ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup)。

---

## 辨析

| | **`except E:`** | **裸 `except:`** |
|--|------------------|------------------|
| 工程建议 | **优先** | **几乎总禁止** |

| | **语法错误 `SyntaxError`** | **运行时异常** |
|--|--------------------------|------------------|
| 何时 | 解析阶段 | 执行阶段 |

---

## 陷阱

1. **`except Exception` 过宽** — 连 `KeyboardInterrupt` 意外吞？应更窄或重抛。  
2. **丢失链** — 包装时忘 `from`。  
3. **用异常做正常流程控制**（极热路径）— 读性能 / 风格双输。

---

## 适用范围 · 延伸

与 **日志 / 观测**结合见 **logging**、**部署**章；与 **async TaskGroup** 搭配见 **asyncio**。

---

## 双重示例

### A. 极简｜链式因果

```python
def load_number(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        raise RuntimeError("转换失败") from e


try:
    load_number("x")
except RuntimeError as e:
    assert e.__cause__ is not None
```

### B. 工程切片｜领域异常 + 窄捕获

```python
class PaymentError(Exception): ...


def charge(cents: int):
    if cents <= 0:
        raise PaymentError("金额非法")
    return "ok"


try:
    charge(-1)
except PaymentError as e:
    handled = str(e)
assert handled == "金额非法"
```

---

## 练习

- **基础**：写 `safe_int` 返回 `int|None` **与** 「抛自定义」两版比对。  
- **进阶**：`pytest.raises(..., match=...)`断言信息。  
- **开放**：读 EAFP vs LBYL 一篇短文并各写 12 行业务伪代码对比。

---

## 费曼反问

1. `else`/`finally` 在什么「return 路径」仍存在？  
2. **`raise X from Y`** 解决的是哪类人读堆栈的痛？  
3. 自定义异常层级 **应该多深**？

---

> **闭环**：解释 **为什么不能依赖裸 `except:`**。
