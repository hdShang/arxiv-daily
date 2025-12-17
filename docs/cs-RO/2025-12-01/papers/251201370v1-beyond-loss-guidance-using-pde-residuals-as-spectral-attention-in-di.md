---
layout: default
title: Beyond Loss Guidance: Using PDE Residuals as Spectral Attention in Diffusion Neural Operators
---

# Beyond Loss Guidance: Using PDE Residuals as Spectral Attention in Diffusion Neural Operators

**arXiv**: [2512.01370v1](https://arxiv.org/abs/2512.01370) | [PDF](https://arxiv.org/pdf/2512.01370.pdf)

**作者**: Medha Sawhney, Abhilash Neog, Mridul Khurana, Anuj Karpatne

---

## 💡 一句话要点

**提出PRISMA方法，通过谱域注意力嵌入PDE残差，实现无梯度优化的快速扩散神经算子求解偏微分方程。**

**关键词**: `偏微分方程求解` `扩散模型` `神经算子` `谱域注意力` `无梯度优化` `噪声鲁棒性`

## 📋 核心要点

1. 核心问题：传统基于扩散的PDE求解器依赖梯度优化，导致推理慢、不稳定且对噪声敏感。
2. 方法要点：PRISMA将PDE残差作为谱域注意力机制直接集成到模型架构中，避免外部损失引导。
3. 实验或效果：在五个基准PDE上，PRISMA以更少去噪步骤实现竞争性精度，推理速度提升15倍至250倍。

## 📄 摘要（原文）

> Diffusion-based solvers for partial differential equations (PDEs) are often bottle-necked by slow gradient-based test-time optimization routines that use PDE residuals for loss guidance. They additionally suffer from optimization instabilities and are unable to dynamically adapt their inference scheme in the presence of noisy PDE residuals. To address these limitations, we introduce PRISMA (PDE Residual Informed Spectral Modulation with Attention), a conditional diffusion neural operator that embeds PDE residuals directly into the model's architecture via attention mechanisms in the spectral domain, enabling gradient-descent free inference. In contrast to previous methods that use PDE loss solely as external optimization targets, PRISMA integrates PDE residuals as integral architectural features, making it inherently fast, robust, accurate, and free from sensitive hyperparameter tuning. We show that PRISMA has competitive accuracy, at substantially lower inference costs, compared to previous methods across five benchmark PDEs, especially with noisy observations, while using 10x to 100x fewer denoising steps, leading to 15x to 250x faster inference.

