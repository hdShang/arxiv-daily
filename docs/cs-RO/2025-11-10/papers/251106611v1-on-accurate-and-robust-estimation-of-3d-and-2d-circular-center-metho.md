---
layout: default
title: On Accurate and Robust Estimation of 3D and 2D Circular Center: Method and Application to Camera-Lidar Calibration
---

# On Accurate and Robust Estimation of 3D and 2D Circular Center: Method and Application to Camera-Lidar Calibration

**arXiv**: [2511.06611v1](https://arxiv.org/abs/2511.06611) | [PDF](https://arxiv.org/pdf/2511.06611.pdf)

**作者**: Jiajun Jiang, Xiao Hu, Wancheng Liu, Wei Jiang

---

## 💡 一句话要点

**提出基于几何原理的框架以解决LiDAR-相机标定中3D-2D圆中心对应不准确问题**

**关键词**: `LiDAR-相机标定` `圆中心估计` `共形几何代数` `RANSAC` `弦长方差最小化` `外参估计`

## 📋 核心要点

1. 核心问题：现有方法因3D拟合与2D椭圆中心估计分离导致标定误差大
2. 方法要点：使用共形几何代数与RANSAC估计3D中心，弦长方差最小化解决2D中心歧义
3. 实验或效果：在合成和真实数据集上显著优于现有方法，降低外参估计误差

## 📄 摘要（原文）

> Circular targets are widely used in LiDAR-camera extrinsic calibration due to
> their geometric consistency and ease of detection. However, achieving accurate
> 3D-2D circular center correspondence remains challenging. Existing methods
> often fail due to decoupled 3D fitting and erroneous 2D ellipse-center
> estimation. To address this, we propose a geometrically principled framework
> featuring two innovations: (i) a robust 3D circle center estimator based on
> conformal geometric algebra and RANSAC; and (ii) a chord-length variance
> minimization method to recover the true 2D projected center, resolving its
> dual-minima ambi- guity via homography validation or a quasi-RANSAC fallback.
> Evaluated on synthetic and real-world datasets, our framework significantly
> outperforms state-of-the-art approaches. It reduces extrinsic estimation error
> and enables robust calibration across diverse sensors and target types,
> including natural circular objects. Our code will be publicly released for
> reproducibility.

