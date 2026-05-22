---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, string, formatting, f-string]
source_count: 1
---

# 字符串格式化

Python 中将数据嵌入字符串的几种方式。

## f-string（推荐，3.6+）

```python
name = "World"
f"Hello, {name}!"           # 基本嵌入
f"{math.pi:.3f}"            # 格式说明符
f"{value:>10}"              # 右对齐，宽度10
f"{price:.2f}"              # 两位小数
f"{name!r}"                 # 用 repr()
f"{bugs=}"                  # 自说明型（3.8+）：输出 "bugs='roaches'"
```

### 格式说明符

`{value:[ [fill]align][sign][#][0][width][grouping][.precision][type]}`（此处为格式说明语法，不是 wiki 链接）

常用：
- 对齐：`<`（左）、`>`（右）、`^`（居中）
- 类型：`d`（整数）、`f`（浮点）、`%`（百分比）、`e`（科学计数）
- 宽度：`{x:10d}` 最小10字符宽

## str.format()

```python
"Hello, {}!".format(name)
"{0} and {1}".format('spam', 'eggs')
"{name} is {age}".format(name="Alice", age=30)
```

- 支持位置参数和关键字参数混用
- 可用 `**dict` 解包字典

## % 格式化（旧式）

```python
"Hello, %s! You are %d years old." % (name, age)
```

- C 风格 printf，仍可用但不推荐
- 不如 f-string 灵活

## str() vs repr()

- `str()`：面向用户的可读输出
- `repr()`：面向开发者，能重建对象的表示
- 字符串的区别：`str('hello')` → `hello`，`repr('hello')` → `'hello'`

## 选择建议

| 场景 | 推荐方式 |
|------|----------|
| 日常字符串拼接 | f-string |
| 需要复用模板 | str.format() |
| 简单日志 | f-string |
| 兼容旧代码 | % 格式化 |

## 来源

- [[sources/2026-05-13-python311-tutorial]]


