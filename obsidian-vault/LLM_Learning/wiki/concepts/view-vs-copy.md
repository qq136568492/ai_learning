---
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [numpy, memory, performance]
source_count: 1
---

# view-vs-copy

NumPy 中切片通常返回 view（共享底层内存），而部分高级索引/类型转换会创建 copy（独立内存）。理解该区别是避免隐性 bug 和内存浪费的关键。

## 判断线索
- `arr.base is None` 常表示拥有自身数据
- 切片多为 view；花式索引多为 copy
- 修改 view 可能影响原数组

## 工程影响
- view：高性能、低内存，但需谨慎副作用
- copy：更安全隔离，但会增加内存与复制成本

## 建议
- 在关键路径显式 `.copy()` 或注释共享语义
- 调试数据污染时优先排查 view 链路

## 来源
- [[sources/2026-05-14-numpy-devdocs]]
