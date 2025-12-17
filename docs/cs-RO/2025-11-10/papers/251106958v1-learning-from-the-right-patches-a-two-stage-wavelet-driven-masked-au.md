---
layout: default
title: Learning from the Right Patches: A Two-Stage Wavelet-Driven Masked Autoencoder for Histopathology Representation Learning
---

# Learning from the Right Patches: A Two-Stage Wavelet-Driven Masked Autoencoder for Histopathology Representation Learning

**arXiv**: [2511.06958v1](https://arxiv.org/abs/2511.06958) | [PDF](https://arxiv.org/pdf/2511.06958.pdf)

**作者**: Raneen Younis, Louay Hamdi, Lukas Chavez, Zahra Ahmadi

---

## 💡 一句话要点

**提出基于小波的掩码自编码器，通过两阶段选择提升组织病理学表示学习质量。**

**关键词**: `掩码自编码器` `小波分析` `组织病理学` `表示学习` `弱监督学习`

## 📋 核心要点

1. 核心问题：随机采样包含无关区域，限制模型捕获组织模式。
2. 方法要点：使用小波筛选结构丰富区域，分两阶段提取高分辨率特征。
3. 实验或效果：在多种癌症数据集上实现竞争性表示质量和分类性能。

## 📄 摘要（原文）

> Whole-slide images are central to digital pathology, yet their extreme size
> and scarce annotations make self-supervised learning essential. Masked
> Autoencoders (MAEs) with Vision Transformer backbones have recently shown
> strong potential for histopathology representation learning. However,
> conventional random patch sampling during MAE pretraining often includes
> irrelevant or noisy regions, limiting the model's ability to capture meaningful
> tissue patterns. In this paper, we present a lightweight and domain-adapted
> framework that brings structure and biological relevance into MAE-based
> learning through a wavelet-informed patch selection strategy. WISE-MAE applies
> a two-step coarse-to-fine process: wavelet-based screening at low magnification
> to locate structurally rich regions, followed by high-resolution extraction for
> detailed modeling. This approach mirrors the diagnostic workflow of
> pathologists and improves the quality of learned representations. Evaluations
> across multiple cancer datasets, including lung, renal, and colorectal tissues,
> show that WISE-MAE achieves competitive representation quality and downstream
> classification performance while maintaining efficiency under weak supervision.

