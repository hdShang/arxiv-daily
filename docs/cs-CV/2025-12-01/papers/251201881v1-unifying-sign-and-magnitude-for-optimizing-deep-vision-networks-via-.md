---
layout: default
title: Unifying Sign and Magnitude for Optimizing Deep Vision Networks via ThermoLion
---

# Unifying Sign and Magnitude for Optimizing Deep Vision Networks via ThermoLion

**arXiv**: [2512.01881v1](https://arxiv.org/abs/2512.01881) | [PDF](https://arxiv.org/pdf/2512.01881.pdf)

**作者**: Ahmed Nebli

---

## 💡 一句话要点

**提出ThermoLion框架，通过动态调制更新比特率优化深度视觉网络训练**

**关键词**: `深度视觉网络优化` `梯度噪声处理` `动态比特率调制` `信噪比门控` `动量对齐机制` `超参数自由训练`

## 📋 核心要点

1. 核心问题：现有优化方法在梯度噪声与精度间静态妥协，导致收敛效率低
2. 方法要点：基于局部信噪比门控，动态切换低比特探索与高精度利用阶段
3. 实验或效果：在12个视觉数据集上超越AdamW和Lion，无需超参数调优

## 📄 摘要（原文）

> The training of deep vision models is fundamentally a signal recovery problem amidst high-dimensional stochastic noise. Current optimization paradigms impose a static compromise on information channel capacity. For instance, magnitude-based methods, such as AdamW, operate on the assumption that gradient norms are high-fidelity curvature signals. While this allows for precision in smooth regimes, it leads to catastrophic noise amplification when applied to rugged, non-convex landscapes. Conversely, sign-based methods (e.g., Lion) perform a radical 1-bit quantization of the gradient, which aims to provide robust regularization at the cost of discarding fine-grained descent information. We propose that optimal convergence requires neither static prior, but rather a dynamic modulation of the update bitrate. We introduce \textbf{ThermoLion}, a vision-centric framework that utilizes local Signal-to-Noise Ratio (SNR) gating to autonomously transition parameters between a "low-bit" exploration phase and a "high-precision" exploitation phase. Furthermore, we introduce a Momentum Alignment mechanism that detects constructive interference between historical drift and instantaneous gradients to accelerate convergence during stable trajectories. Empirical benchmarks across 12 diverse vision datasets (including CIFAR, SVHN, and GTSRB) demonstrate that ThermoLion serves as a hyperparameter-free generalist, surpassing both AdamW and Lion in convergence speed and terminal accuracy without architecture-specific tuning.

