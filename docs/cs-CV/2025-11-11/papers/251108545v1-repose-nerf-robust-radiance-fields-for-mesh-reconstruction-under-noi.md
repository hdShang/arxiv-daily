---
layout: default
title: RePose-NeRF: Robust Radiance Fields for Mesh Reconstruction under Noisy Camera Poses
---

# RePose-NeRF: Robust Radiance Fields for Mesh Reconstruction under Noisy Camera Poses

**arXiv**: [2511.08545v1](https://arxiv.org/abs/2511.08545) | [PDF](https://arxiv.org/pdf/2511.08545.pdf)

**作者**: Sriram Srinivasan, Gautam Ramachandra

---

## 💡 一句话要点

**提出RePose-NeRF以从噪声相机位姿的多视角图像中重建可编辑3D网格**

**关键词**: `神经辐射场` `3D网格重建` `相机位姿优化` `多视角图像` `机器人视觉` `隐式表示`

## 📋 核心要点

1. 核心问题：真实场景中相机位姿不精确，限制NeRF方法实用性，且隐式体积表示与多边形网格不兼容。
2. 方法要点：联合优化相机位姿并学习隐式场景表示，捕获几何细节和真实感外观。
3. 实验或效果：在标准基准测试中，实现位姿不确定性下的准确鲁棒3D重建，提升机器人应用兼容性。

## 📄 摘要（原文）

> Accurate 3D reconstruction from multi-view images is essential for downstream robotic tasks such as navigation, manipulation, and environment understanding. However, obtaining precise camera poses in real-world settings remains challenging, even when calibration parameters are known. This limits the practicality of existing NeRF-based methods that rely heavily on accurate extrinsic estimates. Furthermore, their implicit volumetric representations differ significantly from the widely adopted polygonal meshes, making rendering and manipulation inefficient in standard 3D software. In this work, we propose a robust framework that reconstructs high-quality, editable 3D meshes directly from multi-view images with noisy extrinsic parameters. Our approach jointly refines camera poses while learning an implicit scene representation that captures fine geometric detail and photorealistic appearance. The resulting meshes are compatible with common 3D graphics and robotics tools, enabling efficient downstream use. Experiments on standard benchmarks demonstrate that our method achieves accurate and robust 3D reconstruction under pose uncertainty, bridging the gap between neural implicit representations and practical robotic applications.

