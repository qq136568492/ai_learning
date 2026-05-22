# 魔术方法（特殊方法）｜从小白到能用的系统讲义

<参考资料>

- https://docs.python.org/3/reference/datamodel.html#special-method-names ：Python 官方数据模型，特殊方法总览
- https://docs.python.org/3/reference/datamodel.html#basic-customization ：`__repr__`、`__str__`、比较、哈希、布尔值
- https://docs.python.org/3/reference/datamodel.html#emulating-container-types ：容器相关特殊方法
- https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types ：数值与运算符相关特殊方法
- https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers ：上下文管理器协议
- https://docs.python.org/3/howto/descriptor.html ：描述符 HowTo，用于后续理解方法绑定与 `property`

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/classes-and-oop.md`：类、对象、`self`、`__init__`、特殊方法入口
- `obsidian-vault/LLM_Learning/wiki/topics/python-data-model.md`：一切皆对象、身份/类型/值、可变性、序列协议、映射协议、真值
- `obsidian-vault/LLM_Learning/wiki/concepts/iterators-and-generators.md`：`__iter__`、`__next__`、`for` 循环本质
- `obsidian-vault/LLM_Learning/wiki/concepts/context-managers.md`：`__enter__`、`__exit__` 与资源生命周期
- `obsidian-vault/LLM_Learning/wiki/concepts/string-formatting.md`：`str()`、`repr()`、f-string 中的 `!r`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md` 与 `raw/Python进阶到AI应用_完整学习地图.md`：本章位于 D3/D4，承接 OOP、迭代器、上下文管理器，进入 Python 进阶语法

---

## 小白视角：原文教学缺口与本版修复

原文适合已经懂类和 OOP 的读者快速复习，但对完全不了解魔术方法的初学者来说有明显缺口。本版补齐以下内容。

| 原文缺口 | 小白会卡在哪里 | 本版修复 |
|---|---|---|
| 前置知识默认过高 | 不知道类、对象、`self`、普通方法调用和魔术方法调用有什么关系 | 新增“前置知识极速补齐” |
| 缺少触发映射 | 不知道 `len(x)`、`x + y`、`for x in obj` 到底调用了谁 | 新增“语法到魔术方法映射表” |
| 示例过短 | 看得懂单点代码，但不知道如何组合成一个类 | 用 `Money` 贯穿展示、相等、加法、布尔值 |
| 没有反例 | 不知道错误写法为什么危险 | 新增可变哈希、错误 `__eq__`、错误 `__len__`、递归属性访问等反例 |
| 覆盖范围偏窄 | 只知道少数方法，不知道魔术方法全局版图 | 新增常见魔术方法分类地图 |
| 缺少练习答案 | 自学后无法判断自己写得对不对 | 新增基础/进阶/开放题与参考答案 |
| 没有明确边界 | 容易为了炫技重载一堆运算符 | 新增适用范围、禁忌边界、工程取舍 |

---

## 上一章核心收获回顾（衔接「上下文管理器」）

- 你已经知道 `with` 可以帮我们管理资源的进入和退出。
- 你已经见过 `__enter__` 和 `__exit__`，它们会被 `with` 自动调用。
- 你已经学过类、对象、`self` 和 `__init__`，知道实例属性通常写在 `self.xxx` 上。
- 你已经接触过 Python 数据模型：对象有身份 `id`、类型 `type` 和值 `value`。
- 你已经知道 `is` 比较“是不是同一个对象”，`==` 更常用于比较“值是否相等”。

但是，我们遇到了一个新问题……

我们自己写的类默认不像内置类型那样好用。比如 `list` 可以 `len(x)`，`dict` 可以 `key in d`，数字可以 `a + b`，字符串可以 `print(s)`。可是我们自己写的 `Money`、`Vector`、`Cart` 默认并不知道这些语法该怎么工作。

因此本章需要：学会给自己的类接上 Python 内置语法的“插口”，让对象可以自然地参与 `print()`、`len()`、`==`、`+`、`in`、`for`、`with`、`obj()` 等操作，同时知道什么时候不该接、接错了会带来什么 bug。

---

## 本章学习目标

学完本章，你应该能做到：

1. 说清楚魔术方法是什么，以及为什么它们通常不应该被手动调用。
2. 看懂常见语法背后触发的特殊方法，例如 `len(obj)` 触发 `__len__`。
3. 为自己的类实现常用方法：`__repr__`、`__str__`、`__eq__`、`__hash__`、`__len__`、`__bool__`、`__getitem__`、`__contains__`、`__iter__`、`__add__`、`__call__`。
4. 理解 `NotImplemented` 的作用，并区分它和 `NotImplementedError`。
5. 避免高频坑：可变对象乱写 `__hash__`、运算符乱抛 `TypeError`、随便自创 `__xxx__` 名字。
6. 在工程中判断：这个类到底应该实现魔术方法，还是用普通命名方法更清晰。

---

## 前置知识极速补齐

### 1. 类、对象、实例方法是什么

一句话：类像“图纸”，对象像“按图纸造出来的具体东西”，实例方法是这个东西能做的动作。

```python
class Student:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def is_passed(self) -> bool:
        return self.score >= 60


s = Student("小明", 85)
print(s.name)          # 小明
print(s.is_passed())   # True
```

关键点：

- `Student` 是类。
- `s` 是对象，也叫实例。
- `self` 指向当前这个对象。
- `__init__` 负责初始化对象，不是“真正创建对象”的全部过程，但初学阶段可以先理解为“对象刚出生时要填哪些信息”。

### 2. 对象有身份、类型和值

来自 Python 数据模型的核心观点：Python 中每个值都是对象，每个对象有三件事。

```python
x = [1, 2, 3]

print(id(x))      # 身份：这个对象是谁
print(type(x))    # 类型：这个对象支持哪些操作
print(x)          # 值：这个对象当前包含什么数据
```

理解这点后，魔术方法就不神秘了：对象的“类型”决定它支持哪些操作，而魔术方法就是你告诉 Python“我的类型支持这些操作”的方式。

### 3. 普通方法 vs 魔术方法

普通方法由你直接调用。

```python
class Bag:
    def size(self) -> int:
        return 3


bag = Bag()
print(bag.size())  # 3
```

魔术方法通常由 Python 语法或内置函数自动调用。

```python
class Bag:
    def __len__(self) -> int:
        return 3


bag = Bag()
print(len(bag))    # 3，背后会找 Bag.__len__
```

工程习惯：日常代码里写 `len(bag)`，不要写 `bag.__len__()`。后者能跑，但破坏了 Python 的统一表达方式。

---

## 动机：为什么要学魔术方法

先看一个没有魔术方法的写法。

```python
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents


def money_to_text(money: Money) -> str:
    return f"{money.cents / 100:.2f} 元"


def money_equal(left: Money, right: Money) -> bool:
    return left.cents == right.cents


def money_add(left: Money, right: Money) -> Money:
    return Money(left.cents + right.cents)


m1 = Money(1200)
m2 = Money(800)

print(money_to_text(money_add(m1, m2)))
print(money_equal(m1, m2))
```

问题不是“不能用”，而是表达不自然：

- 打印金额要记住 `money_to_text()`。
- 比较金额要记住 `money_equal()`。
- 金额相加要记住 `money_add()`。
- 读业务代码的人要额外背一套函数名。

使用魔术方法后，可以写成更接近自然语言的代码。

```python
m1 = Money(1200)
m2 = Money(800)

print(m1 + m2)
print(m1 == m2)
```

这就是魔术方法的价值：让你的对象接入 Python 已经存在的语法系统。

---

## 类比：遥控器按钮和机器插口

把一个类想象成一台机器。普通方法像你自己贴上去的按钮，比如 `.pay()`、`.add_item()`、`.total()`。

魔术方法像机器背后的标准插口。Python 已经规定好：

- 如果你想让 `len(obj)` 能用，就提供 `__len__` 这个插口。
- 如果你想让 `obj1 + obj2` 能用，就提供 `__add__` 这个插口。
- 如果你想让 `for x in obj` 能用，就提供 `__iter__` 这个插口。

注意：不是插口越多越好。一个遥控器如果有 80 个按钮，初学者和团队成员都会迷路。只实现真实需要的魔术方法，才是工程上更好的选择。

---

## 核心定义：什么是魔术方法

魔术方法，也叫特殊方法、dunder 方法，是类中一类名字固定、以双下划线开头并以双下划线结尾的方法，例如 `__len__`、`__str__`、`__add__`。

它的核心特点：

1. 名字由 Python 语言协议规定，不能随便自创。
2. 通常不是你手动调用，而是由语法或内置函数自动触发。
3. 作用是让自定义对象表现得像 Python 内置对象。
4. 本质上没有“魔法”，只是 Python 在固定时机查找固定名字。

最小例子：

```python
class Box:
    def __len__(self) -> int:
        return 5


box = Box()
print(len(box))  # 5
```

当你写 `len(box)` 时，Python 会去 `Box` 这个类型上找 `__len__`，找到后调用它。

---

## 语法到魔术方法映射表

这是本章最重要的地图。先记常用的，不需要一次背完整张表。

| 你写的代码 | Python 大致会找的方法 | 用途 |
|---|---|---|
| `obj = Class(...)` | `__new__`、`__init__` | 创建和初始化对象 |
| `repr(obj)` | `__repr__` | 开发者视角的对象表示 |
| `str(obj)` | `__str__` | 用户视角的可读文本 |
| `print(obj)` | `__str__`，没有时退回 `__repr__` | 打印对象 |
| `f"{obj}"` | `__format__`，常退回 `__str__` | 格式化输出 |
| `f"{obj!r}"` | `__repr__` | f-string 中强制使用开发者表示 |
| `obj == other` | `__eq__` | 判断值是否相等 |
| `obj < other` | `__lt__` | 小于比较 |
| `hash(obj)` | `__hash__` | 计算哈希值 |
| `if obj:` | `__bool__`，没有时看 `__len__` | 真值判断 |
| `len(obj)` | `__len__` | 长度 |
| `obj[index]` | `__getitem__` | 索引或切片读取 |
| `obj[index] = value` | `__setitem__` | 索引赋值 |
| `del obj[index]` | `__delitem__` | 索引删除 |
| `item in obj` | `__contains__`，没有时尝试迭代 | 成员检测 |
| `for item in obj` | `__iter__`，迭代器再用 `__next__` | 遍历 |
| `next(iterator)` | `__next__` | 取下一个元素 |
| `obj + other` | `__add__` | 加法 |
| `other + obj` | `__radd__` | 右侧加法兜底 |
| `obj += other` | `__iadd__`，没有时退回 `__add__` | 原地加法 |
| `obj()` | `__call__` | 让对象像函数一样被调用 |
| `with obj as x:` | `__enter__`、`__exit__` | 上下文管理 |

学习建议：

- 第一批掌握：`__repr__`、`__str__`、`__eq__`、`__len__`、`__bool__`。
- 第二批掌握：`__getitem__`、`__contains__`、`__iter__`、`__next__`。
- 第三批掌握：`__add__`、`__radd__`、`__iadd__`、`__hash__`、`__call__`。
- 高级再学：`__new__`、属性访问、描述符、异步魔术方法。

---

## 精讲一：展示对象，`__repr__` 与 `__str__`

### What：它们是什么

`__repr__` 和 `__str__` 都负责把对象变成字符串，但目标读者不同。

- `__repr__` 面向开发者，目标是清楚、无歧义、方便调试。
- `__str__` 面向普通用户，目标是好读、简洁、适合展示。

### Why：为什么需要它们

默认情况下，自定义对象打印出来通常像这样：

```python
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents


m = Money(1200)
print(m)      # <__main__.Money object at 0x...>
```

这个输出对排查问题帮助很小，因为你看不到金额是多少。

### How：怎么写

```python
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money(cents={self.cents})"

    def __str__(self) -> str:
        return f"{self.cents / 100:.2f} 元"


m = Money(1200)
print(repr(m))   # Money(cents=1200)
print(str(m))    # 12.00 元
print(m)         # 12.00 元
print(f"{m!r}") # Money(cents=1200)
```

工程建议：

- 优先写好 `__repr__`，因为调试、日志、测试失败时更依赖它。
- 如果对象要展示给用户，再写 `__str__`。
- 两者都必须返回 `str`，不能返回数字、列表或 `None`。

---

## 精讲二：相等判断，`__eq__`

### What：它是什么

`__eq__` 决定 `obj == other` 的结果。

默认情况下，如果你没有写 `__eq__`，自定义对象通常按身份比较：是不是同一个对象。

```python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)  # False，因为默认不是比较 x/y，而是比较是不是同一个对象
print(p1 is p2)  # False
```

### Why：为什么要自定义

在业务中，我们经常关心“值是否相等”，而不是“是不是同一个对象”。

两个 `Money(1200)` 通常应该被认为金额相等。

### How：正确写法

```python
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money(cents={self.cents})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents


print(Money(1200) == Money(1200))  # True
print(Money(1200) == Money(800))   # False
print(Money(1200) == 1200)         # False
```

关键点：

- 参数类型通常写成 `object`，因为别人可以拿任何东西和你比较。
- 遇到不认识的类型，推荐 `return NotImplemented`，让 Python 尝试对方的比较逻辑或给出合理结果。
- 不要直接访问 `other.cents`，除非你已经确认 `other` 是 `Money`。

错误写法：

```python
class BadMoney:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __eq__(self, other: object) -> bool:
        return self.cents == other.cents  # other 可能是 int、str、None
```

这会导致：

```python
BadMoney(1200) == 1200  # AttributeError: 'int' object has no attribute 'cents'
```

---

## 精讲三：哈希，`__hash__`

### What：它是什么

`__hash__` 决定一个对象能否放进 `set`，或能否当 `dict` 的键。

```python
x = "name"
d = {x: "小明"}  # 字符串可哈希，所以能当 key
```

### Why：为什么它危险

字典和集合依赖一个前提：键的哈希值在它待在字典或集合期间不能变化。

如果对象的内容变了，哈希也跟着变，字典就可能找不到原来的键。

### 规则：相等与哈希必须一致

核心规则：如果 `a == b` 为 `True`，那么 `hash(a) == hash(b)` 也必须为 `True`。

正确示例：不可变金额可以哈希。

```python
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents

    def __hash__(self) -> int:
        return hash(self.cents)


prices = {Money(1200): "午餐"}
print(prices[Money(1200)])  # 午餐
```

但这段代码还有隐患：`cents` 仍然能被改。

```python
m = Money(1200)
prices = {m: "午餐"}
m.cents = 9999
# 现在 m 的哈希值变了，字典内部位置可能对不上
```

更稳妥的写法：用 `frozen=True` 的数据类。

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    cents: int


prices = {Money(1200): "午餐"}
print(prices[Money(1200)])  # 午餐
```

边界原则：

- 可变对象通常不要写 `__hash__`。
- 写了 `__eq__` 后，如果没有写 `__hash__`，Python 通常会把对象变成不可哈希，这是安全设计。
- 真要当字典键，优先使用不可变对象、不可变快照或外部稳定 id。

---

## 精讲四：真值判断，`__bool__` 与 `__len__`

### What：它们是什么

`__bool__` 决定 `bool(obj)` 和 `if obj:` 的结果。

如果没有 `__bool__`，Python 会看 `__len__`。长度为 0 时是假，非 0 时是真。

```python
class Cart:
    def __init__(self, items: list[str]) -> None:
        self.items = items

    def __len__(self) -> int:
        return len(self.items)


empty_cart = Cart([])
full_cart = Cart(["apple"])

print(bool(empty_cart))  # False
print(bool(full_cart))   # True
```

### Why：为什么有用

你可以写出更自然的业务代码。

```python
if full_cart:
    print("可以结算")
else:
    print("购物车为空")
```

### How：什么时候用哪个

- 如果对象天然有长度，例如购物车、队列、结果集，写 `__len__` 即可。
- 如果对象没有长度，但有明确真假状态，例如连接是否打开，可以写 `__bool__`。

```python
class Connection:
    def __init__(self) -> None:
        self.closed = False

    def close(self) -> None:
        self.closed = True

    def __bool__(self) -> bool:
        return not self.closed


conn = Connection()
print(bool(conn))  # True
conn.close()
print(bool(conn))  # False
```

注意：`__len__` 必须返回大于等于 0 的整数。

---

## 精讲五：容器味道，`__len__`、`__getitem__`、`__contains__`

### What：它们是什么

如果你的对象像列表、字典、购物车、配置表、只读数据集，就可以考虑实现容器相关魔术方法。

| 方法 | 触发语法 | 说明 |
|---|---|---|
| `__len__` | `len(obj)` | 返回元素数量 |
| `__getitem__` | `obj[key]` | 按索引或键取值 |
| `__setitem__` | `obj[key] = value` | 按索引或键赋值 |
| `__delitem__` | `del obj[key]` | 按索引或键删除 |
| `__contains__` | `item in obj` | 判断成员是否存在 |

### 极简示例：只读课程表

```python
class CourseList:
    def __init__(self, courses: list[str]) -> None:
        self._courses = list(courses)

    def __len__(self) -> int:
        return len(self._courses)

    def __getitem__(self, index: int) -> str:
        return self._courses[index]

    def __contains__(self, course: object) -> bool:
        return course in self._courses


courses = CourseList(["Python", "FastAPI", "RAG"])

print(len(courses))          # 3
print(courses[0])            # Python
print("FastAPI" in courses)  # True
```

### 切片怎么处理

`obj[1:3]` 传给 `__getitem__` 的不是整数，而是 `slice` 对象。

```python
class CourseList:
    def __init__(self, courses: list[str]) -> None:
        self._courses = list(courses)

    def __getitem__(self, index: int | slice):
        return self._courses[index]


courses = CourseList(["Python", "FastAPI", "RAG"])
print(courses[1:])  # ['FastAPI', 'RAG']
```

工程提醒：

- 如果 `in` 很常用，优先写 `__contains__`，避免退化成逐个遍历。
- 如果对象是只读的，不要为了“完整”去写 `__setitem__` 和 `__delitem__`。
- 只实现真实需要的协议，不要抄满整张表。

---

## 精讲六：遍历对象，`__iter__` 与 `__next__`

### What：它们是什么

先用白话说：如果一个对象能被 `for` 一个个取出内容，它就是“可遍历的”。正式术语叫“可迭代对象”。

`for item in obj` 背后大致做了三步：

```python
it = iter(obj)       # 找 obj.__iter__()
item = next(it)      # 找 it.__next__()
# 没有下一个元素时，__next__ 抛出 StopIteration，for 循环结束
```

### 初学者最常用写法：让 `__iter__` 交给内部列表

```python
class CourseList:
    def __init__(self, courses: list[str]) -> None:
        self._courses = list(courses)

    def __iter__(self):
        return iter(self._courses)


courses = CourseList(["Python", "FastAPI", "RAG"])

for course in courses:
    print(course)
```

输出：

```text
Python
FastAPI
RAG
```

这种写法最适合初学者：你的类自己不手写 `__next__`，而是复用列表已经实现好的迭代能力。

### 进阶写法：自己写迭代器

```python
class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for number in Countdown(3):
    print(number)
```

输出：

```text
3
2
1
```

边界提醒：

- `__iter__` 负责返回一个能不断取值的对象。
- `__next__` 负责返回下一个值。
- 没有下一个值时，必须抛 `StopIteration`，不是返回 `None`。
- 大多数业务类不需要自己写 `__next__`，让 `__iter__` 返回内部列表、元组、字典的迭代器即可。

---

## 精讲七：运算符重载，`__add__`、`__radd__`、`__iadd__`

### What：它们是什么

运算符重载就是让自定义对象支持 `+`、`-`、`*`、`/`、`@` 等运算符。

| 语法 | 常见方法 | 说明 |
|---|---|---|
| `a + b` | `__add__` | 左侧对象处理加法 |
| `b + a` | `__radd__` | 右侧对象处理加法兜底 |
| `a += b` | `__iadd__` | 原地加法，常见于可变对象 |
| `a - b` | `__sub__` | 减法 |
| `a * b` | `__mul__` | 乘法 |
| `a @ b` | `__matmul__` | 矩阵乘法或类似领域运算 |

### Why：什么时候值得用

适合：

- 金额相加：`Money(100) + Money(200)`。
- 向量相加：`Vector(1, 2) + Vector(3, 4)`。
- 矩阵乘法：`matrix_a @ matrix_b`。

不适合：

- 有副作用的操作，例如 `user + role` 顺便写数据库。
- 参数复杂的业务动作，例如付款、审批、发消息。
- 团队看到运算符也猜不出含义的场景。

### How：实现 `Money + Money`

```python
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money(cents={self.cents})"

    def __add__(self, other: object):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.cents + other.cents)


print(Money(1200) + Money(800))  # Money(cents=2000)
```

### `NotImplemented` 是什么

`NotImplemented` 是一个特殊返回值，意思是：“这个类型组合我不会处理，请 Python 尝试别的方案。”

它不是异常，不等于 `NotImplementedError`。

```python
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __add__(self, other: object):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.cents + other.cents)
```

不要把它写成：

```python
raise NotImplementedError
```

`NotImplementedError` 通常用于“这个方法我以后要实现，但现在没写”，不是运算符协作的正确返回值。

### `__radd__`：为什么 `sum()` 可能需要它

`sum([Money(100), Money(200)])` 的起点默认是 `0`，所以它会先尝试 `0 + Money(100)`。

```python
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money(cents={self.cents})"

    def __add__(self, other: object):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.cents + other.cents)

    def __radd__(self, other: object):
        if other == 0:
            return self
        return self.__add__(other)


print(sum([Money(100), Money(200), Money(300)]))  # Money(cents=600)
```

### `__iadd__`：`+=` 到底会不会改原对象

对不可变值对象，通常不写 `__iadd__`，让 `a += b` 创建新对象。

```python
m1 = Money(100)
old_id = id(m1)
m1 += Money(200)
print(m1)              # Money(cents=300)
print(id(m1) == old_id) # False，通常是新对象
```

如果你的对象是可变容器，例如购物车，才考虑让 `__iadd__` 修改原对象。

---

## 精讲八：可调用对象，`__call__`

### What：它是什么

`__call__` 让对象可以像函数一样被调用。

```python
class AddTax:
    def __init__(self, rate: float) -> None:
        self.rate = rate

    def __call__(self, price: float) -> float:
        return price * (1 + self.rate)


tax_6_percent = AddTax(0.06)
print(tax_6_percent(100))  # 106.0
```

### Why：什么时候有用

适合把“带配置的函数”封装成对象。

例如：

- 带税率的价格计算器。
- 带阈值的文本过滤器。
- 带模型配置的预测器。
- 带状态的回调函数。

如果对象没有配置或状态，普通函数通常更简单。

---

## 精讲九：上下文管理，`__enter__` 与 `__exit__`

### What：它们是什么

`__enter__` 和 `__exit__` 让对象支持 `with`。

```python
class DemoContext:
    def __enter__(self):
        print("进入")
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        print("退出")
        return False


with DemoContext():
    print("处理中")
```

输出：

```text
进入
处理中
退出
```

### Why：为什么和上一章有关

上下文管理器用于安全管理资源生命周期：获取资源、使用资源、释放资源。

常见场景：

- 文件自动关闭。
- 数据库连接自动释放。
- 锁自动释放。
- 临时配置恢复。

### How：最小文件风格示例

```python
class ManagedResource:
    def __enter__(self):
        print("打开资源")
        return self

    def use(self) -> None:
        print("使用资源")

    def __exit__(self, exc_type, exc, tb) -> bool:
        print("清理资源")
        return False


with ManagedResource() as resource:
    resource.use()
```

初学阶段先记住：

- `__enter__` 在进入 `with` 代码块前调用。
- `__exit__` 在离开 `with` 代码块时调用，即使中间发生异常也会调用。
- `__exit__` 返回 `True` 表示吞掉异常，返回 `False` 表示异常继续抛出。通常返回 `False`。

---

## 精讲十：对象创建与属性访问，高级入口先认识

这一节先建立地图，不要求本章完全掌握。

### `__new__` 与 `__init__`

`Class(...)` 大致会经历：

1. `__new__` 创建对象。
2. `__init__` 初始化对象。
3. 返回对象。

初学阶段大多数时候只写 `__init__`。

```python
class User:
    def __init__(self, name: str) -> None:
        self.name = name
```

什么时候才关注 `__new__`：

- 写不可变类型的子类。
- 控制对象创建过程。
- 实现单例等特殊模式。

### `__del__`

`__del__` 可能在对象被回收前调用，但不建议依赖它做关键资源清理。

原因：对象什么时候被回收与 Python 实现、引用关系、解释器退出时机有关。资源清理优先用 `with` 或显式 `close()`。

### 属性访问相关方法

| 方法 | 作用 | 初学者建议 |
|---|---|---|
| `__getattr__` | 属性不存在时兜底 | 可以了解，少量使用 |
| `__getattribute__` | 每次访问属性都会经过它 | 高风险，容易无限递归 |
| `__setattr__` | 设置属性时触发 | 谨慎使用 |
| `__delattr__` | 删除属性时触发 | 谨慎使用 |

错误示例：

```python
class Bad:
    def __getattribute__(self, name: str):
        return self.name  # 访问 self.name 又会触发 __getattribute__，无限递归
```

本章只需要知道：这些属于高级魔术方法，遇到框架源码时能认出来即可。

---

## 常用魔术方法分类地图

| 类别 | 常见方法 | 常见语法 | 本章掌握要求 |
|---|---|---|---|
| 创建初始化 | `__new__`、`__init__` | `Class(...)` | 会用 `__init__`，知道 `__new__` 更底层 |
| 销毁 | `__del__` | 对象回收前可能触发 | 知道不应依赖它清理关键资源 |
| 展示 | `__repr__`、`__str__`、`__format__` | `repr()`、`str()`、`print()`、f-string | 重点掌握 |
| 比较 | `__eq__`、`__lt__`、`__le__`、`__gt__`、`__ge__` | `==`、`<`、`<=`、`>`、`>=` | 重点掌握 `__eq__` |
| 哈希 | `__hash__` | `hash()`、`set`、`dict` key | 理解规则，谨慎实现 |
| 真值 | `__bool__`、`__len__` | `bool()`、`if obj:` | 重点掌握 |
| 容器 | `__len__`、`__getitem__`、`__setitem__`、`__delitem__`、`__contains__` | `len()`、`obj[i]`、`in` | 重点掌握只读场景 |
| 迭代 | `__iter__`、`__next__` | `for`、`iter()`、`next()` | 重点掌握 `__iter__` |
| 算术 | `__add__`、`__sub__`、`__mul__`、`__truediv__`、`__matmul__` | `+`、`-`、`*`、`/`、`@` | 按领域需要掌握 |
| 反向算术 | `__radd__`、`__rsub__`、`__rmul__` | `other + obj` | 了解协作链 |
| 原地算术 | `__iadd__`、`__isub__` | `+=`、`-=` | 可变对象再考虑 |
| 可调用 | `__call__` | `obj()` | 掌握常见用法 |
| 上下文 | `__enter__`、`__exit__` | `with` | 已在上一章重点学过 |
| 属性访问 | `__getattr__`、`__getattribute__`、`__setattr__` | `obj.x`、`obj.x = v` | 高级主题，谨慎使用 |
| 描述符 | `__get__`、`__set__`、`__delete__` | `property`、方法绑定 | 后续深入 |
| 异步 | `__aiter__`、`__anext__`、`__aenter__`、`__aexit__` | `async for`、`async with` | asyncio 章节学习 |

---

## 辨析：容易混淆的概念

### 1. `__repr__` vs `__str__`

| 对比项 | `__repr__` | `__str__` |
|---|---|---|
| 读者 | 开发者 | 普通用户 |
| 触发 | `repr(obj)`、`f"{obj!r}"` | `str(obj)`、`print(obj)` |
| 风格 | 信息完整、无歧义 | 简洁、好读 |
| 没写时 | 使用默认对象表示 | 常退回 `__repr__` |

### 2. `is` vs `==`

| 表达式 | 含义 | 依赖魔术方法吗 |
|---|---|---|
| `a is b` | 是否同一个对象 | 不依赖 `__eq__` |
| `a == b` | 值是否相等 | 依赖 `__eq__` |

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True，值相等
print(a is b)  # False，不是同一个列表对象
```

### 3. `NotImplemented` vs `NotImplementedError`

| 名称 | 类型 | 用法 |
|---|---|---|
| `NotImplemented` | 特殊返回值 | 运算符或比较方法不会处理当前类型组合时返回 |
| `NotImplementedError` | 异常 | 抽象方法、暂未实现的方法中抛出 |

### 4. `__add__` vs `__radd__` vs `__iadd__`

| 方法 | 触发 | 含义 |
|---|---|---|
| `__add__` | `a + b` | 让左侧对象处理加法 |
| `__radd__` | 左侧处理不了时 | 让右侧对象兜底处理加法 |
| `__iadd__` | `a += b` | 尝试原地加法 |

### 5. `__iter__` vs `__next__`

| 方法 | 职责 |
|---|---|
| `__iter__` | 返回一个能取值的迭代器 |
| `__next__` | 返回下一个值，没有时抛 `StopIteration` |

---

## 陷阱：高频错误与改法

### 陷阱 1：手动调用魔术方法

错误写法：

```python
length = obj.__len__()
```

推荐写法：

```python
length = len(obj)
```

原因：魔术方法是接入语言协议的钩子，调用处应该使用 Python 的统一语法。

### 陷阱 2：随便自创双下划线名字

错误写法：

```python
class User:
    def __save_to_db__(self):
        pass
```

推荐写法：

```python
class User:
    def save_to_db(self):
        pass
```

原因：`__xxx__` 命名空间留给 Python 语言协议和标准生态。业务方法用普通名字。

### 陷阱 3：`__repr__` 返回的不是字符串

错误写法：

```python
class Money:
    def __repr__(self):
        return 123
```

后果：

```text
TypeError: __repr__ returned non-string
```

推荐写法：

```python
class Money:
    def __repr__(self) -> str:
        return "Money(cents=123)"
```

### 陷阱 4：`__eq__` 不检查类型

错误写法：

```python
def __eq__(self, other):
    return self.cents == other.cents
```

推荐写法：

```python
def __eq__(self, other: object) -> bool:
    if not isinstance(other, Money):
        return NotImplemented
    return self.cents == other.cents
```

### 陷阱 5：可变对象实现 `__hash__`

错误原因：对象内容变了，哈希值可能变，字典和集合会出错。

推荐做法：

- 不可变值对象：可以考虑 `frozen=True` 的 `dataclass`。
- 可变对象：通常不要实现 `__hash__`。
- 需要当 key：使用稳定 id 或不可变快照。

### 陷阱 6：运算符里直接抛 `TypeError`

不推荐：

```python
def __add__(self, other: object):
    if not isinstance(other, Money):
        raise TypeError("只能和 Money 相加")
```

更推荐：

```python
def __add__(self, other: object):
    if not isinstance(other, Money):
        return NotImplemented
    return Money(self.cents + other.cents)
```

原因：`NotImplemented` 允许 Python 尝试反向方法，例如 `other.__radd__(self)`。

### 陷阱 7：`__len__` 返回负数或非整数

错误写法：

```python
def __len__(self):
    return -1
```

推荐写法：

```python
def __len__(self) -> int:
    return len(self.items)
```

`__len__` 必须返回大于等于 0 的整数。

### 陷阱 8：为了炫技实现一堆运算符

错误方向：

```python
user1 + user2
order1 * coupon
config_a - config_b
```

如果团队无法一眼看懂运算符的领域含义，就应该用普通方法。

```python
user.merge(user2)
order.apply_coupon(coupon)
config_a.diff(config_b)
```

---

## 双重示例 A：极简入门 Demo，`Money` 值对象

目标：实现一个可以展示、比较、相加、用于 `if` 判断的金额类。

```python
class Money:
    def __init__(self, cents: int) -> None:
        if cents < 0:
            raise ValueError("金额不能为负数")
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money(cents={self.cents})"

    def __str__(self) -> str:
        return f"{self.cents / 100:.2f} 元"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents

    def __bool__(self) -> bool:
        return self.cents != 0

    def __add__(self, other: object):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.cents + other.cents)


m1 = Money(1200)
m2 = Money(800)
zero = Money(0)

print(repr(m1))       # Money(cents=1200)
print(str(m1))        # 12.00 元
print(m1 == Money(1200))
print(m1 + m2)        # 20.00 元
print(bool(zero))     # False
```

运行方式：

```bash
python money_demo.py
```

预期输出：

```text
Money(cents=1200)
12.00 元
True
20.00 元
False
```

这个例子适合学习魔术方法的第一阶段，因为它只实现了业务真正需要的几个按钮。

---

## 双重示例 B：工程最小切片，只读配置对象

场景：项目中经常有配置字典，但你不希望外部随便改内部数据。可以封装一个只读对象，让它支持 `len()`、`[]`、`in`、`for`。

```python
class ReadonlySettings:
    def __init__(self, data: dict[str, str]) -> None:
        self._data = dict(data)

    def __repr__(self) -> str:
        return f"ReadonlySettings(keys={list(self._data)})"

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key: str) -> str:
        return self._data[key]

    def __contains__(self, key: object) -> bool:
        return key in self._data

    def __iter__(self):
        return iter(self._data)

    def get(self, key: str, default: str | None = None) -> str | None:
        return self._data.get(key, default)


settings = ReadonlySettings({
    "host": "127.0.0.1",
    "port": "8000",
    "debug": "false",
})

print(settings)
print(len(settings))
print(settings["host"])
print("debug" in settings)

for key in settings:
    print(key, "=", settings[key])
```

预期输出：

```text
ReadonlySettings(keys=['host', 'port', 'debug'])
3
127.0.0.1
True
host = 127.0.0.1
port = 8000
debug = false
```

工程取舍：

- 这里没有实现 `__setitem__`，因为对象目标是只读。
- 这里保留了普通方法 `.get()`，因为 `dict.get()` 是团队熟悉的显式 API。
- 如果未来要完整模拟字典，再考虑继承或组合 `collections.abc.Mapping`，不要一开始就抄满所有方法。

---

## 什么时候该用魔术方法，什么时候别用

### 适合使用

- 对象天然像某种内置类型：容器、数值、函数、上下文资源。
- 语法含义清晰，不需要额外解释。
- 实现后能明显提升可读性，例如 `len(cart)`、`item in cart`、`money1 + money2`。
- 你能写出清楚的测试，证明行为符合直觉。

### 不适合使用

- 操作有明显副作用，例如写数据库、发网络请求、扣款。
- 运算符含义不符合大多数人的直觉。
- 只是为了“看起来高级”。
- 普通方法更能表达业务含义，例如 `.pay()`、`.merge()`、`.validate()`。

一句工程原则：魔术方法应该让代码更像 Python，而不是让代码像谜语。

---

## 与 `dataclass` 的关系

如果一个类主要是保存数据，优先考虑 `dataclass`。

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p = Point(1, 2)
print(p)                 # Point(x=1, y=2)
print(p == Point(1, 2))  # True
```

`dataclass` 会自动生成常见方法，例如：

- `__init__`
- `__repr__`
- `__eq__`

如果希望对象不可变并且适合当字典键，可以考虑：

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


points = {Point(1, 2): "A"}
print(points[Point(1, 2)])
```

注意：`dataclass` 不是替代所有魔术方法。它适合数据类；如果你要实现容器、迭代、上下文管理、可调用对象，仍然需要理解对应协议。

---

## 练习

### 基础题：展示与相等

实现 `Score(value: int)`：

- `repr(Score(90))` 输出 `Score(value=90)`。
- `str(Score(90))` 输出 `90 分`。
- `Score(90) == Score(90)` 为 `True`。
- `Score(90) == 90` 不应报错。

参考答案：

```python
class Score:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Score(value={self.value})"

    def __str__(self) -> str:
        return f"{self.value} 分"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value


assert repr(Score(90)) == "Score(value=90)"
assert str(Score(90)) == "90 分"
assert Score(90) == Score(90)
assert Score(90) != 90
```

### 进阶题：容器对象

实现 `TodoList`：

- 支持 `len(todos)`。
- 支持 `todos[0]`。
- 支持 `"学 Python" in todos`。
- 支持 `for item in todos`。

参考答案：

```python
class TodoList:
    def __init__(self, items: list[str]) -> None:
        self._items = list(items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> str:
        return self._items[index]

    def __contains__(self, item: object) -> bool:
        return item in self._items

    def __iter__(self):
        return iter(self._items)


todos = TodoList(["学 Python", "写练习", "复盘"])

assert len(todos) == 3
assert todos[0] == "学 Python"
assert "写练习" in todos
assert list(todos) == ["学 Python", "写练习", "复盘"]
```

### 开放题：团队规范

为团队制定三条“不建议使用运算符重载”的规则。

参考方向：

- 运算符有副作用时不用，例如写数据库、发请求、扣款。
- 运算符含义不符合数学或领域直觉时不用。
- 普通方法名更清晰时不用，例如 `.merge()` 比 `+` 更能表达业务含义。

---

## 费曼反问

1. 如果别人问你“魔术方法到底魔在哪里”，你能不能用 `len(obj)` 和 `__len__` 的关系讲清楚？
2. 为什么 `Money(100) == Money(100)` 默认可能是 `False`，而写了 `__eq__` 后可以变成 `True`？
3. 为什么可变对象实现 `__hash__` 往往是危险信号？
4. `NotImplemented` 和 `NotImplementedError` 的区别是什么？
5. 什么时候你会选择普通方法 `.merge()`，而不是重载 `+`？

---

## 本章闭环

不看资料，尝试口述下面这段话：

> 魔术方法是 Python 规定好的特殊方法名。我们在类里实现这些方法，不是为了手动调用它们，而是为了让对象接入 Python 的内置语法。`__repr__` 负责开发者视角展示，`__str__` 负责用户视角展示，`__eq__` 负责 `==`，`__len__` 负责 `len()`，`__iter__` 负责 `for`，`__add__` 负责 `+`。工程上只实现真正能提升可读性的魔术方法，避免炫技和破坏直觉。

---

## 来源分层

本地知识库文件：

- `obsidian-vault/LLM_Learning/wiki/concepts/classes-and-oop.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-data-model.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/iterators-and-generators.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/context-managers.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/string-formatting.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md`

外部补充：

- https://docs.python.org/3/reference/datamodel.html
- https://docs.python.org/3/howto/descriptor.html
