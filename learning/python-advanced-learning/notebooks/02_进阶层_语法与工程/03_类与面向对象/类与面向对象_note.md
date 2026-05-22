# 类与面向对象｜讲义笔记

<参考资料>

- https://docs.python.org/3/tutorial/classes.html — 官方教程：类入门
- https://docs.python.org/3/tutorial/classes.html#a-word-about-names-and-objects — 对象、名字与赋值
- https://docs.python.org/3/reference/datamodel.html#special-method-names — 特殊方法总览（进阶查阅）

外部补充：`dataclasses` 官方说明见 https://docs.python.org/3/library/dataclasses.html

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/classes-and-oop.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **D3 类与面向对象**
- `obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`
- `obsidian-vault/LLM_Learning/wiki/index.md`（概念索引导航）

---

## 上一章核心收获回顾（衔接 `02_迭代器与生成器`）

你已经能口述：Python 如何用 **`iter()` / `next()`** 驱动 `for`，以及 **`StopIteration`** 如何收尾一段遍历。

你已能写出或读懂 **惰性**流水线：不把整份数据塞进内存也能一段段取值（对标「边读文件边加工」的工程场景）。

你已建立心智：**遍历状态要能挂在什么地方**——要么靠生成器的内部挂起，要么靠可迭代／迭代器对象上的字段来维持。

你已能区分：**一口气算完的容器（eager）** 对比 **走一步算一步的惰性流水线（lazy）**，并能在简单场景选对。

你能把本节与前一章接上：当「状态和操作」不止是迭代，还要在多张业务卡里长期存在时，需要比「单靠函数套生成器」更系统的打包方式——于是进入 **类 / 实例**。

---

## 但是，我们遇到了一个新的问题……

真实业务里常出现三组痛：

1. **状态散装**：同一种「购物车 / 会话 / 用户配置」散落在多个字典和全局变量里，谁都可以改，`KeyError`/串改很难找到源头。
2. **职责不清**：处理支付、开票、发短信的函数互相调用，`if flag` 越叠越多。
3. **复用与安全**：你希望「只对合法状态调用打折」，却只能靠调用方自律。

**因此本章需要：**引入 **类** 这一种组织方式：**把和数据相关的操作收口到同一种对象上**，并分清 **写在类上的字段** 对比 **写在每个实例身上的字段**，再按需使用 **继承 + `super()`**。**Python 不靠「硬隐藏」来保证安全，而是用约定与清晰边界**（鸭子类型、`组合优于继承` 等）。

---

## 动机：一个会翻车的小场景（为什么需要类）

下面这种「全局函数 + 全局 dict」在项目早期很常见，但一旦模块变多就变脆：

```python
# 反模式示意：不推荐长期维持
sessions = {}

def login(user_id):
    sessions["current"] = user_id  # 谁都能改 sessions

def add_to_cart(item):
    uid = sessions.get("current")
    if uid is None:
        raise RuntimeError("未登录")  # 规则散落在函数里，难统一
    # ...

def checkout():
    uid = sessions.get("current")
    # ...
```

**痛在哪里？** 任何人只要能 `import` 该模块就可能改写 `sessions`；「登录态 + 购物车 + 结账规则」三件事没有贴在同一张职责卡上。  
**用一个类**：实例可以代表一张「会话卡」，规则和状态一起带走，读起来像在读业务对象本身。

---

## 类比（非编程）

- **类**像**空白表格模版**（印着「姓名、余额、可操作按钮」）。
- **实例（对象）**像**每一份已经填好的表**——张三一张、李四一张；改张三的余额不会顺带把李四的一起改掉。
- **`self`**就是那行字「本表持有者」：**方法要知道自己在操作哪一张表**，所以要把「这张表」传进来。

这和上一章迭代器类比可以连起来：**迭代器类**也是让「遍历状态挂在对象上」，而不是散落在函数外的全局计数器。

---

## 精讲

### 第一层：一句话人话定义

**类**是程序员自己定义的一种类型；**用它构造出来的东西叫实例**。  
写在类里的函数叫**方法**：实例方法通常会收到**第一个固定参数**，习惯命名 **`self`**，表示「正在被操作的那一个实例」（名字可以改，永远不要改，团队会抓狂）。

---

### 第二层：最短可用：`__init__` + 实例字段

下面的类表示「购物车里有啥」：**每个实例有自己一份 `items` 列表**。

```python
class Cart:
    """购物车：只管自己这一单的物品列表。"""

    def __init__(self):
        """构造一个空购物车实例（先理解：init 里没有 return 新业务对象）。"""
        self.items: list[str] = []

    def add(self, name: str) -> None:
        self.items.append(name)

    def describe(self) -> str:
        return f"购物车共有 {len(self.items)} 件：{', '.join(self.items)}"


c1 = Cart()
c2 = Cart()
c1.add("苹果")
assert "苹果" in c1.items
assert "苹果" not in c2.items  # 第二张表不受影响
```

**运行**：无需额外 pip，直接用 `python` 执行或在 REPL 里粘贴。

**初学提醒**：你已经在上一章学过「多个名字绑定同一可变对象会怎样」——**这里 `items` 是挂在 `self` 上的**，每个 `Cart()` 都有自己新的 `items` **除非你在类层级上共享可变默认值**（见后文陷阱）。

---

### 第三层：辨析核心 —— 类变量 vs 实例变量

| 存放在哪 | Python 写什么 | **人话** | 典型用途 |
|-----------|---------------|----------|----------|
| **类变量** | 写在 `class` 体里、**不在任何方法里的赋值**（如 `tag = ...`） | 像是「公告栏：**所有店员抬头看见同一条默认值**」（若实例自己没有覆盖） | 跨实例常量、默认值、枚举式标签 |
| **实例变量** | 一般在 `__init__` 里写 `self.x = ...` | **每张员工卡右上角手写的具体内容** | 每个对象独享状态 |

```python
class Counter:
    default_step = 1  # 类变量（公告栏）

    def __init__(self, start=0):
        self.value = start  # 实例变量（这张卡当前读数）

    def tick(self, step=None):
        s = step if step is not None else self.default_step
        self.value += s


a = Counter(0)
b = Counter(10)
Counter.default_step = 2    # 改公告栏会影响之后“没写 step 默认值”的计算
```

**进阶对比**：如果你对「赋值语句到底改的是类还是实例」不熟，回看基础层 **`数据模型与对象_note.md`**里的「名字绑定」小节。

---

### 第四层：继承 —— 「在模版上增补」而非复制粘贴

**继承**让一个类在不拷代码的前提下重用另一个类的字段与方法；需要扩展时用 **`super()`** 请父类先做一段。

```python
class BaseGreeter:
    def greet(self) -> str:
        return "您好"

class LoudGreeter(BaseGreeter):
    def greet(self) -> str:
        return super().greet() + "！"  # 先走父类的行为，再接龙


lg = LoudGreeter()
assert lg.greet().endswith("！")
```

Python 的属性查找：**先从实例找**，找不到再顺着**类型与父类链路**往外找。**不要假设「永远只问爸爸」**：若存在多个父类，顺序由 **`MRO`（下一小节）定**。

---

### 第五层：（术语闸门）「描述符」与 `obj.method(...)`——只给最小认知

你可能会听到：**实例方法其实是一种「描述符」**，所以 `cart.add("苹果")` 会自动把 **`cart`** 塞进 `self`。

**一段话定义**：可以把「描述符」理解成附着在类属性上的一个**钩子**：当你通过实例用 `.` 去取这个方法名时，Python 会跑出一段固定逻辑：**把当前的实例塞进第一个参数**。

你现在**不需要手写描述符**。只要记住结论：**只要是「定义在类里、约定第一个参数为 `self`」的实例方法**，`self` 就永远是「点号左边的那一个对象」。深实现见后续 **`魔术方法_note.md`** / 官方 Descriptor HowTo（进阶）。

---

### 第六层：（术语闸门）`MRO` ——「多个爹时，探视顺序的一张清单」

当类写的是 `class Child(A, B):`，Python 要提前排好：**找方法时应该先问谁、再问谁**，避免祖传代码互相打架。**这张顺序表叫作 MRO**，由 **C3 线性化算法**算出（你只记「有保证的一张单」即可）。

**最小可打印验证**：

```python
class A: ...
class B(A): ...
class C(A): ...
class D(B, C): ...

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

**`super()`** 在这条链上向前走一步：不是玄学「叫爸爸」，而是 **「在当前类的 MRO 里，让父母链上的下一个候选人出场」**。多重继承时请**画 MRO、写 mixin 注释**，这比背算法重要。

---

### 第七层：（术语闸门）`__` 双下划线与「名字改写」

以 **`__spam` 这类双下划线（且后缀不是另一条下划线）**开头的属性，会引发 **名字改写（history 里常被误叫 name mangling）**：编译期把名字改成 `_ClassName__spam`，从而减少**子类里不小心同名覆盖父类私有实现**的几率。

这不是「私有到别人绝对读不到」（Python 不靠这个），而是一个**务实的碰撞缓冲**：

```python
class Box:
    def __init__(self):
        self.__secret = 42  # → 实际是 _Box__secret

class SubBox(Box):
    def leak(self):
        # return self.__secret  # 常会去找 _SubBox__secret，容易 AttributeError
        return self._Box__secret   # “知道规则的人”仍可访问——所以别当安全围栏


x = Box()
assert x._Box__secret == 42
```

团队协作里：**单下划线 `_x`** 就够表达「不建议外部依赖」。

---

### 第八层：`@dataclass` —— 当你主要在「记事」时用语法糖减负

你已用手写过 `PointPlain`：**如果类只是老老实实存几项数据**，可以让解释器替你生成 **`__init__` / `__repr__`** 等样板。

```python
from dataclasses import dataclass, field


@dataclass(frozen=True)  # frozen：实例字段不可就地改，可作 dict/set 的键（在满足可哈希时）
class Point:
    x: float
    y: float


@dataclass
class Receipt:
    items: list[str] = field(default_factory=list)  # 禁止 list 直接当默认值！

```

---

## 辨析

| 对比 | **类** | **实例** |
|------|--------|----------|
| 类比 | 空白表格模版 | 已填的一张表 |
| 典型操作 | `MyClass.cls_method()`（类方法少用）、改类变量要极度谨慎 | `obj.method()`、读写 `obj.x` |
| **是否算「那一个对象」？** | 类型对象本身是单例模版 | **业务里你几乎总在跟实例较劲** |

| 写法 | **`@staticmethod`** | **`@classmethod`** | **普通实例方法** |
|------|---------------------|---------------------|------------------|
| 第一参 | 无隐含 | `cls`（类本身） | `self`（实例） |
| 何时考虑 | 与类略相关又与实例无关的工具 | **替代构造**：`.from_config(...)` | 读写实例状态的主力军 |

---

## 陷阱

1. **可变默认参数 / `dataclass` 默认值**。**成因**：可变对象（列表、字典）在**定义的那一刻只创建一次**，所有实例共用同一只桶。**改法**：`dataclass` 用 `field(default_factory=list)`；手写 `__init__` 用 `None` 哨兵：`def __init__(self, items=None): self.items = items or []`。参见 **`函数与作用域_note.md`**、**`数据类型与可变性_note.md`**。  

2. **以为 `self.total = Class.total` 就一定能隔离**。**成因**：可读性误判——若 `total` 是**可变对象**且在类上与实例共享引用，仍然会串改；**不可变赋值**才可放心「覆盖」。**改法**：想每实例独享，始终在 `__init__` **新建**，不要「偷类上的那只 list」。  

3. **多重继承 + 乱用 `super()` 不写文档**。**成因**：菱形结构下 MRO 不直观，`super()` 顺序与手写想象不一致。**改法**：**画一张 MRO**，给 mixin / 特质类起名并写注释；能组合就不要硬叠继承；**组合注入**（本节双重示例 B）常为更清爽的默认解。

---

## 适用范围 · 延伸

**适用范围**：带状态的业务域模型、给外部 SDK 包一层组合薄壳、协作里比「散装 `dict`」更可读的建模。

**禁忌 / 边界**：单行脚本硬套大而全 OOP 往往更臃肿；勿把 **`__`** 当真安全围栏；可变对象要谨慎自定义 **`__hash__` / `__eq__`**，以免破坏字典/集合语义（详见 **`数据模型与对象_note.md`**）。

**延伸（按地图）**：魔术方法：`魔术方法_note.md`；上下文：`上下文管理器_note.md`；类型补墙：`类型提示_note.md`；编排横切：`装饰器_note.md`。

---

## 双重示例

### A. 极简｜购物车（组合数据 + 规则）

可直接运行：**无第三方依赖**，Python ≥3.10 最佳（类型注解可有可无）。

```python
class ShoppingCart:
    def __init__(self) -> None:
        self._lines: dict[str, int] = {}

    def add(self, name: str, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("qty 必须为正")
        self._lines[name] = self._lines.get(name, 0) + qty

    def total_quantity(self) -> int:
        return sum(self._lines.values())


cart = ShoppingCart()
cart.add("牛奶", 2)
cart.add("牛奶", 1)
assert cart.total_quantity() == 3
print("lines =", cart._lines)
```

常见报错：**`ValueError`** 来自自检；说明你开始把不变式放回类里了。

---

### B. 工程切片｜支付适配（组合优于继承）

需求：可能对接多套支付网关。**不要为每个网关继承一个大类**，用「组合注入」更清晰：

```python
from typing import Protocol, runtime_checkable


@runtime_checkable
class PaymentGateway(Protocol):
    """协议：长得像能 charge 就够（鸭子类型）。"""
    def charge(self, amount_cents: int) -> str: ...


class OrderService:
    def __init__(self, gateway: PaymentGateway) -> None:
        self._gw = gateway  # “拿一张可用的支付网关卡插进来”

    def checkout(self, amount_cents: int) -> str:
        if amount_cents <= 0:
            raise ValueError("金额非法")
        return self._gw.charge(amount_cents)


class FakeStripe:
    def charge(self, amount_cents: int) -> str:
        return f"stripe:{amount_cents}"


svc = OrderService(FakeStripe())
assert svc.checkout(199) == "stripe:199"
```

**关联**：这里的 `Protocol` 属于进阶类型系统；学不会就先手写 `CheckoutService(gateway)` 也一样能跑。**组合**把「接单」与「具体支付」撕开，符合学习地图强调的演进方式。

依赖安装：**无**。若你要静态检查可加 `typing_extensions`/`mypy`（可选）。

---

## 练习

- **基础**：用 **`@dataclass(frozen=True)`** 写 `Point(x,y)`，尝试放进 **`set`**；口述 **`obj.method()`** 时第一个参数为什么自动是当前实例（用本节「描述符」那句人话就够）。  

- **进阶**：故意写一个「共享可变类变量列表」翻车，再用「每实例自建 list」或 `default_factory` 修复；写一个 `Child(A,B)`，`A/B` 各有 `kick`，子类只用 **`super()` 链**拼成一句输出，并对照 **`print(Child.__mro__)`** 口述顺序。  

- **开放**：**支付 / 开票 / 通知**三件能力，任选「继承树」对比「注入三个依赖」两套设计，写约 10 行（可读性、改动成本）；读官方 tutorial **`scopes and namespaces`** 一页，用你自己的话复述「方法里为何要显式写 `self`」。

---

## 费曼反问

1. 用你的话说明：**类和实例**的差别，如果只允许各用一句类比，你会怎么说？
2. **`super()`「不是只管爸爸」**这句话，结合 `__mro__`，你能否举一个小例子说明？
3. 为什么在 Python 团队里人们常说 **「约定优于隐藏」**，这和你怎么用 `_`/`__`/组合有什么关系？

---

> **闭环**：不看笔记，白板默写：**类变量 vs 实例变量**，并口述 **`cart.add(...)` → `Cart.add(self, …)` → `self` 是谁**整条因果链。
