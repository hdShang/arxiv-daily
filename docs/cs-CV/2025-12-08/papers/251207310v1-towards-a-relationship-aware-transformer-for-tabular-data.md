---
layout: default
title: Towards a Relationship-Aware Transformer for Tabular Data
---

# Towards a Relationship-Aware Transformer for Tabular Data

**arXiv**: [2512.07310v1](https://arxiv.org/abs/2512.07310) | [PDF](https://arxiv.org/pdf/2512.07310.pdf)

**作者**: Andrei V. Konstantinov, Valerii A. Zuev, Lev V. Utkin

---

## 💡 一句话要点

**提出关系感知Transformer以解决表格数据中外部依赖图建模问题，适用于处理效应估计等任务。**

**关键词**: `表格数据建模` `关系感知Transformer` `注意力机制改进` `处理效应估计` `稀疏图处理`

## 📋 核心要点

1. 核心问题：现有深度学习模型难以在表格数据中融入样本间外部依赖图，如图神经网络仅考虑相邻节点，不适用于稀疏图。
2. 方法要点：基于改进的注意力机制，通过在注意力矩阵中添加项来建模数据点间可能的关系，提出多个解决方案。
3. 实验或效果：在合成和真实数据集上进行回归任务比较，以及在IHDP数据集上进行处理效应估计任务，与梯度提升决策树等模型对比。

## 📄 摘要（原文）

> Deep learning models for tabular data typically do not allow for imposing a graph of external dependencies between samples, which can be useful for accounting for relatedness in tasks such as treatment effect estimation. Graph neural networks only consider adjacent nodes, making them difficult to apply to sparse graphs. This paper proposes several solutions based on a modified attention mechanism, which accounts for possible relationships between data points by adding a term to the attention matrix. Our models are compared with each other and the gradient boosting decision trees in a regression task on synthetic and real-world datasets, as well as in a treatment effect estimation task on the IHDP dataset.

