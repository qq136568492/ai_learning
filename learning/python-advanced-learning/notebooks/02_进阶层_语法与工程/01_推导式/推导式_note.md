# 推导式｜讲义笔记

<参考资料>

- https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries
- PEP 202 / PEP 274

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/list-comprehension.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/iterators-and-generators.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **进阶层 D1**

---

## 上一章核心收获回顾（衔接 `07_模块包与虚拟环境`）

你已能 **激活 venv、锁依赖**，知道 **`import` 执行一次顶层**的长期副作用。

你已理解 **模块化拆分**如何避免「全屋共享调味罐式的版本踩踏」。

你开始写 **可被其他文件 import** 的小工具函数 ——推导式就是这些函数里最常见的一行数据处理武器。

你已具备 **可读性 vs 花哨**的心智标尺（不写不可维护的一行特技）。

你已准备在同一屏里 **声明映射/过滤**：少写脚手架 `append` 循环。

---

## 但是，我们遇到了一个新的问题……

手写：

```python
out = []
for x in nums:
    if x > 0:
        out.append(x * x)
```

在大量 ETL / 预处理里 **又长又吵闹**。**生成器惰性**时又需要另一套括号心智。

**因此本章需要：**掌握 **列表 / 集合 / 字典推导** 与 **`( expr for … )`** 生成器表达式，并知道何时 **退回朴素 `for`**。

---

## 动机：数据处理脚本里九成是「对每个元素 ifelse」。

---

## 类比（非编程）

推导式像在超市收银台 **勾选筛选项后直接输出小票条目**，而不是逐项口述进货动作。生成器像 **一条条吐小票**：打印多少拿多少袋子。

术语「惰性生成器背后是 **`yield`/迭代协议」详见 **`迭代器与生成器_note.md`**——本节只接住衔接。

---

## 精讲

### 四层语法糖

```python
nums = range(4)
squares = [x * x for x in range(5)]
evens = {x for x in range(10) if x % 2 == 0}
invert = {v: k for k, v in {"a": 1}.items()}
lazy_sum_squares = sum(x * x for x in nums)  # 外层无 []，惰性喂给 sum
```

多层嵌套：**能写≠该写**；超过 ~3 层考虑拆函数。

### Python 3 作用域

推导式自带 **局部循环变量遮蔽**语义（不要依赖奇怪泄漏）。

---

## 辨析

| | **列表推导 `[...]`** | **生成器表达式 `(... )`** |
|--|--|--|
|即时性|立刻得到 list|逐项惰性|
|内存|一次性占满 intermediate|常为流式更小|

---

## 陷阱（≥2）

1. **把生成器塞进单元素列表**形如 `[ (f(x) for x in xs) ]`——得到的是「含一个 generator 对象的列表」，常非本意；需要物化时请用 **`list(gen)`**。  
2. **在推导式里写复杂副作用与大段逻辑 —**可读性崩。**改法：**退回多行 `for` 并拆函数。

---

## 适用范围 · 延伸

与 NumPy/Pandas矢量化：**数据科学层换掉 Python 二层循环**。见接轨层 note。

---

## 双重示例

### A. 极简｜展平矩阵一行

```python
matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]
assert flat == [1, 2, 3, 4]
```

### B. 工程切片｜字典清洗

```python
raw = {"name": "  Ada ", "age": " 42 "}

def clean(kv: tuple[str, str]) -> tuple[str, str]:
    k, v = kv
    return k.strip(), v.strip()


clean_map = dict(clean((k, v)) for k, v in raw.items())
```

---

## 练习

- **基础**：`dict` 推导实现值 upper-case。  
- **进阶**：对比 `sum(x * x for x in nums)` 与 `sum([x * x for x in nums])` 的内存直觉。
- **开放**：`dis`/粗 `timeit`做一次（了解即可）。

---

## 费曼反问

1. 何时推导式反而 **削弱可读性**？  
2. 生成器表达式放在 **函数调用唯一参数括号里**为什么是常见姿势？  
3. 嵌套 `for/if`推导与 **可读团队规范**阈值？

---

> **闭环**：默写 **列表 vs 集合 vs 字典 vs 生成器括号** quartet。
