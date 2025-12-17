---
layout: default
title: MCAQ-YOLO: Morphological Complexity-Aware Quantization for Efficient Object Detection with Curriculum Learning
---

# MCAQ-YOLO: Morphological Complexity-Aware Quantization for Efficient Object Detection with Curriculum Learning

**arXiv**: [2511.12976v1](https://arxiv.org/abs/2511.12976) | [PDF](https://arxiv.org/pdf/2511.12976.pdf)

**作者**: Yoonjae Seo, Ermal Elbasani, Jaehong Lee

---

## 💡 一句话要点

**提出形态复杂度感知量化方法以提升受限计算场景下的目标检测效率**

**关键词**: `目标检测` `神经网络量化` `形态复杂度感知` `课程学习` `空间自适应量化` `高效视觉识别`

## 📋 核心要点

1. 核心问题：均匀量化忽略视觉数据空间异质性，导致检测精度下降。
2. 方法要点：基于形态学指标动态分配比特，结合课程学习稳定训练。
3. 实验效果：在安全装备数据集上，mAP@0.5达85.6%，优于均匀量化。

## 📄 摘要（原文）

> Most neural network quantization methods apply uniform bit precision across spatial regions, ignoring the heterogeneous structural and textural complexity of visual data. This paper introduces MCAQ-YOLO, a morphological complexity-aware quantization framework for object detection. The framework employs five morphological metrics - fractal dimension, texture entropy, gradient variance, edge density, and contour complexity - to characterize local visual morphology and guide spatially adaptive bit allocation. By correlating these metrics with quantization sensitivity, MCAQ-YOLO dynamically adjusts bit precision according to spatial complexity. In addition, a curriculum-based quantization-aware training scheme progressively increases quantization difficulty to stabilize optimization and accelerate convergence. Experimental results demonstrate a strong correlation between morphological complexity and quantization sensitivity and show that MCAQ-YOLO achieves superior detection accuracy and convergence efficiency compared with uniform quantization. On a safety equipment dataset, MCAQ-YOLO attains 85.6 percent mAP@0.5 with an average of 4.2 bits and a 7.6x compression ratio, yielding 3.5 percentage points higher mAP than uniform 4-bit quantization while introducing only 1.8 ms of additional runtime overhead per image. Cross-dataset validation on COCO and Pascal VOC further confirms consistent performance gains, indicating that morphology-driven spatial quantization can enhance efficiency and robustness for computationally constrained, safety-critical visual recognition tasks.

