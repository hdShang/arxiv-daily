---
layout: default
title: Performance Evaluation of Transfer Learning Based Medical Image Classification Techniques for Disease Detection
---

# Performance Evaluation of Transfer Learning Based Medical Image Classification Techniques for Disease Detection

**arXiv**: [2512.04397v1](https://arxiv.org/abs/2512.04397) | [PDF](https://arxiv.org/pdf/2512.04397.pdf)

**作者**: Zeeshan Ahmad, Shudi Bao, Meng Chen

---

## 💡 一句话要点

**评估迁移学习在医学图像分类中的性能，为疾病检测提供模型选择依据**

**关键词**: `医学图像分类` `迁移学习` `深度学习` `疾病检测` `模型评估` `胸部X光`

## 📋 核心要点

1. 核心问题：医学图像分类中训练大型深度学习模型从零开始通常不可行，需借助迁移学习技术。
2. 方法要点：使用六个预训练模型（如AlexNet、VGG16、ResNet系列、InceptionV3）在自定义胸部X光数据集上进行疾病检测分类。
3. 实验或效果：InceptionV3在所有标准指标上表现最佳，ResNet系列随深度增加性能提升，迁移学习在数据有限时尤其有益。

## 📄 摘要（原文）

> Medical image classification plays an increasingly vital role in identifying various diseases by classifying medical images, such as X-rays, MRIs and CT scans, into different categories based on their features. In recent years, deep learning techniques have attracted significant attention in medical image classification. However, it is usually infeasible to train an entire large deep learning model from scratch. To address this issue, one of the solutions is the transfer learning (TL) technique, where a pre-trained model is reused for a new task. In this paper, we present a comprehensive analysis of TL techniques for medical image classification using deep convolutional neural networks. We evaluate six pre-trained models (AlexNet, VGG16, ResNet18, ResNet34, ResNet50, and InceptionV3) on a custom chest X-ray dataset for disease detection. The experimental results demonstrate that InceptionV3 consistently outperforms other models across all the standard metrics. The ResNet family shows progressively better performance with increasing depth, whereas VGG16 and AlexNet perform reasonably well but with lower accuracy. In addition, we also conduct uncertainty analysis and runtime comparison to assess the robustness and computational efficiency of these models. Our findings reveal that TL is beneficial in most cases, especially with limited data, but the extent of improvement depends on several factors such as model architecture, dataset size, and domain similarity between source and target tasks. Moreover, we demonstrate that with a well-trained feature extractor, only a lightweight feedforward model is enough to provide efficient prediction. As such, this study contributes to the understanding of TL in medical image classification, and provides insights for selecting appropriate models based on specific requirements.

