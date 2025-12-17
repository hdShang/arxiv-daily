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

**关键词**: `扩散模型加速` `无分类器引导优化` `稀疏计算` `自适应缓存` `进化算法调度` `变换器块校准` `图像生成效率` `计算节省`

## 📋 核心要点

1. 核心问题：CFG虽提升扩散模型质量，但需双倍计算，且现有缓存方法在可变引导下失效，阻碍高效加速。
2. 方法要点：提出两阶段框架，先优化引导调度减少CFG步数，再自适应缓存补偿偏差，实现稀疏计算。
3. 实验或效果：在多个DiT模型上显著节省计算并提升质量，如DiT-XL/2节省53%计算且质量提升15%。

## 📝 摘要（中文）

扩散模型已成为高质量图像生成的主导范式，但其迭代去噪过程计算开销巨大。无分类器引导（CFG）显著提升了生成质量和可控性，但需要在每个时间步同时执行条件前向传播和无条件前向传播，导致计算量加倍。本文提出了OUSAC（优化引导调度与自适应缓存）框架，通过系统优化加速扩散变换器（DiT）。核心洞见是：可变的引导尺度能够实现稀疏计算——在某些时间步调整引导尺度可以补偿在其他时间步跳过CFG的操作，从而在保持质量的同时减少总采样步数和CFG步数。然而，可变的引导模式会引入去噪偏差，破坏标准缓存方法的有效性（这些方法假设CFG尺度在步间恒定）。此外，在动态条件下，不同的变换器块受到的影响程度不同。本文基于这些洞见开发了一种两阶段方法：第一阶段使用进化算法联合优化跳过哪些时间步以及使用何种引导尺度，最多可消除82%的无条件前向传播；第二阶段引入自适应秩分配，针对每个变换器块定制校准工作，在可变引导下保持缓存有效性。实验表明，OUSAC显著优于最先进的加速方法，在DiT-XL/2（ImageNet 512x512）上实现了53%的计算节省和15%的质量提升，在PixArt-alpha（MSCOCO）上实现了60%的节省和16.1%的提升，在FLUX上实现了5倍加速，同时CLIP分数超过50步基线。

## 🔬 方法详解

OUSAC是一个两阶段框架，旨在加速扩散变换器（DiT）。整体框架包括：第一阶段使用进化算法联合优化时间步跳过策略和引导尺度，实现稀疏计算，最多可消除82%的无条件前向传播；第二阶段引入自适应秩分配，根据动态引导条件为每个变换器块定制校准秩，以维持缓存有效性。关键技术创新点在于利用可变引导尺度补偿跳过CFG的偏差，以及自适应缓存机制应对不同块的异质性影响。与现有方法的主要区别在于：现有方法通常假设恒定CFG尺度或采用固定缓存策略，而OUSAC通过系统优化和自适应设计，在可变引导下实现更高效的加速，同时保持或提升生成质量。

## 📊 实验亮点

OUSAC在多个基准测试中表现优异：DiT-XL/2上节省53%计算且FID提升15%，PixArt-alpha上节省60%计算且质量提升16.1%，FLUX上实现5倍加速并超越基线CLIP分数，显著优于现有加速方法。

## 🎯 应用场景

该研究可应用于需要高效高质量图像生成的领域，如内容创作、游戏开发、广告设计和虚拟现实，通过减少扩散模型的计算开销，降低部署成本并提升实时性，具有实际商业价值。

## 📄 摘要（原文）

> Diffusion models have emerged as the dominant paradigm for high-quality image generation, yet their computational expense remains substantial due to iterative denoising. Classifier-Free Guidance (CFG) significantly enhances generation quality and controllability but doubles the computation by requiring both conditional and unconditional forward passes at every timestep. We present OUSAC (Optimized gUidance Scheduling with Adaptive Caching), a framework that accelerates diffusion transformers (DiT) through systematic optimization. Our key insight is that variable guidance scales enable sparse computation: adjusting scales at certain timesteps can compensate for skipping CFG at others, enabling both fewer total sampling steps and fewer CFG steps while maintaining quality. However, variable guidance patterns introduce denoising deviations that undermine standard caching methods, which assume constant CFG scales across steps. Moreover, different transformer blocks are affected at different levels under dynamic conditions. This paper develops a two-stage approach leveraging these insights. Stage-1 employs evolutionary algorithms to jointly optimize which timesteps to skip and what guidance scale to use, eliminating up to 82% of unconditional passes. Stage-2 introduces adaptive rank allocation that tailors calibration efforts per transformer block, maintaining caching effectiveness under variable guidance. Experiments demonstrate that OUSAC significantly outperforms state-of-the-art acceleration methods, achieving 53% computational savings with 15% quality improvement on DiT-XL/2 (ImageNet 512x512), 60% savings with 16.1% improvement on PixArt-alpha (MSCOCO), and 5x speedup on FLUX while improving CLIP Score over the 50-step baseline.

