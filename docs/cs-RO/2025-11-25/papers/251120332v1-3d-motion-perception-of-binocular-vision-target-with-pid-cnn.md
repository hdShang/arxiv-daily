---
layout: default
title: 3D Motion Perception of Binocular Vision Target with PID-CNN
---

# 3D Motion Perception of Binocular Vision Target with PID-CNN

**arXiv**: [2511.20332v1](https://arxiv.org/abs/2511.20332) | [PDF](https://arxiv.org/pdf/2511.20332.pdf)

**作者**: Shi Jiazhao, Pan Pan, Shi Haotian

---

## 💡 一句话要点

**提出PID-CNN以感知双目视觉目标的三维运动信息**

**关键词**: `三维运动感知` `PID卷积神经网络` `双目视觉` `特征复用` `高维卷积`

## 📋 核心要点

1. 核心问题：实时感知双目视觉目标的三维坐标、速度和加速度
2. 方法要点：设计17层PID卷积网络，结合特征复用和PID视角分析非线性拟合
3. 实验或效果：在模拟数据集上预测精度接近输入图像分辨率上限

## 📄 摘要（原文）

> This article trained a network for perceiving three-dimensional motion information of binocular vision target, which can provide real-time three-dimensional coordinate, velocity, and acceleration, and has a basic spatiotemporal perception capability. Understood the ability of neural networks to fit nonlinear problems from the perspective of PID. Considered a single-layer neural network as using a second-order difference equation and a nonlinearity to describe a local problem. Multilayer networks gradually transform the raw representation to the desired representation through multiple such combinations. Analysed some reference principles for designing neural networks. Designed a relatively small PID convolutional neural network, with a total of 17 layers and 413 thousand parameters. Implemented a simple but practical feature reuse method by concatenation and pooling. The network was trained and tested using the simulated randomly moving ball datasets, and the experimental results showed that the prediction accuracy was close to the upper limit that the input image resolution can represent. Analysed the experimental results and errors, as well as the existing shortcomings and possible directions for improvement. Finally, discussed the advantages of high-dimensional convolution in improving computational efficiency and feature space utilization. As well as the potential advantages of using PID information to implement memory and attention mechanisms.

