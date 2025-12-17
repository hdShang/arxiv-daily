---
layout: default
title: Computing Strategic Responses to Non-Linear Classifiers
---

# Computing Strategic Responses to Non-Linear Classifiers

**arXiv**: [2511.21560v1](https://arxiv.org/abs/2511.21560) | [PDF](https://arxiv.org/pdf/2511.21560.pdf)

**作者**: Jack Geary, Boyan Gao, Henry Gouk

---

## 💡 一句话要点

**提出基于拉格朗日对偶的方法以计算非线性分类器中的最优策略响应**

**关键词**: `战略分类` `非线性分类器` `最优响应计算` `拉格朗日对偶` `分布偏移`

## 📋 核心要点

1. 核心问题：战略分类中非线性分类器难以计算代理最优响应，导致分布偏移
2. 方法要点：通过优化代理目标的拉格朗日对偶来计算最佳响应
3. 实验或效果：在线性设置中复现最优响应，并应用于非线性分类器评估与训练

## 📄 摘要（原文）

> We consider the problem of strategic classification, where the act of deploying a classifier leads to strategic behaviour that induces a distribution shift on subsequent observations. Current approaches to learning classifiers in strategic settings are focused primarily on the linear setting, but in many cases non-linear classifiers are more suitable. A central limitation to progress for non-linear classifiers arises from the inability to compute best responses in these settings. We present a novel method for computing the best response by optimising the Lagrangian dual of the Agents' objective. We demonstrate that our method reproduces best responses in linear settings, identifying key weaknesses in existing approaches. We present further results demonstrating our method can be straight-forwardly applied to non-linear classifier settings, where it is useful for both evaluation and training.

