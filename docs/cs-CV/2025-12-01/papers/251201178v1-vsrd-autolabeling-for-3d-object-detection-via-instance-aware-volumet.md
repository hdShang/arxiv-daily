---
layout: default
title: VSRD++: Autolabeling for 3D Object Detection via Instance-Aware Volumetric Silhouette Rendering
---

# VSRD++: Autolabeling for 3D Object Detection via Instance-Aware Volumetric Silhouette Rendering

**arXiv**: [2512.01178v1](https://arxiv.org/abs/2512.01178) | [PDF](https://arxiv.org/pdf/2512.01178.pdf)

**作者**: Zihua Liu, Hiroki Sakuma, Masatoshi Okutomi

---

## 💡 一句话要点

**提出VSRD++，通过实例感知体积轮廓渲染实现弱监督单目3D目标检测，减少对3D标注的依赖。**

**关键词**: `单目3D目标检测` `弱监督学习` `体积渲染` `自动标注` `动态场景处理`

## 📋 核心要点

1. 核心问题：单目3D目标检测依赖大量3D标注，标注成本高且耗时。
2. 方法要点：使用两阶段流程，包括多视图3D自动标注和单目检测器训练，基于SDF和RDF优化3D边界框。
3. 实验或效果：在KITTI-360数据集上显著优于现有弱监督方法，适用于静态和动态场景。

## 📄 摘要（原文）

> Monocular 3D object detection is a fundamental yet challenging task in 3D scene understanding. Existing approaches heavily depend on supervised learning with extensive 3D annotations, which are often acquired from LiDAR point clouds through labor-intensive labeling processes. To tackle this problem, we propose VSRD++, a novel weakly supervised framework for monocular 3D object detection that eliminates the reliance on 3D annotations and leverages neural-field-based volumetric rendering with weak 2D supervision. VSRD++ consists of a two-stage pipeline: multi-view 3D autolabeling and subsequent monocular 3D detector training. In the multi-view autolabeling stage, object surfaces are represented as signed distance fields (SDFs) and rendered as instance masks via the proposed instance-aware volumetric silhouette rendering. To optimize 3D bounding boxes, we decompose each instance's SDF into a cuboid SDF and a residual distance field (RDF) that captures deviations from the cuboid. To address the geometry inconsistency commonly observed in volume rendering methods applied to dynamic objects, we model the dynamic objects by including velocity into bounding box attributes as well as assigning confidence to each pseudo-label. Moreover, we also employ a 3D attribute initialization module to initialize the dynamic bounding box parameters. In the monocular 3D object detection phase, the optimized 3D bounding boxes serve as pseudo labels for training monocular 3D object detectors. Extensive experiments on the KITTI-360 dataset demonstrate that VSRD++ significantly outperforms existing weakly supervised approaches for monocular 3D object detection on both static and dynamic scenes. Code is available at https://github.com/Magicboomliu/VSRD_plus_plus

