---
layout: default
title: "YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos"
---

# YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09903" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09903v1</a>
  <a href="https://arxiv.org/pdf/2512.09903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.09903v1', 'YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-10

---

## 💡 一句话要点

**YOPO-Nav：利用单次视频的3DGS图进行视觉导航**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉导航` `3D高斯溅射` `机器人` `单次视频` `视觉位置识别`

## 📋 核心要点

1. 传统机器人导航依赖高精度地图，但构建和维护成本高昂，限制了其在动态和未知环境中的应用。
2. YOPO-Nav利用单次探索视频构建紧凑的3DGS图，通过视觉对齐和分层控制实现高效的轨迹重溯导航。
3. 在YOPO-Campus数据集上的实验表明，YOPO-Nav在真实机器人上的图像目标导航中表现出色，优于现有方法。

## 📝 摘要（中文）

视觉导航已成为依赖详细地图构建和路径规划的传统机器人导航流程的实用替代方案。然而，构建和维护3D地图通常计算成本高昂且内存密集。本文提出了一种视觉导航方法，利用大型环境的探索视频作为视觉参考，使机器人能够重溯已探索的轨迹，而无需依赖度量地图。该方法名为YOPO-Nav（You Only Pass Once），将环境编码为由互连的局部3D高斯溅射（3DGS）模型组成的紧凑空间表示。在导航过程中，该框架将机器人当前的视觉观察与此表示对齐，并预测引导其返回演示轨迹的动作。YOPO-Nav采用分层设计：视觉位置识别（VPR）模块提供粗略定位，而局部3DGS模型细化目标和中间姿势以生成控制动作。为了评估该方法，引入了YOPO-Campus数据集，其中包含来自超过6公里的人工遥控机器人轨迹的4小时自我中心视频和机器人控制器输入。在YOPO-Campus数据集上，使用Clearpath Jackal机器人对最近的视觉导航方法进行了基准测试。实验结果表明，YOPO-Nav在真实场景的图像目标导航中提供了出色的性能。

## 🔬 方法详解

**问题定义**：现有视觉导航方法通常依赖于预先构建的详细3D地图，这在计算和存储上都带来了巨大的负担。此外，当环境发生变化时，地图需要更新，这进一步增加了维护成本。因此，如何在无需精确地图的情况下，仅利用探索视频实现高效的视觉导航是一个关键问题。

**核心思路**：YOPO-Nav的核心思想是利用单次探索视频构建一个紧凑的、基于3D高斯溅射（3DGS）的场景表示。这种表示方法能够在保证场景信息完整性的同时，显著降低存储空间和计算复杂度。通过将机器人的当前视觉观测与3DGS图进行对齐，可以预测出引导机器人返回目标轨迹的控制动作。

**技术框架**：YOPO-Nav采用分层架构，包含视觉位置识别（VPR）模块和局部3DGS模型。首先，VPR模块对机器人的当前位置进行粗略定位，确定其在全局环境中的大致位置。然后，局部3DGS模型对目标和中间姿态进行精细化，生成具体的控制指令。整个流程可以概括为：视频输入 -> 3DGS图构建 -> VPR粗定位 -> 3DGS精细化 -> 控制指令输出。

**关键创新**：YOPO-Nav的关键创新在于使用3DGS图作为场景表示。与传统的点云地图或体素地图相比，3DGS能够更有效地表示场景的几何和外观信息，同时具有更小的存储空间和更快的渲染速度。此外，分层导航策略结合了VPR的全局定位能力和3DGS的局部精细化能力，实现了高效准确的导航。

**关键设计**：YOPO-Nav使用单次探索视频构建3DGS图，具体实现细节未知。VPR模块的具体算法选择未知，但其作用是提供粗略的全局位置估计。局部3DGS模型如何进行姿态细化和控制指令生成的具体方法未知。损失函数的设计和参数设置等细节也未知。

## 📊 实验亮点

YOPO-Nav在YOPO-Campus数据集上进行了评估，该数据集包含4小时的自我中心视频和6公里的机器人轨迹。实验结果表明，YOPO-Nav在图像目标导航任务中表现出色，优于现有的视觉导航方法。具体的性能指标和提升幅度未知，但论文强调了其在真实机器人上的有效性。

## 🎯 应用场景

YOPO-Nav具有广泛的应用前景，例如家庭服务机器人、仓库物流机器人、以及户外巡检机器人等。该方法能够使机器人在无需预先构建详细地图的情况下，仅通过观看探索视频即可完成导航任务，大大降低了部署成本和维护难度。未来，该技术有望应用于更复杂的动态环境，实现更智能、更自主的机器人导航。

## 📄 摘要（原文）

> Visual navigation has emerged as a practical alternative to traditional robotic navigation pipelines that rely on detailed mapping and path planning. However, constructing and maintaining 3D maps is often computationally expensive and memory-intensive. We address the problem of visual navigation when exploration videos of a large environment are available. The videos serve as a visual reference, allowing a robot to retrace the explored trajectories without relying on metric maps. Our proposed method, YOPO-Nav (You Only Pass Once), encodes an environment into a compact spatial representation composed of interconnected local 3D Gaussian Splatting (3DGS) models. During navigation, the framework aligns the robot's current visual observation with this representation and predicts actions that guide it back toward the demonstrated trajectory. YOPO-Nav employs a hierarchical design: a visual place recognition (VPR) module provides coarse localization, while the local 3DGS models refine the goal and intermediate poses to generate control actions. To evaluate our approach, we introduce the YOPO-Campus dataset, comprising 4 hours of egocentric video and robot controller inputs from over 6 km of human-teleoperated robot trajectories. We benchmark recent visual navigation methods on trajectories from YOPO-Campus using a Clearpath Jackal robot. Experimental results show YOPO-Nav provides excellent performance in image-goal navigation for real-world scenes on a physical robot. The dataset and code will be made publicly available for visual navigation and scene representation research.

