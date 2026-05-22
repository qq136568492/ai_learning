---
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [numpy, broadcasting]
source_count: 1
---

# broadcasting-rules

NumPy 广播机制允许不同 shape 的数组在满足规则时进行逐元素运算，避免显式循环与重复拷贝。

## 核心规则
- 从尾维开始对齐比较
- 两维相等，或其中一维为 1，则兼容
- 否则广播失败（shape 不可对齐）

## 实战价值
- 用小张量“扩展”到大张量计算
- 减少 for-loop，提升性能与可读性
- 常用于特征归一化、批量向量运算

## 常见坑
- 维度位置错导致意外结果
- 隐式扩展后中间结果过大，造成内存压力

## 来源
- [[sources/2026-05-14-numpy-devdocs]]
