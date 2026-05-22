# 函数与作用域｜讲义笔记

<参考资料>

- https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- https://docs.python.org/3/reference/compound_stmts.html#function-definitions
- https://docs.python.org/3/reference/executionmodel.html#naming-and-binding

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/functions.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-fundamentals.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **A5**

---

## 上一章核心收获回顾（衔接「字符串 / 文件 I/O」）

你能 **安全地用 UTF-8 读写文本**，并理解 **别把大文件整块 `read()`**。

你已能在局部逻辑里拼装 **格式化字符串**，把「数据来源」拆成可读步骤。

你已接触 **`Path`** 这种把路径当对象来写 API 的思路——与「函数是可调用对象」同方向。

你已具备写 **多块 try/拆分职责**的前期心智（本章与异常章互相引用）。

你已准备系统化 **函数的参数契约**——这是 API / 可读性分水岭。

---

## 但是，我们遇到了一个新的问题……

- **`lambda` / 闭包**搭配循环推导时，拿到的常是「**最后一个变量的最终值**」而不是当场快照。  
- 不清楚 **`/`（仅限位置）、`*`（之后仅限关键字）、`*args`/`**kwargs` 组合拳**怎么用。  
- 默认参数的 **可变对象共享**再次出现（与 **`数据类型与可变性_note.md`** 呼应）。

**因此本章需要：**掌握 **签名**、LEGB **`global`/`nonlocal` 谨慎点**、**闭包捕获规则**。

---

## 动机：API 失守

签名太宽（全部 `**kwargs`）会让调用者在文档外猜参数；签名太死板又挡住演进——需要语言机制表达 **可选 / 必填 / keyword-only / positional-only**。

---

## 类比（非编程）

函数像厨房 **配方卡**：**「食材槽位」（参数）**写清顺序与必选；`/ *`像在卡上贴纸「此两项必须原位倒入，此项必须写调料名倾倒」——减少误调用。

---

## 精讲（要点）

### 1. LEGB — 名字的查找梯子

局部 **L** ↔ 闭包 **E** ↔ 模块全局 **G** ↔ 内置 **B**。  
**赋值**默认在函数里 **创建局部绑定**（除非你 `global x`/`nonlocal x` 声明）。

### 2. 参数五件套 + 分隔符

```python
def f(a, /, b, *args, c, **kwargs):
    return a + b + c + sum(args) + sum(kwargs.values())
```

### 3. lambda 极简

单行表达式匿名函数：**不要塞业务**。

### 4. **闭包延迟绑定**Bug + 解法

```python
# 反例
funcs_wrong = [lambda: i for i in range(3)]        # → 全是 2
# 正例之一
funcs_ok = [lambda i=i: i for i in range(3)]
assert [fn() for fn in funcs_ok] == [0, 1, 2]
```

「装饰器如何利用闭包」→ **`装饰器_note.md`**。

---

## 辨析

| | **`def`** | **`lambda`** |
|--|-----------|----------------|
| 用途 | **主力**可读 / 可调栈 | **局部小表达式** |

| | **`global`** | **`nonlocal`** |
|--|---------------|----------------|
| 改谁的绑定 | **模块顶层名** | **外层函数的非全局名** |

---

## 陷阱

1. **可变默认值** — 回看数据类型讲义。  
2. **外层循环 + lambda 无默认参数捕获** — 上文示范。  
3. **在非 global 外层给同名赋值却以为改了外层」— 其实是 **新建局部**。用 `nonlocal`。

---

## 适用范围 · 延伸

`functools.partial` / wraps；类型签名 → **`类型提示_note.md`**。

---

## 双重示例

### A. 极简｜keyword-only API

```python
def divide(a, b, /, *, safe: bool):
    if safe and b == 0:
        raise ValueError("b不能为0")
    return a / b


assert divide(10, 2, safe=True) == 5.0
```

### B. 工程切片｜参数透传

```python
def logged_call(fn, *args, **kwargs):
    print("CALL", getattr(fn, "__name__", "anon"), args, kwargs)
    return fn(*args, **kwargs)
```

---

## 练习

- **基础**：写一个 `clamp(x, low, high)` 与两个 keyword-only flags。  
- **进阶**：造「循环 lambda Bug」并用两种修法。  
- **开放**：浏览 `inspect.signature` 读出某函数契约。

---

## 费曼反问

1. `LEGB` 少一环会怎样？
2. 为什么纯 `**kwargs` 公共 API **可能伤协作**？
3. `lambda` 里 **不写默认参数捕获**会发生什么心智模型？

---

> **闭环**：口述 **可变默认参数只求值一次的实验**。
