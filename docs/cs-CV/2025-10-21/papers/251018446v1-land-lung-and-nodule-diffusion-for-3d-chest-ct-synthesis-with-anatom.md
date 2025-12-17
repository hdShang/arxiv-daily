---
layout: default
title: LAND: Lung and Nodule Diffusion for 3D Chest CT Synthesis with Anatomical Guidance
---

# LAND: Lung and Nodule Diffusion for 3D Chest CT Synthesis with Anatomical Guidance

**arXiv**: [2510.18446v1](https://arxiv.org/abs/2510.18446) | [PDF](https://arxiv.org/pdf/2510.18446.pdf)

**作者**: Anna Oliveras, Roger Marí, Rafael Redondo, Oriol Guardià, Ana Tost, Bhalaji Nagarajan, Carolina Migliorelli, Vicent Ribas, Petia Radeva

---

## 💡 一句话要点

**提出基于解剖掩码的潜在扩散模型以生成高质量3D胸部CT扫描**

**关键词**: `潜在扩散模型` `3D医学图像合成` `胸部CT扫描` `解剖条件生成` `肺结节检测`

## 📋 核心要点

1. 核心问题：现有方法生成3D胸部CT扫描计算成本高，且难以精确控制解剖特征。
2. 方法要点：使用3D解剖掩码作为条件，在单GPU上合成256x256x256体积图像。
3. 实验或效果：仅结节掩码导致解剖错误，需结合全局肺结构实现准确合成。

## 📄 摘要（原文）

> This work introduces a new latent diffusion model to generate high-quality 3D
> chest CT scans conditioned on 3D anatomical masks. The method synthesizes
> volumetric images of size 256x256x256 at 1 mm isotropic resolution using a
> single mid-range GPU, significantly lowering the computational cost compared to
> existing approaches. The conditioning masks delineate lung and nodule regions,
> enabling precise control over the output anatomical features. Experimental
> results demonstrate that conditioning solely on nodule masks leads to
> anatomically incorrect outputs, highlighting the importance of incorporating
> global lung structure for accurate conditional synthesis. The proposed approach
> supports the generation of diverse CT volumes with and without lung nodules of
> varying attributes, providing a valuable tool for training AI models or
> healthcare professionals.

