---
layout: default
title: DQ3D: Depth-guided Query for Transformer-Based 3D Object Detection in Traffic Scenarios
---

# DQ3D: Depth-guided Query for Transformer-Based 3D Object Detection in Traffic Scenarios

**arXiv**: [2510.23144v1](https://arxiv.org/abs/2510.23144) | [PDF](https://arxiv.org/pdf/2510.23144.pdf)

**作者**: Ziyu Wang, Wenhao Li, Ji Wu

---

## 💡 一句话要点

**提出深度引导查询生成器以解决交通场景中3D物体检测的误检问题**

**关键词**: `3D物体检测` `深度引导查询` `交通场景` `混合注意力机制` `nuScenes数据集`

## 📋 核心要点

1. 核心问题：现有方法中3D参考点可能远离目标物体，导致误检。
2. 方法要点：利用深度信息和2D检测，从物体表面或内部采样参考点。
3. 实验或效果：在nuScenes数据集上，mAP和NDS分别提升6.3%和4.3%。

## 📄 摘要（原文）

> 3D object detection from multi-view images in traffic scenarios has garnered
> significant attention in recent years. Many existing approaches rely on object
> queries that are generated from 3D reference points to localize objects.
> However, a limitation of these methods is that some reference points are often
> far from the target object, which can lead to false positive detections. In
> this paper, we propose a depth-guided query generator for 3D object detection
> (DQ3D) that leverages depth information and 2D detections to ensure that
> reference points are sampled from the surface or interior of the object.
> Furthermore, to address partially occluded objects in current frame, we
> introduce a hybrid attention mechanism that fuses historical detection results
> with depth-guided queries, thereby forming hybrid queries. Evaluation on the
> nuScenes dataset demonstrates that our method outperforms the baseline by 6.3\%
> in terms of mean Average Precision (mAP) and 4.3\% in the NuScenes Detection
> Score (NDS).

