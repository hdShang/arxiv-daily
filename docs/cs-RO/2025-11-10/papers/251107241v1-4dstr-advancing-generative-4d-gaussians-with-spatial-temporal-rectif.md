---
layout: default
title: 4DSTR: Advancing Generative 4D Gaussians with Spatial-Temporal Rectification for High-Quality and Consistent 4D Generation
---

# 4DSTR: Advancing Generative 4D Gaussians with Spatial-Temporal Rectification for High-Quality and Consistent 4D Generation

**arXiv**: [2511.07241v1](https://arxiv.org/abs/2511.07241) | [PDF](https://arxiv.org/pdf/2511.07241.pdf)

**作者**: Mengmeng Liu, Jiuming Liu, Yunpeng Zhang, Jiangtao Li, Michael Ying Yang, Francesco Nex, Hao Cheng

---

## 💡 一句话要点

**提出4DSTR网络，通过时空校正解决4D生成中的一致性和快速变化适应问题。**

**关键词**: `4D生成` `高斯泼溅` `时空一致性` `视频到4D生成` `自适应密度策略`

## 📋 核心要点

1. 核心问题：现有4D生成方法缺乏有效时空建模，导致时空一致性差和快速变化适应不良。
2. 方法要点：引入时空校正机制，调制生成4D高斯泼溅，确保变形尺度和旋转的时序一致性。
3. 实验效果：在视频到4D生成中实现SOTA，提升重建质量、时空一致性和快速运动适应性。

## 📄 摘要（原文）

> Remarkable advances in recent 2D image and 3D shape generation have induced a
> significant focus on dynamic 4D content generation. However, previous 4D
> generation methods commonly struggle to maintain spatial-temporal consistency
> and adapt poorly to rapid temporal variations, due to the lack of effective
> spatial-temporal modeling. To address these problems, we propose a novel 4D
> generation network called 4DSTR, which modulates generative 4D Gaussian
> Splatting with spatial-temporal rectification. Specifically, temporal
> correlation across generated 4D sequences is designed to rectify deformable
> scales and rotations and guarantee temporal consistency. Furthermore, an
> adaptive spatial densification and pruning strategy is proposed to address
> significant temporal variations by dynamically adding or deleting Gaussian
> points with the awareness of their pre-frame movements. Extensive experiments
> demonstrate that our 4DSTR achieves state-of-the-art performance in video-to-4D
> generation, excelling in reconstruction quality, spatial-temporal consistency,
> and adaptation to rapid temporal movements.

