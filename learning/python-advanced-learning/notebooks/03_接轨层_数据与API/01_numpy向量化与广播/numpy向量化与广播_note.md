# NumPy 向量化与广播｜讲义笔记

<参考资料>

- https://numpy.org/doc/stable/user/whatisnumpy.html
- https://numpy.org/doc/stable/user/basics.broadcasting.html — **广播**
- 仓库笔记：`obsidian-vault/LLM_Learning/wiki/topics/numpy-numerical-foundations.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/broadcasting-rules.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/view-vs-copy.md`

```bash
pip install numpy
```

```powershell
python -c "import numpy as np; print(np.__version__)"
```

**常见报错：**`ImportError` — 请先激活本项目 venv 再安装。

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/topics/numpy-numerical-foundations.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/broadcasting-rules.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/view-vs-copy.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **G1**

---

## 上一章核心收获回顾（衔接「logging / pytest」工程底座）

你能跑 **`pytest`**、写断言，并有「改逻辑要有红灯兜底」的意识。

你已能配置 **分级日志**，知道 **`print`** 撑不起线上检索。

你已掌握 **虚拟环境与依赖**，准备把双层 Python 循环换来的性能债交给底层实现。

你已准备好接受：**切片有时不拷贝**——长得像复制，其实只是 **共享同一块底板**。

你即将上手 **`ndarray`：形状、`axis`、dtype、广播、何时 `.copy()`** 五条主干。

---

## 但是，我们遇到了一个新的问题……

纯 Python 双重循环对大数组 **慢**，也和 **PyTorch/TensorFlow 张量**的心智脱节。**因此本章需要：**会用 **`numpy` 向量化**表达「对整块格子同一种操作」；读懂 **广播**如何把形状对齐；在改数组前想清楚 **视图还是拷贝**。  
**进阶名词** stride / Fortran order：入门可先只在 wiki 留个锚点。

---

## 动机

特征缩放、打分矩阵、占位嵌入——在进深度学习框架之前，先要 **整块数组思维**。

---

## 类比（非编程）

**`ndarray`** 像一块铺好格子的烤盘：**ufunc（如加法）** 对每个格子套用同一道菜的做法；**广播** 像在某一维 **自动垫上长度为 1 的虚拟尺子**，使两盘烤盘能对齐入锅。

---

## 精讲（由浅入深）

### **`shape` / `dtype` / `axis`**

- **`axis=0`**：沿「第 0 维」聚拢，常理解成「压扁行」求每列；
- **`keepdims=True`**：保留长度为 1 的维度，方便与原始数组广播回去。

### **广播心智**

从尾部维度对齐，**逐项比较是否为相等或其中之一为 1**；读官方 **Visualization** 图比死记规则更快。

### **视图 vs 拷贝**

**`b = a[:, 0]`** 常与 **base** 共享内存；要「彻底独立拷贝」时用 **`.copy()`** 或对 wiki **`view-vs-copy`** 的规则团队化。

---

## 辨析

| | **`list`** | **`ndarray`** |
|--|------------|----------------|
| 同质与速度 | 元素类型可混搭 | **`dtype`** 对齐，贴近底层 C |

---

## 陷阱（≥2）：成因 → 改法

1. **花哨索引 ⇒ 往往得到拷贝**却仍当视图改。  
2. **silent `float64` 推导**在非预期尺度上吃掉内存。**改：**显式 **`astype`** 与校准。

---

## 适用范围 · 延伸

**`np.linalg`、随机种子 `default_rng`、`einsum`**；下一节 **`pandas`** 在表格语义上封装一层索引。

---

## 双重示例

### A. 极简｜按轴批量归一

```python
import numpy as np

x = np.array([[10.0], [30.0], [50.0]])
mu = x.mean(axis=0, keepdims=True)
sigma = x.std(axis=0, keepdims=True) + 1e-6
z = (x - mu) / sigma
assert np.allclose(z.mean(axis=0), 0)
```

### B. 工程切片｜嵌入表占位索引

```python
import numpy as np

rng = np.random.default_rng(0)
E = rng.normal(size=(512, 64)).astype(np.float32)
idx = np.array([0, 31, 400])
vectors = E[idx]
assert vectors.shape == (3, 64)
```

---

## 练习

- **基础**：故意写一档 **广播不匹配**的运算，修好并口述规则。  

- **进阶**：手写 softmax（指定 **`axis`**）。  

- **开放：**读完 wiki **`view-vs-copy`**，写五条团队规范 bullets。

---

## 费曼反问

1. 对你而言 **`axis=k`**「消掉的是哪一档维度」？  
2. **广播对齐**一句话口诀？  
3. 何时 **`.astype(copy=False)` 仍不够用**必须用 **`.copy()`**？

---

> **闭环**：举一个 **切片视图**口述「改掉会不会影响母体」。
