---
layout: default
title: CNN-Based Camera Pose Estimation and Localisation of Scan Images for Aircraft Visual Inspection
---

# CNN-Based Camera Pose Estimation and Localisation of Scan Images for Aircraft Visual Inspection

**arXiv**: [2511.18702v1](https://arxiv.org/abs/2511.18702) | [PDF](https://arxiv.org/pdf/2511.18702.pdf)

**作者**: Xueyan Oh, Leonard Loh, Shaohui Foong, Zhong Bao Andy Koh, Kow Leong Ng, Poh Kang Tan, Pei Lin Pearlin Toh, U-Xuan Tan

---

## 💡 一句话要点

**提出基于CNN的相机姿态估计方法，用于飞机视觉检查中的图像定位。**

**关键词**: `相机姿态估计` `卷积神经网络` `飞机视觉检查` `图像定位` `合成数据训练`

## 📋 核心要点

1. 核心问题：飞机视觉检查中，无基础设施的相机姿态估计在户外环境受限。
2. 方法要点：使用合成图像微调CNN，结合几何损失函数预测相机姿态。
3. 实验或效果：真实飞机实验显示姿态估计误差小于0.24米和2度。

## 📄 摘要（原文）

> General Visual Inspection is a manual inspection process regularly used to detect and localise obvious damage on the exterior of commercial aircraft. There has been increasing demand to perform this process at the boarding gate to minimise the downtime of the aircraft and automating this process is desired to reduce the reliance on human labour. Automating this typically requires estimating a camera's pose with respect to the aircraft for initialisation but most existing localisation methods require infrastructure, which is very challenging in uncontrolled outdoor environments and within the limited turnover time (approximately 2 hours) on an airport tarmac. Additionally, many airlines and airports do not allow contact with the aircraft's surface or using UAVs for inspection between flights, and restrict access to commercial aircraft. Hence, this paper proposes an on-site method that is infrastructure-free and easy to deploy for estimating a pan-tilt-zoom camera's pose and localising scan images. This method initialises using the same pan-tilt-zoom camera used for the inspection task by utilising a Deep Convolutional Neural Network fine-tuned on only synthetic images to predict its own pose. We apply domain randomisation to generate the dataset for fine-tuning the network and modify its loss function by leveraging aircraft geometry to improve accuracy. We also propose a workflow for initialisation, scan path planning, and precise localisation of images captured from a pan-tilt-zoom camera. We evaluate and demonstrate our approach through experiments with real aircraft, achieving root-mean-square camera pose estimation errors of less than 0.24 m and 2 degrees for all real scenes.

