---
layout: default
title: Jacobian Aligned Random Forests
---

# Jacobian Aligned Random Forests

**arXiv**: [2512.08306v1](https://arxiv.org/abs/2512.08306) | [PDF](https://arxiv.org/pdf/2512.08306.pdf)

**作者**: Sarwesh Rauniyar

---

## 💡 一句话要点

**提出JARF方法，通过雅可比对齐预处理器提升轴对齐森林在旋转或交互依赖决策边界数据集上的性能。**

**关键词**: `随机森林` `雅可比对齐` `特征预处理器` `决策边界优化` `表格数据学习`

## 📋 核心要点

1. 轴对齐决策树在旋转或交互依赖决策边界上表现不佳，需要线性组合特征而非单特征阈值。
2. JARF利用森林预测的梯度计算雅可比外积，作为全局线性预处理器旋转特征空间，再训练轴对齐森林。
3. 实验表明，该方法在表格分类和回归基准上提升轴对齐森林性能，常匹配或超越斜森林，同时保持训练效率。

## 📄 摘要（原文）

> Axis-aligned decision trees are fast and stable but struggle on datasets with rotated or interaction-dependent decision boundaries, where informative splits require linear combinations of features rather than single-feature thresholds. Oblique forests address this with per-node hyperplane splits, but at added computational cost and implementation complexity. We propose a simple alternative: JARF, Jacobian-Aligned Random Forests. Concretely, we first fit an axis-aligned forest to estimate class probabilities or regression outputs, compute finite-difference gradients of these predictions with respect to each feature, aggregate them into an expected Jacobian outer product that generalizes the expected gradient outer product (EGOP), and use it as a single global linear preconditioner for all inputs. This supervised preconditioner applies a single global rotation of the feature space, then hands the transformed data back to a standard axis-aligned forest, preserving off-the-shelf training pipelines while capturing oblique boundaries and feature interactions that would otherwise require many axis-aligned splits to approximate. The same construction applies to any model that provides gradients, though we focus on random forests and gradient-boosted trees in this work. On tabular classification and regression benchmarks, this preconditioning consistently improves axis-aligned forests and often matches or surpasses oblique baselines while improving training time. Our experimental results and theoretical analysis together indicate that supervised preconditioning can recover much of the accuracy of oblique forests while retaining the simplicity and robustness of axis-aligned trees.

