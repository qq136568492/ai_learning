# 数据类型与可变性｜讲义笔记

<参考资料>

- https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator — 字面量入门
- https://docs.python.org/3/tutorial/datastructures.html — 列表 / 字典结构
- https://docs.python.org/3/reference/datamodel.html#objects-values-and-types — 对象、值与类型
- https://docs.python.org/3/library/copy.html — 浅拷贝与深拷贝

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/data-types.md`
- `obsidian-vault/LLM_Learning/wiki/topics/python-data-model.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **基础层 A1**

---

## 上一章核心收获回顾（本节为路径起点时可读作「你已具备的日常基础」）

你能在 Python 里使用 **数字、字符串、`list`、`dict`、`tuple`、`set`** 等字面量，并写出简单表达式。

你已见过 **变量名**这个概念：给一个对象贴标签，用它来读写数据。

你已用 **函数**包住重复逻辑（若尚未学完，可把「本章」视作与函数章并行补强数据心智）。

你已知道程序里处处是 **赋值语句**，但还不太确定「赋值」到底是复制还是指路牌。

你已写过或即将写 **默认参数**：那里藏着一个与「可变 / 不可变」强相关的千古坑——本章用它来收尾加深印象。

---

## 但是，我们遇到了一个新的问题……

- 写 `b = a` 后改 `b`，为什么有时 **`a` 也跟着变**？  
- 为什么 **列表不能当 `dict` 键**，而数字、字符串、`tuple（元素皆可哈希）` 可以？  
- 为什么在函数默认值里 **`def f(items=[])`** 会在多次调用间「共享列表」？

**因此本章需要：**建立 **可变 vs 不可变**、**赋值 ≠ 拷贝**、**可哈希大致意味着什么**这三块地基，后面凡是「参数传递 / 默认值 / 容器语义」都不再玄学。

---

## 动机：一个静默串改的 Bug

```python
def normalize_users(rows):
    for r in rows:
        r.append("DONE")   # rows 里是多个 list 时...

a = [["alice"], ["bob"]]
normalize_users(a)
# 也许你期待原数据不变？
```

若没有 **浅拷贝 / 深拷贝 / 可读性自检**的意识，团队协作里会像「谁在我不注意时改了公共货架」——排障很贵。

---

## 类比（非编程）

把 **变量名**看成**写有 ID 的卡纸**，把 **内存里的对象**当成**库房里的托盘**。**不可变**像「贴了封条的礼盒」：要改变只能换一盒新的。**可变**托盘则随时可往里加减货。

**哈希键**像在图书馆编目：**号码不能今天 A、明天改成 B**，否则整张目录卡会炸。

---

## 精讲｜由浅入深

### 1. 一句话人话

内置类型可按 **能不能在原地改内容**粗略分成 **可变**（`list`、`dict`、`set` 以及多数自编对象默认）与 **不可变**（`int`、`str`、`tuple`（元素皆可哈希时可哈希）、`frozenset` 等）。

### 2. 身份 / 类型 / 值的直觉

Python 对象是 **三块牌子**：谁在内存里 (`id()`)、是啥类型 (`type()`)、读起来是否等价 (`==`)，**不要盲目把 `is`（身份）当场 `==`（值相等）**。

### 3. `a = b` 是指路牌绑定

下面 **没有复制新列表**——只是两个名字对准同一只托盘。

```python
a = [1, 2, 3]
b = a
b.append(4)
assert a == [1, 2, 3, 4]
```

拷贝要显式：`b = list(a)` / `copy.copy` / `copy.deepcopy`。

### 4. 切片「浅拷贝」与嵌套

```python
import copy

outer = [[1], [2]]
shallow = copy.copy(outer)      # 外层新托盘，元素仍指向内层两个小列表
shallow[0].append(9)            # 影响 outer[0]

outer2 = [[1], [2]]
deep = copy.deepcopy(outer2)
deep[0].append(9)
assert outer2[0] == [1]         # deep 独立于 outer2
```

### 5. 可哈希 ⇄ 可当 `dict/set` 键的核心约束（人话）

**可哈希**：在对象一生中 `hash(...)` **稳定**，且 **`a == b` ⇒ hash 一致**。  
可变容器若可哈希会破坏表格内部结构 ⇒ **一般不让你把 `list` 嵌进 `set`**。

最小例子：

```python
assert hash((1, 2))
s = {[1]}  # TypeError — list 不可哈希
```

术语「**可迭代协议**」详讲在 **`02_迭代器与生成器_note.md`**。

---

## 辨析速查

| | **不可变侧重** | **可变侧重** |
|---|------------------|----------------|
| 记忆句 | 「改写法常意味着新对象」 | 「就地方法改内部状态」 |
| 典型坑 | Small int 缓存等少碰即忘 | **共享可变对象**引发的串改 |

| | **`==`** | **`is`** |
|---|----------|----------|
| 看什么 | **值等价**（常调 `__eq__`） | **是否同一块托盘** |

---

## 陷阱（≥2）

1. **`def bad(x, acc=[])`** — **成因**：可变默认值在一次函数定义求值。**改法**：`acc=None`，函数里 `acc = [] if acc is None else acc` 或拷贝。详见 **`函数与作用域_note.md`**。
2. **`b = a` 当拷贝** — **成因**：指路牌复述。**改法**：显式拷贝并理解浅/深。
3. **`set`/`dict` 键里塞可变** — **成因**：哈希不稳定。**改法**：换 `tuple`/`frozenset` 或由不可变快照键化。

---

## 适用范围 · 禁忌 · 延伸

- **适用**：结构化数据建模、缓存键设计、并行前思考共享状态。
- **禁忌**：多线程读写共享可变结构无锁≠安全（进阶主题）。
- **延伸**：NumPy **`view/copy`** 是本节心智在数值数组上的外延（接轨层）。

---

## 双重示例

### A. 极简 Demo｜看穿「共享」

```python
import copy

xs = [{"n": 1}, {"n": 2}]
ys = xs[:]              # 浅拷贝外层 list
ys[0]["n"] = 999
assert xs[0]["n"] == 999      # dict 仍为同一只
zs = copy.deepcopy(xs)
zs[1]["n"] = 0
assert xs[1]["n"] != 0
```

PowerShell：**`pip` 不需**（标准库）；`python .\script.py`。若 **`NameError: copy`**，写 `import copy`。

### B. 工程最小切片｜配置快照

传入下游前把「可被意外修改的 dict」**冻结成拷贝**，避免 callee 弄脏调用方上下文：

```python
import copy


def freeze_cfg(cfg: dict) -> dict:
    return copy.deepcopy(cfg)


ORIG = {"db": {"url": "x"}}
safe = freeze_cfg(ORIG)
safe["db"]["url"] = "y"
assert ORIG["db"]["url"] == "x"
```

---

## 练习｜基础 / 进阶 / 开放

- **基础**：口述 `=` / `copy.copy` / `deepcopy` 差异；手写反例演示「共享嵌套字典」。
- **进阶**：用 `tuple`/`frozenset` 组装键，塞进 `dict`/`set`，再解释失败案例。
- **开放**：查阅「为什么默认参数只求值一次」官方 FAQ，用你的话重写 150 字。

---

## 费曼反问（只提问）

1. 为什么可变对象通常 **不可哈希**？
2. 浅拷贝能解决所有「误以为复制」的事故吗？
3. 函数里 **原地改动入参**，对外层调用方意味着什么设计信号？

---

> **闭环**：白板默画 **名字 → 对象 → 可变 / 不可变 → 哈希键** 四角关系。
