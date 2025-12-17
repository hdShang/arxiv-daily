---
layout: default
title: One Layer Is Enough: Adapting Pretrained Visual Encoders for Image Generation
---

# One Layer Is Enough: Adapting Pretrained Visual Encoders for Image Generation

**arXiv**: [2512.07829v1](https://arxiv.org/abs/2512.07829) | [PDF](https://arxiv.org/pdf/2512.07829.pdf)

**作者**: Yuan Gao, Chen Chen, Tianrong Chen, Jiatao Gu

---

## 💡 一句话要点

**提出FAE框架，通过单层注意力适配预训练视觉编码器用于图像生成**

**关键词**: `图像生成` `预训练视觉编码器` `特征适配` `扩散模型` `归一化流` `自监督学习`

## 📋 核心要点

1. 核心问题：预训练视觉特征与生成模型潜在空间不匹配，导致适配困难
2. 方法要点：使用两个独立解码器，一个重构特征空间，另一个用于图像生成
3. 实验或效果：在ImageNet等基准上达到接近SOTA的FID，支持扩散模型和归一化流

## 📄 摘要（原文）

> Visual generative models (e.g., diffusion models) typically operate in compressed latent spaces to balance training efficiency and sample quality. In parallel, there has been growing interest in leveraging high-quality pre-trained visual representations, either by aligning them inside VAEs or directly within the generative model. However, adapting such representations remains challenging due to fundamental mismatches between understanding-oriented features and generation-friendly latent spaces. Representation encoders benefit from high-dimensional latents that capture diverse hypotheses for masked regions, whereas generative models favor low-dimensional latents that must faithfully preserve injected noise. This discrepancy has led prior work to rely on complex objectives and architectures. In this work, we propose FAE (Feature Auto-Encoder), a simple yet effective framework that adapts pre-trained visual representations into low-dimensional latents suitable for generation using as little as a single attention layer, while retaining sufficient information for both reconstruction and understanding. The key is to couple two separate deep decoders: one trained to reconstruct the original feature space, and a second that takes the reconstructed features as input for image generation. FAE is generic; it can be instantiated with a variety of self-supervised encoders (e.g., DINO, SigLIP) and plugged into two distinct generative families: diffusion models and normalizing flows. Across class-conditional and text-to-image benchmarks, FAE achieves strong performance. For example, on ImageNet 256x256, our diffusion model with CFG attains a near state-of-the-art FID of 1.29 (800 epochs) and 1.70 (80 epochs). Without CFG, FAE reaches the state-of-the-art FID of 1.48 (800 epochs) and 2.08 (80 epochs), demonstrating both high quality and fast learning.

