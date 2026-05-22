---
type: concept
created: 2026-05-19
updated: 2026-05-19
tags: [machine-learning, supervised-learning]
source_count: 1
---

# supervised-learning

监督学习使用带标签数据训练模型：输入是特征 `X`，输出目标是标签/目标 `y`，模型学习从 `X` 到 `y` 的映射。

## 两类核心任务
- 分类：预测离散类别，如 spam/not-spam、gamma/hadron。
- 回归：预测连续数值，如房价、温度、价格。

## 基本流程
1. 准备特征矩阵 `X` 与目标向量 `y`
2. 划分训练集、验证集、测试集
3. 训练模型
4. 用指标评估泛化能力
5. 调参并复验

## 来源
- [[sources/2026-05-19-machine-learning-for-everybody]]
