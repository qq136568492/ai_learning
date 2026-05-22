# 迭代器与生成器｜讲义笔记

<参考资料>

- https://docs.python.org/3/library/stdtypes.html#iterator-types
- https://docs.python.org/3/tutorial/classes.html#iterators — 等价思想
- https://docs.python.org/3/reference/datamodel.html#object.__iter__

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/iterators-and-generators.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **D2**

---

## 上一章核心收获回顾（衔接「推导式」）

你能用 **`[ … ]`、`{ … }`、`( … for …)`** 写出声明式数据处理。

你已理解 **外层 `[]` vs 裸生成器括号** 的差异。

你已具备 **可读性边界**：复杂副作用退回 `for`。

你即将把 **`for`** 的神经末梢接到 **`iter`/`StopIteration`** 这一协议层。

你已知道「惰性」在巨大日志或分页 API 场景的价值——本章把它系统化成「可暂停的函数」（`yield`）。

---

## 但是，我们遇到了一个新的问题……

- 预处理 **10GB 日志**时还 `readlines()` ⇒ OOM。
- 想要流水线 **`read → parse → enrich`** 又不想中间巨型 `list`。

**因此本章需要：**理解 **`__next__` + `StopIteration`** 收尾，以及 **`yield` 生成器**。**可迭代**：人话里是「能被 `iter()` 接受」，协议细节本节点到为止。

---

## 动机

**时间与内存**不能同时为「整块物化」付两次账。

---

## 类比（非编程）

惰性迭代像 **一片片取披萨吃完再拿下一片**；`list(...)`像 **整摞端上桌再放凉**。

---

## 精讲（渐进）

### 1. `for x in obj` 三部曲

1. `it = iter(obj)`
2. 反复 `next(it)`
3. 直到 `StopIteration`：循环收尾（不向用户抛出）

### 2. 手写极小迭代器

```python
class CountTo:
    def __init__(self, n: int):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        v = self.i
        self.i += 1
        return v


assert list(CountTo(3)) == [0, 1, 2]
```

### 3. 生成器

```python
def squares(n: int):
    for i in range(n):
        yield i * i


assert list(squares(3)) == [0, 1, 4]
```

---

## 辨析

| | **列表物化** | **生成器 / 惰性文件行** |
|--|--------------|------------------------|
| 内存 | 常更高 | 常更低 |

---

## 陷阱（≥2）

1. **耗尽型迭代**：很多迭代器只能走一遍；要复扫就 **重新构造** 或 **`list(...)` 物化**（付内存）。
2. **惰性资源≠免费再扫**：文件指针到尾后要继续读必须重新 `open`；网络分页要重新请求。

---

## 适用范围 · 延伸

`yield from`、`itertools`、`async for` 见 **asyncio** 与其它进阶笔记。

---

## 双重示例

### A. 极简｜分页生成器

```python
def fake_pages(total, size):
    start = 0
    while start < total:
        yield list(range(start, min(start + size, total)))
        start += size


assert len(list(fake_pages(5, 2))) == 3
```

### B. 工程切片｜按行惰性读

```python
from pathlib import Path

def lines(path: Path):
    with path.open(encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


# demo: Path("demo.txt").write_text("a\nb\n", encoding="utf-8")
```

运行：自备 `demo.txt`，`python`。

---

## 练习

- **基础**：类 / 生成器两版计数器。
- **进阶**：`yield from` 展平二层列表。
- **开放**：阅读 PEP 255 引言，写 120 字摘要。

---

## 费曼反问

1. `StopIteration` 对 `for` 意味着什么？
2. 生成器与带 `return` 的普通函数在「可从中间.resume」这一点上差什么？
3. 惰性链路在运维上要额外观察哪类指标？

---

> **闭环**：口述 **`iter` → `next` → `StopIteration`** 链路。
