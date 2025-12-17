---
layout: default
title: DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management
---

# DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management

**arXiv**: [2511.23030v1](https://arxiv.org/abs/2511.23030) | [PDF](https://arxiv.org/pdf/2511.23030.pdf)

**作者**: Casimir Feldmann, Maximum Wilder-Smith, Vaishakh Patil, Michael Oechsle, Michael Niemeyer, Keisuke Tateno, Marco Hutter

---

## 💡 一句话要点

**提出DiskChunGS，通过分块内存管理实现大规模3D高斯SLAM，克服GPU内存限制。**

**关键词**: `3D高斯SLAM` `内存管理` `外核方法` `场景分块` `大规模重建` `实时渲染`

## 📋 核心要点

1. 核心问题：3D高斯SLAM受GPU内存限制，难以重建大规模场景。
2. 方法要点：采用外核方法，将场景分块，仅GPU内存中保留活跃区域，非活跃区域存储于磁盘。
3. 实验或效果：在室内、城市驾驶及资源受限平台验证，完成所有KITTI序列，无内存故障，视觉质量优越。

## 📄 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have demonstrated impressive results for novel view synthesis with real-time rendering capabilities. However, integrating 3DGS with SLAM systems faces a fundamental scalability limitation: methods are constrained by GPU memory capacity, restricting reconstruction to small-scale environments. We present DiskChunGS, a scalable 3DGS SLAM system that overcomes this bottleneck through an out-of-core approach that partitions scenes into spatial chunks and maintains only active regions in GPU memory while storing inactive areas on disk. Our architecture integrates seamlessly with existing SLAM frameworks for pose estimation and loop closure, enabling globally consistent reconstruction at scale. We validate DiskChunGS on indoor scenes (Replica, TUM-RGBD), urban driving scenarios (KITTI), and resource-constrained Nvidia Jetson platforms. Our method uniquely completes all 11 KITTI sequences without memory failures while achieving superior visual quality, demonstrating that algorithmic innovation can overcome the memory constraints that have limited previous 3DGS SLAM methods.

