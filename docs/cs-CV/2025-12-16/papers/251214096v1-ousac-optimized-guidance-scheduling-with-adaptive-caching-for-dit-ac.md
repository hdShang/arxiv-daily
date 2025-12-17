---
layout: default
title: OUSAC: Optimized Guidance Scheduling with Adaptive Caching for DiT Acceleration
---

# OUSAC: Optimized Guidance Scheduling with Adaptive Caching for DiT Acceleration

**arXiv**: [2512.14096v1](https://arxiv.org/abs/2512.14096) | [PDF](https://arxiv.org/pdf/2512.14096.pdf)

**作者**: Ruitong Sun, Tianze Yang, Wei Niu, Jin Sun

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 29 pages

---

## 💡 一句话要点

**提出OUSAC框架以解决扩散模型中无分类器引导计算开销大的问题，通过优化引导调度与自适应缓存实现高效加速。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `扩散模型加速` `无分类器引导优化` `稀疏计算调度` `自适应缓存` `扩散变换器` `进化算法` `图像生成效率` `计算节省`

## 📋 核心要点

1. 扩散模型中无分类器引导（CFG）虽提升质量，但需在每个时间步执行两次前向传播，计算开销加倍，成为加速瓶颈。
2. 提出OUSAC框架，通过可变引导尺度实现稀疏计算，结合进化算法优化调度和自适应缓存，减少CFG步数并保持质量。
3. 实验显示OUSAC在多个模型上显著节省计算并提升质量，如DiT-XL/2节省53%计算且质量提升15%，优于现有方法。

## 📝 摘要（中文）

扩散模型已成为高质量图像生成的主导范式，但其迭代去噪过程计算开销巨大。无分类器引导（CFG）显著提升了生成质量和可控性，但需要在每个时间步同时执行条件前向传播和无条件前向传播，导致计算量加倍。本文提出了OUSAC（优化引导调度与自适应缓存）框架，通过系统优化加速扩散变换器（DiT）。我们的核心洞察是：可变的引导尺度可以实现稀疏计算——在某些时间步调整引导尺度可以补偿在其他时间步跳过CFG的操作，从而在保持质量的同时减少总采样步数和CFG步数。然而，可变引导模式会引入去噪偏差，破坏标准缓存方法的有效性（这些方法假设CFG尺度在步间恒定）。此外，在动态条件下，不同的变换器块受到的影响程度不同。本文基于这些洞察开发了一种两阶段方法。第一阶段采用进化算法联合优化跳过哪些时间步以及使用何种引导尺度，最多可消除82%的无条件前向传播。第二阶段引入自适应秩分配，针对每个变换器块定制校准工作，在可变引导下保持缓存有效性。实验表明，OUSAC显著优于最先进的加速方法：在DiT-XL/2（ImageNet 512x512）上实现53%的计算节省和15%的质量提升，在PixArt-alpha（MSCOCO）上实现60%的节省和16.1%的提升，在FLUX上实现5倍加速且CLIP分数超过50步基线。

## 🔬 方法详解

OUSAC框架采用两阶段方法。整体框架包括：第一阶段使用进化算法联合优化时间步跳过策略和引导尺度，实现稀疏计算，最多减少82%无条件前向传播；第二阶段引入自适应秩分配，针对扩散变换器中不同块在动态引导下的敏感性差异，定制化校准缓存，以应对可变引导导致的去噪偏差。关键技术创新点在于可变引导尺度的调度优化和自适应缓存机制，与现有方法的主要区别在于：传统方法假设恒定CFG尺度，而OUSAC允许尺度变化，并通过系统优化和自适应设计维持缓存有效性，从而在减少计算的同时保持或提升生成质量。

## 📊 实验亮点

OUSAC在多个基准测试中表现优异：DiT-XL/2上节省53%计算且质量提升15%，PixArt-alpha上节省60%计算且提升16.1%，FLUX上实现5倍加速并超越基线CLIP分数，显著优于现有加速方法。

## 🎯 应用场景

该研究可应用于需要高效高质量图像生成的领域，如创意设计、媒体内容制作、游戏开发和虚拟现实，通过加速扩散模型降低计算成本，提升实时性和可扩展性，具有实际工业价值。

## 📄 摘要（原文）

> Diffusion models have emerged as the dominant paradigm for high-quality image generation, yet their computational expense remains substantial due to iterative denoising. Classifier-Free Guidance (CFG) significantly enhances generation quality and controllability but doubles the computation by requiring both conditional and unconditional forward passes at every timestep. We present OUSAC (Optimized gUidance Scheduling with Adaptive Caching), a framework that accelerates diffusion transformers (DiT) through systematic optimization. Our key insight is that variable guidance scales enable sparse computation: adjusting scales at certain timesteps can compensate for skipping CFG at others, enabling both fewer total sampling steps and fewer CFG steps while maintaining quality. However, variable guidance patterns introduce denoising deviations that undermine standard caching methods, which assume constant CFG scales across steps. Moreover, different transformer blocks are affected at different levels under dynamic conditions. This paper develops a two-stage approach leveraging these insights. Stage-1 employs evolutionary algorithms to jointly optimize which timesteps to skip and what guidance scale to use, eliminating up to 82% of unconditional passes. Stage-2 introduces adaptive rank allocation that tailors calibration efforts per transformer block, maintaining caching effectiveness under variable guidance. Experiments demonstrate that OUSAC significantly outperforms state-of-the-art acceleration methods, achieving 53% computational savings with 15% quality improvement on DiT-XL/2 (ImageNet 512x512), 60% savings with 16.1% improvement on PixArt-alpha (MSCOCO), and 5x speedup on FLUX while improving CLIP Score over the 50-step baseline.

