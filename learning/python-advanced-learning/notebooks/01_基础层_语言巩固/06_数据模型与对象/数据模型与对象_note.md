# 数据模型与对象｜讲义笔记

<参考资料>

- https://docs.python.org/3/reference/datamodel.html
- https://docs.python.org/3/glossary.html#term-hashable
- https://docs.python.org/3/library/copy.html

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/topics/python-data-model.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/data-types.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **基础层 B**

---

## 上一章核心收获回顾（衔接「异常」）

你已能把 **出错路径编码成异常对象**，并开始写 **小而明确的 except**。

你已理解 **`raise … from`** 对排障链路的价值——这与「对象的公开行为如何被自省」同属工程可读性版图。

你已准备把 **`is` / `==` 的差异**放回「对象三心」：**身份 / 类型 / 等价**。

你即将解释 **为啥 `len(x)`、`x[i]`、 `for`** 等对不同类型都能工作——背后是 **同名协议不同实现**。

你已能衔接「可变 / 哈希 / 拷贝」三件事与「容器里放什么合法」：**本章把这些协议摊开说人话**。

---

## 但是，我们遇到了一个新的问题……

- 重写 **`__eq__`** 后发现 **突然不能进 `set`**？  
- 以为实现了 **`__getitem__`** 就足够迭代，却仍缺某些角落行为？  
- `copy.copy`/`deepcopy` 与赋值混读。

**因此本章需要：**用最少的 **特殊方法名词**对齐 **对象的「插座面板」隐喻**——知道插在哪个孔上就能得到某种语法糖。

---

## 动机：`Point`放进 `dict` 却散作 `(x,y)` 元组的维护成本。

---

## 类比（非编程）

对象像多功能插排：你不想买齐市面所有规格的转接头——只 **实现本项目真会用到的插座（协议）**。标准库看到对应孔就接上灯泡（`len`/`/`for`/…）。

术语「完整 **可迭代协议**」：**`迭代器与生成器_note.md`**。

---

## 精讲（入门层）

### 1. **`id`/`type`/值相等**

### 2. 最小「像点」数据结构

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))
```

可变 `Point` 若仍 `__hash__` ⇒ **悖论**——别这么干。

### 3. `dataclass` 语法糖衔接

详见 **`类与面向对象_note.md`** 的 **`@dataclass(frozen=True)`** 小节：冻结 + 自动生成 `repr/eq/hash`。

### 4. 「老式序列」剪影

只靠 **`__len__ + __getitem__`** 也常能让 `iter()` 动起来——初学记现象即可：**不同孔位组合的兼容策略**在历史代码里仍存在。

---

## 辨析

| 协议钩子（口语） | 常见触发的写法 |
|------------------|----------------|
| `__repr__` | `repr(x)` / 交互环境里「裸对象回显」 |
| `__str__` | `str(x)`、`print(x)` |
| `__len__` | `len(x)` |
| `__getitem__` | `x[i]`，并在老式语义下常与迭代协作 |
| `__eq__`、`__hash__` | `==` / 能否当 `dict` 键、`set` 成员 |

---

## 陷阱（≥2）

1. **`__eq__` 后默认可哈希关闭** — **成因**：哈希须与等价一致。**改法**：immutable + 显式 `__hash__` 或就别进 `set`。  
2. **`copy.copy`误以为深拷贝深层嵌套** — 回看数据类型讲义。  

---

## 适用范围 · 延伸

魔术方法运算符重载：**`魔术方法_note.md`**；上下文：`__enter__`。

---

## 双重示例

### A. 极简｜可当键的冻结点（手写版）

前述 `Point` + `frozen`心智：放 ` {(Point(1,2)) }`。

### B. 工程切片｜只读视作序列

```python
class RangeList:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if 0 <= i < self.n:
            return i
        raise IndexError


assert list(RangeList(3)) == [0, 1, 2]
```

---

## 练习

- **基础**：口述 **何时需要 `__hash__`**。  
- **进阶**：实现 `Money`/`Currency`是否需要 `Decimal`而非 `float`？写下判断。  
- **开放**：读 Data model 一页 **callable / descriptor** headline，不写代码只写 120 字笔记。

---

## 费曼反问

1. `is` vs `==` vs `hash` 三件事怎么串？  
2. 可变对象的 **`__eq__`** 与 **`__hash__`**冲突根因？  
3. **协议式鸭子类型**对本章的意义？

---

> **闭环**：默写：**哪些钩子让对象「可哈希」**。 
