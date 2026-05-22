# 控制流与 match｜讲义笔记

<参考资料>

- https://docs.python.org/3/tutorial/controlflow.html
- https://docs.python.org/3/reference/compound_stmts.html
- PEP 634 / PEP 636 — `match` / `case`（需 Python ≥3.10）

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/control-flow.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **基础层 A2**

---

## 上一章核心收获回顾（衔接「数据类型与可变性」）

你已弄清 **指路牌赋值** vs **拷贝**，知道 **可变对象的共享**会如何悄悄串数据。

你已能熟练使用 **布尔条件**、短路逻辑，以及 **`in`/`not in`** 等基本成员检测。

你已理解 **迭代 `for`** 常与 **序列 / 可迭代对象**配合（本节只用人话带过，不深究协议）。

你能开始把「数据结构」接上「流程」：**先分清数据对不对，再走哪条支线**——控制流就是这些支线的交通规则。

你已意识到 **误用循环 `else`** 或 **`match`/`if`混读**都会产生「以为执行了却没执行」的错觉。

---

## 但是，我们遇到了一个新的问题……

- **`if / elif`** 链路一长，读者跟丢「异常路径」在哪儿。  
- 在遍历集合时 **`remove`/原地改`** 跳过元素或与迭代器语义打架。  
- JSON / 二元组 / AST 结点形态多变时，只靠 `type(...)`/`len`/`if` 组合容易写出「维护地狱」。（若环境尚无 3.10，可把 `match` 当延伸阅读。）

**因此本章需要：**把 **结构化分支 / 遍历 / 跳转语义**想清楚，必要时用 **`match` 对齐形态**陈述意图。

---

## 动机：`for ... else` 被误读为维护缺口

初学者常把 **`for … else`** 等同于「否则打印没找到」——但一旦中间 **`break`**，else 整块 **不执行**。

---

## 类比（非编程）

- **`if`** 像 **路口指示牌一次择道**。  
- **`while`** 像 **烘干机：门没关上就一直转**。  
- **`for`** 像 **取号机一条条叫号**。  
- **`match`**（若可用）像 **分拣线：快件形状不一，各有各的滑道**。

---

## 精讲｜从轻到稳

### 1. `if / elif / else` — 单层决策树

每条分支要能 **穷尽或显式兜底**；团队里别把业务规则藏在五层括号里不写注释。

### 2. `for` 与枚举

```python
for i, ch in enumerate("abc", start=0):
    print(i, ch)
```

### 3. 谨慎：循环体内改原容器

反向删会坑位；可复制副本：**`for x in xs[:]`** 或建新容器收集结果。

### 4. **`for … else`** 精确语义（MECE）

- **走完迭代且未触发 `break`** ⇒ 运行 `else`  
- **中途 `break` 出逃** ⇒ `else` **跳过**

```python
def find_index(xs, target):
    for i, x in enumerate(xs):
        if x == target:
            return i
    else:
        return -1      # 「整圈都没 return」才来这儿
```

### 5. `match-case` — 结构化形态（术语闸门：**模式匹配**，不是字符串 `match`)

**一句话**：从左到右对 **结构**做一次「长得像就命中」的快速路由；常量与捕获变量要写清：  

```python
def axis_label(p):
    match p:
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"x={x}"
        case (_, y):
            return f"y={y}"
```

<details><summary>没有 3.10？</summary>用字典分发或 `if/elif`/`typing.Union`/`isinstance` 组合等价表达。</details>

术语「可迭代如何让 `for` 工作」的协议细节：**`迭代器与生成器_note.md`**。

---

## 辨析

| | **朴素 `switch` 心智**（Python无） | **`match`** |
|--|----------------------------------|---------------|
| 适用 | — | **结构解构 + 常量分支** |

| | **`while`** | **`for`** |
|--|----------|----------|
| 驱动 | **谓词真值** | **迭代耗尽** |

---

## 陷阱

1. **遍历中 `.remove`/`.pop`** — **成因**：索引漂移。**改法**：倒序删 / 建新表 / iterator invalidation。  
2. **`case None`** vs **`case x`** 语义混读 — **成因**：`None`匹配字面值。**改法**：认真读 PEP 范例。  
3. **把极简二分支写成 `match`** — **成因**：花哨。**改法**：`if` 更直白则退回。

---

## 适用范围 · 延伸

- **`match`** 适合命令解析 / AST / `_note` 数据结构。
- **`else`/`finally`**与异常结合见 **`异常处理_note.md`**。

---

## 双重示例

### A. 极简｜枚举 + 线性查找

上文 `find_index` 即运行示例：`python`，无依赖。

### B. 工程最小切片｜命令分发

```python
def handle(cmd: str) -> str:
    match cmd.split():
        case ["quit"]:
            return "bye"
        case ["say", msg]:
            return f"ECHO:{msg}"
        case _:
            return "unknown"


assert handle("say hi") == "ECHO:hi"
```

---

## 练习

- **基础**：实现 `contains_break_else_demo()` 口述 `break`与否对 `else` 的影响。
- **进阶**：把两段嵌套 `if` 转成 `match`（或退回理由）。
- **开放**：检索「EAFP vs LBYL」与控制流选型。

---

## 费曼反问

1. **`for`** 为什么在 Python 里是 **迭代语义**？
2. 何时应避免用 `match`？
3. 循环 **`else`** 与 **`if`** 后续 **else**，心智差在哪里？

---

> **闭环**：不看资料解释 **`for/for-else`** 的执行真值表。
