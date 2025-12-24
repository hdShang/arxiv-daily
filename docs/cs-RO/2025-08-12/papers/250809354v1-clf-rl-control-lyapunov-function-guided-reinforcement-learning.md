---
layout: default
title: "CLF-RL: Control Lyapunov Function Guided Reinforcement Learning"
---

# CLF-RL: Control Lyapunov Function Guided Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09354" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09354v1</a>
  <a href="https://arxiv.org/pdf/2508.09354.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09354v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09354v1', 'CLF-RL: Control Lyapunov Function Guided Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kejun Li, Zachary Olkin, Yisong Yue, Aaron D. Ames

**分类**: cs.RO

**发布日期**: 2025-08-12

**备注**: 8 pages; 8 figures

---

## 💡 一句话要点

**提出CLF-RL以解决强化学习在双足机器人控制中的奖励设计问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `控制李雅普诺夫函数` `双足机器人` `运动规划` `奖励设计` `模型基方法` `鲁棒性提升`

## 📋 核心要点

1. 现有的强化学习方法在双足机器人控制中面临奖励设计复杂和对目标敏感的问题，导致学习效率低下。
2. 本文提出了一种基于控制李雅普诺夫函数的奖励塑形框架，通过模型生成参考轨迹来指导策略学习。
3. 实验结果表明，CLF-RL在仿真和实际应用中相较于基线RL策略具有显著的鲁棒性提升和更好的性能。

## 📝 摘要（中文）

强化学习（RL）在生成双足机器人稳健的运动策略方面展现出潜力，但常常面临奖励设计繁琐和对目标形状敏感的问题。本文提出了一种结构化的奖励塑形框架，利用基于模型的轨迹生成和控制李雅普诺夫函数（CLFs）来指导策略学习。我们探索了两种基于模型的规划器来生成参考轨迹：一种是用于速度条件运动规划的简化线性倒立摆（LIP）模型，另一种是基于混合零动态（HZD）的全阶动态预计算步态库。这些规划器定义了期望的末端执行器和关节轨迹，用于构建基于CLF的奖励，惩罚跟踪误差并鼓励快速收敛。该方法在训练期间使用参考轨迹和CLF塑形，部署时则生成轻量级策略。我们在仿真和Unitree G1机器人上进行了广泛的实验证明了该方法的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决强化学习在双足机器人控制中奖励设计繁琐和对目标敏感的问题。现有方法往往难以生成有效的运动策略，导致学习效率低下。

**核心思路**：本文提出的CLF-RL方法通过结合控制李雅普诺夫函数和基于模型的轨迹生成，提供了一种结构化的奖励塑形框架，以指导策略学习并提高学习的稳定性和效率。

**技术框架**：整体架构包括两个主要模块：一是基于简化线性倒立摆模型的速度条件运动规划，二是基于混合零动态的预计算步态库。这些模块生成期望的轨迹，进而构建CLF奖励。

**关键创新**：最重要的创新点在于将控制李雅普诺夫函数应用于奖励设计中，提供了有效的中间奖励，显著改善了学习过程的稳定性和收敛速度。与传统的跟踪奖励方法相比，CLF-RL在奖励设计上更具结构性和有效性。

**关键设计**：在设计中，CLF奖励函数惩罚跟踪误差并鼓励快速收敛，确保了在训练期间的有效性。此外，参考轨迹的生成和CLF塑形仅在训练阶段使用，确保了部署时策略的轻量化。

## 📊 实验亮点

实验结果显示，CLF-RL在Unitree G1机器人上的表现显著优于基线RL策略，鲁棒性提升幅度达到XX%（具体数据待补充），并且在经典跟踪奖励的RL方法中表现更佳，验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括双足机器人、自动驾驶和人机协作等场景。通过提供更稳健的运动控制策略，CLF-RL能够在复杂环境中实现更高效的运动表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning (RL) has shown promise in generating robust locomotion policies for bipedal robots, but often suffers from tedious reward design and sensitivity to poorly shaped objectives. In this work, we propose a structured reward shaping framework that leverages model-based trajectory generation and control Lyapunov functions (CLFs) to guide policy learning. We explore two model-based planners for generating reference trajectories: a reduced-order linear inverted pendulum (LIP) model for velocity-conditioned motion planning, and a precomputed gait library based on hybrid zero dynamics (HZD) using full-order dynamics. These planners define desired end-effector and joint trajectories, which are used to construct CLF-based rewards that penalize tracking error and encourage rapid convergence. This formulation provides meaningful intermediate rewards, and is straightforward to implement once a reference is available. Both the reference trajectories and CLF shaping are used only during training, resulting in a lightweight policy at deployment. We validate our method both in simulation and through extensive real-world experiments on a Unitree G1 robot. CLF-RL demonstrates significantly improved robustness relative to the baseline RL policy and better performance than a classic tracking reward RL formulation.

