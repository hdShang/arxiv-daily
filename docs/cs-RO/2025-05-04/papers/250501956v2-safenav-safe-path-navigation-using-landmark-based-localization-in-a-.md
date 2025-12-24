---
layout: default
title: SafeNav: Safe Path Navigation using Landmark Based Localization in a GPS-denied Environment
---

# SafeNav: Safe Path Navigation using Landmark Based Localization in a GPS-denied Environment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01956" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01956v2</a>
  <a href="https://arxiv.org/pdf/2505.01956.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01956v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01956v2', 'SafeNav: Safe Path Navigation using Landmark Based Localization in a GPS-denied Environment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ganesh Sapkota, Sanjay Madria

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-04 (更新: 2025-05-13)

**备注**: 10 pages, conference paper. arXiv admin note: text overlap with arXiv:2402.14280

---

## 💡 一句话要点

**提出LanBLoc-BMM以解决GPS受限环境中的导航问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `地标定位` `扩展卡尔曼滤波` `安全导航` `战场环境` `路径规划` `视觉定位` `动态网络`

## 📋 核心要点

1. 现有的视觉定位方法在GPS受限环境中面临高计算需求和复杂传感器融合的问题。
2. 本文提出的LanBLoc-BMM结合了地标定位和战场特定运动模型，以提高导航精度和稳定性。
3. 实验结果显示，LanBLoc-BMM在多个性能指标上优于现有方法，尤其是在真实模拟数据集上表现突出。

## 📝 摘要（中文）

在战场环境中，敌方常常干扰GPS信号，因此需要替代的定位和导航方法。传统的基于视觉的方法如同时定位与地图构建（SLAM）和视觉里程计（VO）涉及复杂的传感器融合和高计算需求，而无范围的方法如DV-HOP在稀疏动态网络中面临准确性和稳定性挑战。本文提出了一种结合地标定位（LanBLoc）和战场特定运动模型（BMM）及扩展卡尔曼滤波器（EKF）的导航方法LanBLoc-BMM，并与三种最先进的视觉定位算法进行了基准测试。结果表明，LanBLoc-BMM在真实模拟数据集上在平均位移误差（ADE）、最终位移误差（FDE）和新引入的平均加权风险评分（AWRS）方面表现优越。此外，文中还提出了两种安全导航方法SafeNav-CHull和SafeNav-Centroid，旨在实现障碍物规避和风险暴露最小化。

## 🔬 方法详解

**问题定义**：本文旨在解决在GPS受限环境中进行安全路径导航的挑战，现有方法如SLAM和VO存在计算复杂性和准确性不足的问题。

**核心思路**：提出的LanBLoc-BMM方法通过结合地标定位和战场特定运动模型，利用扩展卡尔曼滤波器来提高定位精度和导航安全性。

**技术框架**：该方法的整体架构包括地标定位模块、运动模型模块和扩展卡尔曼滤波器模块，形成一个闭环的导航系统。

**关键创新**：LanBLoc-BMM的主要创新在于将地标定位与战场特定运动模型相结合，显著提升了在动态环境中的导航性能。

**关键设计**：在设计中，采用了扩展卡尔曼滤波器来处理传感器数据，优化了运动模型的参数设置，并引入了新的风险评分指标以评估导航安全性。

## 📊 实验亮点

实验结果表明，LanBLoc-BMM在真实模拟数据集上在平均位移误差（ADE）、最终位移误差（FDE）和平均加权风险评分（AWRS）方面均表现优于三种现有视觉定位算法，显示出显著的性能提升。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在军事和救援领域，能够在GPS信号受限的情况下提供可靠的导航解决方案。未来，该方法还可以扩展到无人驾驶、机器人导航等领域，提升其在复杂环境中的应用价值。

## 📄 摘要（原文）

> In battlefield environments, adversaries frequently disrupt GPS signals, requiring alternative localization and navigation methods. Traditional vision-based approaches like Simultaneous Localization and Mapping (SLAM) and Visual Odometry (VO) involve complex sensor fusion and high computational demand, whereas range-free methods like DV-HOP face accuracy and stability challenges in sparse, dynamic networks. This paper proposes LanBLoc-BMM, a navigation approach using landmark-based localization (LanBLoc) combined with a battlefield-specific motion model (BMM) and Extended Kalman Filter (EKF). Its performance is benchmarked against three state-of-the-art visual localization algorithms integrated with BMM and Bayesian filters, evaluated on synthetic and real-imitated trajectory datasets using metrics including Average Displacement Error (ADE), Final Displacement Error (FDE), and a newly introduced Average Weighted Risk Score (AWRS). LanBLoc-BMM (with EKF) demonstrates superior performance in ADE, FDE, and AWRS on real-imitated datasets. Additionally, two safe navigation methods, SafeNav-CHull and SafeNav-Centroid, are introduced by integrating LanBLoc-BMM(EKF) with a novel Risk-Aware RRT* (RAw-RRT*) algorithm for obstacle avoidance and risk exposure minimization. Simulation results in battlefield scenarios indicate SafeNav-Centroid excels in accuracy, risk exposure, and trajectory efficiency, while SafeNav-CHull provides superior computational speed.

