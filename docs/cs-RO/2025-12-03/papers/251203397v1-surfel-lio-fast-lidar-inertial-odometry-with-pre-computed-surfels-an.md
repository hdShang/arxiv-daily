---
layout: default
title: Surfel-LIO: Fast LiDAR-Inertial Odometry with Pre-computed Surfels and Hierarchical Z-order Voxel Hashing
---

# Surfel-LIO: Fast LiDAR-Inertial Odometry with Pre-computed Surfels and Hierarchical Z-order Voxel Hashing

**arXiv**: [2512.03397v1](https://arxiv.org/abs/2512.03397) | [PDF](https://arxiv.org/pdf/2512.03397.pdf)

**作者**: Seungwon Choi, Dong-Gyu Park, Seo-Yeon Hwang, Tae-Wan Kim

---

## 💡 一句话要点

**提出Surfel-LIO，通过预计算面元与分层Z序体素哈希，实现快速激光雷达-惯性里程计。**

**关键词**: `激光雷达-惯性里程计` `面元表示` `分层体素哈希` `Z序曲线编码` `实时状态估计`

## 📋 核心要点

1. 核心问题：现有LIO系统在最近邻搜索和平面参数重复计算上效率不足。
2. 方法要点：采用分层体素结构预计算面元，结合Z序曲线编码，实现O(1)对应检索。
3. 实验或效果：在M3DGR数据集上，处理速度显著提升，同时保持可比状态估计精度。

## 📄 摘要（原文）

> LiDAR-inertial odometry (LIO) is an active research area, as it enables accurate real-time state estimation in GPS-denied environments. Recent advances in map data structures and spatial indexing have significantly improved the efficiency of LIO systems. Nevertheless, we observe that two aspects may still leave room for improvement: (1) nearest neighbor search often requires examining multiple spatial units to gather sufficient points for plane fitting, and (2) plane parameters are typically recomputed at every iteration despite unchanged map geometry. Motivated by these observations, we propose Surfel-LIO, which employs a hierarchical voxel structure (hVox) with pre-computed surfel representation. This design enables O(1) correspondence retrieval without runtime neighbor enumeration or plane fitting, combined with Z-order curve encoding for cache-friendly spatial indexing. Experimental results on the M3DGR dataset demonstrate that our method achieves significantly faster processing speed compared to recent state-of-the-art methods while maintaining comparable state estimation accuracy. Our implementation is publicly available at https://github.com/93won/lidar_inertial_odometry.

