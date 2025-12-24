---
layout: default
title: "Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination"
---

# Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14200" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14200v1</a>
  <a href="https://arxiv.org/pdf/2512.14200.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14200v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14200v1', 'Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**SkyLume：一个大规模多光照城市重建航拍数据集，用于解决光照变化下的三维重建问题。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `三维重建` `无人机` `城市建模` `光照鲁棒性` `数据集` `逆渲染` `新视角合成`

## 📋 核心要点

1. 现有基于NeRF和3D Gaussian Splatting的方法在无人机三维重建中表现出色，但多时相数据采集导致的光照不一致会引入伪影。
2. SkyLume数据集通过在不同光照条件下系统地捕获同一区域的数据，旨在解决城市场景三维重建中的光照鲁棒性问题。
3. 该数据集包含高分辨率无人机图像、LiDAR扫描和3D真值，并提出了时间一致性系数（TCC）用于评估光照和材质解耦的鲁棒性。

## 📝 摘要（中文）

本文提出了SkyLume，一个大规模的真实世界航拍数据集，专门用于研究城市场景建模中光照鲁棒的三维重建。该数据集包含来自10个城市区域的超过10万张高分辨率无人机图像（四个倾斜视图和正射视图），每个区域在一天中的三个不同时段进行拍摄，以系统地隔离光照变化。为了支持对几何和外观的精确评估，本文提供了每个场景的LiDAR扫描和精确的3D真值，用于评估不同光照下的深度、表面法线和重建质量。此外，针对逆渲染任务，本文引入了时间一致性系数（TCC），该指标衡量跨时间反照率的稳定性，并直接评估光照和材质解耦的鲁棒性。该资源旨在为大规模逆渲染、几何重建和新视角合成的研究和实际评估奠定基础。

## 🔬 方法详解

**问题定义**：现有基于无人机图像的三维重建方法，尤其是在大规模场景下，容易受到不同时间段光照变化的影响，导致重建结果出现颜色伪影、几何不准确以及外观不一致等问题。缺乏系统性的、针对不同光照条件下的无人机数据集，使得这一问题难以得到充分研究和解决。

**核心思路**：SkyLume数据集的核心思路是通过系统地采集同一区域在不同光照条件下的图像数据，从而为研究光照鲁棒的三维重建方法提供基础。通过提供高质量的图像、LiDAR扫描和3D真值，以及提出新的评估指标，促进相关算法的开发和评估。

**技术框架**：SkyLume数据集的构建流程主要包括以下几个阶段：1) 选择10个城市区域作为研究对象；2) 使用无人机在每个区域的不同时间段（一天中的三个时段）进行数据采集，包括四个倾斜视图和正射视图；3) 对采集到的数据进行处理，包括图像校正、配准等；4) 使用LiDAR扫描获取每个场景的精确点云数据；5) 构建每个场景的3D真值模型；6) 提出时间一致性系数（TCC）用于评估逆渲染任务的性能。

**关键创新**：SkyLume数据集的关键创新在于其系统性地考虑了光照变化对三维重建的影响，并提供了大规模的、高质量的数据集以及相应的评估指标。与现有数据集相比，SkyLume更加关注光照鲁棒性，并提供了更全面的数据和评估工具。时间一致性系数（TCC）是另一个创新点，它提供了一种量化评估光照和材质解耦效果的指标。

**关键设计**：SkyLume数据集的关键设计包括：1) 在不同时间段采集数据，以系统地捕捉光照变化；2) 提供高分辨率的无人机图像，以保证重建的精度；3) 使用LiDAR扫描获取精确的点云数据，作为几何真值；4) 构建高质量的3D真值模型，用于评估重建结果；5) 提出时间一致性系数（TCC），用于评估逆渲染任务中光照和材质解耦的鲁棒性。TCC的具体计算方法未知，但其核心思想是衡量不同时间段反照率的稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14200v1/images/pipeline.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14200v1/images/post1.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14200v1/images/lidarmesh.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SkyLume数据集包含来自10个城市区域的超过10万张高分辨率无人机图像，每个区域在一天中的三个不同时段进行拍摄。此外，该数据集还提供了每个场景的LiDAR扫描和精确的3D真值，以及用于评估逆渲染任务性能的时间一致性系数（TCC）。具体的性能数据和对比基线需要在后续的实验中进行评估。

## 🎯 应用场景

SkyLume数据集可广泛应用于城市三维建模、自动驾驶、增强现实、虚拟现实等领域。通过研究光照鲁棒的三维重建方法，可以提高这些应用在复杂光照条件下的性能和可靠性。例如，在自动驾驶中，可以提高车辆在不同光照条件下的感知能力；在城市三维建模中，可以生成更真实、更准确的城市模型。

## 📄 摘要（原文）

> Recent advances in Neural Radiance Fields and 3D Gaussian Splatting have demonstrated strong potential for large-scale UAV-based 3D reconstruction tasks by fitting the appearance of images. However, real-world large-scale captures are often based on multi-temporal data capture, where illumination inconsistencies across different times of day can significantly lead to color artifacts, geometric inaccuracies, and inconsistent appearance. Due to the lack of UAV datasets that systematically capture the same areas under varying illumination conditions, this challenge remains largely underexplored. To fill this gap, we introduceSkyLume, a large-scale, real-world UAV dataset specifically designed for studying illumination robust 3D reconstruction in urban scene modeling: (1) We collect data from 10 urban regions data comprising more than 100k high resolution UAV images (four oblique views and nadir), where each region is captured at three periods of the day to systematically isolate illumination changes. (2) To support precise evaluation of geometry and appearance, we provide per-scene LiDAR scans and accurate 3D ground-truth for assessing depth, surface normals, and reconstruction quality under varying illumination. (3) For the inverse rendering task, we introduce the Temporal Consistency Coefficient (TCC), a metric that measuress cross-time albedo stability and directly evaluates the robustness of the disentanglement of light and material. We aim for this resource to serve as a foundation that advances research and real-world evaluation in large-scale inverse rendering, geometry reconstruction, and novel view synthesis.

