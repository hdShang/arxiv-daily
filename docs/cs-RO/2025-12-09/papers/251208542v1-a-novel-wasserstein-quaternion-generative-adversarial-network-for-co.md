---
layout: default
title: A Novel Wasserstein Quaternion Generative Adversarial Network for Color Image Generation
---

# A Novel Wasserstein Quaternion Generative Adversarial Network for Color Image Generation

**arXiv**: [2512.08542v1](https://arxiv.org/abs/2512.08542) | [PDF](https://arxiv.org/pdf/2512.08542.pdf)

**作者**: Zhigang Jia, Duan Wang, Hengkai Wang, Yajun Xie, Meixiang Zhao, Xiaoyu Zhao

---

## 💡 一句话要点

**提出基于四元数Wasserstein距离的生成对抗网络，以解决彩色图像生成中的通道相关性和数据分布问题。**

**关键词**: `彩色图像生成` `四元数Wasserstein距离` `生成对抗网络` `数据分布理论` `通道相关性` `强对偶形式`

## 📋 核心要点

1. 核心问题：现有彩色图像生成模型忽略颜色通道相关性，可能导致色差，且缺乏系统理论衡量不同数据集分布。
2. 方法要点：定义新四元数Wasserstein距离并发展对偶理论，利用四元数凸集分离定理和Farkas引理推导强对偶形式，构建Wasserstein四元数生成对抗网络。
3. 实验或效果：实验表明该模型在生成效率和图像质量上超越传统（四元数）生成对抗网络和Wasserstein生成对抗网络。

## 📄 摘要（原文）

> Color image generation has a wide range of applications, but the existing generation models ignore the correlation among color channels, which may lead to chromatic aberration problems. In addition, the data distribution problem of color images has not been systematically elaborated and explained, so that there is still the lack of the theory about measuring different color images datasets. In this paper, we define a new quaternion Wasserstein distance and develop its dual theory. To deal with the quaternion linear programming problem, we derive the strong duality form with helps of quaternion convex set separation theorem and quaternion Farkas lemma. With using quaternion Wasserstein distance, we propose a novel Wasserstein quaternion generative adversarial network. Experiments demonstrate that this novel model surpasses both the (quaternion) generative adversarial networks and the Wasserstein generative adversarial network in terms of generation efficiency and image quality.

