---
layout: default
title: Driving in Spikes: An Entropy-Guided Object Detector for Spike Cameras
---

# Driving in Spikes: An Entropy-Guided Object Detector for Spike Cameras

**arXiv**: [2511.15459v1](https://arxiv.org/abs/2511.15459) | [PDF](https://arxiv.org/pdf/2511.15459.pdf)

**作者**: Ziyan Liu, Qi Su, Lulu Tang, Zhaofei Yu, Tiejun Huang

---

## 💡 一句话要点

**提出EASD检测器以解决自动驾驶中尖峰相机对象检测的稀疏数据挑战**

**关键词**: `尖峰相机检测` `熵引导注意力` `双分支网络` `自动驾驶视觉` `模拟基准数据集`

## 📋 核心要点

1. 核心问题：尖峰相机输出稀疏离散，标准图像检测器无法处理，导致端到端检测困难。
2. 方法要点：采用双分支设计，包括全局语义融合分支和熵选择注意力分支。
3. 实验或效果：引入DSEC Spike基准，填补数据空白，提升检测性能。

## 📄 摘要（原文）

> Object detection in autonomous driving suffers from motion blur and saturation under fast motion and extreme lighting. Spike cameras, offer microsecond latency and ultra high dynamic range for object detection by using per pixel asynchronous integrate and fire. However, their sparse, discrete output cannot be processed by standard image-based detectors, posing a critical challenge for end to end spike stream detection. We propose EASD, an end to end spike camera detector with a dual branch design: a Temporal Based Texture plus Feature Fusion branch for global cross slice semantics, and an Entropy Selective Attention branch for object centric details. To close the data gap, we introduce DSEC Spike, the first driving oriented simulated spike detection benchmark.

