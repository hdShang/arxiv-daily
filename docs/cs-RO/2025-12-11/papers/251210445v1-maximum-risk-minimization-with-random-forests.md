---
layout: default
title: Maximum Risk Minimization with Random Forests
---

# Maximum Risk Minimization with Random Forests

**arXiv**: [2512.10445v1](https://arxiv.org/abs/2512.10445) | [PDF](https://arxiv.org/pdf/2512.10445.pdf)

**作者**: Francesco Freni, Anya Fries, Linus Kühne, Markus Reichstein, Jonas Peters

---

## 💡 一句话要点

**提出基于最大风险最小化的随机森林变体，以提升分布外泛化能力。**

**关键词**: `分布外泛化` `最大风险最小化` `随机森林` `回归分析` `统计一致性`

## 📋 核心要点

1. 核心问题：回归任务中训练与测试环境分布不同，需提升分布外泛化性能。
2. 方法要点：基于最大风险最小化原则，设计随机森林变体，支持均方误差、负奖励和遗憾三种风险。
3. 实验或效果：在模拟和真实数据上评估，证明统计一致性并提供计算高效算法。

## 📄 摘要（原文）

> We consider a regression setting where observations are collected in different environments modeled by different data distributions. The field of out-of-distribution (OOD) generalization aims to design methods that generalize better to test environments whose distributions differ from those observed during training. One line of such works has proposed to minimize the maximum risk across environments, a principle that we refer to as MaxRM (Maximum Risk Minimization). In this work, we introduce variants of random forests based on the principle of MaxRM. We provide computationally efficient algorithms and prove statistical consistency for our primary method. Our proposed method can be used with each of the following three risks: the mean squared error, the negative reward (which relates to the explained variance), and the regret (which quantifies the excess risk relative to the best predictor). For MaxRM with regret as the risk, we prove a novel out-of-sample guarantee over unseen test distributions. Finally, we evaluate the proposed methods on both simulated and real-world data.

