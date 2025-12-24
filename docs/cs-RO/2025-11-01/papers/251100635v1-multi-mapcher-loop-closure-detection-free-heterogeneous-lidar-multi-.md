---
layout: default
title: "Multi-Mapcher: Loop Closure Detection-Free Heterogeneous LiDAR Multi-Session SLAM Leveraging Outlier-Robust Registration for Autonomous Vehicles"
---

# Multi-Mapcher: Loop Closure Detection-Free Heterogeneous LiDAR Multi-Session SLAM Leveraging Outlier-Robust Registration for Autonomous Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00635" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00635v1</a>
  <a href="https://arxiv.org/pdf/2511.00635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00635v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00635v1', 'Multi-Mapcher: Loop Closure Detection-Free Heterogeneous LiDAR Multi-Session SLAM Leveraging Outlier-Robust Registration for Autonomous Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyungtae Lim, Daebeom Kim, Hyun Myung

**分类**: cs.RO

**发布日期**: 2025-11-01

**备注**: 13 pages, 12 figures

**🔗 代码/项目**: [GITHUB](https://github.com/url-kaist/multi-mapcher)

---

## 💡 一句话要点

**提出Multi-Mapcher，一种无需回环检测的异构LiDAR多会话SLAM，用于自动驾驶。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多会话SLAM` `异构LiDAR` `点云配准` `回环检测` `位姿图优化`

## 📋 核心要点

1. 现有MSS方法依赖回环检测进行会话间对齐，但异构LiDAR传感器在密度和视场上的差异会降低回环检测性能。
2. Multi-Mapcher通过稳健的点云配准实现大规模地图间的初始对齐，无需依赖回环检测即可进行会话间的粗略对齐。
3. 实验证明，该方法在多种LiDAR传感器数据上表现出更好的MSS性能，且速度优于现有方法。

## 📝 摘要（中文）

本文提出了一种名为Multi-Mapcher的新型多会话同步定位与地图构建(MSS)框架，用于处理异构LiDAR传感器数据。该框架挑战了传统MSS方法对回环检测的依赖，利用稳健的点云配准实现大规模地图间的初始对齐。随后，在初始对齐的基础上，通过半径搜索寻找会话间的闭环，并采用基于锚节点的鲁棒位姿图优化构建一致的全局地图。实验结果表明，该方法在处理不同LiDAR传感器采集的数据时，能够实现优于现有方法的MSS性能，并且速度更快。代码已开源。

## 🔬 方法详解

**问题定义**：现有的多会话SLAM（MSS）方法严重依赖回环检测来实现不同会话之间的地图对齐。然而，当使用异构LiDAR传感器时，由于传感器在点云密度、视场（FoV）等方面的差异，回环检测的性能会显著下降，导致MSS的精度和鲁棒性降低。因此，如何在异构LiDAR传感器条件下，实现无需依赖回环检测的鲁棒MSS是一个关键问题。

**核心思路**：Multi-Mapcher的核心思路是利用稳健的点云配准算法，直接进行大规模地图间的初始对齐，从而避免对回环检测的依赖。该方法假设通过稳健的配准算法，可以获得足够精确的初始对齐结果，然后在此基础上进行后续的优化。这种思路的关键在于找到一种能够有效处理异构LiDAR数据差异的稳健配准方法。

**技术框架**：Multi-Mapcher框架主要包含以下几个阶段：1) **大规模地图间初始对齐**：使用稳健的点云配准算法，将不同会话的地图进行初始对齐。2) **会话间闭环检测**：在初始对齐的基础上，通过半径搜索等方法寻找会话间的闭环。由于初始对齐已经提供了较好的位姿估计，因此闭环检测的范围可以大大缩小。3) **基于锚节点的鲁棒位姿图优化**：利用检测到的闭环信息，构建位姿图，并采用基于锚节点的鲁棒优化方法，消除累积误差，构建一致的全局地图。

**关键创新**：Multi-Mapcher最关键的创新在于它挑战了传统MSS方法对回环检测的依赖，提出了一种基于大规模地图间初始对齐的MSS框架。与现有方法相比，Multi-Mapcher能够更好地处理异构LiDAR传感器数据，避免了因回环检测性能下降而导致的MSS精度降低问题。

**关键设计**：论文中使用了 outlier-robust 的点云配准方法，可能是基于 GICP 或其他鲁棒的 ICP 变体。在位姿图优化中，使用了基于锚节点的优化策略，具体实现细节未知，但其目的是为了提高优化过程的鲁棒性。半径搜索的半径大小是一个关键参数，需要根据实际场景和初始对齐的精度进行调整。具体的损失函数和网络结构等技术细节在论文中没有详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，Multi-Mapcher在异构LiDAR数据集上实现了优于现有方法的MSS性能。具体性能数据和对比基线在摘要中未提及，但强调了该方法在处理不同LiDAR传感器数据时，能够实现更好的MSS性能，并且速度更快。具体的提升幅度未知。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、机器人导航、三维地图重建等领域。特别是在需要融合多种不同类型LiDAR传感器数据的场景下，例如自动驾驶车辆配备不同型号的LiDAR，或机器人同时使用多个LiDAR进行环境感知，该方法能够有效提高SLAM系统的鲁棒性和精度，具有重要的实际应用价值。

## 📄 摘要（原文）

> As various 3D light detection and ranging (LiDAR) sensors have been introduced to the market, research on multi-session simultaneous localization and mapping (MSS) using heterogeneous LiDAR sensors has been actively conducted. Existing MSS methods mostly rely on loop closure detection for inter-session alignment; however, the performance of loop closure detection can be potentially degraded owing to the differences in the density and field of view (FoV) of the sensors used in different sessions. In this study, we challenge the existing paradigm that relies heavily on loop detection modules and propose a novel MSS framework, called Multi-Mapcher, that employs large-scale map-to-map registration to perform inter-session initial alignment, which is commonly assumed to be infeasible, by leveraging outlier-robust 3D point cloud registration. Next, after finding inter-session loops by radius search based on the assumption that the inter-session initial alignment is sufficiently precise, anchor node-based robust pose graph optimization is employed to build a consistent global map. As demonstrated in our experiments, our approach shows substantially better MSS performance for various LiDAR sensors used to capture the sessions and is faster than state-of-the-art approaches. Our code is available at https://github.com/url-kaist/multi-mapcher.

