---
layout: default
title: GeoDiff: Geometry-Guided Diffusion for Metric Depth Estimation
---

# GeoDiff: Geometry-Guided Diffusion for Metric Depth Estimation

**arXiv**: [2510.18291v1](https://arxiv.org/abs/2510.18291) | [PDF](https://arxiv.org/pdf/2510.18291.pdf)

**作者**: Tuan Pham, Thanh-Tung Le, Xiaohui Xie, Stephan Mandt

---

## 💡 一句话要点

**提出GeoDiff框架，结合立体视觉引导扩散模型以解决单图像度量深度估计的尺度模糊问题**

**关键词**: `度量深度估计` `扩散模型` `立体视觉` `几何约束` `无训练方法`

## 📋 核心要点

1. 核心问题：单图像深度估计存在尺度模糊，难以预测绝对度量深度
2. 方法要点：利用预训练潜在扩散模型，结合立体几何约束学习尺度和偏移
3. 实验或效果：无需训练，在室内外及复杂场景中匹配或超越现有方法

## 📄 摘要（原文）

> We introduce a novel framework for metric depth estimation that enhances
> pretrained diffusion-based monocular depth estimation (DB-MDE) models with
> stereo vision guidance. While existing DB-MDE methods excel at predicting
> relative depth, estimating absolute metric depth remains challenging due to
> scale ambiguities in single-image scenarios. To address this, we reframe depth
> estimation as an inverse problem, leveraging pretrained latent diffusion models
> (LDMs) conditioned on RGB images, combined with stereo-based geometric
> constraints, to learn scale and shift for accurate depth recovery. Our
> training-free solution seamlessly integrates into existing DB-MDE frameworks
> and generalizes across indoor, outdoor, and complex environments. Extensive
> experiments demonstrate that our approach matches or surpasses state-of-the-art
> methods, particularly in challenging scenarios involving translucent and
> specular surfaces, all without requiring retraining.

