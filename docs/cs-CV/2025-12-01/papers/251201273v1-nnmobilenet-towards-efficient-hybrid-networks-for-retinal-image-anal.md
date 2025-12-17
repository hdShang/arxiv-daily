---
layout: default
title: nnMobileNet++: Towards Efficient Hybrid Networks for Retinal Image Analysis
---

# nnMobileNet++: Towards Efficient Hybrid Networks for Retinal Image Analysis

**arXiv**: [2512.01273v1](https://arxiv.org/abs/2512.01273) | [PDF](https://arxiv.org/pdf/2512.01273.pdf)

**作者**: Xin Li, Wenhui Zhu, Xuanzhao Dong, Hao Wang, Yujian Xiong, Oana Dumitrascu, Yalin Wang

---

## 💡 一句话要点

**提出nnMobileNet++混合网络以提升视网膜图像分析效率与准确性**

**关键词**: `视网膜图像分析` `混合网络架构` `动态蛇形卷积` `Transformer块` `轻量级网络` `图像分类`

## 📋 核心要点

1. 核心问题：卷积网络难以捕获视网膜图像中的长距离依赖和不规则病变模式。
2. 方法要点：结合动态蛇形卷积和阶段特定Transformer块，实现边界感知与全局上下文建模。
3. 实验或效果：在多个公共数据集上达到先进精度，同时保持低计算成本。

## 📄 摘要（原文）

> Retinal imaging is a critical, non-invasive modality for the early detection and monitoring of ocular and systemic diseases. Deep learning, particularly convolutional neural networks (CNNs), has significant progress in automated retinal analysis, supporting tasks such as fundus image classification, lesion detection, and vessel segmentation. As a representative lightweight network, nnMobileNet has demonstrated strong performance across multiple retinal benchmarks while remaining computationally efficient. However, purely convolutional architectures inherently struggle to capture long-range dependencies and model the irregular lesions and elongated vascular patterns that characterize on retinal images, despite the critical importance of vascular features for reliable clinical diagnosis. To further advance this line of work and extend the original vision of nnMobileNet, we propose nnMobileNet++, a hybrid architecture that progressively bridges convolutional and transformer representations. The framework integrates three key components: (i) dynamic snake convolution for boundary-aware feature extraction, (ii) stage-specific transformer blocks introduced after the second down-sampling stage for global context modeling, and (iii) retinal image pretraining to improve generalization. Experiments on multiple public retinal datasets for classification, together with ablation studies, demonstrate that nnMobileNet++ achieves state-of-the-art or highly competitive accuracy while maintaining low computational cost, underscoring its potential as a lightweight yet effective framework for retinal image analysis.

