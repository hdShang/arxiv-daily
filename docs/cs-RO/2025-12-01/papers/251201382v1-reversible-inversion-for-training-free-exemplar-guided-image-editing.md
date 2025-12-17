---
layout: default
title: Reversible Inversion for Training-Free Exemplar-guided Image Editing
---

# Reversible Inversion for Training-Free Exemplar-guided Image Editing

**arXiv**: [2512.01382v1](https://arxiv.org/abs/2512.01382) | [PDF](https://arxiv.org/pdf/2512.01382.pdf)

**作者**: Yuke Li, Lianli Gao, Ji Zhang, Pengpeng Zeng, Lichuan Xiang, Hongkai Wen, Heng Tao Shen, Jingkuan Song

---

## 💡 一句话要点

**提出Reversible Inversion以实现免训练的示例引导图像编辑**

**关键词**: `示例引导图像编辑` `免训练方法` `反转技术` `去噪过程` `掩码引导`

## 📋 核心要点

1. 核心问题：标准反转方法在示例引导图像编辑中效果差且效率低
2. 方法要点：采用两阶段去噪过程，先基于源图像再基于参考图像，结合掩码引导选择性去噪
3. 实验或效果：在质量和计算开销上达到最先进性能

## 📄 摘要（原文）

> Exemplar-guided Image Editing (EIE) aims to modify a source image according to a visual reference. Existing approaches often require large-scale pre-training to learn relationships between the source and reference images, incurring high computational costs. As a training-free alternative, inversion techniques can be used to map the source image into a latent space for manipulation. However, our empirical study reveals that standard inversion is sub-optimal for EIE, leading to poor quality and inefficiency. To tackle this challenge, we introduce \textbf{Reversible Inversion ({ReInversion})} for effective and efficient EIE. Specifically, ReInversion operates as a two-stage denoising process, which is first conditioned on the source image and subsequently on the reference. Besides, we introduce a Mask-Guided Selective Denoising (MSD) strategy to constrain edits to target regions, preserving the structural consistency of the background. Both qualitative and quantitative comparisons demonstrate that our ReInversion method achieves state-of-the-art EIE performance with the lowest computational overhead.

