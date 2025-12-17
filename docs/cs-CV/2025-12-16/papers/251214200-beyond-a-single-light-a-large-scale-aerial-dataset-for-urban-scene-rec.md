---
layout: default
title: Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination
---

# Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14200" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14200</a>
  <a href="https://arxiv.org/pdf/2512.14200.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14200" onclick="toggleFavorite(this, '2512.14200', 'Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出SkyLume数据集，用于解决城市场景三维重建中光照变化带来的挑战。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `三维重建` `无人机航拍` `光照鲁棒性` `城市建模` `数据集` `逆渲染` `神经辐射场` `3D高斯溅射`

## 📋 核心要点

1. 现有方法在多时相数据下，由于光照不一致，导致三维重建出现颜色伪影和几何误差。
2. SkyLume数据集通过系统地捕捉不同光照条件下的城市区域图像，为研究光照鲁棒性提供了数据基础。
3. 论文提出了时间一致性系数（TCC）指标，用于评估逆渲染中光照和材质解耦的鲁棒性。

## 📝 摘要（中文）

本文提出了SkyLume，一个大规模的真实无人机航拍数据集，专门用于研究城市场景建模中光照鲁棒的三维重建。现有的基于神经辐射场和3D高斯溅射的方法在拟合图像外观方面表现出强大的潜力，但真实场景的大规模数据采集通常基于多时相数据，不同时间段的光照不一致会导致颜色伪影、几何不准确和外观不一致。SkyLume数据集包含10个城市区域，超过10万张高分辨率无人机图像（四个倾斜视图和正射视图），每个区域在一天中的三个时段进行拍摄，以系统地隔离光照变化。为了支持对几何和外观的精确评估，本文提供了每个场景的LiDAR扫描和精确的3D真值，用于评估深度、表面法线和不同光照下的重建质量。此外，本文还引入了时间一致性系数（TCC），用于衡量跨时间的反照率稳定性，并直接评估光照和材质解耦的鲁棒性。该数据集旨在为大规模逆渲染、几何重建和新视角合成的研究和实际评估提供基础。

## 🔬 方法详解

**问题定义**：论文旨在解决城市场景三维重建中，由于多时相数据采集导致的光照变化问题。现有方法在处理此类数据时，容易产生颜色伪影、几何不准确和外观不一致等问题，严重影响重建质量。缺乏系统性的、包含不同光照条件下的无人机数据集是阻碍相关研究进展的关键因素。

**核心思路**：论文的核心思路是构建一个大规模的、包含不同光照条件下的城市区域无人机数据集，从而为研究光照鲁棒的三维重建方法提供数据基础。通过在一天中的不同时段对同一区域进行多次拍摄，系统性地捕捉光照变化，并提供高精度的几何真值，为算法的评估和改进提供支持。

**技术框架**：SkyLume数据集的构建流程主要包括以下几个阶段：1) 数据采集：使用无人机在10个不同的城市区域进行数据采集，每个区域在一天中的三个不同时段（例如早晨、中午和傍晚）进行拍摄，以捕捉不同的光照条件。2) 图像获取：每个区域采集超过10万张高分辨率无人机图像，包括四个倾斜视图和一个正射视图。3) 几何真值获取：使用LiDAR扫描仪获取每个场景的精确三维点云数据，作为几何真值。4) 数据处理与标注：对采集到的图像和点云数据进行处理和标注，生成可用于训练和评估的数据集。

**关键创新**：SkyLume数据集的关键创新在于其系统性地捕捉了不同光照条件下的城市区域图像，并提供了高精度的几何真值。此外，论文还提出了时间一致性系数（TCC）指标，用于评估逆渲染中光照和材质解耦的鲁棒性。这是现有数据集和评估方法所缺乏的。

**关键设计**：数据集包含10个城市区域，每个区域在三个不同时段拍摄，图像分辨率高。提供了LiDAR扫描数据作为几何真值，并提出了时间一致性系数（TCC）作为评估指标。TCC的具体计算方法未知，但其目的是衡量跨时间的反照率稳定性，从而评估光照和材质解耦的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14200/images/pipeline.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14200/images/post1.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14200/images/lidarmesh.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SkyLume数据集包含10个城市区域，超过10万张高分辨率无人机图像，并提供了高精度的LiDAR扫描数据作为几何真值。论文提出了时间一致性系数（TCC）指标，用于评估逆渲染中光照和材质解耦的鲁棒性。这些数据和评估指标为研究光照鲁棒的三维重建方法提供了有力支持。

## 🎯 应用场景

该研究成果可广泛应用于城市建模、自动驾驶、虚拟现实、增强现实等领域。通过利用SkyLume数据集训练的光照鲁棒的三维重建算法，可以提高城市模型的精度和真实感，为自动驾驶车辆提供更可靠的环境感知，并为虚拟现实和增强现实应用提供更逼真的场景。

## 📄 摘要（原文）

> Recent advances in Neural Radiance Fields and 3D Gaussian Splatting have demonstrated strong potential for large-scale UAV-based 3D reconstruction tasks by fitting the appearance of images. However, real-world large-scale captures are often based on multi-temporal data capture, where illumination inconsistencies across different times of day can significantly lead to color artifacts, geometric inaccuracies, and inconsistent appearance. Due to the lack of UAV datasets that systematically capture the same areas under varying illumination conditions, this challenge remains largely underexplored. To fill this gap, we introduceSkyLume, a large-scale, real-world UAV dataset specifically designed for studying illumination robust 3D reconstruction in urban scene modeling: (1) We collect data from 10 urban regions data comprising more than 100k high resolution UAV images (four oblique views and nadir), where each region is captured at three periods of the day to systematically isolate illumination changes. (2) To support precise evaluation of geometry and appearance, we provide per-scene LiDAR scans and accurate 3D ground-truth for assessing depth, surface normals, and reconstruction quality under varying illumination. (3) For the inverse rendering task, we introduce the Temporal Consistency Coefficient (TCC), a metric that measuress cross-time albedo stability and directly evaluates the robustness of the disentanglement of light and material. We aim for this resource to serve as a foundation that advances research and real-world evaluation in large-scale inverse rendering, geometry reconstruction, and novel view synthesis.

