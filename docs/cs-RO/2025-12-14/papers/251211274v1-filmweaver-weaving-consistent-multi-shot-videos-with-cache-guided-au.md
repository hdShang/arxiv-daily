---
layout: default
title: FilmWeaver: Weaving Consistent Multi-Shot Videos with Cache-Guided Autoregressive Diffusion
---

# FilmWeaver: Weaving Consistent Multi-Shot Videos with Cache-Guided Autoregressive Diffusion

**arXiv**: [2512.11274v1](https://arxiv.org/abs/2512.11274) | [PDF](https://arxiv.org/pdf/2512.11274.pdf)

**作者**: Xiangyang Luo, Qingyu Li, Xiaokun Liu, Wenyu Qin, Miao Yang, Meng Wang, Pengfei Wan, Di Zhang, Kun Gai, Shao-Lun Huang

---

## 💡 一句话要点

**提出FilmWeaver框架，通过缓存引导的自回归扩散生成一致的多镜头视频**

**关键词**: `多镜头视频生成` `一致性保持` `自回归扩散模型` `缓存机制` `视频数据集构建`

## 📋 核心要点

1. 核心问题：现有视频生成模型难以保持多镜头视频中角色和背景的一致性，且无法灵活生成长度和镜头数任意的视频。
2. 方法要点：采用自回归扩散范式实现任意长度生成，通过双级缓存机制（镜头记忆和时序记忆）解耦镜头间一致性和镜头内连贯性。
3. 实验或效果：在一致性和美学质量指标上超越现有方法，支持多概念注入和视频扩展等下游任务，并构建了高质量多镜头视频数据集。

## 📄 摘要（原文）

> Current video generation models perform well at single-shot synthesis but struggle with multi-shot videos, facing critical challenges in maintaining character and background consistency across shots and flexibly generating videos of arbitrary length and shot count. To address these limitations, we introduce \textbf{FilmWeaver}, a novel framework designed to generate consistent, multi-shot videos of arbitrary length. First, it employs an autoregressive diffusion paradigm to achieve arbitrary-length video generation. To address the challenge of consistency, our key insight is to decouple the problem into inter-shot consistency and intra-shot coherence. We achieve this through a dual-level cache mechanism: a shot memory caches keyframes from preceding shots to maintain character and scene identity, while a temporal memory retains a history of frames from the current shot to ensure smooth, continuous motion. The proposed framework allows for flexible, multi-round user interaction to create multi-shot videos. Furthermore, due to this decoupled design, our method demonstrates high versatility by supporting downstream tasks such as multi-concept injection and video extension. To facilitate the training of our consistency-aware method, we also developed a comprehensive pipeline to construct a high-quality multi-shot video dataset. Extensive experimental results demonstrate that our method surpasses existing approaches on metrics for both consistency and aesthetic quality, opening up new possibilities for creating more consistent, controllable, and narrative-driven video content. Project Page: https://filmweaver.github.io

