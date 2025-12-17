---
layout: default
title: Cycle-Sync: Robust Global Camera Pose Estimation through Enhanced Cycle-Consistent Synchronization
---

# Cycle-Sync: Robust Global Camera Pose Estimation through Enhanced Cycle-Consistent Synchronization

**arXiv**: [2511.02329v1](https://arxiv.org/abs/2511.02329) | [PDF](https://arxiv.org/pdf/2511.02329.pdf)

**作者**: Shaohan Li, Yunpeng Shi, Gilad Lerman

---

## 💡 一句话要点

**提出Cycle-Sync框架，通过增强循环一致性实现鲁棒全局相机位姿估计**

**关键词**: `相机位姿估计` `循环一致性` `消息传递最小二乘法` `鲁棒优化` `全局同步` `结构从运动`

## 📋 核心要点

1. 核心问题：相机位姿估计中旋转和位置的全局鲁棒同步，避免依赖束调整。
2. 方法要点：改进消息传递最小二乘法，强调循环一致性，引入Welsch型鲁棒损失。
3. 实验效果：在合成和真实数据集上优于现有位姿估计器，包括带束调整的SfM流程。

## 📄 摘要（原文）

> We introduce Cycle-Sync, a robust and global framework for estimating camera
> poses (both rotations and locations). Our core innovation is a location solver
> that adapts message-passing least squares (MPLS) -- originally developed for
> group synchronization -- to camera location estimation. We modify MPLS to
> emphasize cycle-consistent information, redefine cycle consistencies using
> estimated distances from previous iterations, and incorporate a Welsch-type
> robust loss. We establish the strongest known deterministic exact-recovery
> guarantee for camera location estimation, showing that cycle consistency alone
> -- without access to inter-camera distances -- suffices to achieve the lowest
> sample complexity currently known. To further enhance robustness, we introduce
> a plug-and-play outlier rejection module inspired by robust subspace recovery,
> and we fully integrate cycle consistency into MPLS for rotation
> synchronization. Our global approach avoids the need for bundle adjustment.
> Experiments on synthetic and real datasets show that Cycle-Sync consistently
> outperforms leading pose estimators, including full structure-from-motion
> pipelines with bundle adjustment.

