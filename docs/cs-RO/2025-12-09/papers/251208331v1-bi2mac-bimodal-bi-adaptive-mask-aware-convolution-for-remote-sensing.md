---
layout: default
title: Bi^2MAC: Bimodal Bi-Adaptive Mask-Aware Convolution for Remote Sensing Pansharpening
---

# Bi^2MAC: Bimodal Bi-Adaptive Mask-Aware Convolution for Remote Sensing Pansharpening

**arXiv**: [2512.08331v1](https://arxiv.org/abs/2512.08331) | [PDF](https://arxiv.org/pdf/2512.08331.pdf)

**作者**: Xianghong Xiao, Zeyu Xia, Zhou Fei, Jinliang Xiao, Haorui Chen, Liangjian Deng

---

## 💡 一句话要点

**提出Bi^2MAC卷积以解决遥感图像融合中区域异质性和计算效率问题**

**关键词**: `遥感图像融合` `自适应卷积` `掩码生成` `计算效率优化` `异质区域处理`

## 📋 核心要点

1. 核心问题：传统自适应卷积方法在遥感图像中捕获异质区域能力有限且计算成本高
2. 方法要点：设计轻量级模块生成软硬掩码，将冗余和异质特征分别路由到紧凑分支和聚焦分支处理
3. 实验或效果：在多个基准数据集上实现SOTA性能，同时显著降低训练时间、参数量和计算成本

## 📄 摘要（原文）

> Pansharpening aims to fuse a high-resolution panchromatic (PAN) image with a low-resolution multispectral (LRMS) image to generate a high-resolution multispectral image (HRMS). Conventional deep learning-based methods are inherently limited in their ability to adapt to regional heterogeneity within feature representations. Although various adaptive convolution methods have been proposed to address this limitation, they often suffer from excessive computational costs and a limited ability to capture heterogeneous regions in remote sensing images effectively. To overcome these challenges, we propose Bimodal Bi-Adaptive Mask-Aware Convolution (Bi^2MAC), which effectively exploits information from different types of regions while intelligently allocating computational resources. Specifically, we design a lightweight module to generate both soft and hard masks, which are used to modulate the input features preliminarily and to guide different types of regions into separate processing branches, respectively. Redundant features are directed to a compact branch for low-cost global processing. In contrast, heterogeneous features are routed to a focused branch that invests more computational resources for fine-grained modeling. Extensive experiments on multiple benchmark datasets demonstrate that Bi^2MAC achieves state-of-the-art (SOTA) performance while requiring substantially lower training time and parameter counts, and the minimal computational cost among adaptive convolution models.

