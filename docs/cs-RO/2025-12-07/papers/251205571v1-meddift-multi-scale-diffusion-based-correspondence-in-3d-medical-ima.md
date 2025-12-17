---
layout: default
title: MedDIFT: Multi-Scale Diffusion-Based Correspondence in 3D Medical Imaging
---

# MedDIFT: Multi-Scale Diffusion-Based Correspondence in 3D Medical Imaging

**arXiv**: [2512.05571v1](https://arxiv.org/abs/2512.05571) | [PDF](https://arxiv.org/pdf/2512.05571.pdf)

**作者**: Xingyu Zhang, Anna Reithmeir, Fryderyk Kögl, Rickmer Braren, Julia A. Schnabel, Daniel M. Lang

---

## 💡 一句话要点

**提出MedDIFT框架，利用预训练扩散模型特征实现3D医学图像无训练对应匹配**

**关键词**: `医学图像配准` `扩散模型` `3D对应匹配` `无训练框架` `多尺度特征融合`

## 📋 核心要点

1. 医学图像配准依赖局部强度相似性，在低对比度区域易失配
2. MedDIFT融合预训练扩散模型多尺度特征作为体素描述符，通过余弦相似度匹配
3. 在肺部CT数据集上，性能媲美学习型方法，优于传统B样条配准

## 📄 摘要（原文）

> Accurate spatial correspondence between medical images is essential for longitudinal analysis, lesion tracking, and image-guided interventions. Medical image registration methods rely on local intensity-based similarity measures, which fail to capture global semantic structure and often yield mismatches in low-contrast or anatomically variable regions. Recent advances in diffusion models suggest that their intermediate representations encode rich geometric and semantic information. We present MedDIFT, a training-free 3D correspondence framework that leverages multi-scale features from a pretrained latent medical diffusion model as voxel descriptors. MedDIFT fuses diffusion activations into rich voxel-wise descriptors and matches them via cosine similarity, with an optional local-search prior. On a publicly available lung CT dataset, MedDIFT achieves correspondence accuracy comparable to the state-of-the-art learning-based UniGradICON model and surpasses conventional B-spline-based registration, without requiring any task-specific model training. Ablation experiments confirm that multi-level feature fusion and modest diffusion noise improve performance.

