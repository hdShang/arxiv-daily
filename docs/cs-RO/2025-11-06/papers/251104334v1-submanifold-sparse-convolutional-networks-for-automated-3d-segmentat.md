---
layout: default
title: Submanifold Sparse Convolutional Networks for Automated 3D Segmentation of Kidneys and Kidney Tumours in Computed Tomography
---

# Submanifold Sparse Convolutional Networks for Automated 3D Segmentation of Kidneys and Kidney Tumours in Computed Tomography

**arXiv**: [2511.04334v1](https://arxiv.org/abs/2511.04334) | [PDF](https://arxiv.org/pdf/2511.04334.pdf)

**作者**: Saúl Alonso-Monsalve, Leigh H. Whitehead, Adam Aurisano, Lorena Escudero Sanchez

---

## 💡 一句话要点

**提出子流形稀疏卷积网络以高效分割CT图像中的肾脏和肿瘤**

**关键词**: `3D医学图像分割` `子流形稀疏卷积` `CT图像分析` `计算效率优化` `肾脏肿瘤分割`

## 📋 核心要点

1. 核心问题：3D CT图像分割计算量大，传统方法需降采样或分块处理
2. 方法要点：采用体素稀疏化和子流形稀疏卷积，支持高分辨率3D输入
3. 实验效果：在KiTS23数据集上达到高精度，显著降低推理时间和显存使用

## 📄 摘要（原文）

> The accurate delineation of tumours in radiological images like Computed
> Tomography is a very specialised and time-consuming task, and currently a
> bottleneck preventing quantitative analyses to be performed routinely in the
> clinical setting. For this reason, developing methods for the automated
> segmentation of tumours in medical imaging is of the utmost importance and has
> driven significant efforts in recent years. However, challenges regarding the
> impracticality of 3D scans, given the large amount of voxels to be analysed,
> usually requires the downsampling of such images or using patches thereof when
> applying traditional convolutional neural networks. To overcome this problem,
> in this paper we propose a new methodology that uses, divided into two stages,
> voxel sparsification and submanifold sparse convolutional networks. This method
> allows segmentations to be performed with high-resolution inputs and a native
> 3D model architecture, obtaining state-of-the-art accuracies while
> significantly reducing the computational resources needed in terms of GPU
> memory and time. We studied the deployment of this methodology in the context
> of Computed Tomography images of renal cancer patients from the KiTS23
> challenge, and our method achieved results competitive with the challenge
> winners, with Dice similarity coefficients of 95.8% for kidneys + masses, 85.7%
> for tumours + cysts, and 80.3% for tumours alone. Crucially, our method also
> offers significant computational improvements, achieving up to a 60% reduction
> in inference time and up to a 75\% reduction in VRAM usage compared to an
> equivalent dense architecture, across both CPU and various GPU cards tested.

