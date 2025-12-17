---
layout: default
title: Direction-aware multi-scale gradient loss for infrared and visible image fusion
---

# Direction-aware multi-scale gradient loss for infrared and visible image fusion

**arXiv**: [2510.13067v1](https://arxiv.org/abs/2510.13067) | [PDF](https://arxiv.org/pdf/2510.13067.pdf)

**作者**: Kaixuan Yang, Wei Xiang, Zhenshuai Chen, Tong Jin, Yunpeng Liu

---

## 💡 一句话要点

**提出方向感知多尺度梯度损失以提升红外与可见光图像融合的边缘保真度**

**关键词**: `图像融合` `梯度损失` `方向感知` `多尺度监督` `边缘保真`

## 📋 核心要点

1. 核心问题：现有方法将梯度压缩为幅值，丢失方向信息，导致边缘模糊和纹理损失。
2. 方法要点：引入方向感知多尺度梯度损失，分别监督水平和垂直梯度分量并保留符号。
3. 实验或效果：在开源模型和多个基准测试中验证，能提升边缘清晰度和纹理丰富度。

## 📄 摘要（原文）

> Infrared and visible image fusion aims to integrate complementary information
> from co-registered source images to produce a single, informative result. Most
> learning-based approaches train with a combination of structural similarity
> loss, intensity reconstruction loss, and a gradient-magnitude term. However,
> collapsing gradients to their magnitude removes directional information,
> yielding ambiguous supervision and suboptimal edge fidelity. We introduce a
> direction-aware, multi-scale gradient loss that supervises horizontal and
> vertical components separately and preserves their sign across scales. This
> axis-wise, sign-preserving objective provides clear directional guidance at
> both fine and coarse resolutions, promoting sharper, better-aligned edges and
> richer texture preservation without changing model architectures or training
> protocols. Experiments on open-source model and multiple public benchmarks
> demonstrate effectiveness of our approach.

