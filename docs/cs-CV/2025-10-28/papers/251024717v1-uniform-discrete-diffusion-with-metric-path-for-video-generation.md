---
layout: default
title: Uniform Discrete Diffusion with Metric Path for Video Generation
---

# Uniform Discrete Diffusion with Metric Path for Video Generation

**arXiv**: [2510.24717v1](https://arxiv.org/abs/2510.24717) | [PDF](https://arxiv.org/pdf/2510.24717.pdf)

**作者**: Haoge Deng, Ting Pan, Fan Zhang, Yang Liu, Zhuoyan Luo, Yufeng Cui, Wenxuan Wang, Chunhua Shen, Shiguang Shan, Zhaoxiang Zhang, Xinlong Wang

---

## 💡 一句话要点

**提出URSA框架以解决离散视频生成中的误差累积和长上下文不一致问题**

**关键词**: `离散扩散模型` `视频生成` `度量路径` `时间步偏移` `异步时间微调` `高分辨率合成`

## 📋 核心要点

1. 核心问题：离散视频生成方法存在误差累积和长上下文不一致，落后于连续方法
2. 方法要点：采用线性化度量路径和分辨率相关时间步偏移机制，实现高效迭代全局优化
3. 实验或效果：在视频和图像生成基准上超越现有离散方法，性能接近最先进连续扩散方法

## 📄 摘要（原文）

> Continuous-space video generation has advanced rapidly, while discrete
> approaches lag behind due to error accumulation and long-context inconsistency.
> In this work, we revisit discrete generative modeling and present Uniform
> discRete diffuSion with metric pAth (URSA), a simple yet powerful framework
> that bridges the gap with continuous approaches for the scalable video
> generation. At its core, URSA formulates the video generation task as an
> iterative global refinement of discrete spatiotemporal tokens. It integrates
> two key designs: a Linearized Metric Path and a Resolution-dependent Timestep
> Shifting mechanism. These designs enable URSA to scale efficiently to
> high-resolution image synthesis and long-duration video generation, while
> requiring significantly fewer inference steps. Additionally, we introduce an
> asynchronous temporal fine-tuning strategy that unifies versatile tasks within
> a single model, including interpolation and image-to-video generation.
> Extensive experiments on challenging video and image generation benchmarks
> demonstrate that URSA consistently outperforms existing discrete methods and
> achieves performance comparable to state-of-the-art continuous diffusion
> methods. Code and models are available at https://github.com/baaivision/URSA

