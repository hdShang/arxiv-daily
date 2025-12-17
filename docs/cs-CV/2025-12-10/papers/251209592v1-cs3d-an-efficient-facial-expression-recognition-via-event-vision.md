---
layout: default
title: CS3D: An Efficient Facial Expression Recognition via Event Vision
---

# CS3D: An Efficient Facial Expression Recognition via Event Vision

**arXiv**: [2512.09592v1](https://arxiv.org/abs/2512.09592) | [PDF](https://arxiv.org/pdf/2512.09592.pdf)

**作者**: Zhe Wang, Qijin Song, Yucen Peng, Weibang Bai

---

## 💡 一句话要点

**提出CS3D框架以解决事件相机面部表情识别中的计算复杂性和能耗问题**

**关键词**: `事件相机` `面部表情识别` `计算效率` `时空注意力` `边缘计算`

## 📋 核心要点

1. 核心问题：事件相机面部表情识别中，传统深度学习方法计算复杂、能耗高，难以部署于边缘设备
2. 方法要点：通过分解C3D方法降低计算复杂度，结合软脉冲神经元和时空注意力机制增强信息保留能力
3. 实验或效果：在多个数据集上，CS3D比RNN、Transformer和C3D等架构精度更高，能耗仅为原C3D的21.97%

## 📄 摘要（原文）

> Responsive and accurate facial expression recognition is crucial to human-robot interaction for daily service robots. Nowadays, event cameras are becoming more widely adopted as they surpass RGB cameras in capturing facial expression changes due to their high temporal resolution, low latency, computational efficiency, and robustness in low-light conditions. Despite these advantages, event-based approaches still encounter practical challenges, particularly in adopting mainstream deep learning models. Traditional deep learning methods for facial expression analysis are energy-intensive, making them difficult to deploy on edge computing devices and thereby increasing costs, especially for high-frequency, dynamic, event vision-based approaches. To address this challenging issue, we proposed the CS3D framework by decomposing the Convolutional 3D method to reduce the computational complexity and energy consumption. Additionally, by utilizing soft spiking neurons and a spatial-temporal attention mechanism, the ability to retain information is enhanced, thus improving the accuracy of facial expression detection. Experimental results indicate that our proposed CS3D method attains higher accuracy on multiple datasets compared to architectures such as the RNN, Transformer, and C3D, while the energy consumption of the CS3D method is just 21.97\% of the original C3D required on the same device.

