---
layout: default
title: Dynamic Weight Adjustment for Knowledge Distillation: Leveraging Vision Transformer for High-Accuracy Lung Cancer Detection and Real-Time Deployment
---

# Dynamic Weight Adjustment for Knowledge Distillation: Leveraging Vision Transformer for High-Accuracy Lung Cancer Detection and Real-Time Deployment

**arXiv**: [2510.20438v1](https://arxiv.org/abs/2510.20438) | [PDF](https://arxiv.org/pdf/2510.20438.pdf)

**作者**: Saif Ur Rehman Khan, Muhammad Nabeel Asim, Sebastian Vollmer, Andreas Dengel

---

## 💡 一句话要点

**提出动态模糊知识蒸馏方法，用于高精度肺癌检测与实时部署。**

**关键词**: `知识蒸馏` `肺癌检测` `Vision Transformer` `动态权重调整` `图像融合` `遗传算法`

## 📋 核心要点

1. 核心问题：传统知识蒸馏权重固定，难以处理肺癌图像中的不确定性和复杂性。
2. 方法要点：使用模糊逻辑动态调整蒸馏权重，结合ViT-B32和MobileNet进行知识转移。
3. 实验或效果：在LC25000和IQOTH/NCCD数据集上分别达到99.16%和99.54%的准确率。

## 📄 摘要（原文）

> This paper presents the FuzzyDistillViT-MobileNet model, a novel approach for
> lung cancer (LC) classification, leveraging dynamic fuzzy logic-driven
> knowledge distillation (KD) to address uncertainty and complexity in disease
> diagnosis. Unlike traditional models that rely on static KD with fixed weights,
> our method dynamically adjusts the distillation weight using fuzzy logic,
> enabling the student model to focus on high-confidence regions while reducing
> attention to ambiguous areas. This dynamic adjustment improves the model
> ability to handle varying uncertainty levels across different regions of LC
> images. We employ the Vision Transformer (ViT-B32) as the instructor model,
> which effectively transfers knowledge to the student model, MobileNet,
> enhancing the student generalization capabilities. The training process is
> further optimized using a dynamic wait adjustment mechanism that adapts the
> training procedure for improved convergence and performance. To enhance image
> quality, we introduce pixel-level image fusion improvement techniques such as
> Gamma correction and Histogram Equalization. The processed images (Pix1 and
> Pix2) are fused using a wavelet-based fusion method to improve image resolution
> and feature preservation. This fusion method uses the wavedec2 function to
> standardize images to a 224x224 resolution, decompose them into multi-scale
> frequency components, and recursively average coefficients at each level for
> better feature representation. To address computational efficiency, Genetic
> Algorithm (GA) is used to select the most suitable pre-trained student model
> from a pool of 12 candidates, balancing model performance with computational
> cost. The model is evaluated on two datasets, including LC25000
> histopathological images (99.16% accuracy) and IQOTH/NCCD CT-scan images
> (99.54% accuracy), demonstrating robustness across different imaging domains.

