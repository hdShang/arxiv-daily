---
layout: default
title: Exploring Surround-View Fisheye Camera 3D Object Detection
---

# Exploring Surround-View Fisheye Camera 3D Object Detection

**arXiv**: [2511.18695v1](https://arxiv.org/abs/2511.18695) | [PDF](https://arxiv.org/pdf/2511.18695.pdf)

**作者**: Changcai Li, Wenwei Lin, Zuoxun Hou, Gang Chen, Wei Zhang, Huihui Zhou, Weishi Zheng

---

## 💡 一句话要点

**提出FisheyeBEVDet和FisheyePETR方法，提升环视鱼眼相机3D目标检测精度**

**关键词**: `鱼眼相机3D检测` `环视系统` `球面表示` `BEV检测` `查询检测` `合成数据集`

## 📋 核心要点

1. 核心问题：经典针孔相机3D检测器在鱼眼图像上性能下降
2. 方法要点：采用球面空间表示整合鱼眼几何到BEV和查询框架
3. 实验效果：在Fisheye3DOD数据集上精度提升最高6.2%

## 📄 摘要（原文）

> In this work, we explore the technical feasibility of implementing end-to-end 3D object detection (3DOD) with surround-view fisheye camera system. Specifically, we first investigate the performance drop incurred when transferring classic pinhole-based 3D object detectors to fisheye imagery. To mitigate this, we then develop two methods that incorporate the unique geometry of fisheye images into mainstream detection frameworks: one based on the bird's-eye-view (BEV) paradigm, named FisheyeBEVDet, and the other on the query-based paradigm, named FisheyePETR. Both methods adopt spherical spatial representations to effectively capture fisheye geometry. In light of the lack of dedicated evaluation benchmarks, we release Fisheye3DOD, a new open dataset synthesized using CARLA and featuring both standard pinhole and fisheye camera arrays. Experiments on Fisheye3DOD show that our fisheye-compatible modeling improves accuracy by up to 6.2% over baseline methods.

