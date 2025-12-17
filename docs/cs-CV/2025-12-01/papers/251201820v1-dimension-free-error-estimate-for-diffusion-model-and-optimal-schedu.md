---
layout: default
title: Dimension-free error estimate for diffusion model and optimal scheduling
---

# Dimension-free error estimate for diffusion model and optimal scheduling

**arXiv**: [2512.01820v1](https://arxiv.org/abs/2512.01820) | [PDF](https://arxiv.org/pdf/2512.01820.pdf)

**作者**: Valentin de Bortoli, Romuald Elie, Anna Kazeykina, Zhenjie Ren, Jiacheng Zhang

---

## 💡 一句话要点

**提出扩散模型的维度无关误差估计与最优时间调度，以解决高维生成中的误差缩放问题。**

**关键词**: `扩散模型` `误差估计` `维度无关` `时间调度` `生成模型` `最优控制`

## 📋 核心要点

1. 核心问题：现有误差度量（如Wasserstein距离）在高维下缩放差，导致误差界限不实用。
2. 方法要点：使用有界导数的平滑测试泛函，推导维度无关的误差界限，并优化时间调度以最小化离散化误差。
3. 实验或效果：推导出最优时间调度策略，为文献中已有调度提供基于最小化离散化偏差的新理论依据。

## 📄 摘要（原文）

> Diffusion generative models have emerged as powerful tools for producing synthetic data from an empirically observed distribution. A common approach involves simulating the time-reversal of an Ornstein-Uhlenbeck (OU) process initialized at the true data distribution. Since the score function associated with the OU process is typically unknown, it is approximated using a trained neural network. This approximation, along with finite time simulation, time discretization and statistical approximation, introduce several sources of error whose impact on the generated samples must be carefully understood. Previous analyses have quantified the error between the generated and the true data distributions in terms of Wasserstein distance or Kullback-Leibler (KL) divergence. However, both metrics present limitations: KL divergence requires absolute continuity between distributions, while Wasserstein distance, though more general, leads to error bounds that scale poorly with dimension, rendering them impractical in high-dimensional settings. In this work, we derive an explicit, dimension-free bound on the discrepancy between the generated and the true data distributions. The bound is expressed in terms of a smooth test functional with bounded first and second derivatives. The key novelty lies in the use of this weaker, functional metric to obtain dimension-independent guarantees, at the cost of higher regularity on the test functions. As an application, we formulate and solve a variational problem to minimize the time-discretization error, leading to the derivation of an optimal time-scheduling strategy for the reverse-time diffusion. Interestingly, this scheduler has appeared previously in the literature in a different context; our analysis provides a new justification for its optimality, now grounded in minimizing the discretization bias in generative sampling.

