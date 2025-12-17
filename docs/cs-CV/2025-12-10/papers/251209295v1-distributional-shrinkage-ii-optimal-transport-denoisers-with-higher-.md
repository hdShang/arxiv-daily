---
layout: default
title: Distributional Shrinkage II: Optimal Transport Denoisers with Higher-Order Scores
---

# Distributional Shrinkage II: Optimal Transport Denoisers with Higher-Order Scores

**arXiv**: [2512.09295v1](https://arxiv.org/abs/2512.09295) | [PDF](https://arxiv.org/pdf/2512.09295.pdf)

**作者**: Tengyuan Liang

---

## 💡 一句话要点

**提出基于高阶分数函数的最优传输去噪器，用于信号分布恢复**

**关键词**: `最优传输` `信号去噪` `高阶分数函数` `Wasserstein距离` `经验贝叶斯`

## 📋 核心要点

1. 核心问题：从高斯噪声观测中恢复未知信号分布，无需先验知识
2. 方法要点：构建去噪器层次，利用高阶分数函数逐步优化Wasserstein距离
3. 实验或效果：提供两种估计策略，分析收敛率，实现渐进去噪质量提升

## 📄 摘要（原文）

> We revisit the signal denoising problem through the lens of optimal transport: the goal is to recover an unknown scalar signal distribution $X \sim P$ from noisy observations $Y = X + σZ$, with $Z$ being standard Gaussian independent of $X$ and $σ>0$ a known noise level. Let $Q$ denote the distribution of $Y$. We introduce a hierarchy of denoisers $T_0, T_1, \ldots, T_\infty : \mathbb{R} \to \mathbb{R}$ that are agnostic to the signal distribution $P$, depending only on higher-order score functions of $Q$. Each denoiser $T_K$ is progressively refined using the $(2K-1)$-th order score function of $Q$ at noise resolution $σ^{2K}$, achieving better denoising quality measured by the Wasserstein metric $W(T_K \sharp Q, P)$. The limiting denoiser $T_\infty$ identifies the optimal transport map with $T_\infty \sharp Q = P$.
>   We provide a complete characterization of the combinatorial structure underlying this hierarchy through Bell polynomial recursions, revealing how higher-order score functions encode the optimal transport map for signal denoising. We study two estimation strategies with convergence rates for higher-order scores from i.i.d. samples drawn from $Q$: (i) plug-in estimation via Gaussian kernel smoothing, and (ii) direct estimation via higher-order score matching. This hierarchy of agnostic denoisers opens new perspectives in signal denoising and empirical Bayes.

