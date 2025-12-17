---
layout: default
title: CuSfM: CUDA-Accelerated Structure-from-Motion
---

# CuSfM: CUDA-Accelerated Structure-from-Motion

**arXiv**: [2510.15271v1](https://arxiv.org/abs/2510.15271) | [PDF](https://arxiv.org/pdf/2510.15271.pdf)

**作者**: Jingrui Yu, Jun Liu, Kefei Ren, Joydeep Biswas, Rurui Ye, Keqiang Wu, Chirag Majithia, Di Zeng

---

## 💡 一句话要点

**提出CUDA加速的离线SfM系统以提升自主导航和机器人感知中的相机位姿估计效率与精度**

**关键词**: `结构从运动` `GPU加速` `相机位姿估计` `离线处理` `机器人感知` `开源实现`

## 📋 核心要点

1. 核心问题：离线SfM中相机位姿估计的计算效率与精度不足，影响密集重建应用。
2. 方法要点：利用GPU并行化加速特征提取，生成非冗余数据关联，优化相机位姿与地图。
3. 实验或效果：相比COLMAP，在多种场景下显著提升处理速度和精度，保持全局一致性。

## 📄 摘要（原文）

> Efficient and accurate camera pose estimation forms the foundational
> requirement for dense reconstruction in autonomous navigation, robotic
> perception, and virtual simulation systems. This paper addresses the challenge
> via cuSfM, a CUDA-accelerated offline Structure-from-Motion system that
> leverages GPU parallelization to efficiently employ computationally intensive
> yet highly accurate feature extractors, generating comprehensive and
> non-redundant data associations for precise camera pose estimation and globally
> consistent mapping. The system supports pose optimization, mapping, prior-map
> localization, and extrinsic refinement. It is designed for offline processing,
> where computational resources can be fully utilized to maximize accuracy.
> Experimental results demonstrate that cuSfM achieves significantly improved
> accuracy and processing speed compared to the widely used COLMAP method across
> various testing scenarios, while maintaining the high precision and global
> consistency essential for offline SfM applications. The system is released as
> an open-source Python wrapper implementation, PyCuSfM, available at
> https://github.com/nvidia-isaac/pyCuSFM, to facilitate research and
> applications in computer vision and robotics.

