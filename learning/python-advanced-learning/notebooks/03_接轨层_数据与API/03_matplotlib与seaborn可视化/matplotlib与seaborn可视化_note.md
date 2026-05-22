# matplotlib / seaborn 可视化｜讲义笔记

<参考资料>

- https://matplotlib.org/stable/tutorials/pyplot.html
- https://matplotlib.org/stable/api/axes_api.html — **Axes 面向对象 API**
- https://seaborn.pydata.org/tutorial/introduction.html

```bash
pip install matplotlib seaborn pandas numpy
```

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **可视化（地图 G）**
- pandas **`.plot`** 接口（延伸阅读）

---

## 上一章核心收获回顾（衔接「pandas」）

你能 **分组、清洗、对齐**，并把宽表转成可统计的中间结果。

你已具备数字摘要——但 **肉眼对分布漂移、离群值的警觉**要先于指标。

你已理解：**向量列**可以直接驱动绘图管线。

你已准备：**`Figure` vs `Axes`** 的分工，不把全局 **`pyplot`** 揉进库的深处。

你已意识到：**默认 bins、调色**会改变读者结论——图示可能「诚实地说谎」。

---

## 但是，我们遇到了一个新的问题……

老板要 **一页看清 train/test 直方偏移、相关性散点、分类计数**。**因此本章需要：**能手写 **histogram / scatter / bar / subplot**；分清 **脚本式 `.pyplot` 快速草图 vs 面向对象 `axes` API**（库代码偏向后者）。

**Seaborn `FacetGrid` / hue**：按需阅读官方图示。

---

## 动机：**漂移、泄漏线索**往往早于指标告警被眼睛抓住

---

## 类比（非编程）

先有 **整张桌子（Figure）**，再摆 **每只碟（Axes）**；每道菜知道自己的标题与刻度。

---

## 精讲（由浅入深）

脚本快速探索可以用 **`plt.subplots`** 拿 **Axes**；再在 **`ax`** 上调用绘图方法。**避免：**在可被 import 的库模块里大量使用 **隐式当前 axes**——难以测试与重用。

```python
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(7)
xs = rng.normal(size=1200)

fig, ax = plt.subplots(1, 1, figsize=(5, 3))
ax.hist(xs, bins=40)
ax.set_title("demo gaussian")
plt.tight_layout()
plt.savefig("hist.png")
```

---

## 辨析

| | **`pyplot` 快速** | **OO `Axes`** |
|--|-------------------|---------------|
| 脚本 / Notebook | ✅ | ✅ |
| 可复现库封装 | ⚠️ 易隐含全局状态 | ✅ 首选 |

---

## 陷阱（≥2）：成因 → 改法

1. **不写 `tight_layout`/`constrained_layout` 重叠文字**。  
2. **过少 / 过多的 bin 诱导错误形状判断**。

---

## 适用范围 · 延伸

Seaborn **`relplot`、`pairplot`**。**交互：**Plotly（另一选型）。矢量输出 **`pdf/svg`** 进报告 safer than 糊截图。

---

## 双重示例

### A. 双子图：直方图 + 散点（可运行）

```python
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
xs = rng.normal(size=600)
ys = rng.normal(size=600)

fig, axes = plt.subplots(1, 2, figsize=(8, 3))
axes[0].hist(xs, bins=30)
axes[0].set_title("hist")
axes[1].scatter(xs, ys, s=8, alpha=0.35)
axes[1].set_title("scatter")

plt.tight_layout()
plt.savefig("eda.png")
```

### B. Seaborn **`relplot`** 分面一页

```python
import seaborn as sns

df = sns.load_dataset("tips")
g = sns.relplot(data=df, x="total_bill", y="tip", col="sex", hue="smoker")
g.set_axis_labels("账单", "小费")
g.savefig("sns_facet.png")  # 纯脚本可无 plt.show()
```

---

## 练习

- **基础**：在同一图画 **train/test 直方重叠**比对漂移。  

- **进阶：**导出 **矢量 PDF**。  

- **开放**：读一页 **无障碍调色 / 颜色盲友好**建议并写摘录。

---

## 费曼反问

1. 显式 **`Axes`** 的工程优势？  
2. 哪一种图最常「视觉误导」？  
3. 你是否能说出一种 **无障碍调色思路**？

---

> **闭环**：口述 **何时 `plt.subplots` + 显式 `ax.xxx`** 好过裸 `plt.xxx`。 
