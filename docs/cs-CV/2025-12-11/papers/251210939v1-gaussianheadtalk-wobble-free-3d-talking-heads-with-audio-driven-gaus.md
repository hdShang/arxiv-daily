---
layout: default
title: GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting
---

# GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting

**arXiv**: [2512.10939v1](https://arxiv.org/abs/2512.10939) | [PDF](https://arxiv.org/pdf/2512.10939.pdf)

**作者**: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh

---

## 💡 一句话要点

**提出基于3D Morphable Models和Transformer的Gaussian Splatting方法，以生成实时稳定的音频驱动3D说话头**

**关键词**: `3D说话头生成` `Gaussian Splatting` `音频驱动` `时间一致性` `3D Morphable Models` `Transformer预测`

## 📋 核心要点

1. 核心问题：现有方法在实时性和时间稳定性上存在不足，导致视频伪影和不稳定输出
2. 方法要点：使用3D Morphable Models映射Gaussian Splatting，结合Transformer从音频直接预测参数以驱动时间一致性
3. 实验或效果：从单目视频和独立音频输入生成实时说话头视频，在定量和定性评估中报告竞争性能

## 📄 摘要（原文）

> Speech-driven talking heads have recently emerged and enable interactive avatars. However, real-world applications are limited, as current methods achieve high visual fidelity but slow or fast yet temporally unstable. Diffusion methods provide realistic image generation, yet struggle with oneshot settings. Gaussian Splatting approaches are real-time, yet inaccuracies in facial tracking, or inconsistent Gaussian mappings, lead to unstable outputs and video artifacts that are detrimental to realistic use cases. We address this problem by mapping Gaussian Splatting using 3D Morphable Models to generate person-specific avatars. We introduce transformer-based prediction of model parameters, directly from audio, to drive temporal consistency. From monocular video and independent audio speech inputs, our method enables generation of real-time talking head videos where we report competitive quantitative and qualitative performance.

