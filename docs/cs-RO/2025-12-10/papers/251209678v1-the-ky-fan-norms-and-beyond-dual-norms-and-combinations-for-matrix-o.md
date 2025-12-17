---
layout: default
title: The Ky Fan Norms and Beyond: Dual Norms and Combinations for Matrix Optimization
---

# The Ky Fan Norms and Beyond: Dual Norms and Combinations for Matrix Optimization

**arXiv**: [2512.09678v1](https://arxiv.org/abs/2512.09678) | [PDF](https://arxiv.org/pdf/2512.09678.pdf)

**作者**: Alexey Kravatskiy, Ivan Kozyrev, Nikolai Kozlov, Alexander Vinogradov, Daniil Merkulov, Ivan Oseledets

---

## 💡 一句话要点

**提出基于Ky Fan范数对偶的Fanions算法族，用于大语言模型权重矩阵优化。**

**关键词**: `矩阵优化` `Ky Fan范数` `大语言模型训练` `算法设计` `权重矩阵范数`

## 📋 核心要点

1. 核心问题：探索矩阵范数在训练大语言模型权重矩阵优化中的应用。
2. 方法要点：利用Ky Fan k-范数的对偶，结合Frobenius或l∞范数，构建F-Fanions和S-Fanions算法族。
3. 实验或效果：F-Muon和S-Muon在广泛任务中匹配Muon性能，并在合成线性最小二乘问题上超越Muon。

## 📄 摘要（原文）

> In this article, we explore the use of various matrix norms for optimizing functions of weight matrices, a crucial problem in training large language models. Moving beyond the spectral norm underlying the Muon update, we leverage duals of the Ky Fan $k$-norms to introduce a family of Muon-like algorithms we name Fanions, which are closely related to Dion. By working with duals of convex combinations of the Ky Fan $k$-norms with either the Frobenius norm or the $l_\infty$ norm, we construct the families of F-Fanions and S-Fanions, respectively. Their most prominent members are F-Muon and S-Muon. We complement our theoretical analysis with an extensive empirical study of these algorithms across a wide range of tasks and settings, demonstrating that F-Muon and S-Muon consistently match Muon's performance, while outperforming vanilla Muon on a synthetic linear least squares problem.

