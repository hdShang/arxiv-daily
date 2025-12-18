---
layout: default
title: Multi-directional Safe Rectangle Corridor-Based MPC for Nonholonomic Robots Navigation in Cluttered Environment
---

# Multi-directional Safe Rectangle Corridor-Based MPC for Nonholonomic Robots Navigation in Cluttered Environment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13215" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13215v1</a>
  <a href="https://arxiv.org/pdf/2512.13215.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13215v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13215v1', 'Multi-directional Safe Rectangle Corridor-Based MPC for Nonholonomic Robots Navigation in Cluttered Environment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinsong Qu, Yunxiang Li, Shanlin Zhong

**分类**: cs.RO

**发布日期**: 2025-12-15

**备注**: 9 pages, 11 figures, conference paper for the 2025 International Conference on Advanced Robotics and Mechatronics (ICARM), accepted

---

## 💡 一句话要点

**提出基于多方向安全矩形走廊的MPC方法，解决非完整机器人复杂环境导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `移动机器人导航` `模型预测控制` `非完整约束` `动态避障` `安全走廊` `路径规划` `最优控制`

## 📋 核心要点

1. 现有AMR在复杂环境中导航面临非完整约束、动态障碍物交互以及非凸约束空间等挑战。
2. 论文提出ISMPC框架，利用多方向安全矩形走廊编码自由空间，并结合障碍函数约束实现避障。
3. 实验结果表明，该框架在自由空间利用率上提升了41.05%，同时保持了3ms的实时走廊生成速度。

## 📝 摘要（中文）

本文提出了一种改进的序列模型预测控制（ISMPC）导航框架，旨在解决AMR在复杂、半结构化环境中导航的挑战。该框架将导航任务系统地重构为序列切换最优控制问题，并通过两个关键创新解决上述挑战：1）实现多方向安全矩形走廊（MDSRC）算法，通过矩形凸区域编码自由空间，避免与静态障碍物碰撞，消除冗余计算负担并加速求解器收敛；2）提出了一种集成了走廊约束和障碍函数约束的序列MPC导航框架，以实现静态和动态障碍物规避。ISMPC导航框架能够为AMR直接生成速度，简化了传统导航算法架构。对比实验表明，该框架在自由空间利用率方面具有优越性（平均走廊面积增加了41.05％），同时保持了实时的计算性能（平均走廊生成延迟为3毫秒）。

## 🔬 方法详解

**问题定义**：论文旨在解决非完整约束移动机器人在复杂、拥挤环境中安全高效导航的问题。现有方法通常计算复杂度高，难以在动态环境中实现实时避障，并且在自由空间利用率方面存在不足。传统方法难以兼顾非完整约束、动态障碍物和非凸环境约束，导致导航性能下降。

**核心思路**：论文的核心思路是将复杂的导航问题分解为一系列序列切换最优控制问题，并通过构建安全走廊来简化环境表示，降低计算复杂度。同时，结合模型预测控制（MPC）和障碍函数，实现动态避障和轨迹优化。通过多方向安全矩形走廊（MDSRC）算法，高效地编码自由空间，并利用矩形凸区域的特性加速求解器收敛。

**技术框架**：ISMPC导航框架主要包含以下几个阶段：1) 环境感知与地图构建：获取环境信息，构建静态障碍物地图。2) 多方向安全矩形走廊生成：利用MDSRC算法，在自由空间中生成一系列矩形走廊，形成安全通道。3) 序列MPC优化：将导航任务分解为一系列MPC问题，每个MPC问题在当前走廊内进行轨迹优化，并考虑动态障碍物的威胁。4) 速度指令生成与执行：根据MPC的优化结果，生成机器人的速度指令，并控制机器人运动。

**关键创新**：论文的关键创新在于多方向安全矩形走廊（MDSRC）算法和集成了走廊约束与障碍函数约束的序列MPC框架。MDSRC算法能够更有效地利用自由空间，生成更宽敞的走廊，从而提高导航效率。序列MPC框架则能够更好地处理动态障碍物，保证机器人的安全。与传统方法相比，该方法能够直接生成速度指令，简化了导航算法的架构。

**关键设计**：MDSRC算法的关键设计在于矩形走廊的方向选择和尺寸优化。论文采用了一种启发式方法来选择矩形走廊的方向，并利用凸优化方法来确定矩形走廊的尺寸，以最大化自由空间利用率。在序列MPC框架中，论文使用了障碍函数来约束机器人与动态障碍物之间的距离，并设计了合适的权重系数来平衡导航效率和安全性。

## 📊 实验亮点

实验结果表明，所提出的ISMPC导航框架在自由空间利用率方面相比传统方法提升了41.05%，这意味着机器人可以在更宽敞的走廊中移动，从而提高导航效率。同时，该框架保持了实时的计算性能，平均走廊生成延迟仅为3毫秒，满足了实际应用的需求。这些结果验证了该框架在复杂环境中导航的有效性和优越性。

## 🎯 应用场景

该研究成果可广泛应用于工业自动化、仓储物流、服务机器人等领域。通过提高AMR在复杂环境中的导航能力，可以显著提升生产效率、降低运营成本，并为实现更智能化的自动化生产线提供技术支撑。未来，该技术有望进一步拓展到无人驾驶、智能交通等领域，为构建更安全、高效的智能移动系统做出贡献。

## 📄 摘要（原文）

> Autonomous Mobile Robots (AMRs) have become indispensable in industrial applications due to their operational flexibility and efficiency. Navigation serves as a crucial technical foundation for accomplishing complex tasks. However, navigating AMRs in dense, cluttered, and semi-structured environments remains challenging, primarily due to nonholonomic vehicle dynamics, interactions with mixed static/dynamic obstacles, and the non-convex constrained nature of such operational spaces. To solve these problems, this paper proposes an Improved Sequential Model Predictive Control (ISMPC) navigation framework that systematically reformulates navigation tasks as sequential switched optimal control problems. The framework addresses the aforementioned challenges through two key innovations: 1) Implementation of a Multi-Directional Safety Rectangular Corridor (MDSRC) algorithm, which encodes the free space through rectangular convex regions to avoid collision with static obstacles, eliminating redundant computational burdens and accelerating solver convergence; 2) A sequential MPC navigation framework that integrates corridor constraints with barrier function constraints is proposed to achieve static and dynamic obstacle avoidance. The ISMPC navigation framework enables direct velocity generation for AMRs, simplifying traditional navigation algorithm architectures. Comparative experiments demonstrate the framework's superiority in free-space utilization ( an increase of 41.05$\%$ in the average corridor area) while maintaining real-time computational performance (average corridors generation latency of 3 ms).

