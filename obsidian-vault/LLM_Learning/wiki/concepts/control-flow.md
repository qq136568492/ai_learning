---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, control-flow]
source_count: 1
---

# 控制流

Python 的程序执行控制结构。

## if / elif / else

```python
if x < 0:
    print('负数')
elif x == 0:
    print('零')
else:
    print('正数')
```

- `elif` 是 `else if` 的缩写，避免过深缩进
- 没有 switch/case（3.10 前），用 if/elif 链或 dict 映射替代

## for 循环

Python 的 for 是**迭代器模式**，遍历任意可迭代对象：

```python
for item in sequence:
    process(item)
```

- 不是 C 风格的计数循环
- 迭代时不要修改被迭代的集合，应迭代副本或创建新集合
- `range()` 生成等差数列（惰性，不创建列表）
- `enumerate()` 同时获取索引和值
- `zip()` 并行迭代多个序列

## while 循环

```python
while condition:
    do_something()
```

- 任何非零值/非空序列为真，零/空序列为假

## break / continue / else

- `break`：跳出最近一层循环
- `continue`：跳到下一次迭代
- 循环的 `else`：循环正常结束（未被 break）时执行

> [!tip] 循环 else 的理解
> 把它类比 try/else：try 的 else 在无异常时执行，循环的 else 在无 break 时执行。

## match 语句（3.10+）

结构化模式匹配，远超传统 switch/case：

```python
match command:
    case "quit":
        quit()
    case ("go", direction):
        move(direction)
    case Point(x=0, y=y):
        print(f"Y={y}")
    case _:
        print("unknown")
```

支持的模式类型：
- 字面值匹配
- 变量捕获
- 序列解包：`case [x, y, *rest]`
- 映射匹配：`case {"key": value}`
- 类模式：`case Point(x=0, y=y)`
- `|` 组合多个模式
- `if` 约束项（guard）

## pass 语句

空操作占位符，用于语法需要语句但无需动作的场合。

## 来源

- [[sources/2026-05-13-python311-tutorial]]
