---
layout: default
title: Dendritic Convolution for Noise Image Recognition
---

# Dendritic Convolution for Noise Image Recognition

**arXiv**: [2511.18699v1](https://arxiv.org/abs/2511.18699) | [PDF](https://arxiv.org/pdf/2511.18699.pdf)

**作者**: Jiarui Xue, Dongjian Yang, Ye Sun, Gang Liu

---

## 💡 一句话要点

**提出树突卷积以解决噪声图像识别问题**

**关键词**: `树突卷积` `噪声图像识别` `特征提取` `生物启发计算` `图像分类` `目标检测`

## 📋 核心要点

1. 图像识别中噪声干扰严重，现有方法抗噪性能已达瓶颈
2. 模仿神经元树突结构，通过非线性交互重构特征提取数学范式
3. 在分类和检测任务中，准确率和mAP分别提升11.23%和19.80%

## 📄 摘要（原文）

> In real-world scenarios of image recognition, there exists substantial noise interference. Existing works primarily focus on methods such as adjusting networks or training strategies to address noisy image recognition, and the anti-noise performance has reached a bottleneck. However, little is known about the exploration of anti-interference solutions from a neuronal perspective.This paper proposes an anti-noise neuronal convolution. This convolution mimics the dendritic structure of neurons, integrates the neighborhood interaction computation logic of dendrites into the underlying design of convolutional operations, and simulates the XOR logic preprocessing function of biological dendrites through nonlinear interactions between input features, thereby fundamentally reconstructing the mathematical paradigm of feature extraction. Unlike traditional convolution where noise directly interferes with feature extraction and exerts a significant impact, DDC mitigates the influence of noise by focusing on the interaction of neighborhood information. Experimental results demonstrate that in image classification tasks (using YOLOv11-cls, VGG16, and EfficientNet-B0) and object detection tasks (using YOLOv11, YOLOv8, and YOLOv5), after replacing traditional convolution with the dendritic convolution, the accuracy of the EfficientNet-B0 model on noisy datasets is relatively improved by 11.23%, and the mean Average Precision (mAP) of YOLOv8 is increased by 19.80%. The consistency between the computation method of this convolution and the dendrites of biological neurons enables it to perform significantly better than traditional convolution in complex noisy environments.

