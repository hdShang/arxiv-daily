---
layout: default
title: FisheyeGaussianLift: BEV Feature Lifting for Surround-View Fisheye Camera Perception
---

# FisheyeGaussianLift: BEV Feature Lifting for Surround-View Fisheye Camera Perception

**arXiv**: [2511.17210v1](https://arxiv.org/abs/2511.17210) | [PDF](https://arxiv.org/pdf/2511.17210.pdf)

**作者**: Shubham Sonarghare, Prasad Deshpande, Ciaran Hogan, Deepika-Rani Kaliappan-Mahalingam, Ganesh Sistu

---

## 💡 一句话要点

**提出FisheyeGaussianLift框架，通过高斯参数化提升BEV特征以解决鱼眼相机感知中的失真和深度模糊问题。**

**关键词**: `鱼眼相机感知` `BEV语义分割` `高斯参数化` `失真建模` `多相机融合` `不确定性估计`

## 📋 核心要点

1. 核心问题：鱼眼图像因非线性失真、遮挡和深度模糊，导致BEV语义分割困难。
2. 方法要点：利用几何反投影和深度分布估计，将像素提升为3D高斯以建模不确定性。
3. 实验或效果：在停车和城市驾驶场景中，实现高IoU分数，如可行驶区域87.75%。

## 📄 摘要（原文）

> Accurate BEV semantic segmentation from fisheye imagery remains challenging due to extreme non-linear distortion, occlusion, and depth ambiguity inherent to wide-angle projections. We present a distortion-aware BEV segmentation framework that directly processes multi-camera high-resolution fisheye images,utilizing calibrated geometric unprojection and per-pixel depth distribution estimation. Each image pixel is lifted into 3D space via Gaussian parameterization, predicting spatial means and anisotropic covariances to explicitly model geometric uncertainty. The projected 3D Gaussians are fused into a BEV representation via differentiable splatting, producing continuous, uncertainty-aware semantic maps without requiring undistortion or perspective rectification. Extensive experiments demonstrate strong segmentation performance on complex parking and urban driving scenarios, achieving IoU scores of 87.75% for drivable regions and 57.26% for vehicles under severe fisheye distortion and diverse environmental conditions.

