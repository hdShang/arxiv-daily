---
layout: default
title: Domain-Decomposed Graph Neural Network Surrogate Modeling for Ice Sheets
---

# Domain-Decomposed Graph Neural Network Surrogate Modeling for Ice Sheets

**arXiv**: [2512.01888v1](https://arxiv.org/abs/2512.01888) | [PDF](https://arxiv.org/pdf/2512.01888.pdf)

**作者**: Adrienne M. Propp, Mauro Perego, Eric C. Cyr, Anthony Gruber, Amanda A. Howard, Alexander Heinlein, Panos Stinis, Daniel M. Tartakovsky

---

## 💡 一句话要点

**提出基于域分解的图神经网络代理模型，用于高效模拟冰盖动力学**

**关键词**: `图神经网络` `域分解` `代理建模` `冰盖模拟` `不确定性量化` `迁移学习`

## 📋 核心要点

1. 核心问题：大规模偏微分方程模拟中，代理模型需在非结构化网格上实现准确且高效的不确定性量化。
2. 方法要点：采用域分解策略，并行训练局部图神经网络代理，结合迁移学习优化子域模型。
3. 实验或效果：在冰盖模拟中，模型准确预测全场速度，显著减少训练时间，为不确定性量化提供基础。

## 📄 摘要（原文）

> Accurate yet efficient surrogate models are essential for large-scale simulations of partial differential equations (PDEs), particularly for uncertainty quantification (UQ) tasks that demand hundreds or thousands of evaluations. We develop a physics-inspired graph neural network (GNN) surrogate that operates directly on unstructured meshes and leverages the flexibility of graph attention. To improve both training efficiency and generalization properties of the model, we introduce a domain decomposition (DD) strategy that partitions the mesh into subdomains, trains local GNN surrogates in parallel, and aggregates their predictions. We then employ transfer learning to fine-tune models across subdomains, accelerating training and improving accuracy in data-limited settings. Applied to ice sheet simulations, our approach accurately predicts full-field velocities on high-resolution meshes, substantially reduces training time relative to training a single global surrogate model, and provides a ripe foundation for UQ objectives. Our results demonstrate that graph-based DD, combined with transfer learning, provides a scalable and reliable pathway for training GNN surrogates on massive PDE-governed systems, with broad potential for application beyond ice sheet dynamics.

