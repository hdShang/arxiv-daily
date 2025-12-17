---
layout: default
title: GroundLoc: Efficient Large-Scale Outdoor LiDAR-Only Localization
---

# GroundLoc: Efficient Large-Scale Outdoor LiDAR-Only Localization

**arXiv**: [2510.24623v1](https://arxiv.org/abs/2510.24623) | [PDF](https://arxiv.org/pdf/2510.24623.pdf)

**作者**: Nicolai Steinke, Daniel Goehring

---

## 💡 一句话要点

**提出GroundLoc以在大规模室外环境中实现高效LiDAR-only定位**

**关键词**: `LiDAR定位` `鸟瞰图投影` `关键点识别` `地图配准` `多传感器支持` `大规模室外环境`

## 📋 核心要点

1. 核心问题：大规模室外环境下移动机器人的LiDAR-only定位，依赖先验地图。
2. 方法要点：使用BEV图像投影和R2D2或SIFT进行关键点选择与地图配准。
3. 实验或效果：在多个数据集上优于SOTA，ATE低于50厘米，支持多种传感器。

## 📄 摘要（原文）

> In this letter, we introduce GroundLoc, a LiDAR-only localization pipeline
> designed to localize a mobile robot in large-scale outdoor environments using
> prior maps. GroundLoc employs a Bird's-Eye View (BEV) image projection focusing
> on the perceived ground area and utilizes the place recognition network R2D2,
> or alternatively, the non-learning approach Scale-Invariant Feature Transform
> (SIFT), to identify and select keypoints for BEV image map registration. Our
> results demonstrate that GroundLoc outperforms state-of-the-art methods on the
> SemanticKITTI and HeLiPR datasets across various sensors. In the multi-session
> localization evaluation, GroundLoc reaches an Average Trajectory Error (ATE)
> well below 50 cm on all Ouster OS2 128 sequences while meeting online runtime
> requirements. The system supports various sensor models, as evidenced by
> evaluations conducted with Velodyne HDL-64E, Ouster OS2 128, Aeva Aeries II,
> and Livox Avia sensors. The prior maps are stored as 2D raster image maps,
> which can be created from a single drive and require only 4 MB of storage per
> square kilometer. The source code is available at
> https://github.com/dcmlr/groundloc.

