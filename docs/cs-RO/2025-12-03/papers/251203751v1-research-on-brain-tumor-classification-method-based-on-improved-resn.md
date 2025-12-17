---
layout: default
title: Research on Brain Tumor Classification Method Based on Improved ResNet34 Network
---

# Research on Brain Tumor Classification Method Based on Improved ResNet34 Network

**arXiv**: [2512.03751v1](https://arxiv.org/abs/2512.03751) | [PDF](https://arxiv.org/pdf/2512.03751.pdf)

**作者**: Yufeng Li, Wenchao Zhao, Bo Dang, Weimin Wang

---

## 💡 一句话要点

**提出基于改进ResNet34的脑肿瘤分类方法，以提升医学图像分类效率与精度。**

**关键词**: `脑肿瘤分类` `ResNet34改进` `多尺度特征提取` `通道注意力机制` `医学图像分析`

## 📋 核心要点

1. 核心问题：脑肿瘤医学图像手动分类耗时费力，浅层卷积网络精度不足。
2. 方法要点：以ResNet34为骨干，集成多尺度特征提取、Inception v2模块和通道注意力机制。
3. 实验或效果：五折交叉实验平均分类准确率约98.8%，参数减少至原模型80%。

## 📄 摘要（原文）

> Previously, image interpretation in radiology relied heavily on manual methods. However, manual classification of brain tumor medical images is time-consuming and labor-intensive. Even with shallow convolutional neural network models, the accuracy is not ideal. To improve the efficiency and accuracy of brain tumor image classification, this paper proposes a brain tumor classification model based on an improved ResNet34 network. This model uses the ResNet34 residual network as the backbone network and incorporates multi-scale feature extraction. It uses a multi-scale input module as the first layer of the ResNet34 network and an Inception v2 module as the residual downsampling layer. Furthermore, a channel attention mechanism module assigns different weights to different channels of the image from a channel domain perspective, obtaining more important feature information. The results after a five-fold crossover experiment show that the average classification accuracy of the improved network model is approximately 98.8%, which is not only 1% higher than ResNet34, but also only 80% of the number of parameters of the original model. Therefore, the improved network model not only improves accuracy but also reduces clutter, achieving a classification effect with fewer parameters and higher accuracy.

