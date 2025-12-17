---
layout: default
title: Image Restoration via Primal Dual Hybrid Gradient and Flow Generative Model
---

# Image Restoration via Primal Dual Hybrid Gradient and Flow Generative Model

**arXiv**: [2511.06748v1](https://arxiv.org/abs/2511.06748) | [PDF](https://arxiv.org/pdf/2511.06748.pdf)

**作者**: Ji Li, Chao Wang

---

## 💡 一句话要点

**提出基于原始对偶混合梯度的PnP算法，以增强图像恢复对非高斯噪声的鲁棒性。**

**关键词**: `图像恢复` `原始对偶混合梯度` `流匹配生成模型` `Plug-and-Play框架` `非高斯噪声鲁棒性`

## 📋 核心要点

1. 核心问题：传统PnP方法在非高斯噪声下数据保真项适用性有限。
2. 方法要点：结合流匹配生成模型与PDHG，支持ℓ₁和ℓ₂范数损失。
3. 实验效果：在去噪、超分辨率等任务中，验证了ℓ₁和ℓ₂损失优于平方ℓ₂损失。

## 📄 摘要（原文）

> Regularized optimization has been a classical approach to solving imaging
> inverse problems, where the regularization term enforces desirable properties
> of the unknown image. Recently, the integration of flow matching generative
> models into image restoration has garnered significant attention, owing to
> their powerful prior modeling capabilities. In this work, we incorporate such
> generative priors into a Plug-and-Play (PnP) framework based on proximal
> splitting, where the proximal operator associated with the regularizer is
> replaced by a time-dependent denoiser derived from the generative model. While
> existing PnP methods have achieved notable success in inverse problems with
> smooth squared $\ell_2$ data fidelity--typically associated with Gaussian
> noise--their applicability to more general data fidelity terms remains
> underexplored. To address this, we propose a general and efficient PnP
> algorithm inspired by the primal-dual hybrid gradient (PDHG) method. Our
> approach is computationally efficient, memory-friendly, and accommodates a wide
> range of fidelity terms. In particular, it supports both $\ell_1$ and $\ell_2$
> norm-based losses, enabling robustness to non-Gaussian noise types such as
> Poisson and impulse noise. We validate our method on several image restoration
> tasks, including denoising, super-resolution, deblurring, and inpainting, and
> demonstrate that $\ell_1$ and $\ell_2$ fidelity terms outperform the
> conventional squared $\ell_2$ loss in the presence of non-Gaussian noise.

