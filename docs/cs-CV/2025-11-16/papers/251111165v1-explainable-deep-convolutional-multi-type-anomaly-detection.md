---
layout: default
title: Explainable Deep Convolutional Multi-Type Anomaly Detection
---

# Explainable Deep Convolutional Multi-Type Anomaly Detection

**arXiv**: [2511.11165v1](https://arxiv.org/abs/2511.11165) | [PDF](https://arxiv.org/pdf/2511.11165.pdf)

**作者**: Alex George, Lyudmila Mihaylova, Sean Anderson

---

## 💡 一句话要点

**提出MultiTypeFCDD框架以解决轻量级可解释多类型异常检测问题**

**关键词**: `多类型异常检测` `可解释深度学习` `轻量卷积框架` `图像级标签学习` `多通道热图`

## 📋 核心要点

1. 核心问题：现有方法无法区分异常类型且需为每个对象类别训练单独模型
2. 方法要点：使用图像级标签学习多通道热图，每个通道对应特定异常类型
3. 实验或效果：在Real-IAD数据集上表现与复杂模型相当，参数和推理时间显著减少

## 📄 摘要（原文）

> Most explainable anomaly detection methods often identify anomalies but lack the capability to differentiate the type of anomaly. Furthermore, they often require the costly training and maintenance of separate models for each object category. The lack of specificity is a significant research gap, as identifying the type of anomaly (e.g., "Crack" vs. "Scratch") is crucial for accurate diagnosis that facilitates cost-saving operational decisions across diverse application domains. While some recent large-scale Vision-Language Models (VLMs) have begun to address this, they are computationally intensive and memory-heavy, restricting their use in real-time or embedded systems. We propose MultiTypeFCDD, a simple and lightweight convolutional framework designed as a practical alternative for explainable multi-type anomaly detection. MultiTypeFCDD uses only image-level labels to learn and produce multi-channel heatmaps, where each channel is trained to correspond to a specific anomaly type. The model functions as a single, unified framework capable of differentiating anomaly types across multiple object categories, eliminating the need to train and manage separate models for each object category. We evaluated our proposed method on the Real-IAD dataset and it delivers results competitive with state-of-the-art complex models at significantly reduced parametric load and inference times. This makes it a highly practical and viable solution for real-world applications where computational resources are tightly constrained.

