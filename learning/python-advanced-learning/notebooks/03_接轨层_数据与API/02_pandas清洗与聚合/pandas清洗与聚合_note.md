# pandas 清洗与聚合｜讲义笔记

<参考资料>

- https://pandas.pydata.org/docs/user_guide/dsintro.html — **Series / DataFrame**
- https://pandas.pydata.org/docs/user_guide/groupby.html — **分组聚合**

```bash
pip install pandas numpy
```

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/topics/numpy-numerical-foundations.md`（ ndarray 与张量语义延续）
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **G2**

---

## 上一章核心收获回顾（衔接「NumPy」）

你已能按 **`axis`、广播** 思考数组块运算。

你已理解 **视图 vs 拷贝**是张量家族的通用心智负担。

你已接受：**向量化**优先于手写 Python 内层循环。

你即将面对的是 **带行索引、标签、缺失值**的业务表格：**对齐**比「算得快」更让新手头疼。

你已准备：**`groupby` ≈ SQL `GROUP BY`，`merge` ≈ `JOIN`** 的心智翻译。

---

## 但是，我们遇到了一个新的问题……

**NumPy ndarray**缺少 **行列标签语义**——业务里「这一条记录是谁」「按谁分组」无法用数组维度单独讲清楚。**因此本章需要：**熟练使用 **`Series` / `DataFrame`、`merge/join`、`groupby.agg`、`fillna/dropna`；时间字段用 **`pd.to_datetime` 统一**。  
**多级索引**：入门可先跳，遇到宽表再打补丁。

---

## 动机：离线特征、EDA、报错定位几乎都绕不开「对齐后的表」

---

## 类比（非编程）

Excel **多了一层看不见的标尺对齐条**：`merge` 最折磨人的往往是 **尺子拿错**——键不一致、dtype 漂移、多余重复行。

---

## 精讲（由浅入深）

典型管线：**读入 → 处理缺失 → 过滤 → groupby → 汇总落表**

```python
import pandas as pd

df = pd.DataFrame({"x": [1, None, 3], "g": ["a", "a", "b"]})
clean = df.dropna(subset=["x"])
summ = clean.groupby("g")["x"].agg(["mean", "count"]).reset_index()
```

**SettingWithCopyWarning**：链式选取再赋值易被歧义。**改：**一步 **`.loc[row_indexer, col] =`** 写完。

---

## 辨析

| | **pandas** | **SQL** |
|--|-----------|---------|
| 心智 | 向量 + **索引对齐** | 声明式查询 |
| 场景 | Notebook / ETL / 单机 | 数仓 |

---

## 陷阱（≥2）：成因 → 改法

1. **链式赋值踩到拷贝视图**。 — **上文 `.loc`。  
2. **静默 dtype / 精度推断**。**改：**读入后即 **`astype` / `to_datetime`。**

---

## 适用范围 · 延伸

**Parquet、`read_sql`（注意连接安全）**；与 **Spark / DuckDB** 桥接。LLM 管道里常把一行 **转成 prompt 模版填充**——见下游应用小节。

---

## 双重示例

### A. 极简｜布尔筛选 + **`describe()`**

```python
import pandas as pd

df = pd.DataFrame({"age": [20, None, 40], "ok": [1, 0, 1]})
sub = df[df["age"].notna() & (df["ok"] == 1)]
stats = df["age"].describe()
```

### B. **`groupby.agg`** 一页

```python
import pandas as pd

sales = pd.DataFrame(
    {"region": ["East", "East", "West"], "sales": [10, 40, 5]}
)
tbl = sales.groupby("region")["sales"].agg(["mean", "sum"]).reset_index()
```

---

## 练习

- **基础**：`read_csv` → `describe` → `fillna` 全流程跑通并手记结论。  

- **进阶：** `merge` 与 `concat` 各选一题写出 **键**。  

- **开放**：举一个 **长宽透视 `pivot`/ `melt`** 与你的业务最接近的例子。

---

## 费曼反问

1. 索引对齐为什么会「痛」？  
2. **`merge`** 与 **`concat`** 的分界线？  
3. **时间字段**如何避免「以为同一时刻却不是」？

---

> **闭环**：口述 **`SettingWithCopyWarning`** 想提醒你做什么事。
