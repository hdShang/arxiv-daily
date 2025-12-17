---
layout: default
title: Is Image-based Object Pose Estimation Ready to Support Grasping?
---

# Is Image-based Object Pose Estimation Ready to Support Grasping?

**arXiv**: [2512.01856v1](https://arxiv.org/abs/2512.01856) | [PDF](https://arxiv.org/pdf/2512.01856.pdf)

**作者**: Eric C. Joyce, Qianwen Zhao, Nathaniel Burgdorfer, Long Wang, Philippos Mordohai

---

## 💡 一句话要点

**提出基于单RGB图像的6-DoF物体姿态估计框架，评估其在机器人抓取中的适用性。**

**关键词**: `6-DoF姿态估计` `机器人抓取` `单RGB图像` `物理模拟` `BOP数据集` `开源估计器`

## 📋 核心要点

1. 核心问题：评估单RGB图像物体姿态估计器能否作为机器人抓取的唯一感知机制。
2. 方法要点：在物理模拟器中，使用姿态估计指导平行夹爪和欠驱动机器人手抓取物体。
3. 实验或效果：基于BOP数据集子集比较五种开源估计器，填补文献空白。

## 📄 摘要（原文）

> We present a framework for evaluating 6-DoF instance-level object pose estimators, focusing on those that require a single RGB (not RGB-D) image as input. Besides gaining intuition about how accurate these estimators are, we are interested in the degree to which they can serve as the sole perception mechanism for robotic grasping. To assess this, we perform grasping trials in a physics-based simulator, using image-based pose estimates to guide a parallel gripper and an underactuated robotic hand in picking up 3D models of objects. Our experiments on a subset of the BOP (Benchmark for 6D Object Pose Estimation) dataset compare five open-source object pose estimators and provide insights that were missing from the literature.

