---
layout: default
title: Training Feature Attribution for Vision Models
---

# Training Feature Attribution for Vision Models

**arXiv**: [2510.09135v1](https://arxiv.org/abs/2510.09135) | [PDF](https://arxiv.org/pdf/2510.09135.pdf)

**作者**: Aziz Bacha, Thomas George

---

## 💡 一句话要点

**提出训练特征归因方法，联合分析测试预测与训练图像区域，提升视觉模型可解释性。**

**关键词**: `训练特征归因` `视觉模型可解释性` `深度神经网络` `测试预测归因` `虚假相关性检测`

## 📋 核心要点

1. 核心问题：深度神经网络被视为黑盒，需可解释性方法增强信任与问责。
2. 方法要点：联合归因测试预测到特定训练图像区域，提供细粒度解释。
3. 实验或效果：在视觉数据集上识别有害样本和虚假相关性，优于传统方法。

## 📄 摘要（原文）

> Deep neural networks are often considered opaque systems, prompting the need
> for explainability methods to improve trust and accountability. Existing
> approaches typically attribute test-time predictions either to input features
> (e.g., pixels in an image) or to influential training examples. We argue that
> both perspectives should be studied jointly. This work explores *training
> feature attribution*, which links test predictions to specific regions of
> specific training images and thereby provides new insights into the inner
> workings of deep models. Our experiments on vision datasets show that training
> feature attribution yields fine-grained, test-specific explanations: it
> identifies harmful examples that drive misclassifications and reveals spurious
> correlations, such as patch-based shortcuts, that conventional attribution
> methods fail to expose.

