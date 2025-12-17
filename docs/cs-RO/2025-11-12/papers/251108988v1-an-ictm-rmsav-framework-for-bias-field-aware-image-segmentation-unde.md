---
layout: default
title: An ICTM-RMSAV Framework for Bias-Field Aware Image Segmentation under Poisson and Multiplicative Noise
---

# An ICTM-RMSAV Framework for Bias-Field Aware Image Segmentation under Poisson and Multiplicative Noise

**arXiv**: [2511.08988v1](https://arxiv.org/abs/2511.08988) | [PDF](https://arxiv.org/pdf/2511.08988.pdf)

**作者**: Xinyu Wang, Wenjun Yao, Fanghui Song, Zhichang Guo

---

## 💡 一句话要点

**提出ICTM-RMSAV框架以解决噪声和强度不均匀图像分割问题**

**关键词**: `图像分割` `噪声建模` `偏置场估计` `变分方法` `自适应正则化`

## 📋 核心要点

1. 核心问题：图像分割在噪声和强度不均匀下性能下降，需处理Poisson和乘性噪声。
2. 方法要点：结合I-散度和自适应TV正则化，估计偏置场，使用RMSAV优化。
3. 实验或效果：在合成和真实图像上验证，相比其他方法精度和鲁棒性更优。

## 📄 摘要（原文）

> Image segmentation is a core task in image processing, yet many methods degrade when images are heavily corrupted by noise and exhibit intensity inhomogeneity. Within the iterative-convolution thresholding method (ICTM) framework, we propose a variational segmentation model that integrates denoising terms. Specifically, the denoising component consists of an I-divergence term and an adaptive total-variation (TV) regularizer, making the model well suited to images contaminated by Gamma--distributed multiplicative noise and Poisson noise. A spatially adaptive weight derived from a gray-level indicator guides diffusion differently across regions of varying intensity. To further address intensity inhomogeneity, we estimate a smoothly varying bias field, which improves segmentation accuracy. Regions are represented by characteristic functions, with contour length encoded accordingly. For efficient optimization, we couple ICTM with a relaxed modified scalar auxiliary variable (RMSAV) scheme. Extensive experiments on synthetic and real-world images with intensity inhomogeneity and diverse noise types show that the proposed model achieves superior accuracy and robustness compared with competing approaches.

