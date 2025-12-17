---
layout: default
title: Closing the Train-Test Gap in World Models for Gradient-Based Planning
---

# Closing the Train-Test Gap in World Models for Gradient-Based Planning

**arXiv**: [2512.09929v1](https://arxiv.org/abs/2512.09929) | [PDF](https://arxiv.org/pdf/2512.09929.pdf)

**作者**: Arjun Parthasarathy, Nimit Kalra, Rohun Agrawal, Yann LeCun, Oumayma Bounou, Pavel Izmailov, Micah Goldblum

---

## 💡 一句话要点

**提出训练时数据合成方法以缩小世界模型在梯度规划中的训练-测试差距**

**关键词**: `世界模型` `梯度规划` `模型预测控制` `训练-测试差距` `数据合成`

## 📋 核心要点

1. 核心问题：世界模型训练基于状态预测，但测试时用于动作序列估计，存在性能差距
2. 方法要点：通过训练时数据合成技术改进世界模型，支持高效梯度规划
3. 实验或效果：在物体操作和导航任务中，性能优于或匹配CEM，时间预算仅需10%

## 📄 摘要（原文）

> World models paired with model predictive control (MPC) can be trained offline on large-scale datasets of expert trajectories and enable generalization to a wide range of planning tasks at inference time. Compared to traditional MPC procedures, which rely on slow search algorithms or on iteratively solving optimization problems exactly, gradient-based planning offers a computationally efficient alternative. However, the performance of gradient-based planning has thus far lagged behind that of other approaches. In this paper, we propose improved methods for training world models that enable efficient gradient-based planning. We begin with the observation that although a world model is trained on a next-state prediction objective, it is used at test-time to instead estimate a sequence of actions. The goal of our work is to close this train-test gap. To that end, we propose train-time data synthesis techniques that enable significantly improved gradient-based planning with existing world models. At test time, our approach outperforms or matches the classical gradient-free cross-entropy method (CEM) across a variety of object manipulation and navigation tasks in 10% of the time budget.

