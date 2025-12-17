---
layout: default
title: DReX: Pure Vision Fusion of Self-Supervised and Convolutional Representations for Image Complexity Prediction
---

# DReX: Pure Vision Fusion of Self-Supervised and Convolutional Representations for Image Complexity Prediction

**arXiv**: [2511.16991v1](https://arxiv.org/abs/2511.16991) | [PDF](https://arxiv.org/pdf/2511.16991.pdf)

**作者**: Jonathan Skaza, Parsa Madinei, Ziqi Wen, Miguel Eckstein

---

## 💡 一句话要点

**提出DReX融合自监督与卷积表示，用于图像复杂度预测。**

**关键词**: `图像复杂度预测` `特征融合` `自监督学习` `卷积神经网络` `注意力机制`

## 📋 核心要点

1. 核心问题：视觉复杂度预测，应用于图像压缩和认知科学。
2. 方法要点：融合ResNet-50和DINOv3特征，使用注意力机制。
3. 实验效果：在IC9600基准上达到SOTA，参数减少21.5倍。

## 📄 摘要（原文）

> Visual complexity prediction is a fundamental problem in computer vision with applications in image compression, retrieval, and classification. Understanding what makes humans perceive an image as complex is also a long-standing question in cognitive science. Recent approaches have leveraged multimodal models that combine visual and linguistic representations, but it remains unclear whether language information is necessary for this task. We propose DReX (DINO-ResNet Fusion), a vision-only model that fuses self-supervised and convolutional representations through a learnable attention mechanism to predict image complexity. Our architecture integrates multi-scale hierarchical features from ResNet-50 with semantically rich representations from DINOv3 ViT-S/16, enabling the model to capture both low-level texture patterns and high-level semantic structure. DReX achieves state-of-the-art performance on the IC9600 benchmark (Pearson r = 0.9581), surpassing previous methods--including those trained on multimodal image-text data--while using approximately 21.5x fewer learnable parameters. Furthermore, DReX generalizes robustly across multiple datasets and metrics, achieving superior results on Pearson and Spearman correlation, Root Mean Square Error (RMSE), and Mean Absolute Error (MAE). Ablation and attention analyses confirm that DReX leverages complementary cues from both backbones, with the DINOv3 [CLS] token enhancing sensitivity to visual complexity. Our findings suggest that visual features alone can be sufficient for human-aligned complexity prediction and that, when properly fused, self-supervised transformers and supervised deep convolutional neural networks offer complementary and synergistic benefits for this task.

