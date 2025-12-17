---
layout: default
title: Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling
---

# Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling

**arXiv**: [2510.17171v1](https://arxiv.org/abs/2510.17171) | [PDF](https://arxiv.org/pdf/2510.17171.pdf)

**作者**: Feihong Yan, Peiru Wang, Yao Zhu, Kaiyu Pang, Qingyan Wei, Huiqi Li, Linfeng Zhang

---

## 💡 一句话要点

**提出GtR两阶段采样方法以加速掩码自回归模型，保持生成质量**

**关键词**: `掩码自回归模型` `两阶段采样` `视觉生成加速` `频率分析` `训练无关方法`

## 📋 核心要点

1. 掩码自回归模型并行生成潜力受限于空间相关视觉令牌建模复杂度
2. GtR分结构生成与细节重建两阶段，结合频率加权令牌选择优化计算分配
3. 实验显示在ImageNet等任务上实现3.72倍加速，质量与原始模型相当

## 📄 摘要（原文）

> Masked Autoregressive (MAR) models promise better efficiency in visual
> generation than autoregressive (AR) models for the ability of parallel
> generation, yet their acceleration potential remains constrained by the
> modeling complexity of spatially correlated visual tokens in a single step. To
> address this limitation, we introduce Generation then Reconstruction (GtR), a
> training-free hierarchical sampling strategy that decomposes generation into
> two stages: structure generation establishing global semantic scaffolding,
> followed by detail reconstruction efficiently completing remaining tokens.
> Assuming that it is more difficult to create an image from scratch than to
> complement images based on a basic image framework, GtR is designed to achieve
> acceleration by computing the reconstruction stage quickly while maintaining
> the generation quality by computing the generation stage slowly. Moreover,
> observing that tokens on the details of an image often carry more semantic
> information than tokens in the salient regions, we further propose
> Frequency-Weighted Token Selection (FTS) to offer more computation budget to
> tokens on image details, which are localized based on the energy of high
> frequency information. Extensive experiments on ImageNet class-conditional and
> text-to-image generation demonstrate 3.72x speedup on MAR-H while maintaining
> comparable quality (e.g., FID: 1.59, IS: 304.4 vs. original 1.59, 299.1),
> substantially outperforming existing acceleration methods across various model
> scales and generation tasks. Our codes will be released in
> https://github.com/feihongyan1/GtR.

