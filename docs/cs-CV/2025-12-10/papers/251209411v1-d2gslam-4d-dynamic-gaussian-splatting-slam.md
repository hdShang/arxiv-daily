---
layout: default
title: D$^2$GSLAM: 4D Dynamic Gaussian Splatting SLAM
---

# D$^2$GSLAM: 4D Dynamic Gaussian Splatting SLAM

**arXiv**: [2512.09411v1](https://arxiv.org/abs/2512.09411) | [PDF](https://arxiv.org/pdf/2512.09411.pdf)

**作者**: Siting Zhu, Yuxiang Huang, Wenhua Wu, Chaokang Jiang, Yongbo Chen, I-Ming Chen, Hesheng Wang

---

## 💡 一句话要点

**提出D²GSLAM系统，利用高斯表示在动态环境中同时实现准确动态重建与稳健跟踪。**

**关键词**: `动态SLAM` `高斯表示` `动静复合建模` `几何一致性` `相机跟踪` `动态重建`

## 📋 核心要点

1. 核心问题：动态环境中密集SLAM挑战，现有方法忽略动态物体运动信息。
2. 方法要点：结合几何提示动态分离、动静复合表示、渐进姿态优化和运动一致性损失。
3. 实验或效果：在动态场景中展示优越的建图和跟踪精度，支持准确动态建模。

## 📄 摘要（原文）

> Recent advances in Dense Simultaneous Localization and Mapping (SLAM) have demonstrated remarkable performance in static environments. However, dense SLAM in dynamic environments remains challenging. Most methods directly remove dynamic objects and focus solely on static scene reconstruction, which ignores the motion information contained in these dynamic objects. In this paper, we present D$^2$GSLAM, a novel dynamic SLAM system utilizing Gaussian representation, which simultaneously performs accurate dynamic reconstruction and robust tracking within dynamic environments. Our system is composed of four key components: (i) We propose a geometric-prompt dynamic separation method to distinguish between static and dynamic elements of the scene. This approach leverages the geometric consistency of Gaussian representation and scene geometry to obtain coarse dynamic regions. The regions then serve as prompts to guide the refinement of the coarse mask for achieving accurate motion mask. (ii) To facilitate accurate and efficient mapping of the dynamic scene, we introduce dynamic-static composite representation that integrates static 3D Gaussians with dynamic 4D Gaussians. This representation allows for modeling the transitions between static and dynamic states of objects in the scene for composite mapping and optimization. (iii) We employ a progressive pose refinement strategy that leverages both the multi-view consistency of static scene geometry and motion information from dynamic objects to achieve accurate camera tracking. (iv) We introduce a motion consistency loss, which leverages the temporal continuity in object motions for accurate dynamic modeling. Our D$^2$GSLAM demonstrates superior performance on dynamic scenes in terms of mapping and tracking accuracy, while also showing capability in accurate dynamic modeling.

