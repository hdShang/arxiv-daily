---
layout: default
title: Drift-Corrected Monocular VIO and Perception-Aware Planning for Autonomous Drone Racing
---

# Drift-Corrected Monocular VIO and Perception-Aware Planning for Autonomous Drone Racing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20475" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20475v1</a>
  <a href="https://arxiv.org/pdf/2512.20475.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20475v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20475v1', 'Drift-Corrected Monocular VIO and Perception-Aware Planning for Autonomous Drone Racing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maulana Bisyir Azhari, Donghun Han, Je In You, Sungjun Park, David Hyunchul Shim

**分类**: cs.RO

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**针对无人机竞速，提出漂移校正的单目VIO与感知规划方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `无人机竞速` `单目视觉` `视觉惯性里程计` `漂移校正` `感知规划` `卡尔曼滤波` `YOLO`

## 📋 核心要点

1. 单目视觉无人机竞速易受VIO漂移影响，尤其在高速和剧烈运动中，限制了其性能。
2. 提出融合YOLO门检测的全局位置信息，使用卡尔曼滤波校正VIO漂移，并进行感知规划。
3. 系统在无人机竞速比赛中获得多个奖项，验证了所提方法在高速运动中的有效性。

## 📝 摘要（中文）

本文提出了一种用于无人机竞速的系统，该系统仅使用单个摄像头和低质量惯性测量单元（IMU）。这种最小化的传感器配置使得视觉惯性里程计（VIO）容易产生漂移，尤其是在长时间、快速飞行和剧烈机动期间。该方法通过卡尔曼滤波器融合VIO的输出和基于YOLO的门检测器获得的全局位置测量来校正VIO漂移。感知规划器生成平衡速度和保持门可见性的轨迹。该系统在多个类别中取得了优异的成绩：在AI Grand Challenge中获得第三名，最高速度为43.2公里/小时；在AI Drag Race中获得第二名，速度超过59公里/小时；在AI Multi-Drone Race中获得第二名。本文详细介绍了完整的系统架构，并基于比赛的实验数据进行了性能分析，为构建基于单目视觉的自主无人机飞行系统提供了见解。

## 🔬 方法详解

**问题定义**：无人机在高速自主竞速中，仅依赖单目视觉和低质量IMU时，VIO会产生显著的漂移，导致定位不准确，影响导航和控制。现有方法难以在资源受限的条件下，实现高精度和鲁棒性的定位。

**核心思路**：通过融合视觉信息（门检测）提供的全局位置信息，来校正VIO的漂移。同时，在路径规划中考虑感知因素，确保无人机在高速运动中始终能够检测到目标门，从而实现更可靠的导航。

**技术框架**：系统主要包含三个模块：1) 基于单目视觉的VIO模块，提供初始的位姿估计；2) 基于YOLO的门检测模块，检测图像中的门，并提供全局位置信息；3) 融合模块，使用卡尔曼滤波器融合VIO和门检测的结果，校正VIO的漂移。此外，还包含一个感知规划器，用于生成考虑感知约束的轨迹。

**关键创新**：将全局视觉信息（门检测）与VIO融合，用于校正漂移，这在资源受限的无人机平台上是一种有效的定位方法。感知规划器的设计，保证了在高速运动中视觉信息的可靠性，提升了系统的整体鲁棒性。

**关键设计**：卡尔曼滤波器的参数需要仔细调整，以平衡VIO和门检测的权重。感知规划器需要考虑无人机的运动学约束和视觉感知范围，以生成可行的轨迹。YOLO模型的选择和训练也至关重要，需要保证在各种光照和视角下都能准确检测到门。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20475v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20475v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20475v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该系统在Abu Dhabi Autonomous Racing League (A2RL) x Drone Champions League competition (DCL)比赛中取得了显著成绩，包括AI Grand Challenge第三名（最高速度43.2 km/h）、AI Drag Race第二名（速度超过59 km/h）和AI Multi-Drone Race第二名。这些结果表明，所提出的漂移校正和感知规划方法在高速无人机竞速中具有优越的性能。

## 🎯 应用场景

该研究成果可应用于资源受限环境下的自主导航，例如室内机器人、无人机巡检等。通过融合视觉信息和惯性测量，可以提高定位精度和鲁棒性，为自主系统提供更可靠的环境感知能力。未来的研究可以探索更高效的视觉特征提取方法和更鲁棒的融合算法，以进一步提升系统的性能。

## 📄 摘要（原文）

> The Abu Dhabi Autonomous Racing League(A2RL) x Drone Champions League competition(DCL) requires teams to perform high-speed autonomous drone racing using only a single camera and a low-quality inertial measurement unit -- a minimal sensor set that mirrors expert human drone racing pilots. This sensor limitation makes the system susceptible to drift from Visual-Inertial Odometry (VIO), particularly during long and fast flights with aggressive maneuvers. This paper presents the system developed for the championship, which achieved a competitive performance. Our approach corrected VIO drift by fusing its output with global position measurements derived from a YOLO-based gate detector using a Kalman filter. A perception-aware planner generated trajectories that balance speed with the need to keep gates visible for the perception system. The system demonstrated high performance, securing podium finishes across multiple categories: third place in the AI Grand Challenge with top speed of 43.2 km/h, second place in the AI Drag Race with over 59 km/h, and second place in the AI Multi-Drone Race. We detail the complete architecture and present a performance analysis based on experimental data from the competition, contributing our insights on building a successful system for monocular vision-based autonomous drone flight.

