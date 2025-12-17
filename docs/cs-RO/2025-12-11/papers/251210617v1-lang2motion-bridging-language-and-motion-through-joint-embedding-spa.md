---
layout: default
title: Lang2Motion: Bridging Language and Motion through Joint Embedding Spaces
---

# Lang2Motion: Bridging Language and Motion through Joint Embedding Spaces

**arXiv**: [2512.10617v1](https://arxiv.org/abs/2512.10617) | [PDF](https://arxiv.org/pdf/2512.10617.pdf)

**作者**: Bishoy Galoaa, Xiangyu Bai, Sarah Ostadabbas

---

## 💡 一句话要点

**提出Lang2Motion框架，通过联合嵌入空间对齐运动流形，实现语言引导的任意物体点轨迹生成。**

**关键词**: `语言引导运动生成` `点轨迹生成` `联合嵌入空间` `CLIP对齐` `Transformer自编码器` `运动域迁移`

## 📋 核心要点

1. 核心问题：现有方法多关注人体运动或视频合成，缺乏从语言生成任意物体显式轨迹的能力。
2. 方法要点：基于Transformer的自编码器，通过CLIP编码器对文本描述和轨迹可视化进行双重监督，学习轨迹表示。
3. 实验或效果：在文本到轨迹检索中Recall@1达34.2%，优于视频方法12.5点；运动精度提升33-52%，支持风格迁移和语义插值。

## 📄 摘要（原文）

> We present Lang2Motion, a framework for language-guided point trajectory generation by aligning motion manifolds with joint embedding spaces. Unlike prior work focusing on human motion or video synthesis, we generate explicit trajectories for arbitrary objects using motion extracted from real-world videos via point tracking. Our transformer-based auto-encoder learns trajectory representations through dual supervision: textual motion descriptions and rendered trajectory visualizations, both mapped through CLIP's frozen encoders. Lang2Motion achieves 34.2% Recall@1 on text-to-trajectory retrieval, outperforming video-based methods by 12.5 points, and improves motion accuracy by 33-52% (12.4 ADE vs 18.3-25.3) compared to video generation baselines. We demonstrate 88.3% Top-1 accuracy on human action recognition despite training only on diverse object motions, showing effective transfer across motion domains. Lang2Motion supports style transfer, semantic interpolation, and latent-space editing through CLIP-aligned trajectory representations.

