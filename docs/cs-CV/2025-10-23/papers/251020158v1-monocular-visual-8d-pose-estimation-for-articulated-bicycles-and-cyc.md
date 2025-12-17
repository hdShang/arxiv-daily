---
layout: default
title: Monocular Visual 8D Pose Estimation for Articulated Bicycles and Cyclists
---

# Monocular Visual 8D Pose Estimation for Articulated Bicycles and Cyclists

**arXiv**: [2510.20158v1](https://arxiv.org/abs/2510.20158) | [PDF](https://arxiv.org/pdf/2510.20158.pdf)

**作者**: Eduardo R. Corral-Soto, Yang Liu, Yuan Ren, Bai Dongfeng, Liu Bingbing

---

## 💡 一句话要点

**提出单目视觉8D姿态估计方法，用于自动驾驶中铰接自行车和骑行者的精细姿态估计。**

**关键词**: `单目视觉姿态估计` `铰接物体建模` `自动驾驶安全` `类别级姿态估计` `关键点检测`

## 📋 核心要点

1. 核心问题：铰接自行车姿态变化导致3D边界框和方向不准确，6D姿态估计不足以捕捉转向/踏板角度。
2. 方法要点：从单RGB图像估计自行车3D平移、旋转及转向和踏板相对于车体的旋转。
3. 实验或效果：使用合成和真实数据训练，在真实图像上评估，与先进6D姿态估计器相比表现竞争性。

## 📄 摘要（原文）

> In Autonomous Driving, cyclists belong to the safety-critical class of
> Vulnerable Road Users (VRU), and accurate estimation of their pose is critical
> for cyclist crossing intention classification, behavior prediction, and
> collision avoidance. Unlike rigid objects, articulated bicycles are composed of
> movable rigid parts linked by joints and constrained by a kinematic structure.
> 6D pose methods can estimate the 3D rotation and translation of rigid bicycles,
> but 6D becomes insufficient when the steering/pedals angles of the bicycle
> vary. That is because: 1) varying the articulated pose of the bicycle causes
> its 3D bounding box to vary as well, and 2) the 3D box orientation is not
> necessarily aligned to the orientation of the steering which determines the
> actual intended travel direction. In this work, we introduce a method for
> category-level 8D pose estimation for articulated bicycles and cyclists from a
> single RGB image. Besides being able to estimate the 3D translation and
> rotation of a bicycle from a single image, our method also estimates the
> rotations of its steering handles and pedals with respect to the bicycle body
> frame. These two new parameters enable the estimation of a more fine-grained
> bicycle pose state and travel direction. Our proposed model jointly estimates
> the 8D pose and the 3D Keypoints of articulated bicycles, and trains with a mix
> of synthetic and real image data to generalize on real images. We include an
> evaluation section where we evaluate the accuracy of our estimated 8D pose
> parameters, and our method shows promising results by achieving competitive
> scores when compared against state-of-the-art category-level 6D pose estimators
> that use rigid canonical object templates for matching.

