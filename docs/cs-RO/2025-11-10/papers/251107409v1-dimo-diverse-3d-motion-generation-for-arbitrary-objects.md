---
layout: default
title: DIMO: Diverse 3D Motion Generation for Arbitrary Objects
---

# DIMO: Diverse 3D Motion Generation for Arbitrary Objects

**arXiv**: [2511.07409v1](https://arxiv.org/abs/2511.07409) | [PDF](https://arxiv.org/pdf/2511.07409.pdf)

**作者**: Linzhan Mou, Jiahui Lei, Chen Wang, Lingjie Liu, Kostas Daniilidis

---

## 💡 一句话要点

**提出DIMO方法，从单张图像生成任意物体的多样3D运动。**

**关键词**: `3D运动生成` `单图像输入` `潜空间学习` `关键点轨迹` `3D高斯模型` `语言引导生成`

## 📋 核心要点

1. 核心问题：从单张图像生成任意物体的多样3D运动。
2. 方法要点：利用视频模型提取运动模式，嵌入共享潜空间，解码为关键点轨迹驱动3D高斯。
3. 实验或效果：支持3D运动插值和语言引导生成，实现单次前向推理。

## 📄 摘要（原文）

> We present DIMO, a generative approach capable of generating diverse 3D
> motions for arbitrary objects from a single image. The core idea of our work is
> to leverage the rich priors in well-trained video models to extract the common
> motion patterns and then embed them into a shared low-dimensional latent space.
> Specifically, we first generate multiple videos of the same object with diverse
> motions. We then embed each motion into a latent vector and train a shared
> motion decoder to learn the distribution of motions represented by a structured
> and compact motion representation, i.e., neural key point trajectories. The
> canonical 3D Gaussians are then driven by these key points and fused to model
> the geometry and appearance. During inference time with learned latent space,
> we can instantly sample diverse 3D motions in a single-forward pass and support
> several interesting applications including 3D motion interpolation and
> language-guided motion generation. Our project page is available at
> https://linzhanm.github.io/dimo.

