---
layout: default
title: Perspective-aware 3D Gaussian Inpainting with Multi-view Consistency
---

# Perspective-aware 3D Gaussian Inpainting with Multi-view Consistency

**arXiv**: [2510.10993v1](https://arxiv.org/abs/2510.10993) | [PDF](https://arxiv.org/pdf/2510.10993.pdf)

**作者**: Yuxin Cheng, Binxiao Huang, Taiqiang Wu, Wenyong Zhou, Chenchen Ding, Zhengwu Liu, Graziano Chesi, Ngai Wong

---

## 💡 一句话要点

**提出PAInpainter方法以解决3D高斯修复中的多视角一致性问题**

**关键词**: `3D高斯修复` `多视角一致性` `视角感知传播` `扩散模型` `虚拟现实` `图像修复`

## 📋 核心要点

1. 核心问题：现有3D高斯修复方法难以确保多视角一致性，影响修复质量。
2. 方法要点：利用视角感知内容传播和一致性验证，迭代优化3D高斯表示。
3. 实验效果：在SPIn-NeRF和NeRFiller数据集上PSNR达26.03dB和29.51dB，优于现有方法。

## 📄 摘要（原文）

> 3D Gaussian inpainting, a critical technique for numerous applications in
> virtual reality and multimedia, has made significant progress with pretrained
> diffusion models. However, ensuring multi-view consistency, an essential
> requirement for high-quality inpainting, remains a key challenge. In this work,
> we present PAInpainter, a novel approach designed to advance 3D Gaussian
> inpainting by leveraging perspective-aware content propagation and consistency
> verification across multi-view inpainted images. Our method iteratively refines
> inpainting and optimizes the 3D Gaussian representation with multiple views
> adaptively sampled from a perspective graph. By propagating inpainted images as
> prior information and verifying consistency across neighboring views,
> PAInpainter substantially enhances global consistency and texture fidelity in
> restored 3D scenes. Extensive experiments demonstrate the superiority of
> PAInpainter over existing methods. Our approach achieves superior 3D inpainting
> quality, with PSNR scores of 26.03 dB and 29.51 dB on the SPIn-NeRF and
> NeRFiller datasets, respectively, highlighting its effectiveness and
> generalization capability.

