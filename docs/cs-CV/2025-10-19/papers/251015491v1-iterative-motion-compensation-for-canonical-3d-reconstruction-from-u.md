---
layout: default
title: Iterative Motion Compensation for Canonical 3D Reconstruction from UAV Plant Images Captured in Windy Conditions
---

# Iterative Motion Compensation for Canonical 3D Reconstruction from UAV Plant Images Captured in Windy Conditions

**arXiv**: [2510.15491v1](https://arxiv.org/abs/2510.15491) | [PDF](https://arxiv.org/pdf/2510.15491.pdf)

**作者**: Andre Rochow, Jonas Marcic, Svetlana Seliunina, Sven Behnke

---

## 💡 一句话要点

**提出迭代运动补偿方法，以在风扰条件下从无人机图像重建植物3D模型**

**关键词**: `3D重建` `运动补偿` `无人机图像` `植物表型` `光流估计`

## 📋 核心要点

1. 核心问题：环境风和无人机下洗气流导致植物叶片运动，影响3D重建精度
2. 方法要点：使用光流估计运动，迭代变形输入图像以对齐中间3D重建
3. 实验或效果：迭代后提升重建质量，支持高分辨率3D网格提取

## 📄 摘要（原文）

> 3D phenotyping of plants plays a crucial role for understanding plant growth,
> yield prediction, and disease control. We present a pipeline capable of
> generating high-quality 3D reconstructions of individual agricultural plants.
> To acquire data, a small commercially available UAV captures images of a
> selected plant. Apart from placing ArUco markers, the entire image acquisition
> process is fully autonomous, controlled by a self-developed Android application
> running on the drone's controller. The reconstruction task is particularly
> challenging due to environmental wind and downwash of the UAV. Our proposed
> pipeline supports the integration of arbitrary state-of-the-art 3D
> reconstruction methods. To mitigate errors caused by leaf motion during image
> capture, we use an iterative method that gradually adjusts the input images
> through deformation. Motion is estimated using optical flow between the
> original input images and intermediate 3D reconstructions rendered from the
> corresponding viewpoints. This alignment gradually reduces scene motion,
> resulting in a canonical representation. After a few iterations, our pipeline
> improves the reconstruction of state-of-the-art methods and enables the
> extraction of high-resolution 3D meshes. We will publicly release the source
> code of our reconstruction pipeline. Additionally, we provide a dataset
> consisting of multiple plants from various crops, captured across different
> points in time.

