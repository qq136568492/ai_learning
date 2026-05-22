# Streamlit 原型｜讲义笔记

<参考资料>

- https://docs.streamlit.io/

```bash
pip install streamlit pandas matplotlib httpx
```

运行：**`streamlit run app.py`**。端口或防火墙打不开时查阅官方 **Network / CORS** 说明。

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **原型 H**

---

## 上一章核心收获回顾（衔接「pandas / pydantic」）

你可对表格做预处理，并已理解：**请求契约（Pydantic）**在服务入口收口失败路径。

你已能画图、导出 **`png`/矢量**——准备把离线分析搬进浏览器。

你已理解：**Streamlit 不是复杂 SPA 框架**：目标在 **对内演示与快速原型**。

你已接触：**脚本从上到下重跑（rerun）** 与 **`st.session_state`** 的必要场景。

你已准备好：**组件式 UI**最小组合即可打动干系人。

---

## 但是，我们遇到了一个新的问题……

干系人要 **拖拽 CSV 就地看图**。**Streamlit：**「整页从上到下重执行」 + **控件事件驱动局部交互（随版本演进）**。**因此本章需要：**会使用 **`st.dataframe`、`file_uploader`、度量卡与列布局**，并弄清 **`cache_data` vs `cache_resource`**：前者适合 **纯数据处理函数**，后者适合 **数据库连接等资源句柄**。  
新版本 **Fragments / 多页面 App**：请以官方首页为准补足。

---

## 动机：**把想法用分钟级原型摊在桌上**，再决定是否值得换 Dash / Reflex / React。

---

## 类比（非编程）

幻灯片：**改一页却整册重播**：这就是 rerun——你要把昂贵计算藏起来或缓存。

---

## 精讲（由浅入深）

```python
import pandas as pd
import streamlit as st

st.title("CSV 速览")
uploaded = st.file_uploader("拖入 CSV")

if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())
```

缓存：**`st.cache_data`** 包住「纯函数、可哈希入参的处理」；**`st.cache_resource`** 包住「连接池、重量级单例」。**别把巨大可变对象无脑塞进 `cache_data`。**

---

## 辨析

| | **Streamlit** | **Dash / Reflex / React** |
|--|----------------|---------------------------|
| 上手曲线 | 低 | 高 |
| 工程形态 | Demo / 对内 | 多端 / SEO / 强交互 |

---

## 陷阱（≥2）：成因 → 改法

1. **重型 I/O 在每次 rerun**都跑。**改：**缓存或预处理离屏作业。  
2. **`session_state` 键名冲突**。 — **命名空间前缀**或与业务 id 拼接。

---

## 适用范围 · 延伸

对内 PoC。**若要 SEO、百人并发运维后台、灵活路由**：换栈更合适。

---

## 双重示例

### A. 三枚 **metric**

```python
import streamlit as st

c1, c2, c3 = st.columns(3)
c1.metric("QPS", "120")
c2.metric("P95(ms)", "38", delta="-2")
c3.metric("错误率%", "0.4", delta="0.1", delta_color="inverse")
```

### B. 占位：请求后端健康检查（替换真实 **`API_BASE`**）

```python
import os

import httpx
import streamlit as st

url = os.getenv("API_BASE", "http://127.0.0.1:8000/healthz")
if st.button("ping api"):
    with httpx.Client(timeout=2.0) as cli:
        st.json(cli.get(url).json())
```

---

## 练习

- **基础**：`file_uploader` 读入 CSV，再对 DataFrame 调用 **`describe()`**。  

- **进阶**：用 **`cache_resource`** 管理 **`sqlite3` 连接**（或等价连接工厂）。

- **开放：**对比 **Gradio** 与你的场景匹配度一段话。

---

## 费曼反问

1. **rerun**如何逼迫你拆分纯函数数据处理？  
2. 何种场景 **必须使用 `session_state`？**
3. 为何不建议把 **高并发租户后台**全押 Streamlit？

---

> **闭环**：口述 **`cache_data` / `cache_resource` 分工**。 
