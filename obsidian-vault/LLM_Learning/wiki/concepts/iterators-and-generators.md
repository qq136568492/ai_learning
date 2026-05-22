---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, iterator, generator, yield]
source_count: 1
---

# 迭代器与生成器

Python 的惰性求值和序列生成机制。

## 迭代器协议

任何实现了以下两个方法的对象就是迭代器：

- `__iter__()`：返回迭代器对象本身
- `__next__()`：返回下一个值，无更多值时抛出 `StopIteration`

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
```

## for 循环的本质

```python
for item in container:
    process(item)
```

等价于：
```python
it = iter(container)  # 调用 container.__iter__()
while True:
    try:
        item = next(it)  # 调用 it.__next__()
    except StopIteration:
        break
    process(item)
```

## 可迭代对象 vs 迭代器

- **可迭代对象（Iterable）**：有 `__iter__()` 方法，如 list、str、dict
- **迭代器（Iterator）**：有 `__iter__()` + `__next__()`，是一次性的
- `iter(iterable)` 从可迭代对象获取迭代器

## 生成器函数

用 `yield` 代替 `return`，自动实现迭代器协议：

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

- 每次 `yield` 暂停执行，保留局部状态
- 下次 `next()` 从暂停处继续
- 函数返回时自动抛出 `StopIteration`

### 优势

- 代码比手写迭代器类简洁得多
- 自动保存/恢复局部变量和执行位置
- 内存高效：按需生成值，不一次性存储

## 生成器表达式

```python
sum_of_squares = sum(x**2 for x in range(10))
```

- 语法类似列表推导式，但用圆括号
- 惰性求值，不创建完整列表
- 适合作为函数参数（如 `sum()`、`max()`、`any()`）

## 常见内置迭代工具

- `range()`：等差数列
- `enumerate()`：带索引迭代
- `zip()`：并行迭代
- `map()`、`filter()`：函数式映射/过滤
- `reversed()`：逆序迭代
- `sorted()`：排序后迭代（返回列表）

## 来源

- [[sources/2026-05-13-python311-tutorial]]
