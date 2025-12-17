---
layout: default
title: Diffusion differentiable resampling
---

# Diffusion differentiable resampling

**arXiv**: [2512.10401v1](https://arxiv.org/abs/2512.10401) | [PDF](https://arxiv.org/pdf/2512.10401.pdf)

**作者**: Jennifer Rosina Andersson, Zheng Zhao

---

## 💡 一句话要点

**提出基于集成分数扩散模型的路径可微重采样方法，用于序列蒙特卡洛场景。**

**关键词**: `序列蒙特卡洛` `可微重采样` `扩散模型` `粒子滤波` `参数估计`

## 📋 核心要点

1. 核心问题：序列蒙特卡洛中可微重采样方法的性能提升需求。
2. 方法要点：利用集成分数扩散模型实现即时路径可微的重采样。
3. 实验或效果：在随机滤波和参数估计中优于现有可微重采样方法。

## 📄 摘要（原文）

> This paper is concerned with differentiable resampling in the context of sequential Monte Carlo (e.g., particle filtering). We propose a new informative resampling method that is instantly pathwise differentiable, based on an ensemble score diffusion model. We prove that our diffusion resampling method provides a consistent estimate to the resampling distribution, and we show by experiments that it outperforms the state-of-the-art differentiable resampling methods when used for stochastic filtering and parameter estimation.

