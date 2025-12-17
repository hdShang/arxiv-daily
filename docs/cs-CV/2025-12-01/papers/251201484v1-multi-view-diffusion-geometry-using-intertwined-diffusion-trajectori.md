---
layout: default
title: Multi-view diffusion geometry using intertwined diffusion trajectories
---

# Multi-view diffusion geometry using intertwined diffusion trajectories

**arXiv**: [2512.01484v1](https://arxiv.org/abs/2512.01484) | [PDF](https://arxiv.org/pdf/2512.01484.pdf)

**作者**: Gwendal Debaussart-Joniec, Argyris Kalogeratos

---

## 💡 一句话要点

**提出多视图交织扩散轨迹框架，统一构建多视图扩散几何用于流形学习和聚类。**

**关键词**: `多视图学习` `扩散几何` `随机游走` `流形学习` `数据聚类` `算子学习`

## 📋 核心要点

1. 核心问题：现有多视图扩散模型缺乏统一框架，视图交互和融合自由度有限。
2. 方法要点：通过迭代组合多视图随机游走算子，定义轨迹依赖的扩散算子，捕获视图间动态交互。
3. 实验或效果：在流形学习和数据聚类实验中验证了MDT算子的实际效果，并提供了评估基线。

## 📄 摘要（原文）

> This paper introduces a comprehensive unified framework for constructing multi-view diffusion geometries through intertwined multi-view diffusion trajectories (MDTs), a class of inhomogeneous diffusion processes that iteratively combine the random walk operators of multiple data views. Each MDT defines a trajectory-dependent diffusion operator with a clear probabilistic and geometric interpretation, capturing over time the interplay between data views. Our formulation encompasses existing multi-view diffusion models, while providing new degrees of freedom for view interaction and fusion. We establish theoretical properties under mild assumptions, including ergodicity of both the point-wise operator and the process in itself. We also derive MDT-based diffusion distances, and associated embeddings via singular value decompositions. Finally, we propose various strategies for learning MDT operators within the defined operator space, guided by internal quality measures. Beyond enabling flexible model design, MDTs also offer a neutral baseline for evaluating diffusion-based approaches through comparison with randomly selected MDTs. Experiments show the practical impact of the MDT operators in a manifold learning and data clustering context.

