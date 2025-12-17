---
layout: default
title: Imbalanced Classification through the Lens of Spurious Correlations
---

# Imbalanced Classification through the Lens of Spurious Correlations

**arXiv**: [2510.27650v1](https://arxiv.org/abs/2510.27650) | [PDF](https://arxiv.org/pdf/2510.27650.pdf)

**作者**: Jakob Hackstein, Sidney Bender

---

## 💡 一句话要点

**提出基于可解释AI的方法以消除类别不平衡中的Clever Hans效应**

**关键词**: `类别不平衡` `Clever Hans效应` `可解释AI` `反事实解释` `分类性能`

## 📋 核心要点

1. 核心问题：类别不平衡放大Clever Hans效应，导致分类不可靠
2. 方法要点：使用反事实解释联合识别并消除不平衡下的CH效应
3. 实验或效果：在三个数据集上实现竞争性分类性能，验证CH效应出现

## 📄 摘要（原文）

> Class imbalance poses a fundamental challenge in machine learning, frequently
> leading to unreliable classification performance. While prior methods focus on
> data- or loss-reweighting schemes, we view imbalance as a data condition that
> amplifies Clever Hans (CH) effects by underspecification of minority classes.
> In a counterfactual explanations-based approach, we propose to leverage
> Explainable AI to jointly identify and eliminate CH effects emerging under
> imbalance. Our method achieves competitive classification performance on three
> datasets and demonstrates how CH effects emerge under imbalance, a perspective
> largely overlooked by existing approaches.

