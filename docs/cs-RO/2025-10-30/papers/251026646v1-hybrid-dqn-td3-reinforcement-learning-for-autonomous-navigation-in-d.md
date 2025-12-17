---
layout: default
title: Hybrid DQN-TD3 Reinforcement Learning for Autonomous Navigation in Dynamic Environments
---

# Hybrid DQN-TD3 Reinforcement Learning for Autonomous Navigation in Dynamic Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26646" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26646v1</a>
  <a href="https://arxiv.org/pdf/2510.26646.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26646v1" onclick="toggleFavorite(this, '2510.26646v1', 'Hybrid DQN-TD3 Reinforcement Learning for Autonomous Navigation in Dynamic Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyi He, Danggui Chen, Zhenshuo Zhang, Zimeng Bai

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-10-30

**备注**: 6 pages, 5 figures; ROS+Gazebo (TurtleBot3) implementation; evaluation with PathBench metrics; code (primary): https://github.com/MayaCHEN-github/HierarchicalRL-robot-navigation; mirror (for reproducibility): https://github.com/ShowyHe/DRL-robot-navigation

---

## 💡 一句话要点

**提出混合DQN-TD3强化学习方法，用于动态环境中自主导航。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `自主导航` `DQN` `TD3` `分层控制` `机器人` `动态环境`

## 📋 核心要点

1. 现有方法在动态环境中自主导航面临挑战，难以兼顾全局规划和局部控制。
2. 采用分层强化学习框架，DQN负责高层决策，TD3负责底层控制，实现全局规划与局部控制的结合。
3. 实验结果表明，该方法在成功率和样本效率方面优于单一算法基线和基于规则的规划器。

## 📝 摘要（中文）

本文提出了一种分层路径规划与控制框架，该框架结合了高层深度Q网络（DQN）用于离散子目标选择，以及低层双延迟深度确定性策略梯度（TD3）控制器用于连续动作控制。高层模块选择行为和子目标；低层模块执行平滑的速度指令。我们设计了一种实用的奖励塑造方案（方向、距离、避障、动作平滑性、碰撞惩罚、时间惩罚和进度），以及一个基于激光雷达的安全门，以防止不安全的运动。该系统在ROS + Gazebo（TurtleBot3）中实现，并使用PathBench指标（包括成功率、碰撞率、路径效率和重规划效率）在动态和部分可观察的环境中进行评估。实验表明，与单一算法基线（单独的DQN或TD3）和基于规则的规划器相比，该方法提高了成功率和样本效率，并且更好地泛化到未见过的障碍物配置，并减少了突发的控制变化。代码和评估脚本可在项目存储库中找到。

## 🔬 方法详解

**问题定义**：在动态和部分可观测环境中，自主导航需要同时考虑全局路径规划和局部运动控制。传统方法，如单独使用DQN或TD3，难以在探索效率、泛化能力和控制平滑性之间取得平衡。基于规则的规划器难以适应复杂和未知的环境。

**核心思路**：采用分层强化学习架构，将导航任务分解为高层离散决策和低层连续控制。高层DQN负责选择子目标，引导全局路径规划；低层TD3负责执行平滑的速度指令，实现局部运动控制。这种分层结构能够有效利用DQN的离散决策能力和TD3的连续控制能力，提高导航效率和鲁棒性。

**技术框架**：整体框架包含两个主要模块：高层DQN子目标选择器和低层TD3速度控制器。首先，DQN根据当前环境状态选择一个子目标。然后，TD3控制器接收该子目标，并生成相应的速度指令，控制机器人运动。通过ROS和Gazebo平台进行仿真实验。

**关键创新**：该方法的核心创新在于混合使用DQN和TD3，形成一个互补的强化学习系统。DQN擅长离散动作空间的决策，TD3擅长连续动作空间的控制。这种混合方法能够更好地适应动态环境中的自主导航任务，提高导航性能。

**关键设计**：奖励函数的设计至关重要，包括方向奖励、距离奖励、避障奖励、动作平滑性奖励、碰撞惩罚、时间惩罚和进度奖励。基于激光雷达的安全门用于防止不安全的运动。DQN使用ε-greedy策略进行探索，TD3使用高斯噪声进行探索。网络的具体结构（层数、神经元数量等）根据实验结果进行调整。

## 📊 实验亮点

实验结果表明，该混合DQN-TD3方法在成功率、碰撞率、路径效率和重规划效率等方面均优于单一算法基线（DQN或TD3）和基于规则的规划器。尤其是在未见过的障碍物配置中，该方法表现出更好的泛化能力，并减少了突发的控制变化。具体性能数据可在项目仓库中找到。

## 🎯 应用场景

该研究成果可应用于各种需要自主导航的机器人系统，例如服务机器人、物流机器人、无人驾驶车辆等。通过提高机器人在复杂动态环境中的导航能力，可以提升工作效率，降低安全风险，并扩展机器人的应用范围。

## 📄 摘要（原文）

> This paper presents a hierarchical path-planning and control framework that combines a high-level Deep Q-Network (DQN) for discrete sub-goal selection with a low-level Twin Delayed Deep Deterministic Policy Gradient (TD3) controller for continuous actuation. The high-level module selects behaviors and sub-goals; the low-level module executes smooth velocity commands. We design a practical reward shaping scheme (direction, distance, obstacle avoidance, action smoothness, collision penalty, time penalty, and progress), together with a LiDAR-based safety gate that prevents unsafe motions. The system is implemented in ROS + Gazebo (TurtleBot3) and evaluated with PathBench metrics, including success rate, collision rate, path efficiency, and re-planning efficiency, in dynamic and partially observable environments. Experiments show improved success rate and sample efficiency over single-algorithm baselines (DQN or TD3 alone) and rule-based planners, with better generalization to unseen obstacle configurations and reduced abrupt control changes. Code and evaluation scripts are available at the project repository.

