---
layout: default
title: BézierFlow: Bézier Stochastic Interpolant Schedulers for Few-Step Generation
---

# BézierFlow: Bézier Stochastic Interpolant Schedulers for Few-Step Generation

**arXiv**: [2512.13255v1](https://arxiv.org/abs/2512.13255) | [PDF](https://arxiv.org/pdf/2512.13255.pdf)

**作者**: Yunhong Min, Juil Koo, Seungwoo Yoo, Minhyuk Sung

---

## 💡 一句话要点

**提出BézierFlow，通过参数化随机插值调度器优化采样轨迹，实现少步生成性能提升。**

**关键词**: `少步生成` `随机插值调度器` `Bézier函数` `扩散模型` `流模型` `轻量训练`

## 📋 核心要点

1. 核心问题：现有轻量训练方法局限于ODE离散化，难以优化采样轨迹变换。
2. 方法要点：使用Bézier函数参数化调度器，满足边界条件和单调性等关键需求。
3. 实验或效果：在预训练扩散和流模型中，BézierFlow在≤10步采样时性能提升2-3倍，训练仅需15分钟。

## 📄 摘要（原文）

> We introduce BézierFlow, a lightweight training approach for few-step generation with pretrained diffusion and flow models. BézierFlow achieves a 2-3x performance improvement for sampling with $\leq$ 10 NFEs while requiring only 15 minutes of training. Recent lightweight training approaches have shown promise by learning optimal timesteps, but their scope remains restricted to ODE discretizations. To broaden this scope, we propose learning the optimal transformation of the sampling trajectory by parameterizing stochastic interpolant (SI) schedulers. The main challenge lies in designing a parameterization that satisfies critical desiderata, including boundary conditions, differentiability, and monotonicity of the SNR. To effectively meet these requirements, we represent scheduler functions as Bézier functions, where control points naturally enforce these properties. This reduces the problem to learning an ordered set of points in the time range, while the interpretation of the points changes from ODE timesteps to Bézier control points. Across a range of pretrained diffusion and flow models, BézierFlow consistently outperforms prior timestep-learning methods, demonstrating the effectiveness of expanding the search space from discrete timesteps to Bézier-based trajectory transformations.

