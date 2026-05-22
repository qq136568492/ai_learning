---
type: concept
created: 2026-05-19
updated: 2026-05-19
tags: [machine-learning, evaluation]
source_count: 1
---

# train-validation-test-split

训练/验证/测试划分用于评估模型泛化能力，避免模型只记住训练数据而无法处理新样本。

## 三个集合
- 训练集：用于拟合模型参数。
- 验证集：用于调参、选择模型。
- 测试集：最终评估泛化表现，尽量只使用一次。

## 工程意义
- 防止过拟合
- 让模型选择有客观依据
- 让实验结果可复现、可比较

## 来源
- [[sources/2026-05-19-machine-learning-for-everybody]]
