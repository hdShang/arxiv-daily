---
layout: default
title: CompEvent: Complex-valued Event-RGB Fusion for Low-light Video Enhancement and Deblurring
---

# CompEvent: Complex-valued Event-RGB Fusion for Low-light Video Enhancement and Deblurring

**arXiv**: [2511.14469v1](https://arxiv.org/abs/2511.14469) | [PDF](https://arxiv.org/pdf/2511.14469.pdf)

**作者**: Mingchen Zhong, Xin Lu, Dong Li, Senyan Xu, Ruixuan Jiang, Xueyang Fu, Baocai Yin

---

## 💡 一句话要点

**提出CompEvent框架，通过复值神经网络融合事件与RGB数据，解决低光视频去模糊问题。**

**关键词**: `低光视频增强` `事件相机融合` `复值神经网络` `视频去模糊` `时空融合`

## 📋 核心要点

1. 核心问题：低光视频中光照不足和运动模糊导致去模糊困难，影响夜间监控和自动驾驶应用。
2. 方法要点：采用复值时序对齐GRU和空间-频率学习模块，实现事件与RGB数据的全流程融合。
3. 实验或效果：在广泛实验中，CompEvent优于现有先进方法，代码已开源。

## 📄 摘要（原文）

> Low-light video deblurring poses significant challenges in applications like nighttime surveillance and autonomous driving due to dim lighting and long exposures. While event cameras offer potential solutions with superior low-light sensitivity and high temporal resolution, existing fusion methods typically employ staged strategies, limiting their effectiveness against combined low-light and motion blur degradations. To overcome this, we propose CompEvent, a complex neural network framework enabling holistic full-process fusion of event data and RGB frames for enhanced joint restoration. CompEvent features two core components: 1) Complex Temporal Alignment GRU, which utilizes complex-valued convolutions and processes video and event streams iteratively via GRU to achieve temporal alignment and continuous fusion; and 2) Complex Space-Frequency Learning module, which performs unified complex-valued signal processing in both spatial and frequency domains, facilitating deep fusion through spatial structures and system-level characteristics. By leveraging the holistic representation capability of complex-valued neural networks, CompEvent achieves full-process spatiotemporal fusion, maximizes complementary learning between modalities, and significantly strengthens low-light video deblurring capability. Extensive experiments demonstrate that CompEvent outperforms SOTA methods in addressing this challenging task. The code is available at https://github.com/YuXie1/CompEvent.

