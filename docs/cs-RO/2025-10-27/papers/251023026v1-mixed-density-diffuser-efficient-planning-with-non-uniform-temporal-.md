---
layout: default
title: Mixed Density Diffuser: Efficient Planning with Non-uniform Temporal Resolution
---

# Mixed Density Diffuser: Efficient Planning with Non-uniform Temporal Resolution

**arXiv**: [2510.23026v1](https://arxiv.org/abs/2510.23026) | [PDF](https://arxiv.org/pdf/2510.23026.pdf)

**作者**: Crimson Stambaugh, Rajesh P. N. Rao

---

## 💡 一句话要点

**提出混合密度扩散器以在规划任务中实现非均匀时间分辨率**

**关键词**: `扩散规划` `非均匀时间分辨率` `轨迹优化` `强化学习` `D4RL基准`

## 📋 核心要点

1. 核心问题：扩散规划中均匀稀疏步长预测可能导致性能下降
2. 方法要点：引入可调超参数控制轨迹不同部分的时间密度
3. 实验或效果：在Maze2D等D4RL任务中达到新SOTA性能

## 📄 摘要（原文）

> Recent studies demonstrate that diffusion planners benefit from sparse-step
> planning over single-step planning. Training models to skip steps in their
> trajectories helps capture long-term dependencies without additional or memory
> computational cost. However, predicting excessively sparse plans degrades
> performance. We hypothesize this temporal density threshold is non-uniform
> across a temporal horizon and that certain parts of a planned trajectory should
> be more densely planned. We propose Mixed Density Diffuser (MDD), a diffusion
> planner where the densities throughout the horizon are tunable hyperparameters.
> MDD achieves a new SOTA across the Maze2D, Franka Kitchen, and Antmaze D4RL
> task domains.

