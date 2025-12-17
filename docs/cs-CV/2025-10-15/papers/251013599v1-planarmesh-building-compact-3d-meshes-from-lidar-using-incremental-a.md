---
layout: default
title: PlanarMesh: Building Compact 3D Meshes from LiDAR using Incremental Adaptive Resolution Reconstruction
---

# PlanarMesh: Building Compact 3D Meshes from LiDAR using Incremental Adaptive Resolution Reconstruction

**arXiv**: [2510.13599v1](https://arxiv.org/abs/2510.13599) | [PDF](https://arxiv.org/pdf/2510.13599.pdf)

**作者**: Jiahao Wang, Nived Chebrolu, Yifu Tao, Lintong Zhang, Ayoung Kim, Maurice Fallon

---

## 💡 一句话要点

**提出PlanarMesh系统，通过自适应分辨率重建实现紧凑实时3D LiDAR建图**

**关键词**: `3D LiDAR建图` `自适应网格重建` `实时系统` `平面建模` `多线程架构` `紧凑表示`

## 📋 核心要点

1. 核心问题：在线3D LiDAR建图需平衡计算效率与表面重建细节
2. 方法要点：结合平面建模与网格化，增量更新基于曲率和自由空间信息
3. 实验效果：精度优于或持平SOTA，输出文件小10倍以上，实时运行约2Hz

## 📄 摘要（原文）

> Building an online 3D LiDAR mapping system that produces a detailed surface
> reconstruction while remaining computationally efficient is a challenging task.
> In this paper, we present PlanarMesh, a novel incremental, mesh-based LiDAR
> reconstruction system that adaptively adjusts mesh resolution to achieve
> compact, detailed reconstructions in real-time. It introduces a new
> representation, planar-mesh, which combines plane modeling and meshing to
> capture both large surfaces and detailed geometry. The planar-mesh can be
> incrementally updated considering both local surface curvature and free-space
> information from sensor measurements. We employ a multi-threaded architecture
> with a Bounding Volume Hierarchy (BVH) for efficient data storage and fast
> search operations, enabling real-time performance. Experimental results show
> that our method achieves reconstruction accuracy on par with, or exceeding,
> state-of-the-art techniques-including truncated signed distance functions,
> occupancy mapping, and voxel-based meshing-while producing smaller output file
> sizes (10 times smaller than raw input and more than 5 times smaller than
> mesh-based methods) and maintaining real-time performance (around 2 Hz for a
> 64-beam sensor).

