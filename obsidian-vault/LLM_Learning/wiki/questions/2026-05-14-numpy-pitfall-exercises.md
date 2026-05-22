---
type: question
created: 2026-05-14
updated: 2026-05-14
tags: [numpy, exercises, pitfalls]
source_count: 1
---

# NumPy 高频坑位练习清单（10题）

## 目标
围绕 [[concepts/broadcasting-rules]]、[[concepts/view-vs-copy]]、[[concepts/dtype-and-memory]] 进行有针对性的实战训练。

## 练习题
1. **广播对齐判断**：给定 `(3,1,5)` 与 `(1,4,5)`，是否可广播？结果 shape 是什么？
2. **广播报错定位**：为什么 `(2,3)` 与 `(3,2)` 不能直接逐元素相加？给出两种修正方式。
3. **隐式扩展风险**：构造一个广播后中间张量暴涨的例子，并说明如何规避内存峰值。
4. **view 还是 copy**：比较 `a[1:5]`、`a[ [1,3,5] ]`、`a[a>0]` 的内存语义。
5. **副作用排查**：为什么改动 `b=a[:,0]` 会影响 `a`？如何安全避免？
6. **链式索引陷阱**：解释 `a[a>0][:3]=0` 可能“不生效”的原因。
7. **dtype 提升**：`int32 + float64`、`float32 + float64` 的结果 dtype 分别是什么？
8. **就地运算报错**：解释 `int` 数组执行 `a += float_arr` 报 casting 错误的根因与修复方法。
9. **字节序问题**：读取 big-endian 二进制后值异常，如何用 `newbyteorder` / `byteswap` 修复？
10. **精度与成本权衡**：在 embedding 后处理里何时用 `float32`，何时保留 `float64`？给出判断标准。

## 自测标准（DoD）
- 能口头说明每题背后的“机制原因”而非仅给代码。
- 每题都有最小可复现代码（10~20 行）。
- 对第 3/5/8 题能给出工程级防坑策略。

## 参考
- [[sources/2026-05-14-numpy-devdocs]]
- [[topics/numpy-numerical-foundations]]

