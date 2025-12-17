---
layout: default
title: InfinityStar: Unified Spacetime AutoRegressive Modeling for Visual Generation
---

# InfinityStar: Unified Spacetime AutoRegressive Modeling for Visual Generation

**arXiv**: [2511.04675v1](https://arxiv.org/abs/2511.04675) | [PDF](https://arxiv.org/pdf/2511.04675.pdf)

**作者**: Jinlai Liu, Jian Han, Bin Yan, Hui Wu, Fengda Zhu, Xing Wang, Yi Jiang, Bingyue Peng, Zehuan Yuan

---

## 💡 一句话要点

**提出InfinityStar统一时空自回归框架，用于高效高分辨率图像和视频生成**

**关键词**: `时空自回归建模` `高分辨率视频生成` `统一视觉生成框架` `离散自回归方法` `高效视频合成`

## 📋 核心要点

1. 核心问题：如何统一建模空间和时间依赖以支持多种视觉生成任务
2. 方法要点：采用纯离散自回归方法，联合捕获时空依赖，支持文本到图像/视频等任务
3. 实验或效果：在VBench得分83.74，生成720p视频速度比扩散方法快约10倍

## 📄 摘要（原文）

> We introduce InfinityStar, a unified spacetime autoregressive framework for
> high-resolution image and dynamic video synthesis. Building on the recent
> success of autoregressive modeling in both vision and language, our purely
> discrete approach jointly captures spatial and temporal dependencies within a
> single architecture. This unified design naturally supports a variety of
> generation tasks such as text-to-image, text-to-video, image-to-video, and long
> interactive video synthesis via straightforward temporal autoregression.
> Extensive experiments demonstrate that InfinityStar scores 83.74 on VBench,
> outperforming all autoregressive models by large margins, even surpassing some
> diffusion competitors like HunyuanVideo. Without extra optimizations, our model
> generates a 5s, 720p video approximately 10x faster than leading
> diffusion-based methods. To our knowledge, InfinityStar is the first discrete
> autoregressive video generator capable of producing industrial level 720p
> videos. We release all code and models to foster further research in efficient,
> high-quality video generation.

