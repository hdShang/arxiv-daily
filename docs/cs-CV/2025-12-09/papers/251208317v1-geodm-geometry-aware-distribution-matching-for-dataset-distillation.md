---
layout: default
title: GeoDM: Geometry-aware Distribution Matching for Dataset Distillation
---

# GeoDM: Geometry-aware Distribution Matching for Dataset Distillation

**arXiv**: [2512.08317v1](https://arxiv.org/abs/2512.08317) | [PDF](https://arxiv.org/pdf/2512.08317.pdf)

**作者**: Xuhui Li, Zhengquan Luo, Zihui Cui, Zhiqiang Xu

---

## 💡 一句话要点

**提出GeoDM框架，通过几何感知分布匹配解决数据集蒸馏中忽略数据内在几何结构的问题。**

**关键词**: `数据集蒸馏` `几何感知` `分布匹配` `流形学习` `最优传输` `泛化误差`

## 📋 核心要点

1. 核心问题：现有分布匹配方法局限于欧氏空间，无法捕捉高维数据的非线性几何结构如曲率。
2. 方法要点：在欧氏、双曲和球面流形的笛卡尔积空间中操作，引入可学习曲率和权重参数以适配数据几何。
3. 实验或效果：在标准基准测试中优于现有数据集蒸馏方法，理论分析显示泛化误差界更小。

## 📄 摘要（原文）

> Dataset distillation aims to synthesize a compact subset of the original data, enabling models trained on it to achieve performance comparable to those trained on the original large dataset. Existing distribution-matching methods are confined to Euclidean spaces, making them only capture linear structures and overlook the intrinsic geometry of real data, e.g., curvature. However, high-dimensional data often lie on low-dimensional manifolds, suggesting that dataset distillation should have the distilled data manifold aligned with the original data manifold. In this work, we propose a geometry-aware distribution-matching framework, called \textbf{GeoDM}, which operates in the Cartesian product of Euclidean, hyperbolic, and spherical manifolds, with flat, hierarchical, and cyclical structures all captured by a unified representation. To adapt to the underlying data geometry, we introduce learnable curvature and weight parameters for three kinds of geometries. At the same time, we design an optimal transport loss to enhance the distribution fidelity. Our theoretical analysis shows that the geometry-aware distribution matching in a product space yields a smaller generalization error bound than the Euclidean counterparts. Extensive experiments conducted on standard benchmarks demonstrate that our algorithm outperforms state-of-the-art data distillation methods and remains effective across various distribution-matching strategies for the single geometries.

