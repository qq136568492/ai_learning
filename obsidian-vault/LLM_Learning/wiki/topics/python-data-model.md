---
type: topic
created: 2026-05-13
updated: 2026-05-13
tags: [python, data-model, types, mutability]
source_count: 1
---

# Python 数据模型

Python 如何组织和操作数据的核心设计。

## 核心原则：一切皆对象

Python 中每个值都是对象，每个对象有：
- **身份**（identity）：`id(obj)`，内存地址，不可变
- **类型**（type）：`type(obj)`，决定支持的操作
- **值**（value）：可变或不可变

## 可变性（Mutability）

这是 Python 数据模型最重要的概念之一：

| 不可变 | 可变 |
|--------|------|
| int, float, str, tuple, frozenset, bool, None | list, dict, set, 自定义对象 |

### 影响

- **赋值语义**：`a = b` 不复制，两个名称指向同一对象
- **函数参数**：传递的是对象引用（"对象引用调用"）
  - 不可变对象：函数内无法修改原对象
  - 可变对象：函数内的修改对调用者可见
- **字典键**：必须是不可变（可哈希）对象
- **默认参数**：可变默认值在调用间共享（经典陷阱）

```python
# 赋值是引用绑定
a = [1, 2, 3]
b = a           # b 和 a 指向同一列表
b.append(4)     # a 也变了：[1, 2, 3, 4]

# 复制的方式
c = a[:]        # 浅拷贝
import copy
d = copy.deepcopy(a)  # 深拷贝
```

## 序列协议

Python 的序列类型（str, list, tuple, range）共享统一接口：

- 索引：`seq[i]`，支持负索引
- 切片：`seq[start:stop:step]`
- 拼接：`seq1 + seq2`
- 重复：`seq * n`
- 成员检测：`item in seq`
- 长度：`len(seq)`
- 迭代：`for item in seq`

### 切片的理解方式

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

索引指向字符**之间**的位置。`s[i:j]` 取 i 到 j 之间的元素。

## 映射协议

dict 是核心映射类型：
- 键必须可哈希（不可变）
- 值可以是任意对象
- 3.7+ 保持插入顺序
- O(1) 查找、插入、删除

## 迭代协议

任何实现 `__iter__()` 的对象都可迭代。详见 [[concepts/iterators-and-generators]]。

## 比较与真值

- 序列按字典序比较
- 任何对象都有布尔值：`0`、`None`、空容器为 False，其余为 True
- `is` 比较身份（同一对象），`==` 比较值

## 来源

- [[sources/2026-05-13-python311-tutorial]]
