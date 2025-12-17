---
layout: default
title: Video Prediction of Dynamic Physical Simulations With Pixel-Space Spatiotemporal Transformers
---

# Video Prediction of Dynamic Physical Simulations With Pixel-Space Spatiotemporal Transformers

**arXiv**: [2510.20807v1](https://arxiv.org/abs/2510.20807) | [PDF](https://arxiv.org/pdf/2510.20807.pdf)

**作者**: Dean L Slack, G Thomas Hudson, Thomas Winterbottom, Noura Al Moubayed

---

## 💡 一句话要点

**提出像素空间时空Transformer模型，以提升动态物理模拟视频预测的长期准确性。**

**关键词**: `视频预测` `时空Transformer` `物理模拟` `自注意力机制` `像素空间表示` `可解释性分析`

## 📋 核心要点

1. 核心问题：现有视频生成方法在物理模拟的因果建模上存在不足，难以实现长期准确预测。
2. 方法要点：采用简单端到端Transformer架构，比较不同时空自注意力布局，无需复杂训练策略。
3. 实验或效果：相比潜在空间方法，物理准确预测时间延长达50%，并保持视频质量指标可比性。

## 📄 摘要（原文）

> Inspired by the performance and scalability of autoregressive large language
> models (LLMs), transformer-based models have seen recent success in the visual
> domain. This study investigates a transformer adaptation for video prediction
> with a simple end-to-end approach, comparing various spatiotemporal
> self-attention layouts. Focusing on causal modeling of physical simulations
> over time; a common shortcoming of existing video-generative approaches, we
> attempt to isolate spatiotemporal reasoning via physical object tracking
> metrics and unsupervised training on physical simulation datasets. We introduce
> a simple yet effective pure transformer model for autoregressive video
> prediction, utilizing continuous pixel-space representations for video
> prediction. Without the need for complex training strategies or latent
> feature-learning components, our approach significantly extends the time
> horizon for physically accurate predictions by up to 50% when compared with
> existing latent-space approaches, while maintaining comparable performance on
> common video quality metrics. In addition, we conduct interpretability
> experiments to identify network regions that encode information useful to
> perform accurate estimations of PDE simulation parameters via probing models,
> and find that this generalizes to the estimation of out-of-distribution
> simulation parameters. This work serves as a platform for further
> attention-based spatiotemporal modeling of videos via a simple, parameter
> efficient, and interpretable approach.

