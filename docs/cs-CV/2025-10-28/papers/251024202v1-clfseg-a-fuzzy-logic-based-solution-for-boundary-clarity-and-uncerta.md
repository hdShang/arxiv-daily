---
layout: default
title: CLFSeg: A Fuzzy-Logic based Solution for Boundary Clarity and Uncertainty Reduction in Medical Image Segmentation
---

# CLFSeg: A Fuzzy-Logic based Solution for Boundary Clarity and Uncertainty Reduction in Medical Image Segmentation

**arXiv**: [2510.24202v1](https://arxiv.org/abs/2510.24202) | [PDF](https://arxiv.org/pdf/2510.24202.pdf)

**作者**: Anshul Kaushal, Kunal Jangid, Vinod K. Kurmi

---

## 💡 一句话要点

**提出CLFSeg框架，结合模糊逻辑与卷积模块，提升医学图像分割的边界清晰度和不确定性处理。**

**关键词**: `医学图像分割` `模糊逻辑` `卷积神经网络` `边界不确定性` `计算效率`

## 📋 核心要点

1. 传统CNN模型泛化性差、边界不确定性高，影响医学图像分割精度。
2. 引入模糊卷积模块，融合局部与全局特征，减少噪声和模糊，保持计算效率。
3. 在多个公开数据集上验证，性能超越现有SOTA，适用于真实诊断场景。

## 📄 摘要（原文）

> Accurate polyp and cardiac segmentation for early detection and treatment is
> essential for the diagnosis and treatment planning of cancer-like diseases.
> Traditional convolutional neural network (CNN) based models have represented
> limited generalizability, robustness, and inability to handle uncertainty,
> which affects the segmentation performance. To solve these problems, this paper
> introduces CLFSeg, an encoder-decoder based framework that aggregates the
> Fuzzy-Convolutional (FC) module leveraging convolutional layers and fuzzy
> logic. This module enhances the segmentation performance by identifying local
> and global features while minimizing the uncertainty, noise, and ambiguity in
> boundary regions, ensuring computing efficiency. In order to handle class
> imbalance problem while focusing on the areas of interest with tiny and
> boundary regions, binary cross-entropy (BCE) with dice loss is incorporated.
> Our proposed model exhibits exceptional performance on four publicly available
> datasets, including CVC-ColonDB, CVC-ClinicDB, EtisLaribPolypDB, and ACDC.
> Extensive experiments and visual studies show CLFSeg surpasses the existing
> SOTA performance and focuses on relevant regions of interest in anatomical
> structures. The proposed CLFSeg improves performance while ensuring computing
> efficiency, which makes it a potential solution for real-world medical
> diagnostic scenarios. Project page is available at
> https://visdomlab.github.io/CLFSeg/

