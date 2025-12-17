---
layout: default
title: Scale-Agnostic Kolmogorov-Arnold Geometry in Neural Networks
---

# Scale-Agnostic Kolmogorov-Arnold Geometry in Neural Networks

**arXiv**: [2511.21626v1](https://arxiv.org/abs/2511.21626) | [PDF](https://arxiv.org/pdf/2511.21626.pdf)

**作者**: Mathew Vanherreweghe, Michael H. Freedman, Keith M. Adams

---

## 💡 一句话要点

**发现多层感知器在MNIST分类中自发形成尺度无关的Kolmogorov-Arnold几何结构**

**关键词**: `Kolmogorov-Arnold几何` `多层感知器` `MNIST分类` `尺度无关性` `空间分析`

## 📋 核心要点

1. 核心问题：Kolmogorov-Arnold几何是否在真实高维数据中持续存在及其空间特性
2. 方法要点：使用2层MLP对MNIST进行多尺度空间分析，涵盖局部到全局
3. 实验或效果：KAG在训练中自发出现，尺度无关性在不同训练方法中一致

## 📄 摘要（原文）

> Recent work by Freedman and Mulligan demonstrated that shallow multilayer perceptrons spontaneously develop Kolmogorov-Arnold geometric (KAG) structure during training on synthetic three-dimensional tasks. However, it remained unclear whether this phenomenon persists in realistic high-dimensional settings and what spatial properties this geometry exhibits.
>   We extend KAG analysis to MNIST digit classification (784 dimensions) using 2-layer MLPs with systematic spatial analysis at multiple scales. We find that KAG emerges during training and appears consistently across spatial scales, from local 7-pixel neighborhoods to the full 28x28 image. This scale-agnostic property holds across different training procedures: both standard training and training with spatial augmentation produce the same qualitative pattern. These findings reveal that neural networks spontaneously develop organized, scale-invariant geometric structure during learning on realistic high-dimensional data.

