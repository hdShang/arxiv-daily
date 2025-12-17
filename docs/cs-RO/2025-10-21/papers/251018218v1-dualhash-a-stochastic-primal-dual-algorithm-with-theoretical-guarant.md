---
layout: default
title: DualHash: A Stochastic Primal-Dual Algorithm with Theoretical Guarantee for Deep Hashing
---

# DualHash: A Stochastic Primal-Dual Algorithm with Theoretical Guarantee for Deep Hashing

**arXiv**: [2510.18218v1](https://arxiv.org/abs/2510.18218) | [PDF](https://arxiv.org/pdf/2510.18218.pdf)

**作者**: Luxuan Li, Xiao Wang, Chunfeng Cui

---

## 💡 一句话要点

**提出DualHash算法，通过随机原始-对偶方法解决深度哈希中的离散量化优化问题。**

**关键词**: `深度哈希` `随机优化` `原始-对偶算法` `图像检索` `W型正则化` `复杂度分析`

## 📋 核心要点

1. 核心问题：深度哈希中离散量化导致优化困难，现有方法缺乏收敛保证。
2. 方法要点：利用Fenchel对偶将W型正则化部分转换，获得闭式近端解。
3. 实验效果：在三个图像检索数据库上表现优越，提供复杂度保证。

## 📄 摘要（原文）

> Deep hashing converts high-dimensional feature vectors into compact binary
> codes, enabling efficient large-scale retrieval. A fundamental challenge in
> deep hashing stems from the discrete nature of quantization in generating the
> codes. W-type regularizations, such as $\|\|z\|-1\|$, have been proven effective as
> they encourage variables toward binary values. However, existing methods often
> directly optimize these regularizations without convergence guarantees. While
> proximal gradient methods offer a promising solution, the coupling between
> W-type regularizers and neural network outputs results in composite forms that
> generally lack closed-form proximal solutions. In this paper, we present a
> stochastic primal-dual hashing algorithm, referred to as DualHash, that
> provides rigorous complexity bounds. Using Fenchel duality, we partially
> transform the nonconvex W-type regularization optimization into the dual space,
> which results in a proximal operator that admits closed-form solutions. We
> derive two algorithm instances: a momentum-accelerated version with
> $\mathcal{O}(\varepsilon^{-4})$ complexity and an improved
> $\mathcal{O}(\varepsilon^{-3})$ version using variance reduction. Experiments
> on three image retrieval databases demonstrate the superior performance of
> DualHash.

