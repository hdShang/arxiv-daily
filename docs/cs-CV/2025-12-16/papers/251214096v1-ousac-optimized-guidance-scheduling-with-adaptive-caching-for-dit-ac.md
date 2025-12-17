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

**提出OUSAC框架，通过优化引导调度与自适应缓存加速扩散变换器，解决CFG计算开销大的问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `扩散模型加速` `无分类器引导优化` `变换器缓存` `进化算法调度` `自适应秩分配` `图像生成效率` `计算节省` `质量提升`

## 📋 核心要点

1. 核心问题：CFG虽提升扩散模型质量，但需双倍计算，现有缓存方法在可变引导下失效，导致加速与质量难以兼顾。
2. 方法要点：提出两阶段框架，先优化引导调度减少CFG步数，再自适应缓存补偿偏差，实现高效加速。
3. 实验或效果：在多个模型上显著节省计算并提升质量，如DiT-XL/2节省53%计算、质量提升15%。

## 📝 摘要（中文）

扩散模型已成为高质量图像生成的主导范式，但由于迭代去噪过程，其计算开销仍然很大。无分类器引导（CFG）显著提升了生成质量和可控性，但需要在每个时间步同时进行条件前向传播和无条件前向传播，使计算量加倍。本文提出了OUSAC（优化引导调度与自适应缓存）框架，通过系统优化加速扩散变换器（DiT）。我们的核心洞察是：可变的引导尺度可以实现稀疏计算——在某些时间步调整引导尺度可以补偿在其他时间步跳过CFG的操作，从而在保持质量的同时减少总采样步数和CFG步数。然而，可变的引导模式会引入去噪偏差，破坏标准缓存方法的有效性，因为标准方法假设CFG尺度在步间恒定。此外，在动态条件下，不同的变换器块受到的影响程度不同。本文基于这些洞察开发了一种两阶段方法。第一阶段采用进化算法联合优化跳过哪些时间步以及使用什么引导尺度，最多可消除82%的无条件前向传播。第二阶段引入自适应秩分配，为每个变换器块定制校准工作，在可变引导下保持缓存有效性。实验表明，OUSAC显著优于最先进的加速方法：在DiT-XL/2（ImageNet 512x512）上实现53%的计算节省和15%的质量提升，在PixArt-alpha（MSCOCO）上实现60%的节省和16.1%的提升，在FLUX上实现5倍加速，同时CLIP分数超过50步基线。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散变换器（DiT）中无分类器引导（CFG）带来的高计算开销问题。现有方法如标准缓存假设CFG尺度恒定，但在可变引导模式下，去噪偏差会破坏缓存有效性，导致加速与质量难以平衡，成为实际部署的瓶颈。

**核心思路**：核心思路是利用可变引导尺度实现稀疏计算，通过在某些时间步跳过CFG并用调整的尺度补偿，减少计算量。同时，针对动态条件引入自适应机制，优化缓存策略以维持质量，从而系统性地加速DiT推理。

**技术框架**：整体框架分为两阶段。第一阶段使用进化算法联合优化时间步跳过策略和引导尺度分配，最小化CFG步数；第二阶段基于自适应秩分配，为每个变换器块动态调整校准资源，确保缓存在不同引导模式下的有效性。两阶段协同工作，实现端到端加速。

**关键创新**：最重要的创新是可变引导调度与自适应缓存的结合。与现有方法（如固定调度或简单缓存）相比，本质区别在于动态优化引导模式并针对块级差异定制缓存，解决了偏差累积问题，实现了计算效率和质量的双重提升。

**关键设计**：关键设计包括：进化算法用于优化调度，目标函数平衡计算节省和质量损失；自适应秩分配基于块敏感度分析，动态分配校准秩；实验设置涵盖DiT-XL/2、PixArt-alpha等模型，使用CLIP分数等指标评估，具体参数如最多消除82%无条件前向传播。

## 📊 实验亮点

实验亮点：OUSAC在多个基准上显著优于现有加速方法。具体数据包括：在DiT-XL/2（ImageNet 512x512）上实现53%计算节省和15%质量提升；在PixArt-alpha（MSCOCO）上节省60%计算、提升16.1%质量；在FLUX上达到5倍加速，CLIP分数超过50步基线。这些结果证明了其高效性和泛化能力。

## 🎯 应用场景

该研究可应用于需要高效高质量图像生成的领域，如内容创作、游戏开发、广告设计和虚拟现实。通过加速扩散变换器，OUSAC能降低计算成本，促进实时或大规模部署，提升AI生成内容的实用性和可访问性，对推动生成式AI的产业化具有重要价值。

## 📄 摘要（原文）

> Diffusion models have emerged as the dominant paradigm for high-quality image generation, yet their computational expense remains substantial due to iterative denoising. Classifier-Free Guidance (CFG) significantly enhances generation quality and controllability but doubles the computation by requiring both conditional and unconditional forward passes at every timestep. We present OUSAC (Optimized gUidance Scheduling with Adaptive Caching), a framework that accelerates diffusion transformers (DiT) through systematic optimization. Our key insight is that variable guidance scales enable sparse computation: adjusting scales at certain timesteps can compensate for skipping CFG at others, enabling both fewer total sampling steps and fewer CFG steps while maintaining quality. However, variable guidance patterns introduce denoising deviations that undermine standard caching methods, which assume constant CFG scales across steps. Moreover, different transformer blocks are affected at different levels under dynamic conditions. This paper develops a two-stage approach leveraging these insights. Stage-1 employs evolutionary algorithms to jointly optimize which timesteps to skip and what guidance scale to use, eliminating up to 82% of unconditional passes. Stage-2 introduces adaptive rank allocation that tailors calibration efforts per transformer block, maintaining caching effectiveness under variable guidance. Experiments demonstrate that OUSAC significantly outperforms state-of-the-art acceleration methods, achieving 53% computational savings with 15% quality improvement on DiT-XL/2 (ImageNet 512x512), 60% savings with 16.1% improvement on PixArt-alpha (MSCOCO), and 5x speedup on FLUX while improving CLIP Score over the 50-step baseline.

