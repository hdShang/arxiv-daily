---
layout: default
title: CylinderDepth: Cylindrical Spatial Attention for Multi-View Consistent Self-Supervised Surround Depth Estimation
---

# CylinderDepth: Cylindrical Spatial Attention for Multi-View Consistent Self-Supervised Surround Depth Estimation

**arXiv**: [2511.16428v1](https://arxiv.org/abs/2511.16428) | [PDF](https://arxiv.org/pdf/2511.16428.pdf)

**作者**: Samer Abualhanud, Christian Grannemann, Max Mehltretter

---

## 💡 一句话要点

**提出圆柱空间注意力方法以解决多视角深度估计不一致问题**

**关键词**: `自监督深度估计` `多视角一致性` `圆柱投影` `空间注意力` `360度感知`

## 📋 核心要点

1. 核心问题：多视角图像深度估计在重叠区域不一致，影响360度感知
2. 方法要点：将3D点投影到共享圆柱，应用非学习空间注意力聚合跨图像特征
3. 实验或效果：在DDAD和nuScenes数据集上提升深度一致性和整体精度

## 📄 摘要（原文）

> Self-supervised surround-view depth estimation enables dense, low-cost 3D perception with a 360° field of view from multiple minimally overlapping images. Yet, most existing methods suffer from depth estimates that are inconsistent between overlapping images. Addressing this limitation, we propose a novel geometry-guided method for calibrated, time-synchronized multi-camera rigs that predicts dense, metric, and cross-view-consistent depth. Given the intrinsic and relative orientation parameters, a first depth map is predicted per image and the so-derived 3D points from all images are projected onto a shared unit cylinder, establishing neighborhood relations across different images. This produces a 2D position map for every image, where each pixel is assigned its projected position on the cylinder. Based on these position maps, we apply an explicit, non-learned spatial attention that aggregates features among pixels across images according to their distances on the cylinder, to predict a final depth map per image. Evaluated on the DDAD and nuScenes datasets, our approach improves the consistency of depth estimates across images and the overall depth compared to state-of-the-art methods.

