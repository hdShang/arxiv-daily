---
layout: default
title: Efficient Spatially-Variant Convolution via Differentiable Sparse Kernel Complex
---

# Efficient Spatially-Variant Convolution via Differentiable Sparse Kernel Complex

**arXiv**: [2512.04556v1](https://arxiv.org/abs/2512.04556) | [PDF](https://arxiv.org/pdf/2512.04556.pdf)

**作者**: Zhizhen Wu, Zhe Cao, Yuchi Huo

---

## 💡 一句话要点

**提出可微分稀疏核分解框架，以高效实现空间变化复杂卷积，适用于移动成像和实时渲染。**

**关键词**: `空间变化卷积` `稀疏核分解` `可微分优化` `核空间插值` `移动成像` `实时渲染`

## 📋 核心要点

1. 核心问题：直接密集卷积计算成本高，现有近似方法效率低或无法处理非凸核。
2. 方法要点：使用稀疏核样本分解目标核，支持可微分优化、非凸核初始化和核空间插值。
3. 实验或效果：在Gaussian和非凸核上比模拟退火保真度高，比低秩分解成本低。

## 📄 摘要（原文）

> Image convolution with complex kernels is a fundamental operation in photography, scientific imaging, and animation effects, yet direct dense convolution is computationally prohibitive on resource-limited devices. Existing approximations, such as simulated annealing or low-rank decompositions, either lack efficiency or fail to capture non-convex kernels. We introduce a differentiable kernel decomposition framework that represents a target spatially-variant, dense, complex kernel using a set of sparse kernel samples. Our approach features (i) a decomposition that enables differentiable optimization of sparse kernels, (ii) a dedicated initialization strategy for non-convex shapes to avoid poor local minima, and (iii) a kernel-space interpolation scheme that extends single-kernel filtering to spatially varying filtering without retraining and additional runtime overhead. Experiments on Gaussian and non-convex kernels show that our method achieves higher fidelity than simulated annealing and significantly lower cost than low-rank decompositions. Our approach provides a practical solution for mobile imaging and real-time rendering, while remaining fully differentiable for integration into broader learning pipelines.

