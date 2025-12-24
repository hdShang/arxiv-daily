---
layout: default
title: "APT*: Asymptotically Optimal Motion Planning via Adaptively Prolated Elliptical R-Nearest Neighbors"
---

# APT*: Asymptotically Optimal Motion Planning via Adaptively Prolated Elliptical R-Nearest Neighbors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19790" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19790v1</a>
  <a href="https://arxiv.org/pdf/2508.19790.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19790v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19790v1', 'APT*: Asymptotically Optimal Motion Planning via Adaptively Prolated Elliptical R-Nearest Neighbors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liding Zhang, Sicheng Wang, Kuanqi Cai, Zhenshan Bing, Fan Wu, Chaoqun Wang, Sami Haddadin, Alois Knoll

**分类**: cs.RO

**发布日期**: 2025-08-27

**期刊**: IEEE Robotics and Automation Letters 2025

**DOI**: [10.1109/LRA.2025.3598616](https://doi.org/10.1109/LRA.2025.3598616)

---

## 💡 一句话要点

**提出APT*以解决动态环境下的最优路径规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `路径规划` `运动规划` `自适应算法` `高维空间` `机器人操作` `采样方法` `动态环境`

## 📋 核心要点

1. 现有的路径规划方法通常使用固定的批处理大小，无法有效应对动态环境中的障碍物信息，导致规划效率低下。
2. APT*通过引入自适应批处理大小和椭圆$r$-最近邻模块，能够根据环境反馈动态调整路径搜索过程，提高了路径规划的灵活性和效率。
3. 实验结果表明，APT*在高维空间中显著优于传统的单查询采样规划器，且在实际机器人操作任务中表现出色。

## 📝 摘要（中文）

最优路径规划旨在确定从起点到目标的一系列状态，同时考虑规划目标。现有方法通常采用固定的批处理大小，忽视了障碍物信息，缺乏针对性。本研究提出了一种新的基于采样的运动规划器APT*，该方法基于力方向信息树（FDIT*）进行扩展，集成了自适应批处理大小和椭圆$r$-最近邻模块，能够根据环境反馈动态调节路径搜索过程。APT*根据信息集的超体积调整批处理大小，并将顶点视为遵循库仑定律的电荷，通过邻居样本定义虚拟力，从而优化椭圆最近邻选择。这些模块采用非线性椭圆方法自适应调整顶点的电荷以定义力，从而提高收敛速度并降低解决成本。比较分析表明，APT*在从$	ext{R}^4$到$	ext{R}^{16}$的维度上优于现有的单查询采样规划器，并通过实际机器人操作任务进行了验证。

## 🔬 方法详解

**问题定义**：本论文旨在解决动态环境下的最优路径规划问题，现有方法的痛点在于固定的批处理大小和对障碍物信息的忽视，导致规划效率低下和路径质量不佳。

**核心思路**：APT*的核心思路是通过自适应批处理大小和椭圆$r$-最近邻模块，结合环境反馈动态调节路径搜索过程，从而提高路径规划的灵活性和效率。

**技术框架**：APT*的整体架构包括信息集的超体积计算、邻居样本的虚拟力定义和椭圆最近邻选择等主要模块。首先，根据环境反馈调整批处理大小，然后通过电荷模型定义虚拟力，最后优化路径搜索过程。

**关键创新**：APT*的主要创新在于将顶点视为遵循库仑定律的电荷，通过非线性椭圆方法自适应调整电荷，从而优化邻居选择和路径搜索过程。这一设计使得APT*在高维空间中具有更好的收敛性和路径质量。

**关键设计**：在设计中，APT*采用了动态调整的批处理大小策略，利用信息集的超体积进行计算，并通过邻居样本的电荷模型定义虚拟力，以实现更高效的路径搜索。

## 📊 实验亮点

实验结果显示，APT*在从$	ext{R}^4$到$	ext{R}^{16}$的高维空间中，相较于现有单查询采样规划器，路径规划效率提高了显著的百分比，并在实际机器人操作任务中成功验证了其有效性。

## 🎯 应用场景

APT*在机器人导航、自动驾驶、无人机飞行等领域具有广泛的应用潜力。其自适应的路径规划能力能够有效应对复杂和动态的环境，提高机器人在实际操作中的灵活性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Optimal path planning aims to determine a sequence of states from a start to a goal while accounting for planning objectives. Popular methods often integrate fixed batch sizes and neglect information on obstacles, which is not problem-specific. This study introduces Adaptively Prolated Trees (APT*), a novel sampling-based motion planner that extends based on Force Direction Informed Trees (FDIT*), integrating adaptive batch-sizing and elliptical $r$-nearest neighbor modules to dynamically modulate the path searching process based on environmental feedback. APT* adjusts batch sizes based on the hypervolume of the informed sets and considers vertices as electric charges that obey Coulomb's law to define virtual forces via neighbor samples, thereby refining the prolate nearest neighbor selection. These modules employ non-linear prolate methods to adaptively adjust the electric charges of vertices for force definition, thereby improving the convergence rate with lower solution costs. Comparative analyses show that APT* outperforms existing single-query sampling-based planners in dimensions from $\mathbb{R}^4$ to $\mathbb{R}^{16}$, and it was further validated through a real-world robot manipulation task. A video showcasing our experimental results is available at: https://youtu.be/gCcUr8LiEw4

