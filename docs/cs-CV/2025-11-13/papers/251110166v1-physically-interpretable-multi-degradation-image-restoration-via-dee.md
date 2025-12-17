---
layout: default
title: Physically Interpretable Multi-Degradation Image Restoration via Deep Unfolding and Explainable Convolution
---

# Physically Interpretable Multi-Degradation Image Restoration via Deep Unfolding and Explainable Convolution

**arXiv**: [2511.10166v1](https://arxiv.org/abs/2511.10166) | [PDF](https://arxiv.org/pdf/2511.10166.pdf)

**作者**: Hu Gao, Xiaoning Lei, Xichen Xu, Depeng Dang, Lizhuang Ma

---

## 💡 一句话要点

**提出InterIR方法，通过深度展开和可解释卷积解决多退化图像恢复问题**

**关键词**: `多退化图像恢复` `深度展开网络` `可解释卷积` `物理可解释性` `图像去噪`

## 📋 核心要点

1. 核心问题：现实图像常同时存在雨、噪声和雾等多种退化，现有方法多针对单一退化且可解释性差
2. 方法要点：基于深度展开网络映射优化算法迭代过程，并设计可解释卷积模块以增强适应性和物理可解释性
3. 实验或效果：在多种退化恢复中表现优异，同时在单一退化任务上保持竞争力

## 📄 摘要（原文）

> Although image restoration has advanced significantly, most existing methods target only a single type of degradation. In real-world scenarios, images often contain multiple degradations simultaneously, such as rain, noise, and haze, requiring models capable of handling diverse degradation types. Moreover, methods that improve performance through module stacking often suffer from limited interpretability. In this paper, we propose a novel interpretability-driven approach for multi-degradation image restoration, built upon a deep unfolding network that maps the iterative process of a mathematical optimization algorithm into a learnable network structure. Specifically, we employ an improved second-order semi-smooth Newton algorithm to ensure that each module maintains clear physical interpretability. To further enhance interpretability and adaptability, we design an explainable convolution module inspired by the human brain's flexible information processing and the intrinsic characteristics of images, allowing the network to flexibly leverage learned knowledge and autonomously adjust parameters for different input. The resulting tightly integrated architecture, named InterIR, demonstrates excellent performance in multi-degradation restoration while remaining highly competitive on single-degradation tasks.

