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

**提出SkyLume大规模无人机数据集以解决多时序光照下城市场景重建的挑战**

**关键词**: `无人机数据集` `光照鲁棒重建` `多时序数据` `逆渲染` `3D高斯溅射` `城市场景建模` `时间一致性系数` `大规模3D重建`

## 📋 核心要点

1. 现有方法在基于多时序无人机数据的大规模3D重建中面临光照不一致性挑战，导致颜色伪影和几何不准确，缺乏系统数据集支持研究。
2. 论文提出SkyLume数据集，包含10个城市区域超过10万张图像，每个区域在三个时间段捕获，并提供激光雷达扫描和3D地面真值以支持评估。
3. 引入时间一致性系数作为评估指标，直接衡量光照与材质解耦的鲁棒性，为逆渲染任务提供量化基准，推动相关研究进展。

## 📝 摘要（中文）

近年来，神经辐射场和3D高斯溅射在基于无人机的大规模3D重建任务中展现出强大潜力，通过拟合图像外观实现重建。然而，现实世界的大规模采集通常基于多时序数据捕获，不同时间段的光照不一致性会显著导致颜色伪影、几何不准确和外观不一致。由于缺乏系统捕获相同区域在不同光照条件下的无人机数据集，这一挑战在很大程度上尚未得到充分探索。为填补这一空白，我们引入了SkyLume，这是一个专门为研究城市场景建模中光照鲁棒3D重建而设计的大规模真实世界无人机数据集：(1) 我们从10个城市区域收集数据，包含超过10万张高分辨率无人机图像（四个倾斜视图和天底视图），每个区域在一天中的三个时间段被捕获，以系统隔离光照变化。(2) 为支持几何和外观的精确评估，我们提供每个场景的激光雷达扫描和准确的3D地面真值，用于评估不同光照下的深度、表面法线和重建质量。(3) 对于逆渲染任务，我们引入了时间一致性系数，这是一个衡量跨时间反照率稳定性的指标，直接评估光照与材质解耦的鲁棒性。我们旨在使这一资源成为推动大规模逆渲染、几何重建和新视图合成研究和现实世界评估的基础。

## 🔬 方法详解

论文的核心方法围绕SkyLume数据集的构建和评估框架展开。整体框架包括数据采集、标注和评估指标设计。关键技术创新点在于系统捕获同一城市区域在一天中三个时间段（如早晨、中午、傍晚）的高分辨率无人机图像，以隔离光照变化，同时提供激光雷达扫描和精确3D地面真值用于几何和外观评估。与现有方法的主要区别在于，SkyLume是首个专门针对多时序光照下大规模城市场景重建的无人机数据集，填补了该领域数据空白，并引入时间一致性系数作为逆渲染任务的新评估指标，直接量化光照解耦的稳定性。

## 📊 实验亮点

SkyLume数据集包含超过10万张高分辨率图像，覆盖10个城市区域，每个区域在三个时间段捕获，系统隔离光照变化。实验通过激光雷达扫描和3D地面真值验证了数据集的几何和外观质量，时间一致性系数为逆渲染任务提供了量化评估基准，显著提升了光照鲁棒重建的研究能力。

## 🎯 应用场景

该研究在计算机视觉和机器人领域具有广泛潜在应用，包括城市建模、自动驾驶环境感知、虚拟现实场景生成和文化遗产数字化。通过提供光照鲁棒的重建数据，可提升现实世界3D重建的准确性和一致性，支持大规模逆渲染算法开发和评估，推动无人机巡检、智慧城市规划和增强现实等实际应用。

## 📄 摘要（原文）

> Recent advances in Neural Radiance Fields and 3D Gaussian Splatting have demonstrated strong potential for large-scale UAV-based 3D reconstruction tasks by fitting the appearance of images. However, real-world large-scale captures are often based on multi-temporal data capture, where illumination inconsistencies across different times of day can significantly lead to color artifacts, geometric inaccuracies, and inconsistent appearance. Due to the lack of UAV datasets that systematically capture the same areas under varying illumination conditions, this challenge remains largely underexplored. To fill this gap, we introduceSkyLume, a large-scale, real-world UAV dataset specifically designed for studying illumination robust 3D reconstruction in urban scene modeling: (1) We collect data from 10 urban regions data comprising more than 100k high resolution UAV images (four oblique views and nadir), where each region is captured at three periods of the day to systematically isolate illumination changes. (2) To support precise evaluation of geometry and appearance, we provide per-scene LiDAR scans and accurate 3D ground-truth for assessing depth, surface normals, and reconstruction quality under varying illumination. (3) For the inverse rendering task, we introduce the Temporal Consistency Coefficient (TCC), a metric that measuress cross-time albedo stability and directly evaluates the robustness of the disentanglement of light and material. We aim for this resource to serve as a foundation that advances research and real-world evaluation in large-scale inverse rendering, geometry reconstruction, and novel view synthesis.

