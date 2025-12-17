---
layout: default
title: Valeo Near-Field: a novel dataset for pedestrian intent detection
---

# Valeo Near-Field: a novel dataset for pedestrian intent detection

**arXiv**: [2510.15673v1](https://arxiv.org/abs/2510.15673) | [PDF](https://arxiv.org/pdf/2510.15673.pdf)

**作者**: Antonyo Musabini, Rachid Benmokhtar, Jagdish Bhanushali, Victor Galizzi, Bertrand Luvison, Xavier Perrotton

---

## 💡 一句话要点

**提出Valeo Near-Field数据集以解决近场行人意图检测问题**

**关键词**: `行人意图检测` `多模态数据集` `3D姿态估计` `近场感知` `嵌入式基准`

## 📋 核心要点

1. 核心问题：在动态环境中检测行人接近自车时的意图，应对传感器遮挡和硬件限制。
2. 方法要点：提供多模态同步数据，包括鱼眼相机、激光雷达、超声波和3D身体姿态。
3. 实验或效果：发布基准套件和基线性能，支持嵌入式系统评估，促进算法开发。

## 📄 摘要（原文）

> This paper presents a novel dataset aimed at detecting pedestrians'
> intentions as they approach an ego-vehicle. The dataset comprises synchronized
> multi-modal data, including fisheye camera feeds, lidar laser scans, ultrasonic
> sensor readings, and motion capture-based 3D body poses, collected across
> diverse real-world scenarios. Key contributions include detailed annotations of
> 3D body joint positions synchronized with fisheye camera images, as well as
> accurate 3D pedestrian positions extracted from lidar data, facilitating robust
> benchmarking for perception algorithms. We release a portion of the dataset
> along with a comprehensive benchmark suite, featuring evaluation metrics for
> accuracy, efficiency, and scalability on embedded systems. By addressing
> real-world challenges such as sensor occlusions, dynamic environments, and
> hardware constraints, this dataset offers a unique resource for developing and
> evaluating state-of-the-art algorithms in pedestrian detection, 3D pose
> estimation and 4D trajectory and intention prediction. Additionally, we provide
> baseline performance metrics using custom neural network architectures and
> suggest future research directions to encourage the adoption and enhancement of
> the dataset. This work aims to serve as a foundation for researchers seeking to
> advance the capabilities of intelligent vehicles in near-field scenarios.

