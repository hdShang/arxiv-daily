---
layout: default
title: A Biophysically-Conditioned Generative Framework for 3D Brain Tumor MRI Synthesis
---

# A Biophysically-Conditioned Generative Framework for 3D Brain Tumor MRI Synthesis

**arXiv**: [2510.09365v1](https://arxiv.org/abs/2510.09365) | [PDF](https://arxiv.org/pdf/2510.09365.pdf)

**作者**: Valentin Biller, Lucas Zimmer, Can Erdur, Sandeep Nagar, Daniel Rückert, Niklas Bubeck, Jonas Weidner

---

## 💡 一句话要点

**提出基于生物物理条件的生成模型以合成3D脑肿瘤MRI和修复健康组织**

**关键词**: `脑肿瘤MRI合成` `潜在扩散模型` `生物物理条件` `图像修复` `3D医学影像`

## 📋 核心要点

1. 核心问题：脑肿瘤MRI合成与健康组织修复需要高保真和空间一致性。
2. 方法要点：使用潜在扩散模型，条件输入组织分割和肿瘤浓度。
3. 实验或效果：健康修复PSNR 18.5，肿瘤合成PSNR 17.4，代码开源。

## 📄 摘要（原文）

> Magnetic resonance imaging (MRI) inpainting supports numerous clinical and
> research applications. We introduce the first generative model that conditions
> on voxel-level, continuous tumor concentrations to synthesize high-fidelity
> brain tumor MRIs. For the BraTS 2025 Inpainting Challenge, we adapt this
> architecture to the complementary task of healthy tissue restoration by setting
> the tumor concentrations to zero. Our latent diffusion model conditioned on
> both tissue segmentations and the tumor concentrations generates 3D spatially
> coherent and anatomically consistent images for both tumor synthesis and
> healthy tissue inpainting. For healthy inpainting, we achieve a PSNR of 18.5,
> and for tumor inpainting, we achieve 17.4. Our code is available at:
> https://github.com/valentin-biller/ldm.git

