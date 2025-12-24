---
layout: default
title: "AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame Covisibility Detection"
---

# AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame Covisibility Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00433" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00433v1</a>
  <a href="https://arxiv.org/pdf/2509.00433.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00433v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00433v1', 'AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame Covisibility Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Houshu He, Naifeng Jing, Li Jiang, Xiaoyao Liang, Zhuoran Song

**分类**: cs.AR, cs.RO

**发布日期**: 2025-08-30

**备注**: 15 pages

---

## 💡 一句话要点

**提出AGS框架以加速3D高斯点云SLAM系统**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯点云` `SLAM` `算法-硬件协同设计` `姿态跟踪` `帧共视性检测` `自主驾驶` `机器人导航`

## 📋 核心要点

1. 现有的3DGS-SLAM系统在处理速度上存在瓶颈，主要由于每帧需要多次训练和高斯数量庞大。
2. 本文提出AGS框架，通过算法与硬件协同设计，利用相邻帧的相似性来加速SLAM过程。
3. 实验结果显示，AGS在不同硬件平台上实现了显著的加速，最高可达17.12倍，展现了其高效性。

## 📝 摘要（中文）

同时定位与地图构建（SLAM）是使自主车辆能够在未知环境中构建地图和定位自身的关键任务。近期的研究将SLAM与3D高斯点云（3DGS）结合，取得了卓越的重建精度。然而，现有的3DGS-SLAM系统由于每帧需要多次训练迭代以及高斯数量庞大，导致吞吐量不足。本文提出AGS，一个算法-硬件协同设计框架，旨在提升3DGS-SLAM的效率，利用相邻帧之间的高相似性进行加速。我们在软件层面提出了一种粗到细的姿态跟踪方法，并通过跨帧共享高斯贡献信息来避免冗余计算。在硬件层面，我们设计了一个帧共视性检测引擎，从视频编解码器中提取中间数据，并实现了姿态跟踪引擎和映射引擎，以高效部署AGS算法。评估结果表明，AGS在移动和高端GPU以及最先进的3DGS加速器GSCore上分别实现了高达17.12倍、6.71倍和5.41倍的加速。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3DGS-SLAM系统在处理速度上的不足，特别是由于每帧需要多次训练迭代和高斯数量庞大导致的吞吐量低下问题。

**核心思路**：AGS框架的核心思路是利用SLAM系统处理帧的流式特性，识别相邻帧之间的高相似性，从而减少冗余计算，提高处理效率。

**技术框架**：AGS框架包括软件层面的粗到细姿态跟踪方法和跨帧高斯贡献信息共享机制，以及硬件层面的帧共视性检测引擎、姿态跟踪引擎和映射引擎，整体协同工作以提升SLAM效率。

**关键创新**：AGS的主要创新在于算法与硬件的协同设计，特别是通过视频编解码器提取中间数据的帧共视性检测引擎，这一设计显著提高了数据处理的效率。

**关键设计**：在软件层面，采用了粗到细的姿态跟踪方法，减少了计算复杂度；在硬件层面，设计了高效的工作负载调度器，以优化AGS算法的部署和执行。

## 📊 实验亮点

AGS在不同硬件平台上的实验结果显示，最高实现了17.12倍的加速，相较于移动和高端GPU以及最先进的3DGS加速器GSCore，分别实现了6.71倍和5.41倍的性能提升，证明了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自主驾驶、机器人导航和增强现实等场景。通过提升SLAM系统的效率，AGS框架能够在复杂环境中实现更快速、更精确的地图构建和定位，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) is a critical task that enables autonomous vehicles to construct maps and localize themselves in unknown environments. Recent breakthroughs combine SLAM with 3D Gaussian Splatting (3DGS) to achieve exceptional reconstruction fidelity. However, existing 3DGS-SLAM systems provide insufficient throughput due to the need for multiple training iterations per frame and the vast number of Gaussians.
>   In this paper, we propose AGS, an algorithm-hardware co-design framework to boost the efficiency of 3DGS-SLAM based on the intuition that SLAM systems process frames in a streaming manner, where adjacent frames exhibit high similarity that can be utilized for acceleration. On the software level: 1) We propose a coarse-then-fine-grained pose tracking method with respect to the robot's movement. 2) We avoid redundant computations of Gaussians by sharing their contribution information across frames. On the hardware level, we propose a frame covisibility detection engine to extract intermediate data from the video CODEC. We also implement a pose tracking engine and a mapping engine with workload schedulers to efficiently deploy the AGS algorithm. Our evaluation shows that AGS achieves up to $17.12\times$, $6.71\times$, and $5.41\times$ speedups against the mobile and high-end GPUs, and a state-of-the-art 3DGS accelerator, GSCore.

