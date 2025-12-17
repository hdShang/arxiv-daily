---
layout: default
title: AdLift: Lifting Adversarial Perturbations to Safeguard 3D Gaussian Splatting Assets Against Instruction-Driven Editing
---

# AdLift: Lifting Adversarial Perturbations to Safeguard 3D Gaussian Splatting Assets Against Instruction-Driven Editing

**arXiv**: [2512.07247v1](https://arxiv.org/abs/2512.07247) | [PDF](https://arxiv.org/pdf/2512.07247.pdf)

**作者**: Ziming Hong, Tianyu Huang, Runnan Chen, Shanshan Ye, Mingming Gong, Bo Han, Tongliang Liu

---

## 💡 一句话要点

**提出AdLift方法，通过提升2D对抗扰动至3D高斯表示，保护3D高斯泼溅资产免受指令驱动编辑的威胁。**

**关键词**: `3D高斯泼溅` `对抗扰动` `指令驱动编辑` `资产保护` `多视角泛化`

## 📋 核心要点

1. 核心问题：3D高斯泼溅资产面临指令驱动编辑的未授权篡改风险，现有2D对抗扰动方法难以直接应用。
2. 方法要点：采用Lifted PGD优化，通过梯度截断和图像到高斯拟合，将严格有界的2D扰动提升为3D高斯保护表示。
3. 实验或效果：AdLift在定性和定量实验中有效抵御先进指令驱动编辑，实现多视角一致保护。

## 📄 摘要（原文）

> Recent studies have extended diffusion-based instruction-driven 2D image editing pipelines to 3D Gaussian Splatting (3DGS), enabling faithful manipulation of 3DGS assets and greatly advancing 3DGS content creation. However, it also exposes these assets to serious risks of unauthorized editing and malicious tampering. Although imperceptible adversarial perturbations against diffusion models have proven effective for protecting 2D images, applying them to 3DGS encounters two major challenges: view-generalizable protection and balancing invisibility with protection capability. In this work, we propose the first editing safeguard for 3DGS, termed AdLift, which prevents instruction-driven editing across arbitrary views and dimensions by lifting strictly bounded 2D adversarial perturbations into 3D Gaussian-represented safeguard. To ensure both adversarial perturbations effectiveness and invisibility, these safeguard Gaussians are progressively optimized across training views using a tailored Lifted PGD, which first conducts gradient truncation during back-propagation from the editing model at the rendered image and applies projected gradients to strictly constrain the image-level perturbation. Then, the resulting perturbation is backpropagated to the safeguard Gaussian parameters via an image-to-Gaussian fitting operation. We alternate between gradient truncation and image-to-Gaussian fitting, yielding consistent adversarial-based protection performance across different viewpoints and generalizes to novel views. Empirically, qualitative and quantitative results demonstrate that AdLift effectively protects against state-of-the-art instruction-driven 2D image and 3DGS editing.

