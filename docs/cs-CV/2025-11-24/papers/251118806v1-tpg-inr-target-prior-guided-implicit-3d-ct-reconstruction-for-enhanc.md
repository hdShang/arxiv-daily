---
layout: default
title: TPG-INR: Target Prior-Guided Implicit 3D CT Reconstruction for Enhanced Sparse-view Imaging
---

# TPG-INR: Target Prior-Guided Implicit 3D CT Reconstruction for Enhanced Sparse-view Imaging

**arXiv**: [2511.18806v1](https://arxiv.org/abs/2511.18806) | [PDF](https://arxiv.org/pdf/2511.18806.pdf)

**作者**: Qinglei Cao, Ziyao Tang, Xiaoqin Tang

---

## 💡 一句话要点

**提出目标先验引导隐式3D CT重建框架，提升稀疏视图成像效率与质量**

**关键词**: `CT重建` `隐式神经表示` `稀疏视图成像` `目标先验` `体素采样` `学习效率`

## 📋 核心要点

1. 核心问题：现有隐式3D CT重建方法忽略解剖先验，导致稀疏视图下精度和效率不足
2. 方法要点：利用投影数据生成目标先验，结合位置和结构编码指导体素采样与重建
3. 实验或效果：在腹部数据集上，学习效率提升10倍，PSNR优于NeRP达3.57-5.70 dB

## 📄 摘要（原文）

> X-ray imaging, based on penetration, enables detailed visualization of internal structures. Building on this capability, existing implicit 3D reconstruction methods have adapted the NeRF model and its variants for internal CT reconstruction. However, these approaches often neglect the significance of objects' anatomical priors for implicit learning, limiting both reconstruction precision and learning efficiency, particularly in ultra-sparse view scenarios. To address these challenges, we propose a novel 3D CT reconstruction framework that employs a 'target prior' derived from the object's projection data to enhance implicit learning. Our approach integrates positional and structural encoding to facilitate voxel-wise implicit reconstruction, utilizing the target prior to guide voxel sampling and enrich structural encoding. This dual strategy significantly boosts both learning efficiency and reconstruction quality. Additionally, we introduce a CUDA-based algorithm for rapid estimation of high-quality 3D target priors from sparse-view projections. Experiments utilizing projection data from a complex abdominal dataset demonstrate that the proposed model substantially enhances learning efficiency, outperforming the current leading model, NAF, by a factor of ten. In terms of reconstruction quality, it also exceeds the most accurate model, NeRP, achieving PSNR improvements of 3.57 dB, 5.42 dB, and 5.70 dB with 10, 20, and 30 projections, respectively. The code is available at https://github.com/qlcao171/TPG-INR.

