---
layout: default
title: Kineo: Calibration-Free Metric Motion Capture From Sparse RGB Cameras
---

# Kineo: Calibration-Free Metric Motion Capture From Sparse RGB Cameras

**arXiv**: [2510.24464v1](https://arxiv.org/abs/2510.24464) | [PDF](https://arxiv.org/pdf/2510.24464.pdf)

**作者**: Charles Javerliat, Pierre Raimbaud, Guillaume Lavoué

---

## 💡 一句话要点

**提出Kineo以解决无标定多视角运动捕捉中的精度与效率问题**

**关键词**: `无标定运动捕捉` `多视角重建` `相机标定` `图优化` `3D关键点检测`

## 📋 核心要点

1. 核心问题：无标定多视角运动捕捉依赖精确相机标定，限制非专家和野外应用。
2. 方法要点：利用2D关键点同时标定相机和重建3D关键点，结合图优化确保鲁棒性。
3. 实验效果：在EgoHumans和Human3.6M上显著降低相机误差和世界关节误差。

## 📄 摘要（原文）

> Markerless multiview motion capture is often constrained by the need for
> precise camera calibration, limiting accessibility for non-experts and
> in-the-wild captures. Existing calibration-free approaches mitigate this
> requirement but suffer from high computational cost and reduced reconstruction
> accuracy.
>   We present Kineo, a fully automatic, calibration-free pipeline for markerless
> motion capture from videos captured by unsynchronized, uncalibrated,
> consumer-grade RGB cameras. Kineo leverages 2D keypoints from off-the-shelf
> detectors to simultaneously calibrate cameras, including Brown-Conrady
> distortion coefficients, and reconstruct 3D keypoints and dense scene point
> maps at metric scale. A confidence-driven spatio-temporal keypoint sampling
> strategy, combined with graph-based global optimization, ensures robust
> calibration at a fixed computational cost independent of sequence length. We
> further introduce a pairwise reprojection consensus score to quantify 3D
> reconstruction reliability for downstream tasks.
>   Evaluations on EgoHumans and Human3.6M demonstrate substantial improvements
> over prior calibration-free methods. Compared to previous state-of-the-art
> approaches, Kineo reduces camera translation error by approximately 83-85%,
> camera angular error by 86-92%, and world mean-per-joint error (W-MPJPE) by
> 83-91%.
>   Kineo is also efficient in real-world scenarios, processing multi-view
> sequences faster than their duration in specific configuration (e.g., 36min to
> process 1h20min of footage). The full pipeline and evaluation code are openly
> released to promote reproducibility and practical adoption at
> https://liris-xr.github.io/kineo/.

