---
layout: default
title: Balanced Multi-Task Attention for Satellite Image Classification: A Systematic Approach to Achieving 97.23% Accuracy on EuroSAT Without Pre-Training
---

# Balanced Multi-Task Attention for Satellite Image Classification: A Systematic Approach to Achieving 97.23% Accuracy on EuroSAT Without Pre-Training

**arXiv**: [2510.15527v1](https://arxiv.org/abs/2510.15527) | [PDF](https://arxiv.org/pdf/2510.15527.pdf)

**作者**: Aditya Vir

---

## 💡 一句话要点

**提出平衡多任务注意力机制，在卫星图像分类中实现97.23%准确率**

**关键词**: `卫星图像分类` `多任务注意力` `卷积神经网络` `EuroSAT数据集` `特征融合`

## 📋 核心要点

1. 核心问题：卫星图像分类中空间和光谱特征提取的平衡与过拟合问题
2. 方法要点：结合坐标注意力和挤压-激励块，通过可学习融合参数统一特征
3. 实验或效果：在EuroSAT数据集上达到97.23%准确率，无需预训练模型

## 📄 摘要（原文）

> This work presents a systematic investigation of custom convolutional neural
> network architectures for satellite land use classification, achieving 97.23%
> test accuracy on the EuroSAT dataset without reliance on pre-trained models.
> Through three progressive architectural iterations (baseline: 94.30%,
> CBAM-enhanced: 95.98%, and balanced multi-task attention: 97.23%) we identify
> and address specific failure modes in satellite imagery classification. Our
> principal contribution is a novel balanced multi-task attention mechanism that
> combines Coordinate Attention for spatial feature extraction with
> Squeeze-Excitation blocks for spectral feature extraction, unified through a
> learnable fusion parameter. Experimental results demonstrate that this
> learnable parameter autonomously converges to alpha approximately 0.57,
> indicating near-equal importance of spatial and spectral modalities for
> satellite imagery. We employ progressive DropBlock regularization (5-20% by
> network depth) and class-balanced loss weighting to address overfitting and
> confusion pattern imbalance. The final 12-layer architecture achieves Cohen's
> Kappa of 0.9692 with all classes exceeding 94.46% accuracy, demonstrating
> confidence calibration with a 24.25% gap between correct and incorrect
> predictions. Our approach achieves performance within 1.34% of fine-tuned
> ResNet-50 (98.57%) while requiring no external data, validating the efficacy of
> systematic architectural design for domain-specific applications. Complete
> code, trained models, and evaluation scripts are publicly available.

