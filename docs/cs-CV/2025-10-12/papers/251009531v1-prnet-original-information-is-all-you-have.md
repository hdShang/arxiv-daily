---
layout: default
title: PRNet: Original Information Is All You Have
---

# PRNet: Original Information Is All You Have

**arXiv**: [2510.09531v1](https://arxiv.org/abs/2510.09531) | [PDF](https://arxiv.org/pdf/2510.09531.pdf)

**作者**: PeiHuang Zheng, Yunlong Zhao, Zheng Cui, Yang Li

---

## 💡 一句话要点

**提出PRNet以解决航拍图像小目标检测中的信息退化问题**

**关键词**: `小目标检测` `航拍图像` `特征保留` `实时检测` `空间语义对齐` `渐进细化`

## 📋 核心要点

1. 核心问题：航拍图像小目标检测中，浅层空间细节与语义信息对齐困难，导致漏检和误检
2. 方法要点：通过渐进细化颈部和增强切片采样模块，保留并高效利用原始浅层特征
3. 实验或效果：在VisDrone等数据集上，PRNet在计算约束下优于现有方法，实现高精度与效率平衡

## 📄 摘要（原文）

> Small object detection in aerial images suffers from severe information
> degradation during feature extraction due to limited pixel representations,
> where shallow spatial details fail to align effectively with semantic
> information, leading to frequent misses and false positives. Existing FPN-based
> methods attempt to mitigate these losses through post-processing enhancements,
> but the reconstructed details often deviate from the original image
> information, impeding their fusion with semantic content. To address this
> limitation, we propose PRNet, a real-time detection framework that prioritizes
> the preservation and efficient utilization of primitive shallow spatial
> features to enhance small object representations. PRNet achieves this via two
> modules:the Progressive Refinement Neck (PRN) for spatial-semantic alignment
> through backbone reuse and iterative refinement, and the Enhanced SliceSamp
> (ESSamp) for preserving shallow information during downsampling via optimized
> rearrangement and convolution. Extensive experiments on the VisDrone, AI-TOD,
> and UAVDT datasets demonstrate that PRNet outperforms state-of-the-art methods
> under comparable computational constraints, achieving superior
> accuracy-efficiency trade-offs.

