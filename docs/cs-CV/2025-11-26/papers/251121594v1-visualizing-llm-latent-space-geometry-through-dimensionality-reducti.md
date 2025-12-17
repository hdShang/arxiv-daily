---
layout: default
title: Visualizing LLM Latent Space Geometry Through Dimensionality Reduction
---

# Visualizing LLM Latent Space Geometry Through Dimensionality Reduction

**arXiv**: [2511.21594v1](https://arxiv.org/abs/2511.21594) | [PDF](https://arxiv.org/pdf/2511.21594.pdf)

**作者**: Alex Ning, Vainateya Rangaraju

---

## 💡 一句话要点

**提出基于降维的可视化方法以分析Transformer语言模型的潜在空间几何**

**关键词**: `潜在空间可视化` `降维分析` `Transformer模型` `几何模式` `可解释性研究`

## 📋 核心要点

1. 核心问题：大语言模型内部机制难以解释，潜在空间几何特性未知
2. 方法要点：提取Transformer层激活，应用PCA和UMAP进行降维可视化
3. 实验或效果：在GPT-2和LLaMa中发现注意力与MLP输出分离等新几何模式

## 📄 摘要（原文）

> Large language models (LLMs) achieve state-of-the-art results across many natural language tasks, but their internal mechanisms remain difficult to interpret. In this work, we extract, process, and visualize latent state geometries in Transformer-based language models through dimensionality reduction. We capture layerwise activations at multiple points within Transformer blocks and enable systematic analysis through Principal Component Analysis (PCA) and Uniform Manifold Approximation (UMAP). We demonstrate experiments on GPT-2 and LLaMa models, where we uncover interesting geometric patterns in latent space. Notably, we identify a clear separation between attention and MLP component outputs across intermediate layers, a pattern not documented in prior work to our knowledge. We also characterize the high norm of latent states at the initial sequence position and visualize the layerwise evolution of latent states. Additionally, we demonstrate the high-dimensional helical structure of GPT-2's positional embeddings, the sequence-wise geometric patterns in LLaMa, and experiment with repeating token sequences. We aim to support systematic analysis of Transformer internals with the goal of enabling further reproducible interpretability research. We make our code available at https://github.com/Vainateya/Feature_Geometry_Visualization.

