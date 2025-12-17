---
layout: default
title: HitoMi-Cam: A Shape-Agnostic Person Detection Method Using the Spectral Characteristics of Clothing
---

# HitoMi-Cam: A Shape-Agnostic Person Detection Method Using the Spectral Characteristics of Clothing

**arXiv**: [2511.08908v1](https://arxiv.org/abs/2511.08908) | [PDF](https://arxiv.org/pdf/2511.08908.pdf)

**作者**: Shuji Ono

---

## 💡 一句话要点

**提出HitoMi-Cam光谱检测方法，以解决形状依赖问题，适用于救援等实时边缘设备场景。**

**关键词**: `光谱检测` `形状无关检测` `边缘计算` `实时处理` `人体检测` `救援场景`

## 📋 核心要点

1. 核心问题：CNN检测器对训练数据外的姿态形状依赖，导致性能下降。
2. 方法要点：利用衣物光谱反射特性，实现轻量级、形状无关的人体检测。
3. 实验效果：在模拟救援场景中，平均精度达93.5%，处理速度23.2 fps。

## 📄 摘要（原文）

> While convolutional neural network (CNN)-based object detection is widely used, it exhibits a shape dependency that degrades performance for postures not included in the training data. Building upon our previous simulation study published in this journal, this study implements and evaluates the spectral-based approach on physical hardware to address this limitation. Specifically, this paper introduces HitoMi-Cam, a lightweight and shape-agnostic person detection method that uses the spectral reflectance properties of clothing. The author implemented the system on a resource-constrained edge device without a GPU to assess its practical viability. The results indicate that a processing speed of 23.2 frames per second (fps) (253x190 pixels) is achievable, suggesting that the method can be used for real-time applications. In a simulated search and rescue scenario where the performance of CNNs declines, HitoMi-Cam achieved an average precision (AP) of 93.5%, surpassing that of the compared CNN models (best AP of 53.8%). Throughout all evaluation scenarios, the occurrence of false positives remained minimal. This study positions the HitoMi-Cam method not as a replacement for CNN-based detectors but as a complementary tool under specific conditions. The results indicate that spectral-based person detection can be a viable option for real-time operation on edge devices in real-world environments where shapes are unpredictable, such as disaster rescue.

