---
layout: default
title: Restora-Flow: Mask-Guided Image Restoration with Flow Matching
---

# Restora-Flow: Mask-Guided Image Restoration with Flow Matching

**arXiv**: [2511.20152v1](https://arxiv.org/abs/2511.20152) | [PDF](https://arxiv.org/pdf/2511.20152.pdf)

**作者**: Arnela Hadzic, Franz Thaler, Lea Bogensperger, Simon Johannes Joham, Martin Urschler

---

## 💡 一句话要点

**提出Restora-Flow方法，通过掩码引导和轨迹校正解决图像修复中的处理时间长和过平滑问题。**

**关键词**: `图像修复` `流匹配` `掩码引导` `轨迹校正` `无训练方法` `感知质量`

## 📋 核心要点

1. 核心问题：现有流匹配方法在图像修复中存在处理时间长或结果过平滑的挑战。
2. 方法要点：引入无训练方法，使用退化掩码引导流匹配采样，并加入轨迹校正机制。
3. 实验或效果：在自然和医学数据集上，相比扩散和流匹配方法，感知质量和处理时间更优。

## 📄 摘要（原文）

> Flow matching has emerged as a promising generative approach that addresses the lengthy sampling times associated with state-of-the-art diffusion models and enables a more flexible trajectory design, while maintaining high-quality image generation. This capability makes it suitable as a generative prior for image restoration tasks. Although current methods leveraging flow models have shown promising results in restoration, some still suffer from long processing times or produce over-smoothed results. To address these challenges, we introduce Restora-Flow, a training-free method that guides flow matching sampling by a degradation mask and incorporates a trajectory correction mechanism to enforce consistency with degraded inputs. We evaluate our approach on both natural and medical datasets across several image restoration tasks involving a mask-based degradation, i.e., inpainting, super-resolution and denoising. We show superior perceptual quality and processing time compared to diffusion and flow matching-based reference methods.

