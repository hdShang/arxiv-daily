---
layout: default
title: DriveFlow: Rectified Flow Adaptation for Robust 3D Object Detection in Autonomous Driving
---

# DriveFlow: Rectified Flow Adaptation for Robust 3D Object Detection in Autonomous Driving

**arXiv**: [2511.18713v1](https://arxiv.org/abs/2511.18713) | [PDF](https://arxiv.org/pdf/2511.18713.pdf)

**作者**: Hongbin Lin, Yiming Yang, Chaoda Zheng, Yifan Zhang, Shuaicheng Niu, Zilu Guo, Yafeng Li, Gui Gui, Shuguang Cui, Zhen Li

---

## 💡 一句话要点

**提出DriveFlow方法，通过整流流适应增强训练数据，以解决自动驾驶中3D物体检测的分布外鲁棒性问题。**

**关键词**: `自动驾驶` `3D物体检测` `整流流` `训练数据增强` `分布外鲁棒性` `频率分解`

## 📋 核心要点

1. 核心问题：自动驾驶视觉3D检测中，训练数据覆盖不足导致分布外场景性能下降。
2. 方法要点：基于频率分解，引入高频前景保持和双频背景优化策略，适配无噪声编辑路径。
3. 实验或效果：在分布外场景中，所有类别均实现全面性能提升，验证方法有效高效。

## 📄 摘要（原文）

> In autonomous driving, vision-centric 3D object detection recognizes and localizes 3D objects from RGB images. However, due to high annotation costs and diverse outdoor scenes, training data often fails to cover all possible test scenarios, known as the out-of-distribution (OOD) issue. Training-free image editing offers a promising solution for improving model robustness by training data enhancement without any modifications to pre-trained diffusion models. Nevertheless, inversion-based methods often suffer from limited effectiveness and inherent inaccuracies, while recent rectified-flow-based approaches struggle to preserve objects with accurate 3D geometry. In this paper, we propose DriveFlow, a Rectified Flow Adaptation method for training data enhancement in autonomous driving based on pre-trained Text-to-Image flow models. Based on frequency decomposition, DriveFlow introduces two strategies to adapt noise-free editing paths derived from text-conditioned velocities. 1) High-Frequency Foreground Preservation: DriveFlow incorporates a high-frequency alignment loss for foreground to maintain precise 3D object geometry. 2) Dual-Frequency Background Optimization: DriveFlow also conducts dual-frequency optimization for background, balancing editing flexibility and semantic consistency. Comprehensive experiments validate the effectiveness and efficiency of DriveFlow, demonstrating comprehensive performance improvements on all categories across OOD scenarios. Code is available at https://github.com/Hongbin98/DriveFlow.

