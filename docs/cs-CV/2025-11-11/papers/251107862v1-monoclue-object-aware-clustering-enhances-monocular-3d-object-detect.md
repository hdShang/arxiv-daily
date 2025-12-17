---
layout: default
title: MonoCLUE : Object-Aware Clustering Enhances Monocular 3D Object Detection
---

# MonoCLUE : Object-Aware Clustering Enhances Monocular 3D Object Detection

**arXiv**: [2511.07862v1](https://arxiv.org/abs/2511.07862) | [PDF](https://arxiv.org/pdf/2511.07862.pdf)

**作者**: Sunghun Yang, Minhyeok Lee, Jungho Lee, Sangyoun Lee

---

## 💡 一句话要点

**提出MonoCLUE以增强单目3D目标检测，通过对象感知聚类和场景记忆解决遮挡与视野限制问题。**

**关键词**: `单目3D目标检测` `对象感知聚类` `场景记忆` `视觉特征增强` `KITTI基准`

## 📋 核心要点

1. 核心问题：单目3D检测因深度模糊和视野限制，在遮挡或截断场景中准确性下降。
2. 方法要点：使用K-means聚类视觉特征捕获对象部分，并构建跨图像场景记忆提升特征一致性。
3. 实验或效果：在KITTI基准测试中实现领先性能，提升遮挡和低可见度下的检测鲁棒性。

## 📄 摘要（原文）

> Monocular 3D object detection offers a cost-effective solution for autonomous driving but suffers from ill-posed depth and limited field of view. These constraints cause a lack of geometric cues and reduced accuracy in occluded or truncated scenes. While recent approaches incorporate additional depth information to address geometric ambiguity, they overlook the visual cues crucial for robust recognition. We propose MonoCLUE, which enhances monocular 3D detection by leveraging both local clustering and generalized scene memory of visual features. First, we perform K-means clustering on visual features to capture distinct object-level appearance parts (e.g., bonnet, car roof), improving detection of partially visible objects. The clustered features are propagated across regions to capture objects with similar appearances. Second, we construct a generalized scene memory by aggregating clustered features across images, providing consistent representations that generalize across scenes. This improves object-level feature consistency, enabling stable detection across varying environments. Lastly, we integrate both local cluster features and generalized scene memory into object queries, guiding attention toward informative regions. Exploiting a unified local clustering and generalized scene memory strategy, MonoCLUE enables robust monocular 3D detection under occlusion and limited visibility, achieving state-of-the-art performance on the KITTI benchmark.

