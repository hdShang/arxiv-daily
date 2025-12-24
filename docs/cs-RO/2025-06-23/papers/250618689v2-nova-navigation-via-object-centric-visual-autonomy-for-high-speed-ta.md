---
layout: default
title: "NOVA: Navigation via Object-Centric Visual Autonomy for High-Speed Target Tracking in Unstructured GPS-Denied Environments"
---

# NOVA: Navigation via Object-Centric Visual Autonomy for High-Speed Target Tracking in Unstructured GPS-Denied Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18689" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18689v2</a>
  <a href="https://arxiv.org/pdf/2506.18689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18689v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18689v2', 'NOVA: Navigation via Object-Centric Visual Autonomy for High-Speed Target Tracking in Unstructured GPS-Denied Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alessandro Saviolo, Giuseppe Loianno

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-23 (更新: 2025-07-07)

---

## 💡 一句话要点

**提出NOVA以解决无GPS环境下的高速目标跟踪问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `目标跟踪` `无GPS导航` `机器人技术` `立体视觉` `动态环境` `碰撞规避` `模型预测控制` `深度学习`

## 📋 核心要点

1. 现有的自动目标跟踪方法在无GPS和复杂环境中表现不佳，依赖于外部定位系统限制了其应用。
2. NOVA通过在目标参考框架内进行感知和控制，利用立体相机和IMU实现目标跟踪和碰撞规避。
3. 实验结果表明，NOVA在多种复杂场景中表现出色，能够以超过50 km/h的速度实现稳定的目标跟踪。

## 📝 摘要（中文）

在无GPS和复杂环境中，自动化空中目标跟踪仍然是机器人技术中的一大挑战。现有方法通常依赖于运动捕捉系统、预先映射的场景或基于特征的定位，限制了其在真实环境中的应用。本文提出NOVA，一个完全基于机载的、以目标为中心的框架，利用立体相机和惯性测量单元（IMU）实现稳健的目标跟踪和碰撞感知导航。NOVA在目标参考框架内进行感知、估计和控制，结合轻量级目标检测器和立体深度补全，通过直方图过滤推断目标距离，进而实现实时的障碍物规避。实验验证了NOVA在城市迷宫、森林小径等复杂场景中的有效性，显示出其在高速（超过50 km/h）目标跟踪中的可靠性。

## 🔬 方法详解

**问题定义**：本文旨在解决在无GPS和复杂环境中进行自动化目标跟踪的挑战。现有方法通常依赖于外部定位和预先映射的环境，限制了其在动态和未知环境中的应用。

**核心思路**：NOVA的核心思路是将感知、估计和控制完全基于目标的参考框架，而不是构建全局地图或依赖绝对定位。这种设计使得系统能够在动态环境中灵活应对。

**技术框架**：NOVA的整体架构包括几个主要模块：轻量级目标检测器、立体深度补全、直方图过滤、视觉惯性状态估计器和非线性模型预测控制器（NMPC）。这些模块紧密集成，形成一个高效的目标跟踪和导航系统。

**关键创新**：NOVA的关键创新在于使用目标参考框架进行感知和控制，结合高阶控制障碍函数实现实时的障碍物规避。这一方法与传统的基于全局地图的定位方法有本质区别。

**关键设计**：在技术细节上，NOVA采用了轻量级的目标检测网络和直方图过滤技术，以提高在遮挡和噪声条件下的目标距离推断精度。此外，NMPC设计确保了动态可行的轨迹规划，增强了系统的安全性和灵活性。

## 📊 实验亮点

NOVA在多种复杂场景中进行了验证，包括城市迷宫和森林小径，显示出在GPS丢失和光照变化严重的情况下，仍能保持稳定的目标跟踪性能。实验结果表明，NOVA能够以超过50 km/h的速度进行目标跟踪，展现出其在高速视觉跟踪中的可靠性。

## 🎯 应用场景

NOVA的研究成果在无人机、自动驾驶和机器人导航等领域具有广泛的应用潜力。其能够在复杂和动态环境中实现高效的目标跟踪，为未来的自主系统提供了新的解决方案，尤其是在城市搜索与救援、监视和环境监测等场景中具有重要价值。

## 📄 摘要（原文）

> Autonomous aerial target tracking in unstructured and GPS-denied environments remains a fundamental challenge in robotics. Many existing methods rely on motion capture systems, pre-mapped scenes, or feature-based localization to ensure safety and control, limiting their deployment in real-world conditions. We introduce NOVA, a fully onboard, object-centric framework that enables robust target tracking and collision-aware navigation using only a stereo camera and an IMU. Rather than constructing a global map or relying on absolute localization, NOVA formulates perception, estimation, and control entirely in the target's reference frame. A tightly integrated stack combines a lightweight object detector with stereo depth completion, followed by histogram-based filtering to infer robust target distances under occlusion and noise. These measurements feed a visual-inertial state estimator that recovers the full 6-DoF pose of the robot relative to the target. A nonlinear model predictive controller (NMPC) plans dynamically feasible trajectories in the target frame. To ensure safety, high-order control barrier functions are constructed online from a compact set of high-risk collision points extracted from depth, enabling real-time obstacle avoidance without maps or dense representations. We validate NOVA across challenging real-world scenarios, including urban mazes, forest trails, and repeated transitions through buildings with intermittent GPS loss and severe lighting changes that disrupt feature-based localization. Each experiment is repeated multiple times under similar conditions to assess resilience, showing consistent and reliable performance. NOVA achieves agile target following at speeds exceeding 50 km/h. These results show that high-speed vision-based tracking is possible in the wild using only onboard sensing, with no reliance on external localization or environment assumptions.

