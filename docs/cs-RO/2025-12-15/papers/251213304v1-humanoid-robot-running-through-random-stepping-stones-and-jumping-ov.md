---
layout: default
title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories
---

# Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13304" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13304v1</a>
  <a href="https://arxiv.org/pdf/2512.13304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13304v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13304v1', 'Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sait Sovukluk, Johannes Englsberger, Christian Ott

**分类**: cs.RO

**发布日期**: 2025-12-15

**备注**: Accepted for publication in Biomimetic Intelligence and Robotics. Supplemental video: https://youtu.be/HlAg2nbNct4

---

## 💡 一句话要点

**提出基于弹簧-质量轨迹的人形机器人步态自适应框架，实现复杂地形运动。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `步态规划` `弹簧-质量模型` `全身控制` `步态自适应`

## 📋 核心要点

1. 现有方法在复杂地形下人形机器人运动控制方面存在挑战，难以兼顾鲁棒性和敏捷性。
2. 该论文提出基于弹簧-质量模型的步态规划与自适应框架，结合全身控制实现复杂地形运动。
3. 实验表明，该框架能使人形机器人在随机踏脚石、跳跃障碍等场景下稳定运动，且无需额外调参。

## 📝 摘要（中文）

本研究提出了一种步态自适应框架，用于通过弹簧-质量轨迹和无差拍控制增益库实现跑步运动。该框架包含四个主要部分：（1）自动生成弹簧-质量轨迹库；（2）通过主动控制的模板模型生成无差拍控制增益库，该模型能够很好地模拟全身动力学；（3）开发用于步态自适应的轨迹选择策略；（4）通过全身控制（WBC）框架将弹簧-质量轨迹映射到人形机器人模型，同时考虑闭链运动系统、自碰撞和反应性肢体摆动。我们通过各种具有挑战性的敏捷行为，例如在随机生成的踏脚石上跑步、跳过随机障碍物、执行蛇形运动、用随机一条腿突然改变跑步方向以及通过MuJoCo物理模拟器抑制显著的扰动和不确定性，展示了所提出框架的包容性和鲁棒性。我们还在一套全面的不确定性和噪声下进行了额外的模拟，以更好地证明所提出的方法对现实世界挑战的鲁棒性，包括信号噪声、不精确性、建模误差和延迟。所有上述行为都是使用单个库和同一组WBC控制参数执行的，无需额外调整。弹簧-质量和无差拍控制增益库总共在4.5秒内自动计算出315条不同的轨迹。

## 🔬 方法详解

**问题定义**：论文旨在解决人形机器人在复杂地形（如随机分布的踏脚石、障碍物）中运动的难题。现有方法通常难以在鲁棒性和敏捷性之间取得平衡，难以适应地形变化，需要大量人工调整参数。

**核心思路**：核心思路是利用弹簧-质量模型来简化人形机器人的运动规划，并结合无差拍控制增益库实现快速的步态自适应。弹簧-质量模型能够捕捉跑步运动的关键动力学特征，而无差拍控制则保证了快速的响应和稳定性。

**技术框架**：整体框架包含四个主要模块：1) 自动生成弹簧-质量轨迹库；2) 生成无差拍控制增益库；3) 开发轨迹选择策略，用于步态自适应；4) 通过全身控制（WBC）框架将弹簧-质量轨迹映射到人形机器人模型，同时考虑闭链运动系统、自碰撞和反应性肢体摆动。

**关键创新**：关键创新在于将弹簧-质量模型与无差拍控制相结合，实现了一种高效且鲁棒的步态自适应方法。此外，该框架能够自动生成轨迹库和控制增益库，减少了人工调整的工作量。

**关键设计**：轨迹选择策略是关键设计之一，它根据当前地形和机器人状态，从轨迹库中选择合适的轨迹。全身控制框架则负责将选定的轨迹转化为机器人关节的控制指令，同时考虑各种约束条件，如自碰撞避免和关节力矩限制。论文中提到，弹簧-质量和无差拍控制增益库总共在4.5秒内自动计算出315条不同的轨迹。

## 📊 实验亮点

实验结果表明，该框架能够使人形机器人在各种复杂地形下稳定运动，包括随机踏脚石、跳跃障碍物、蛇形运动等。所有行为均使用单一库和相同的WBC控制参数执行，无需额外调整。弹簧-质量和无差拍控制增益库在4.5秒内自动计算出315条不同的轨迹，验证了该方法的效率和鲁棒性。

## 🎯 应用场景

该研究成果可应用于人形机器人在复杂环境下的搜索救援、物流运输、灾后重建等领域。通过提高机器人的运动能力和环境适应性，使其能够在人类难以到达或危险的区域执行任务，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> This study proposes a step adaptation framework for running through spring-mass trajectories and deadbeat control gain libraries. It includes four main parts: (1) Automatic spring-mass trajectory library generation; (2) Deadbeat control gain library generation through an actively controlled template model that resembles the whole-body dynamics well; (3) Trajectory selection policy development for step adaptation; (4) Mapping spring-mass trajectories to a humanoid model through a whole-body control (WBC) framework also accounting for closed-kinematic chain systems, self collisions, and reactive limb swinging. We show the inclusiveness and the robustness of the proposed framework through various challenging and agile behaviors such as running through randomly generated stepping stones, jumping over random obstacles, performing slalom motions, changing the running direction suddenly with a random leg, and rejecting significant disturbances and uncertainties through the MuJoCo physics simulator. We also perform additional simulations under a comprehensive set of uncertainties and noise to better justify the proposed method's robustness to real-world challenges, including signal noise, imprecision, modeling errors, and delays. All the aforementioned behaviors are performed with a single library and the same set of WBC control parameters without additional tuning. The spring-mass and the deadbeat control gain library are automatically computed in 4.5 seconds in total for 315 different trajectories.

