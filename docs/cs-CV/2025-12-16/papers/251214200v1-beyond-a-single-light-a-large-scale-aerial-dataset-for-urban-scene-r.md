---
layout: default
title: Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination
---

# Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination

**arXiv**: [2512.14200v1](https://arxiv.org/abs/2512.14200) | [PDF](https://arxiv.org/pdf/2512.14200.pdf)

**作者**: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出SkyLume数据集以解决多时序无人机数据中光照不一致对大规模城市场景重建的挑战。**

🎯 **匹配领域**: **自动驾驶** **深度估计** **强化学习**

**关键词**: `无人机数据集` `光照鲁棒重建` `3D高斯溅射` `神经辐射场` `逆渲染` `城市场景建模` `时间一致性系数` `多时序数据`

## 📋 核心要点

1. 核心问题：现有方法在处理多时序无人机数据时，光照不一致导致颜色伪影和几何误差，缺乏相关数据集限制了研究进展。
2. 方法要点：提出SkyLume数据集，系统捕获城市区域在不同时间段的光照变化，提供激光雷达和3D真值以支持精确评估。
3. 实验或效果：引入时间一致性系数评估逆渲染鲁棒性，数据集促进光照鲁棒重建和逆渲染任务的研究与评估。

## 📝 摘要（中文）

近年来，神经辐射场和3D高斯溅射在基于无人机的大规模3D重建任务中展现出强大潜力，通过拟合图像外观实现重建。然而，真实世界的大规模采集通常基于多时序数据捕获，其中不同时间段的光照不一致会显著导致颜色伪影、几何不准确和外观不一致。由于缺乏系统捕获同一区域在不同光照条件下的无人机数据集，这一挑战在很大程度上尚未得到充分探索。为填补这一空白，我们引入了SkyLume，这是一个大规模、真实世界的无人机数据集，专门用于研究城市场景建模中的光照鲁棒3D重建：(1) 我们从10个城市区域收集数据，包含超过10万张高分辨率无人机图像（四个倾斜视角和天底视角），每个区域在一天中的三个时间段进行捕获，以系统隔离光照变化。(2) 为支持几何和外观的精确评估，我们提供每场景的激光雷达扫描和准确的3D地面真值，用于评估不同光照下的深度、表面法线和重建质量。(3) 对于逆渲染任务，我们引入了时间一致性系数，这是一个度量跨时间反照率稳定性的指标，直接评估光照与材质解耦的鲁棒性。我们旨在使这一资源成为推动大规模逆渲染、几何重建和新视角合成研究和真实世界评估的基础。

## 🔬 方法详解

论文的核心方法是构建SkyLume数据集，整体框架包括数据采集、标注和评估指标设计。关键技术创新点在于系统捕获同一城市区域在一天中三个时间段的光照变化，结合多视角无人机图像和激光雷达扫描，提供全面的3D地面真值。与现有方法的主要区别在于，SkyLume专门针对光照不一致问题，填补了大规模无人机数据集中光照变化研究的空白，并引入时间一致性系数作为逆渲染任务的评估指标，直接量化光照与材质解耦的稳定性。

## 📊 实验亮点

SkyLume数据集包含超过10万张高分辨率图像，覆盖10个城市区域，每个区域在三个时间段捕获，提供激光雷达扫描和3D真值。时间一致性系数作为新指标，有效评估逆渲染中光照解耦的鲁棒性，促进光照不一致条件下的重建性能提升。

## 🎯 应用场景

该研究可应用于城市建模、自动驾驶环境感知、虚拟现实场景生成和文化遗产数字化等领域，通过提供光照鲁棒的重建数据，提升大规模3D重建的准确性和一致性，支持真实世界逆渲染和几何优化任务。

## 📄 摘要（原文）

> Recent advances in Neural Radiance Fields and 3D Gaussian Splatting have demonstrated strong potential for large-scale UAV-based 3D reconstruction tasks by fitting the appearance of images. However, real-world large-scale captures are often based on multi-temporal data capture, where illumination inconsistencies across different times of day can significantly lead to color artifacts, geometric inaccuracies, and inconsistent appearance. Due to the lack of UAV datasets that systematically capture the same areas under varying illumination conditions, this challenge remains largely underexplored. To fill this gap, we introduceSkyLume, a large-scale, real-world UAV dataset specifically designed for studying illumination robust 3D reconstruction in urban scene modeling: (1) We collect data from 10 urban regions data comprising more than 100k high resolution UAV images (four oblique views and nadir), where each region is captured at three periods of the day to systematically isolate illumination changes. (2) To support precise evaluation of geometry and appearance, we provide per-scene LiDAR scans and accurate 3D ground-truth for assessing depth, surface normals, and reconstruction quality under varying illumination. (3) For the inverse rendering task, we introduce the Temporal Consistency Coefficient (TCC), a metric that measuress cross-time albedo stability and directly evaluates the robustness of the disentanglement of light and material. We aim for this resource to serve as a foundation that advances research and real-world evaluation in large-scale inverse rendering, geometry reconstruction, and novel view synthesis.

