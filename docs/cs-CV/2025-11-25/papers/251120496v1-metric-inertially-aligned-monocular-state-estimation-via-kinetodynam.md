---
layout: default
title: Metric, inertially aligned monocular state estimation via kinetodynamic priors
---

# Metric, inertially aligned monocular state estimation via kinetodynamic priors

**arXiv**: [2511.20496v1](https://arxiv.org/abs/2511.20496) | [PDF](https://arxiv.org/pdf/2511.20496.pdf)

**作者**: Jiaxin Liu, Min Li, Wanting Xu, Liang Li, Jiaqi Yang, Laurent Kneip

---

## 💡 一句话要点

**提出基于动力学先验的单目状态估计方法，以解决非刚性机器人系统的姿态估计问题。**

**关键词**: `非刚性状态估计` `单目视觉里程计` `动力学先验` `B样条运动模型` `MLP学习`

## 📋 核心要点

1. 核心问题：非刚性机器人系统因结构变形，无法应用刚体假设进行准确状态估计。
2. 方法要点：使用MLP学习变形-力模型，结合B样条运动模型和牛顿第二定律建立物理链接。
3. 实验或效果：在弹簧-相机系统上验证，实现度量尺度和重力恢复，提升单目视觉里程计鲁棒性。

## 📄 摘要（原文）

> Accurate state estimation for flexible robotic systems poses significant challenges, particular for platforms with dynamically deforming structures that invalidate rigid-body assumptions. This paper tackles this problem and allows to extend existing rigid-body pose estimation methods to non-rigid systems. Our approach hinges on two core assumptions: first, the elastic properties are captured by an injective deformation-force model, efficiently learned via a Multi-Layer Perceptron; second, we solve the platform's inherently smooth motion using continuous-time B-spline kinematic models. By continuously applying Newton's Second Law, our method establishes a physical link between visually-derived trajectory acceleration and predicted deformation-induced acceleration. We demonstrate that our approach not only enables robust and accurate pose estimation on non-rigid platforms, but that the properly modeled platform physics instigate inertial sensing properties. We demonstrate this feasibility on a simple spring-camera system, and show how it robustly resolves the typically ill-posed problem of metric scale and gravity recovery in monocular visual odometry.

