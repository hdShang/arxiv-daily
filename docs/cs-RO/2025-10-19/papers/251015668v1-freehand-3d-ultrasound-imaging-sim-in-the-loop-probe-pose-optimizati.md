---
layout: default
title: Freehand 3D Ultrasound Imaging: Sim-in-the-Loop Probe Pose Optimization via Visual Servoing
---

# Freehand 3D Ultrasound Imaging: Sim-in-the-Loop Probe Pose Optimization via Visual Servoing

**arXiv**: [2510.15668v1](https://arxiv.org/abs/2510.15668) | [PDF](https://arxiv.org/pdf/2510.15668.pdf)

**作者**: Yameng Zhang, Dianye Huang, Max Q. -H. Meng, Nassir Navab, Zhongliang Jiang

---

## 💡 一句话要点

**提出基于视觉伺服的仿真闭环探头位姿优化方法，实现低成本自由手3D超声成像**

**关键词**: `自由手3D超声成像` `视觉伺服` `仿真闭环优化` `图像修复` `探头位姿估计`

## 📋 核心要点

1. 自由手3D超声成像面临探头位姿估计不准确问题，依赖昂贵追踪系统或易受噪声影响
2. 采用轻量相机和视觉伺服，在仿真环境中迭代最小化位姿误差，并引入图像修复处理遮挡
3. 在血管模型和人臂上验证，Hausdorff距离低至0.359毫米，显示高精度和鲁棒性

## 📄 摘要（原文）

> Freehand 3D ultrasound (US) imaging using conventional 2D probes offers
> flexibility and accessibility for diverse clinical applications but faces
> challenges in accurate probe pose estimation. Traditional methods depend on
> costly tracking systems, while neural network-based methods struggle with image
> noise and error accumulation, compromising reconstruction precision. We propose
> a cost-effective and versatile solution that leverages lightweight cameras and
> visual servoing in simulated environments for precise 3D US imaging. These
> cameras capture visual feedback from a textured planar workspace. To counter
> occlusions and lighting issues, we introduce an image restoration method that
> reconstructs occluded regions by matching surrounding texture patterns. For
> pose estimation, we develop a simulation-in-the-loop approach, which replicates
> the system setup in simulation and iteratively minimizes pose errors between
> simulated and real-world observations. A visual servoing controller refines the
> alignment of camera views, improving translational estimation by optimizing
> image alignment. Validations on a soft vascular phantom, a 3D-printed conical
> model, and a human arm demonstrate the robustness and accuracy of our approach,
> with Hausdorff distances to the reference reconstructions of 0.359 mm, 1.171
> mm, and 0.858 mm, respectively. These results confirm the method's potential
> for reliable freehand 3D US reconstruction.

