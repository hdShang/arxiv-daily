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

**OUSAC：通过自适应缓存优化指导调度，加速扩散Transformer模型DiT**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)** **动作生成与物理动画 (Animation & Physics)**

**关键词**: `扩散模型` `图像生成` `模型加速` `无分类器指导` `自适应缓存`

## 📋 核心要点

1. 扩散模型计算开销大，无分类器指导(CFG)虽能提升质量，但计算量翻倍，成为加速瓶颈。
2. OUSAC通过优化指导调度，利用可变指导尺度实现稀疏计算，减少CFG步骤，同时保持生成质量。
3. OUSAC在DiT-XL/2、PixArt-alpha和FLUX上均取得显著加速和质量提升，优于现有加速方法。

## 📝 摘要（中文）

扩散模型已成为高质量图像生成的主流范式，但由于迭代去噪，其计算成本仍然很高。无分类器指导（CFG）通过在每个时间步需要条件和无条件前向传递，显著提高生成质量和可控性，但也使计算量翻倍。我们提出了OUSAC（Optimized gUidance Scheduling with Adaptive Caching），一个通过系统优化加速扩散Transformer（DiT）的框架。我们的关键见解是，可变的指导尺度能够实现稀疏计算：在某些时间步调整尺度可以补偿在其他时间步跳过CFG，从而在保持质量的同时减少总采样步数和CFG步数。然而，可变的指导模式会引入去噪偏差，破坏了标准缓存方法，因为标准缓存方法假设跨步骤的CFG尺度不变。此外，不同的Transformer块在动态条件下受到不同程度的影响。本文开发了一种利用这些见解的两阶段方法。第一阶段采用进化算法来联合优化跳过哪些时间步以及使用什么指导尺度，最多可消除82%的无条件传递。第二阶段引入自适应秩分配，为每个Transformer块定制校准工作，从而在可变指导下保持缓存有效性。实验表明，OUSAC显著优于最先进的加速方法，在DiT-XL/2（ImageNet 512x512）上实现了53%的计算节省和15%的质量提升，在PixArt-alpha（MSCOCO）上实现了60%的节省和16.1%的提升，在FLUX上实现了5倍的加速，同时提高了CLIP Score，超过了50步的基线。

## 🔬 方法详解

**问题定义**：扩散模型，特别是DiT，在图像生成领域表现出色，但其计算复杂度高，限制了应用。无分类器指导(CFG)虽然能提高生成质量，但需要同时进行条件和无条件的前向传播，导致计算量加倍。现有加速方法难以在保证生成质量的前提下，有效减少CFG带来的计算负担。

**核心思路**：论文的核心思路是利用可变的指导尺度来实现稀疏计算。通过在某些时间步调整指导尺度，可以补偿在其他时间步跳过CFG带来的影响，从而在减少总采样步数和CFG步骤的同时，维持甚至提升生成质量。这种方法的核心在于找到最优的指导尺度调度方案。

**技术框架**：OUSAC框架包含两个主要阶段：1. 指导调度优化：使用进化算法联合优化需要跳过CFG的时间步以及对应的指导尺度。目标是在减少计算量的同时，保持生成质量。2. 自适应缓存：针对不同Transformer块在动态指导条件下受到的不同影响，引入自适应秩分配，为每个块定制校准工作，以保持缓存的有效性。

**关键创新**：OUSAC的关键创新在于：1. 提出了可变指导尺度的概念，并利用进化算法自动搜索最优的调度方案。2. 针对可变指导尺度下的缓存失效问题，提出了自适应秩分配方法，能够根据不同Transformer块的特性进行校准，保证缓存的有效性。这与传统缓存方法假设CFG尺度不变有本质区别。

**关键设计**：在指导调度优化阶段，使用进化算法搜索最优的跳过CFG的时间步和对应的指导尺度。进化算法的目标函数需要综合考虑生成质量（如FID、CLIP Score）和计算量。在自适应缓存阶段，根据每个Transformer块的激活值变化情况，动态调整缓存的秩分配，以更好地捕捉可变指导尺度下的特征变化。

## 📊 实验亮点

OUSAC在DiT-XL/2 (ImageNet 512x512)上实现了53%的计算节省和15%的质量提升，在PixArt-alpha (MSCOCO)上实现了60%的节省和16.1%的提升，在FLUX上实现了5倍的加速，同时提高了CLIP Score，超过了50步的基线。这些结果表明OUSAC显著优于现有的加速方法。

## 🎯 应用场景

OUSAC可应用于各种基于扩散模型的图像生成任务，尤其适用于对计算资源有限制或对生成速度有较高要求的场景。例如，移动设备上的图像生成、实时图像编辑、以及大规模图像数据集的生成等。该研究有望推动扩散模型在更广泛领域的应用。

## 📄 摘要（原文）

> Diffusion models have emerged as the dominant paradigm for high-quality image generation, yet their computational expense remains substantial due to iterative denoising. Classifier-Free Guidance (CFG) significantly enhances generation quality and controllability but doubles the computation by requiring both conditional and unconditional forward passes at every timestep. We present OUSAC (Optimized gUidance Scheduling with Adaptive Caching), a framework that accelerates diffusion transformers (DiT) through systematic optimization. Our key insight is that variable guidance scales enable sparse computation: adjusting scales at certain timesteps can compensate for skipping CFG at others, enabling both fewer total sampling steps and fewer CFG steps while maintaining quality. However, variable guidance patterns introduce denoising deviations that undermine standard caching methods, which assume constant CFG scales across steps. Moreover, different transformer blocks are affected at different levels under dynamic conditions. This paper develops a two-stage approach leveraging these insights. Stage-1 employs evolutionary algorithms to jointly optimize which timesteps to skip and what guidance scale to use, eliminating up to 82% of unconditional passes. Stage-2 introduces adaptive rank allocation that tailors calibration efforts per transformer block, maintaining caching effectiveness under variable guidance. Experiments demonstrate that OUSAC significantly outperforms state-of-the-art acceleration methods, achieving 53% computational savings with 15% quality improvement on DiT-XL/2 (ImageNet 512x512), 60% savings with 16.1% improvement on PixArt-alpha (MSCOCO), and 5x speedup on FLUX while improving CLIP Score over the 50-step baseline.

