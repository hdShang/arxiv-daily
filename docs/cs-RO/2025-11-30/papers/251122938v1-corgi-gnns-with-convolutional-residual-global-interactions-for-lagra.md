---
layout: default
title: CORGI: GNNs with Convolutional Residual Global Interactions for Lagrangian Simulation
---

# CORGI: GNNs with Convolutional Residual Global Interactions for Lagrangian Simulation

**arXiv**: [2511.22938v1](https://arxiv.org/abs/2511.22938) | [PDF](https://arxiv.org/pdf/2511.22938.pdf)

**作者**: Ethan Ji, Yuanzhou Chen, Arush Ramteke, Fang Sun, Tianrun Yu, Jai Parera, Wei Wang, Yizhou Sun

---

## 💡 一句话要点

**提出CORGI以增强GNN求解器在拉格朗日模拟中的全局交互能力**

**关键词**: `拉格朗日模拟` `图神经网络` `全局交互` `流体动力学` `卷积残差`

## 📋 核心要点

1. 传统拉格朗日神经代理模型因感受野有限，难以捕捉流体流动的全局交互。
2. CORGI通过轻量欧拉组件，将粒子特征投影到网格进行卷积更新，再映射回粒子域。
3. 在GNS和SEGNN上，CORGI显著提升精度，同时保持较低计算开销。

## 📄 摘要（原文）

> Partial differential equations (PDEs) are central to dynamical systems modeling, particularly in hydrodynamics, where traditional solvers often struggle with nonlinearity and computational cost. Lagrangian neural surrogates such as GNS and SEGNN have emerged as strong alternatives by learning from particle-based simulations. However, these models typically operate with limited receptive fields, making them inaccurate for capturing the inherently global interactions in fluid flows. Motivated by this observation, we introduce Convolutional Residual Global Interactions (CORGI), a hybrid architecture that augments any GNN-based solver with a lightweight Eulerian component for global context aggregation. By projecting particle features onto a grid, applying convolutional updates, and mapping them back to the particle domain, CORGI captures long-range dependencies without significant overhead. When applied to a GNS backbone, CORGI achieves a 57% improvement in rollout accuracy with only 13% more inference time and 31% more training time. Compared to SEGNN, CORGI improves accuracy by 49% while reducing inference time by 48% and training time by 30%. Even under identical runtime constraints, CORGI outperforms GNS by 47% on average, highlighting its versatility and performance on varied compute budgets.

