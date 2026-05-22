---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, functions]
source_count: 1
---

# 函数

Python 函数定义与调用机制。

## 基本定义

```python
def function_name(parameters):
    """Docstring: 描述函数用途。"""
    # 函数体
    return value
```

- 用 `def` 关键字定义
- 没有 return 或 return 无值时，返回 `None`
- 函数是一等对象，可赋值给变量、作为参数传递

## 参数类型

### 位置参数与关键字参数

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass
```

- `/` 之前：仅限位置参数
- `/` 和 `*` 之间：位置或关键字均可
- `*` 之后：仅限关键字参数

### 默认值参数

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    ...
```

> [!warning] 可变默认值陷阱
> 默认值只在定义时求值一次。可变对象（list/dict）作为默认值会在调用间共享：
> ```python
> def f(a, L=[]):      # 错误：L 在调用间累积
>     L.append(a)
>     return L
>
> def f(a, L=None):    # 正确：每次创建新列表
>     if L is None:
>         L = []
>     L.append(a)
>     return L
> ```

### 可变参数

- `*args`：收集额外位置参数为元组
- `**kwargs`：收集额外关键字参数为字典

### 解包调用

- `func(*list_arg)`：解包序列为位置参数
- `func(**dict_arg)`：解包字典为关键字参数

## Lambda 表达式

```python
lambda x, y: x + y
```

- 匿名函数，只能是单个表达式
- 常用于 `sort(key=...)` 等需要短函数的场合

## 作用域规则（LEGB）

变量查找顺序：
1. **L**ocal：函数内部
2. **E**nclosing：外层函数（闭包）
3. **G**lobal：模块级
4. **B**uilt-in：内置名称

- `global` 声明：在函数内修改全局变量
- `nonlocal` 声明：在内层函数修改外层函数变量

## 函数注解

```python
def f(ham: str, eggs: str = 'eggs') -> str:
    return ham + ' and ' + eggs
```

- 存储在 `f.__annotations__` 字典中
- 不影响运行时行为，供类型检查工具使用

## Docstring 约定

- 第一行：简短摘要，大写开头，句点结尾
- 第二行空白
- 后续行：详细描述

## 来源

- [[sources/2026-05-13-python311-tutorial]]
