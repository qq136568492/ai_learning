---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, oop, class, inheritance]
source_count: 1
---

# 类与面向对象

Python 的面向对象编程机制。

## 类定义

```python
class MyClass:
    """类的文档字符串。"""

    class_var = 'shared'  # 类变量（所有实例共享）

    def __init__(self, value):
        self.instance_var = value  # 实例变量

    def method(self):
        return self.instance_var
```

- `self` 是实例引用，必须作为方法的第一个参数（约定名称）
- `__init__` 是初始化方法（不是构造器）
- 类变量 vs 实例变量：类变量在类体中定义，实例变量在 `__init__` 中通过 `self.x = ...` 定义

## 命名空间与作用域

- 类定义创建新的命名空间
- 方法内访问顺序：局部 → 外层函数 → 全局 → 内置
- 方法必须通过 `self` 访问实例属性（Python 没有隐式 this）

## 继承

```python
class DerivedClass(BaseClass):
    def method(self):
        super().method()  # 调用父类方法
        # 扩展行为
```

- 属性查找：实例 → 类 → 基类（深度优先，左到右）
- `isinstance(obj, Class)`：检查实例关系
- `issubclass(A, B)`：检查继承关系

### 多重继承

```python
class C(A, B):
    pass
```

- 方法解析顺序（MRO）：C3 线性化算法
- `super()` 按 MRO 顺序调用

## 私有变量

- `_single_leading_underscore`：约定为内部使用（不强制）
- `__double_leading_underscore`：触发 name mangling（`_ClassName__var`），避免子类意外覆盖

## 特殊方法

- `__init__`：初始化
- `__str__`：`str()` / `print()` 的输出
- `__repr__`：开发者友好的表示
- `__iter__` / `__next__`：迭代器协议（见 [[concepts/iterators-and-generators]]）

## 数据类风格

```python
class Point:
    __match_args__ = ('x', 'y')  # 支持 match 语句位置匹配
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

## 设计原则

- Python 的 OOP 是"约定优于强制"——没有真正的 private
- 鼓励 duck typing："如果它走起来像鸭子、叫起来像鸭子，那它就是鸭子"
- 组合优于继承（但继承在 Python 中很轻量）

## 来源

- [[sources/2026-05-13-python311-tutorial]]
