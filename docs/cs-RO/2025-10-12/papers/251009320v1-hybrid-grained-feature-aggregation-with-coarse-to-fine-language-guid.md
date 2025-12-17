---
layout: default
title: Hybrid-grained Feature Aggregation with Coarse-to-fine Language Guidance for Self-supervised Monocular Depth Estimation
---

# Hybrid-grained Feature Aggregation with Coarse-to-fine Language Guidance for Self-supervised Monocular Depth Estimation

**arXiv**: [2510.09320v1](https://arxiv.org/abs/2510.09320) | [PDF](https://arxiv.org/pdf/2510.09320.pdf)

**作者**: Wenyao Zhang, Hongsi Liu, Bohan Li, Jiawei He, Zekun Qi, Yunnan Wang, Shengyang Zhao, Xinqiang Yu, Wenjun Zeng, Xin Jin

---

## 💡 一句话要点

**提出混合粒度特征聚合框架，通过粗到细语言引导解决自监督单目深度估计中语义-空间知识不足问题。**

**关键词**: `自监督单目深度估计` `混合粒度特征聚合` `语言引导学习` `CLIP模型` `DINO模型` `KITTI基准测试`

## 📋 核心要点

1. 核心问题：自监督单目深度估计中语义-空间知识提取不足，导致性能受限。
2. 方法要点：集成CLIP和DINO模型，通过对比语言引导聚合多粒度特征，并设计代理任务进行深度感知对齐。
3. 实验或效果：在KITTI基准测试中显著优于现有方法，并提升下游任务如BEV感知性能。

## 📄 摘要（原文）

> Current self-supervised monocular depth estimation (MDE) approaches encounter
> performance limitations due to insufficient semantic-spatial knowledge
> extraction. To address this challenge, we propose Hybrid-depth, a novel
> framework that systematically integrates foundation models (e.g., CLIP and
> DINO) to extract visual priors and acquire sufficient contextual information
> for MDE. Our approach introduces a coarse-to-fine progressive learning
> framework: 1) Firstly, we aggregate multi-grained features from CLIP (global
> semantics) and DINO (local spatial details) under contrastive language
> guidance. A proxy task comparing close-distant image patches is designed to
> enforce depth-aware feature alignment using text prompts; 2) Next, building on
> the coarse features, we integrate camera pose information and pixel-wise
> language alignment to refine depth predictions. This module seamlessly
> integrates with existing self-supervised MDE pipelines (e.g., Monodepth2,
> ManyDepth) as a plug-and-play depth encoder, enhancing continuous depth
> estimation. By aggregating CLIP's semantic context and DINO's spatial details
> through language guidance, our method effectively addresses feature granularity
> mismatches. Extensive experiments on the KITTI benchmark demonstrate that our
> method significantly outperforms SOTA methods across all metrics, which also
> indeed benefits downstream tasks like BEV perception. Code is available at
> https://github.com/Zhangwenyao1/Hybrid-depth.

