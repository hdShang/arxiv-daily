---
layout: default
title: TrackingWorld: World-centric Monocular 3D Tracking of Almost All Pixels
---

# TrackingWorld: World-centric Monocular 3D Tracking of Almost All Pixels

**arXiv**: [2512.08358v1](https://arxiv.org/abs/2512.08358) | [PDF](https://arxiv.org/pdf/2512.08358.pdf)

**作者**: Jiahao Lu, Weitao Xiong, Jiacheng Deng, Peng Li, Tianyu Huang, Zhiyang Dou, Cheng Lin, Sai-Kit Yeung, Yuan Liu

---

## 💡 一句话要点

**提出TrackingWorld以解决单目3D跟踪中相机运动分离和新动态物体密集跟踪问题**

**关键词**: `单目3D跟踪` `世界中心坐标系` `密集跟踪` `相机运动分离` `动态物体跟踪` `优化框架`

## 📋 核心要点

1. 核心问题：现有方法难以分离相机运动与前景动态运动，且无法密集跟踪视频中新出现的动态物体。
2. 方法要点：通过跟踪上采样器提升稀疏2D轨迹为密集轨迹，优化框架将密集2D轨迹反投影到世界中心3D坐标系。
3. 实验或效果：在合成和真实数据集上评估，系统在世界中心坐标系中实现准确密集的3D跟踪。

## 📄 摘要（原文）

> Monocular 3D tracking aims to capture the long-term motion of pixels in 3D space from a single monocular video and has witnessed rapid progress in recent years. However, we argue that the existing monocular 3D tracking methods still fall short in separating the camera motion from foreground dynamic motion and cannot densely track newly emerging dynamic subjects in the videos. To address these two limitations, we propose TrackingWorld, a novel pipeline for dense 3D tracking of almost all pixels within a world-centric 3D coordinate system. First, we introduce a tracking upsampler that efficiently lifts the arbitrary sparse 2D tracks into dense 2D tracks. Then, to generalize the current tracking methods to newly emerging objects, we apply the upsampler to all frames and reduce the redundancy of 2D tracks by eliminating the tracks in overlapped regions. Finally, we present an efficient optimization-based framework to back-project dense 2D tracks into world-centric 3D trajectories by estimating the camera poses and the 3D coordinates of these 2D tracks. Extensive evaluations on both synthetic and real-world datasets demonstrate that our system achieves accurate and dense 3D tracking in a world-centric coordinate frame.

