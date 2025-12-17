---
layout: default
title: Integration of Visual SLAM into Consumer-Grade Automotive Localization
---

# Integration of Visual SLAM into Consumer-Grade Automotive Localization

**arXiv**: [2511.06919v1](https://arxiv.org/abs/2511.06919) | [PDF](https://arxiv.org/pdf/2511.06919.pdf)

**作者**: Luis Diener, Jens Kalkkuhl, Markus Enzweiler

---

## 💡 一句话要点

**提出融合视觉SLAM与车辆动力学模型的框架，以改进消费级汽车定位性能**

**关键词**: `视觉SLAM` `汽车定位` `传感器融合` `陀螺仪校准` `车辆动力学模型`

## 📋 核心要点

1. 核心问题：消费级汽车依赖本体感知传感器，存在系统误差和校准限制，影响定位精度
2. 方法要点：融合视觉SLAM与横向车辆动力学模型，实现在线陀螺仪校准
3. 实验或效果：在专有和公共数据集上验证，定位精度优于现有方法

## 📄 摘要（原文）

> Accurate ego-motion estimation in consumer-grade vehicles currently relies on
> proprioceptive sensors, i.e. wheel odometry and IMUs, whose performance is
> limited by systematic errors and calibration. While visual-inertial SLAM has
> become a standard in robotics, its integration into automotive ego-motion
> estimation remains largely unexplored. This paper investigates how visual SLAM
> can be integrated into consumer-grade vehicle localization systems to improve
> performance. We propose a framework that fuses visual SLAM with a lateral
> vehicle dynamics model to achieve online gyroscope calibration under realistic
> driving conditions. Experimental results demonstrate that vision-based
> integration significantly improves gyroscope calibration accuracy and thus
> enhances overall localization performance, highlighting a promising path toward
> higher automotive localization accuracy. We provide results on both proprietary
> and public datasets, showing improved performance and superior localization
> accuracy on a public benchmark compared to state-of-the-art methods.

