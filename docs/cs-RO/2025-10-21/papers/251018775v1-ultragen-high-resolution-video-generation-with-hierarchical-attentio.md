---
layout: default
title: UltraGen: High-Resolution Video Generation with Hierarchical Attention
---

# UltraGen: High-Resolution Video Generation with Hierarchical Attention

**arXiv**: [2510.18775v1](https://arxiv.org/abs/2510.18775) | [PDF](https://arxiv.org/pdf/2510.18775.pdf)

**作者**: Teng Hu, Jiangning Zhang, Zihan Su, Ran Yi

---

## 💡 一句话要点

**提出UltraGen框架以解决高分辨率视频生成的计算瓶颈**

**关键词**: `视频生成` `高分辨率合成` `注意力机制` `计算效率优化` `扩散变换器`

## 📋 核心要点

1. 现有扩散变换器模型因注意力机制计算复杂度高，难以生成高分辨率视频
2. 采用分层双分支注意力架构，分解为全局和局部注意力以提升效率
3. 实验显示UltraGen可扩展至1080P和4K，优于现有方法及两阶段流程

## 📄 摘要（原文）

> Recent advances in video generation have made it possible to produce visually
> compelling videos, with wide-ranging applications in content creation,
> entertainment, and virtual reality. However, most existing diffusion
> transformer based video generation models are limited to low-resolution outputs
> (<=720P) due to the quadratic computational complexity of the attention
> mechanism with respect to the output width and height. This computational
> bottleneck makes native high-resolution video generation (1080P/2K/4K)
> impractical for both training and inference. To address this challenge, we
> present UltraGen, a novel video generation framework that enables i) efficient
> and ii) end-to-end native high-resolution video synthesis. Specifically,
> UltraGen features a hierarchical dual-branch attention architecture based on
> global-local attention decomposition, which decouples full attention into a
> local attention branch for high-fidelity regional content and a global
> attention branch for overall semantic consistency. We further propose a
> spatially compressed global modeling strategy to efficiently learn global
> dependencies, and a hierarchical cross-window local attention mechanism to
> reduce computational costs while enhancing information flow across different
> local windows. Extensive experiments demonstrate that UltraGen can effectively
> scale pre-trained low-resolution video models to 1080P and even 4K resolution
> for the first time, outperforming existing state-of-the-art methods and
> super-resolution based two-stage pipelines in both qualitative and quantitative
> evaluations.

