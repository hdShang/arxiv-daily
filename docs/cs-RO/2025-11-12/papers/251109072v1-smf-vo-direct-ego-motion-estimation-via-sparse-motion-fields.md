---
layout: default
title: SMF-VO: Direct Ego-Motion Estimation via Sparse Motion Fields
---

# SMF-VO: Direct Ego-Motion Estimation via Sparse Motion Fields

**arXiv**: [2511.09072v1](https://arxiv.org/abs/2511.09072) | [PDF](https://arxiv.org/pdf/2511.09072.pdf)

**作者**: Sangheon Yang, Yeongin Yoon, Hong Mo Jung, Jongwoo Lim

---

## 💡 一句话要点

**提出SMF-VO稀疏运动场视觉里程计，以轻量方式估计相机运动，适用于移动设备。**

**关键词**: `视觉里程计` `稀疏运动场` `轻量框架` `实时估计` `移动机器人`

## 📋 核心要点

1. 传统视觉里程计依赖姿态中心范式，计算量大，限制实时性能。
2. SMF-VO直接从稀疏光流估计瞬时线性和角速度，无需显式姿态估计。
3. 在基准数据集上效率高，Raspberry Pi 5上超100 FPS，精度具竞争力。

## 📄 摘要（原文）

> Traditional Visual Odometry (VO) and Visual Inertial Odometry (VIO) methods rely on a 'pose-centric' paradigm, which computes absolute camera poses from the local map thus requires large-scale landmark maintenance and continuous map optimization. This approach is computationally expensive, limiting their real-time performance on resource-constrained devices. To overcome these limitations, we introduce Sparse Motion Field Visual Odometry (SMF-VO), a lightweight, 'motion-centric' framework. Our approach directly estimates instantaneous linear and angular velocity from sparse optical flow, bypassing the need for explicit pose estimation or expensive landmark tracking. We also employed a generalized 3D ray-based motion field formulation that works accurately with various camera models, including wide-field-of-view lenses. SMF-VO demonstrates superior efficiency and competitive accuracy on benchmark datasets, achieving over 100 FPS on a Raspberry Pi 5 using only a CPU. Our work establishes a scalable and efficient alternative to conventional methods, making it highly suitable for mobile robotics and wearable devices.

