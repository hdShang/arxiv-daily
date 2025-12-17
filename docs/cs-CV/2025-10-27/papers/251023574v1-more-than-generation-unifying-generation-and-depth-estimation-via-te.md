---
layout: default
title: More Than Generation: Unifying Generation and Depth Estimation via Text-to-Image Diffusion Models
---

# More Than Generation: Unifying Generation and Depth Estimation via Text-to-Image Diffusion Models

**arXiv**: [2510.23574v1](https://arxiv.org/abs/2510.23574) | [PDF](https://arxiv.org/pdf/2510.23574.pdf)

**作者**: Hongkai Lin, Dingkang Liang, Mingyang Du, Xin Zhou, Xiang Bai

---

## 💡 一句话要点

**提出MERGE模型，统一图像生成与深度估计，基于预训练扩散模型**

**关键词**: `文本到图像扩散模型` `深度估计` `统一模型` `零样本能力` `参数重用`

## 📋 核心要点

1. 问题：训练参数更新导致预训练模型图像生成能力退化
2. 方法：采用即插即用框架和组重用机制，实现模式切换与参数高效利用
3. 效果：在多个深度估计基准上达到最优，保持原始图像生成能力

## 📄 摘要（原文）

> Generative depth estimation methods leverage the rich visual priors stored in
> pre-trained text-to-image diffusion models, demonstrating astonishing zero-shot
> capability. However, parameter updates during training lead to catastrophic
> degra- dation in the image generation capability of the pre-trained model. We
> introduce MERGE, a unified model for image generation and depth estimation,
> starting from a fixed pre-trained text-to-image model. MERGE demonstrates that
> the pre-trained text-to-image model can do more than image generation, but also
> expand to depth estimation effortlessly. Specifically, MERGE introduces a play-
> and-plug framework that enables seamless switching between image generation and
> depth estimation modes through simple and pluggable converters. Meanwhile, we
> propose a Group Reuse Mechanism to encourage parameter reuse and im- prove the
> utilization of the additional learnable parameters. MERGE unleashes the
> powerful depth estimation capability of the pre-trained text-to-image model
> while preserving its original image generation ability. Compared to other
> unified models for image generation and depth estimation, MERGE achieves
> state-of- the-art performance across multiple depth estimation benchmarks. The
> code will be made available at https://github.com/H-EmbodVis/MERGE

