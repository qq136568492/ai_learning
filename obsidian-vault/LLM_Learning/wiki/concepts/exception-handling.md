---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, exceptions, error-handling]
source_count: 1
---

# 异常处理

Python 的错误检测与处理机制。

## 异常 vs 语法错误

- **语法错误（SyntaxError）**：解析阶段发现，程序无法运行
- **异常**：运行时发生，可被捕获和处理

## try / except / else / finally

```python
try:
    risky_operation()
except ValueError as e:
    handle_value_error(e)
except (TypeError, KeyError):
    handle_multiple()
except Exception as e:
    handle_generic(e)
else:
    # try 块未抛异常时执行
    success_action()
finally:
    # 无论如何都执行（清理资源）
    cleanup()
```

### 执行顺序

1. 执行 try 块
2. 若有异常 → 匹配 except（第一个匹配的执行）
3. 若无异常 → 执行 else
4. 无论如何 → 执行 finally

### except 匹配规则

- 按顺序匹配，第一个匹配的生效
- 子类异常能被父类 except 捕获
- 裸 `except:` 捕获所有异常（不推荐）

## 触发异常

```python
raise ValueError("invalid input")
raise  # 重新抛出当前异常
```

## 异常链

```python
raise RuntimeError("failed") from original_exception
raise RuntimeError("failed") from None  # 禁止链式显示
```

## 自定义异常

```python
class MyError(Exception):
    """自定义异常应继承 Exception。"""
    pass

class InputValidationError(MyError):
    def __init__(self, field, message):
        self.field = field
        super().__init__(message)
```

- 通常继承 `Exception`（不是 `BaseException`）
- 按模块/库组织异常层级

## ExceptionGroup（3.11+）

同时引发和处理多个不相关的异常：

```python
raise ExceptionGroup("multiple errors", [
    ValueError("bad value"),
    TypeError("wrong type"),
])
```

用 `except*` 处理：
```python
try:
    ...
except* ValueError as eg:
    handle_value_errors(eg.exceptions)
except* TypeError as eg:
    handle_type_errors(eg.exceptions)
```

## 异常注释（3.11+）

```python
try:
    ...
except Exception as e:
    e.add_note("Additional context")
    raise
```

## 预定义清理操作

`with` 语句确保资源正确释放：

```python
with open('file.txt') as f:
    data = f.read()
# 文件自动关闭，即使发生异常
```

## 来源

- [[sources/2026-05-13-python311-tutorial]]
