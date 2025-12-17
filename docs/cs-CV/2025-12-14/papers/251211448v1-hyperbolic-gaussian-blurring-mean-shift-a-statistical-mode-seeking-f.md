---
layout: default
title: Hyperbolic Gaussian Blurring Mean Shift: A Statistical Mode-Seeking Framework for Clustering in Curved Spaces
---

# Hyperbolic Gaussian Blurring Mean Shift: A Statistical Mode-Seeking Framework for Clustering in Curved Spaces

**arXiv**: [2512.11448v1](https://arxiv.org/abs/2512.11448) | [PDF](https://arxiv.org/pdf/2512.11448.pdf)

**作者**: Arghya Pratihar, Arnab Seal, Swagatam Das, Inesh Chattopadhyay

---

## 💡 一句话要点

**提出HypeGBMS以解决层次结构数据在双曲空间中的聚类问题**

**关键词**: `双曲空间聚类` `均值漂移算法` `层次结构数据` `密度估计` `非欧几何`

## 📋 核心要点

1. 核心问题：传统GBMS在欧氏空间处理层次结构数据效果不佳
2. 方法要点：扩展GBMS至双曲空间，使用双曲距离和Möbius加权均值
3. 实验或效果：在11个真实数据集上验证，显著优于传统方法

## 📄 摘要（原文）

> Clustering is a fundamental unsupervised learning task for uncovering patterns in data. While Gaussian Blurring Mean Shift (GBMS) has proven effective for identifying arbitrarily shaped clusters in Euclidean space, it struggles with datasets exhibiting hierarchical or tree-like structures. In this work, we introduce HypeGBMS, a novel extension of GBMS to hyperbolic space. Our method replaces Euclidean computations with hyperbolic distances and employs Möbius-weighted means to ensure that all updates remain consistent with the geometry of the space. HypeGBMS effectively captures latent hierarchies while retaining the density-seeking behavior of GBMS. We provide theoretical insights into convergence and computational complexity, along with empirical results that demonstrate improved clustering quality in hierarchical datasets. This work bridges classical mean-shift clustering and hyperbolic representation learning, offering a principled approach to density-based clustering in curved spaces. Extensive experimental evaluations on $11$ real-world datasets demonstrate that HypeGBMS significantly outperforms conventional mean-shift clustering methods in non-Euclidean settings, underscoring its robustness and effectiveness.

