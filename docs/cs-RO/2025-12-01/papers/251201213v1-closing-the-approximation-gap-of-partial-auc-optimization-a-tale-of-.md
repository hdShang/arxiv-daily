---
layout: default
title: Closing the Approximation Gap of Partial AUC Optimization: A Tale of Two Formulations
---

# Closing the Approximation Gap of Partial AUC Optimization: A Tale of Two Formulations

**arXiv**: [2512.01213v1](https://arxiv.org/abs/2512.01213) | [PDF](https://arxiv.org/pdf/2512.01213.pdf)

**作者**: Yangbangyan Jiang, Qianqian Xu, Huiyang Shao, Zhiyong Yang, Shilong Bao, Xiaochun Cao, Qingming Huang

---

## 💡 一句话要点

**提出两种实例级极小极大重构以消除部分AUC优化的近似误差，适用于类别不平衡与决策约束场景。**

**关键词**: `部分AUC优化` `近似误差消除` `极小极大重构` `类别不平衡` `泛化界分析` `ROC曲线`

## 📋 核心要点

1. 核心问题：部分AUC优化因NP-hard样本选择导致近似误差不可控或可扩展性受限。
2. 方法要点：通过实例级重构简化样本选择，应用平滑技术实现线性迭代复杂度与收敛率。
3. 实验或效果：在基准数据集上验证方法有效性，并提供紧致泛化界分析约束影响。

## 📄 摘要（原文）

> As a variant of the Area Under the ROC Curve (AUC), the partial AUC (PAUC) focuses on a specific range of false positive rate (FPR) and/or true positive rate (TPR) in the ROC curve. It is a pivotal evaluation metric in real-world scenarios with both class imbalance and decision constraints. However, selecting instances within these constrained intervals during its calculation is NP-hard, and thus typically requires approximation techniques for practical resolution. Despite the progress made in PAUC optimization over the last few years, most existing methods still suffer from uncontrollable approximation errors or a limited scalability when optimizing the approximate PAUC objectives. In this paper, we close the approximation gap of PAUC optimization by presenting two simple instance-wise minimax reformulations: one with an asymptotically vanishing gap, the other with the unbiasedness at the cost of more variables. Our key idea is to first establish an equivalent instance-wise problem to lower the time complexity, simplify the complicated sample selection procedure by threshold learning, and then apply different smoothing techniques. Equipped with an efficient solver, the resulting algorithms enjoy a linear per-iteration computational complexity w.r.t. the sample size and a convergence rate of $O(ε^{-1/3})$ for typical one-way and two-way PAUCs. Moreover, we provide a tight generalization bound of our minimax reformulations. The result explicitly demonstrates the impact of the TPR/FPR constraints $α$/$β$ on the generalization and exhibits a sharp order of $\tilde{O}(α^{-1}\n_+^{-1} + β^{-1}\n_-^{-1})$. Finally, extensive experiments on several benchmark datasets validate the strength of our proposed methods.

