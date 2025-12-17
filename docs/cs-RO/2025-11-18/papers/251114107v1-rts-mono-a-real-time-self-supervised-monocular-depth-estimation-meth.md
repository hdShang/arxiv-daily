---
layout: default
title: RTS-Mono: A Real-Time Self-Supervised Monocular Depth Estimation Method for Real-World Deployment
---

# RTS-Mono: A Real-Time Self-Supervised Monocular Depth Estimation Method for Real-World Deployment

**arXiv**: [2511.14107v1](https://arxiv.org/abs/2511.14107) | [PDF](https://arxiv.org/pdf/2511.14107.pdf)

**作者**: Zeyu Cheng, Tongfei Liu, Tao Lei, Xiang Hua, Yi Zhang, Chengkai Tang

---

## 💡 一句话要点

**提出RTS-Mono实时自监督单目深度估计方法，解决计算资源消耗大问题，适用于自动驾驶部署。**

**关键词**: `自监督学习` `单目深度估计` `实时计算` `轻量模型` `自动驾驶` `编码器-解码器架构`

## 📋 核心要点

1. 核心问题：现有单目深度估计模型计算资源消耗大，性能与效率难以兼顾。
2. 方法要点：采用轻量编码器-解码器架构，多尺度稀疏融合减少冗余，提升推理速度。
3. 实验效果：在KITTI数据集上参数仅3M，精度提升，Nvidia Jetson Orin上达49 FPS实时推理。

## 📄 摘要（原文）

> Depth information is crucial for autonomous driving and intelligent robot navigation. The simplicity and flexibility of self-supervised monocular depth estimation are conducive to its role in these fields. However, most existing monocular depth estimation models consume many computing resources. Although some methods have reduced the model's size and improved computing efficiency, the performance deteriorates, seriously hindering the real-world deployment of self-supervised monocular depth estimation models in the real world. To address this problem, we proposed a real-time self-supervised monocular depth estimation method and implemented it in the real world. It is called RTS-Mono, which is a lightweight and efficient encoder-decoder architecture. The encoder is based on Lite-Encoder, and the decoder is designed with a multi-scale sparse fusion framework to minimize redundancy, ensure performance, and improve inference speed. RTS-Mono achieved state-of-the-art (SoTA) performance in high and low resolutions with extremely low parameter counts (3 M) in experiments based on the KITTI dataset. Compared with lightweight methods, RTS-Mono improved Abs Rel and Sq Rel by 5.6% and 9.8% at low resolution and improved Sq Rel and RMSE by 6.1% and 1.9% at high resolution. In real-world deployment experiments, RTS-Mono has extremely high accuracy and can perform real-time inference on Nvidia Jetson Orin at a speed of 49 FPS. Source code is available at https://github.com/ZYCheng777/RTS-Mono.

