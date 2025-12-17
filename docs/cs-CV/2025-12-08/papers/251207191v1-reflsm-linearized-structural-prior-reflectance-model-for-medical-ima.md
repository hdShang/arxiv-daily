---
layout: default
title: RefLSM: Linearized Structural-Prior Reflectance Model for Medical Image Segmentation and Bias-Field Correction
---

# RefLSM: Linearized Structural-Prior Reflectance Model for Medical Image Segmentation and Bias-Field Correction

**arXiv**: [2512.07191v1](https://arxiv.org/abs/2512.07191) | [PDF](https://arxiv.org/pdf/2512.07191.pdf)

**作者**: Wenqi Zhao, Jiacheng Sang, Fenghua Cheng, Yonglu Shu, Dong Li, Xiaofeng Yang

---

## 💡 一句话要点

**提出RefLSM模型，通过反射率分解和线性结构先验解决医学图像分割中的强度不均匀和噪声问题。**

**关键词**: `医学图像分割` `反射率分解` `水平集方法` `结构先验` `偏置场校正` `ADMM优化`

## 📋 核心要点

1. 核心问题：医学图像分割受强度不均匀、噪声、模糊边界和不规则结构影响，传统水平集方法在严重非均匀成像条件下效果有限。
2. 方法要点：基于Retinex的反射率分解，结合线性结构先验和松弛二元水平集，通过ADMM优化实现稳定分割。
3. 实验或效果：在多个医学影像数据集上验证，RefLSM在分割精度、鲁棒性和计算效率上优于先进水平集方法。

## 📄 摘要（原文）

> Medical image segmentation remains challenging due to intensity inhomogeneity, noise, blurred boundaries, and irregular structures. Traditional level set methods, while effective in certain cases, often depend on approximate bias field estimations and therefore struggle under severe non-uniform imaging conditions. To address these limitations, we propose a novel variational Reflectance-based Level Set Model (RefLSM), which explicitly integrates Retinex-inspired reflectance decomposition into the segmentation framework. By decomposing the observed image into reflectance and bias field components, RefLSM directly segments the reflectance, which is invariant to illumination and preserves fine structural details. Building on this foundation, we introduce two key innovations for enhanced precision and robustness. First, a linear structural prior steers the smoothed reflectance gradients toward a data-driven reference, providing reliable geometric guidance in noisy or low-contrast scenes. Second, a relaxed binary level-set is embedded in RefLSM and enforced via convex relaxation and sign projection, yielding stable evolution and avoiding reinitialization-induced diffusion. The resulting variational problem is solved efficiently using an ADMM-based optimization scheme. Extensive experiments on multiple medical imaging datasets demonstrate that RefLSM achieves superior segmentation accuracy, robustness, and computational efficiency compared to state-of-the-art level set methods.

