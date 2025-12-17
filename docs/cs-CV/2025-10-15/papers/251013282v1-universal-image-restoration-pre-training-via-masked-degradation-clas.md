---
layout: default
title: Universal Image Restoration Pre-training via Masked Degradation Classification
---

# Universal Image Restoration Pre-training via Masked Degradation Classification

**arXiv**: [2510.13282v1](https://arxiv.org/abs/2510.13282) | [PDF](https://arxiv.org/pdf/2510.13282.pdf)

**作者**: JiaKui Hu, Zhengjian Yao, Lujia Jin, Yinghao Chen, Yanye Lu

---

## 💡 一句话要点

**提出MaskDCPT预训练方法，通过掩码退化分类实现通用图像恢复。**

**关键词**: `图像恢复预训练` `掩码退化分类` `双解码器架构` `通用图像恢复` `UIR-2.5M数据集`

## 📋 核心要点

1. 核心问题：图像恢复中退化类型分类与高质量重建的联合学习。
2. 方法要点：使用编码器和双解码器，结合掩码图像建模与对比学习。
3. 实验或效果：在PSNR上提升至少3.77 dB，泛化至未知退化类型。

## 📄 摘要（原文）

> This study introduces a Masked Degradation Classification Pre-Training method
> (MaskDCPT), designed to facilitate the classification of degradation types in
> input images, leading to comprehensive image restoration pre-training. Unlike
> conventional pre-training methods, MaskDCPT uses the degradation type of the
> image as an extremely weak supervision, while simultaneously leveraging the
> image reconstruction to enhance performance and robustness. MaskDCPT includes
> an encoder and two decoders: the encoder extracts features from the masked
> low-quality input image. The classification decoder uses these features to
> identify the degradation type, whereas the reconstruction decoder aims to
> reconstruct a corresponding high-quality image. This design allows the
> pre-training to benefit from both masked image modeling and contrastive
> learning, resulting in a generalized representation suited for restoration
> tasks. Benefit from the straightforward yet potent MaskDCPT, the pre-trained
> encoder can be used to address universal image restoration and achieve
> outstanding performance. Implementing MaskDCPT significantly improves
> performance for both convolution neural networks (CNNs) and Transformers, with
> a minimum increase in PSNR of 3.77 dB in the 5D all-in-one restoration task and
> a 34.8% reduction in PIQE compared to baseline in real-world degradation
> scenarios. It also emergences strong generalization to previously unseen
> degradation types and levels. In addition, we curate and release the UIR-2.5M
> dataset, which includes 2.5 million paired restoration samples across 19
> degradation types and over 200 degradation levels, incorporating both synthetic
> and real-world data. The dataset, source code, and models are available at
> https://github.com/MILab-PKU/MaskDCPT.

