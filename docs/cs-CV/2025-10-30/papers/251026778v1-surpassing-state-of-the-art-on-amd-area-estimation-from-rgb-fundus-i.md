---
layout: default
title: Surpassing state of the art on AMD area estimation from RGB fundus images through careful selection of U-Net architectures and loss functions for class imbalance
---

# Surpassing state of the art on AMD area estimation from RGB fundus images through careful selection of U-Net architectures and loss functions for class imbalance

**arXiv**: [2510.26778v1](https://arxiv.org/abs/2510.26778) | [PDF](https://arxiv.org/pdf/2510.26778.pdf)

**作者**: Valentyna Starodub, Mantas Lukoševičius

---

## 💡 一句话要点

**提出优化U-Net架构与损失函数的方法，以提升RGB眼底图像中AMD病变分割性能**

**关键词**: `语义分割` `U-Net架构` `类别不平衡` `损失函数` `RGB眼底图像` `AMD检测`

## 📋 核心要点

1. 核心问题：年龄相关性黄斑变性（AMD）是老年人视力损伤主因，需从RGB眼底图像进行病变分割
2. 方法要点：基于U-Net框架，评估预处理、编码器类型和损失函数以缓解类别不平衡
3. 实验或效果：在ADAM挑战数据集上，多类分割性能超越所有先前提交结果

## 📄 摘要（原文）

> Age-related macular degeneration (AMD) is one of the leading causes of
> irreversible vision impairment in people over the age of 60. This research
> focuses on semantic segmentation for AMD lesion detection in RGB fundus images,
> a non-invasive and cost-effective imaging technique. The results of the ADAM
> challenge - the most comprehensive AMD detection from RGB fundus images
> research competition and open dataset to date - serve as a benchmark for our
> evaluation. Taking the U-Net connectivity as a base of our framework, we
> evaluate and compare several approaches to improve the segmentation model's
> architecture and training pipeline, including pre-processing techniques,
> encoder (backbone) deep network types of varying complexity, and specialized
> loss functions to mitigate class imbalances on image and pixel levels. The main
> outcome of this research is the final configuration of the AMD detection
> framework, which outperforms all the prior ADAM challenge submissions on the
> multi-class segmentation of different AMD lesion types in non-invasive RGB
> fundus images. The source code used to conduct the experiments presented in
> this paper is made freely available.

