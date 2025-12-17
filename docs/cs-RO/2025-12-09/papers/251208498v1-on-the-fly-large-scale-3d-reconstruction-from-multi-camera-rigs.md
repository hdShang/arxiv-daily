---
layout: default
title: On-the-fly Large-scale 3D Reconstruction from Multi-Camera Rigs
---

# On-the-fly Large-scale 3D Reconstruction from Multi-Camera Rigs

**arXiv**: [2512.08498v1](https://arxiv.org/abs/2512.08498) | [PDF](https://arxiv.org/pdf/2512.08498.pdf)

**作者**: Yijia Guo, Tong Hu, Zhiwei Li, Liwen Hu, Keming Qian, Xitong Lin, Shengbo Chen, Tiejun Huang, Lei Ma

---

## 💡 一句话要点

**提出首个多相机阵列实时3D重建框架，通过增量融合与轻量优化实现高效无漂移重建。**

**关键词**: `实时3D重建` `多相机阵列` `3D高斯溅射` `增量融合` `轻量优化` `无漂移轨迹估计`

## 📋 核心要点

1. 核心问题：单目3D高斯溅射实时重建因视野有限导致覆盖不全，多相机阵列可解决此问题。
2. 方法要点：采用分层相机初始化与轻量多相机束调整，结合冗余无高斯采样和频率感知优化调度。
3. 实验或效果：仅用原始多相机视频流，在2分钟内重建数百米场景，展现高速、鲁棒和高保真度。

## 📄 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have enabled efficient free-viewpoint rendering and photorealistic scene reconstruction. While on-the-fly extensions of 3DGS have shown promise for real-time reconstruction from monocular RGB streams, they often fail to achieve complete 3D coverage due to the limited field of view (FOV). Employing a multi-camera rig fundamentally addresses this limitation. In this paper, we present the first on-the-fly 3D reconstruction framework for multi-camera rigs. Our method incrementally fuses dense RGB streams from multiple overlapping cameras into a unified Gaussian representation, achieving drift-free trajectory estimation and efficient online reconstruction. We propose a hierarchical camera initialization scheme that enables coarse inter-camera alignment without calibration, followed by a lightweight multi-camera bundle adjustment that stabilizes trajectories while maintaining real-time performance. Furthermore, we introduce a redundancy-free Gaussian sampling strategy and a frequency-aware optimization scheduler to reduce the number of Gaussian primitives and the required optimization iterations, thereby maintaining both efficiency and reconstruction fidelity. Our method reconstructs hundreds of meters of 3D scenes within just 2 minutes using only raw multi-camera video streams, demonstrating unprecedented speed, robustness, and Fidelity for on-the-fly 3D scene reconstruction.

