---
layout: default
title: Hyperparameter Transfer Enables Consistent Gains of Matrix-Preconditioned Optimizers Across Scales
---

# Hyperparameter Transfer Enables Consistent Gains of Matrix-Preconditioned Optimizers Across Scales

**arXiv**: [2512.05620v1](https://arxiv.org/abs/2512.05620) | [PDF](https://arxiv.org/pdf/2512.05620.pdf)

**作者**: Shikai Qiu, Zixi Chen, Hoang Phan, Qi Lei, Andrew Gordon Wilson

---

## 💡 一句话要点

**通过超参数转移实现矩阵预条件优化器在不同规模下的稳定加速**

**关键词**: `超参数转移` `矩阵预条件优化器` `模型规模扩展` `学习率缩放` `权重衰减` `优化器比较`

## 📋 核心要点

1. 研究矩阵预条件优化器在规模扩展时性能不稳定的核心问题
2. 提出基于μP的超参数转移方法，结合分块和谱归一化提升稳定性
3. 实验显示Muon和Shampoo在Llama架构模型上实现1.3-1.4倍加速

## 📄 摘要（原文）

> Several recently introduced deep learning optimizers utilizing matrix-level preconditioning have shown promising speedups relative to the current dominant optimizer AdamW, particularly in relatively small-scale experiments. However, efforts to validate and replicate their successes have reported mixed results. To better understand the effectiveness of these optimizers at scale, in this work we investigate how to scale preconditioned optimizers via hyperparameter transfer, building on prior works such as $μ$P. We study how the optimal learning rate and weight decay should scale with model width and depth for a wide range of optimizers, including Shampoo, SOAP, and Muon, accounting for the impact of commonly used techniques such as blocking and grafting. We find that scaling the learning rate according to $μ$P improves transfer, but can still suffer from significant finite-width deviations that cause drifting optimal learning rates, which we show can be mitigated by blocking and explicit spectral normalization. For compute-optimal scaling, we find scaling independent weight decay as $1/\mathrm{width}$ is nearly optimal across optimizers. Applying these scaling rules, we show Muon and Shampoo consistently achieve $1.4\times$ and $1.3\times$ speedup over AdamW for training Llama-architecture language models of sizes ranging from $190$M to $1.4$B, whereas the speedup vanishes rapidly with scale under incorrect scaling. Based on these results and further ablations, we argue that studying optimal hyperparameter transfer is essential for reliably comparing optimizers at scale given a realistic tuning budget.

