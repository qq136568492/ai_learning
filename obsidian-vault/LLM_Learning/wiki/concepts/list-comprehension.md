---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, list, comprehension]
source_count: 1
---

# 列表推导式

用简洁语法从可迭代对象生成新列表的表达式。

## 基本语法

```python
[expression for item in iterable if condition]
```

等价于：
```python
result = []
for item in iterable:
    if condition:
        result.append(expression)
```

## 示例

```python
# 平方列表
squares = [x**2 for x in range(10)]

# 带过滤
evens = [x for x in range(20) if x % 2 == 0]

# 调用方法
stripped = [s.strip() for s in strings]

# 生成元组（必须加括号）
pairs = [(x, x**2) for x in range(6)]
```

## 多重 for

```python
# 笛卡尔积 + 过滤
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# 展平嵌套列表
flat = [num for row in matrix for num in row]
```

for 和 if 的顺序与等价的嵌套循环一致。

## 嵌套推导式

```python
# 矩阵转置
transposed = [ [row[i] for row in matrix] for i in range(4) ]
# 等价于 list(zip(*matrix))
```

## 其他推导式

- **字典推导式**：`{k: v for k, v in pairs}`
- **集合推导式**：`{x for x in 'abracadabra' if x not in 'abc'}`
- **生成器表达式**：`(x**2 for x in range(10))`（惰性求值，见 [[concepts/iterators-and-generators]]）

## 何时使用

- 简单的映射/过滤操作：用推导式
- 逻辑复杂或有副作用：用普通循环
- 需要惰性求值：用生成器表达式

## 来源

- [[sources/2026-05-13-python311-tutorial]]

