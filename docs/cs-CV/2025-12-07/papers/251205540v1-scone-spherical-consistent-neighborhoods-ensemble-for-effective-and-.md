---
layout: default
title: SCoNE: Spherical Consistent Neighborhoods Ensemble for Effective and Efficient Multi-View Anomaly Detection
---

# SCoNE: Spherical Consistent Neighborhoods Ensemble for Effective and Efficient Multi-View Anomaly Detection

**arXiv**: [2512.05540v1](https://arxiv.org/abs/2512.05540) | [PDF](https://arxiv.org/pdf/2512.05540.pdf)

**作者**: Yang Xu, Hang Zhang, Yixiao Ma, Ye Zhu, Kai Ming Ting

---

## 💡 一句话要点

**提出SCoNE方法以解决多视图异常检测中邻居一致性表示与计算效率问题**

**关键词**: `多视图异常检测` `邻居一致性表示` `数据依赖属性` `计算效率优化` `无监督学习`

## 📋 核心要点

1. 核心问题：多视图异常检测需跨视图一致表示正常实例的局部邻居，现有方法因独立处理视图和密度差异导致准确性低且计算成本高
2. 方法要点：SCoNE直接使用多视图实例表示一致邻居，无需中间表示，并基于数据依赖属性自适应调整邻居大小，避免学习过程
3. 实验或效果：实证评估显示SCoNE在大型数据集上检测准确性更高，运行速度比现有方法快数个数量级，时间复杂度为O(N)

## 📄 摘要（原文）

> The core problem in multi-view anomaly detection is to represent local neighborhoods of normal instances consistently across all views. Recent approaches consider a representation of local neighborhood in each view independently, and then capture the consistent neighbors across all views via a learning process. They suffer from two key issues. First, there is no guarantee that they can capture consistent neighbors well, especially when the same neighbors are in regions of varied densities in different views, resulting in inferior detection accuracy. Second, the learning process has a high computational cost of $\mathcal{O}(N^2)$, rendering them inapplicable for large datasets. To address these issues, we propose a novel method termed \textbf{S}pherical \textbf{C}onsistent \textbf{N}eighborhoods \textbf{E}nsemble (SCoNE). It has two unique features: (a) the consistent neighborhoods are represented with multi-view instances directly, requiring no intermediate representations as used in existing approaches; and (b) the neighborhoods have data-dependent properties, which lead to large neighborhoods in sparse regions and small neighborhoods in dense regions. The data-dependent properties enable local neighborhoods in different views to be represented well as consistent neighborhoods, without learning. This leads to $\mathcal{O}(N)$ time complexity. Empirical evaluations show that SCoNE has superior detection accuracy and runs orders-of-magnitude faster in large datasets than existing approaches.

