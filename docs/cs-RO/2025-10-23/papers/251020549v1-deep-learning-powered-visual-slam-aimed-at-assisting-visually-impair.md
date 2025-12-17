---
layout: default
title: Deep Learning-Powered Visual SLAM Aimed at Assisting Visually Impaired Navigation
---

# Deep Learning-Powered Visual SLAM Aimed at Assisting Visually Impaired Navigation

**arXiv**: [2510.20549v1](https://arxiv.org/abs/2510.20549) | [PDF](https://arxiv.org/pdf/2510.20549.pdf)

**作者**: Marziyeh Bamdad, Hans-Peter Hutter, Alireza Darvishy

---

## 💡 一句话要点

**提出SELM-SLAM3以增强视觉SLAM在挑战性条件下的导航辅助**

**关键词**: `视觉SLAM` `深度学习增强` `特征提取` `导航辅助` `鲁棒性优化`

## 📋 核心要点

1. 核心问题：SLAM在低纹理、运动模糊等挑战条件下定位精度和跟踪稳定性不足
2. 方法要点：集成SuperPoint和LightGlue进行鲁棒特征提取与匹配
3. 实验或效果：在多个数据集上平均优于ORB-SLAM3 87.84%，提升导航可靠性

## 📄 摘要（原文）

> Despite advancements in SLAM technologies, robust operation under challenging
> conditions such as low-texture, motion-blur, or challenging lighting remains an
> open challenge. Such conditions are common in applications such as assistive
> navigation for the visually impaired. These challenges undermine localization
> accuracy and tracking stability, reducing navigation reliability and safety. To
> overcome these limitations, we present SELM-SLAM3, a deep learning-enhanced
> visual SLAM framework that integrates SuperPoint and LightGlue for robust
> feature extraction and matching. We evaluated our framework using TUM RGB-D,
> ICL-NUIM, and TartanAir datasets, which feature diverse and challenging
> scenarios. SELM-SLAM3 outperforms conventional ORB-SLAM3 by an average of
> 87.84% and exceeds state-of-the-art RGB-D SLAM systems by 36.77%. Our framework
> demonstrates enhanced performance under challenging conditions, such as
> low-texture scenes and fast motion, providing a reliable platform for
> developing navigation aids for the visually impaired.

