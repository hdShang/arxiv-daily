---
layout: default
title: "Conflict-Based Search as a Protocol: A Multi-Agent Motion Planning Protocol for Heterogeneous Agents, Solvers, and Independent Tasks"
---

# Conflict-Based Search as a Protocol: A Multi-Agent Motion Planning Protocol for Heterogeneous Agents, Solvers, and Independent Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00425" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00425v1</a>
  <a href="https://arxiv.org/pdf/2510.00425.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00425v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00425v1', 'Conflict-Based Search as a Protocol: A Multi-Agent Motion Planning Protocol for Heterogeneous Agents, Solvers, and Independent Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rishi Veerapaneni, Alvin Tang, Haodong He, Sophia Zhao, Viraj Shah, Yidai Cen, Ziteng Ji, Gabriel Olin, Jon Arrizabalaga, Yorai Shaoul, Jiaoyang Li, Maxim Likhachev

**分类**: cs.MA, cs.RO

**发布日期**: 2025-10-01

**备注**: Project webpage: https://rishi-v.github.io/CBS-Protocol/

---

## 💡 一句话要点

**提出基于冲突搜索协议的多智能体异构运动规划方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体系统` `运动规划` `冲突搜索` `异构机器人` `机器人协同`

## 📋 核心要点

1. 现有方法难以协调异构机器人团队在复杂环境中完成独立任务，面临算法兼容性挑战。
2. 利用冲突搜索（CBS）作为协议，通过统一的单智能体运动规划API实现异构智能体间的无碰撞路径规划。
3. 实验验证了该协议在多种单智能体规划器上的有效性，实现了异构智能体团队的高效协同运动。

## 📝 摘要（中文）

本文提出了一种基于冲突搜索（CBS）协议的多智能体运动规划方法，旨在解决由不同制造商生产的异构机器人团队在共享环境中高效移动的问题。该方法的核心是利用CBS协议，仅需一个满足特定时空约束的单智能体运动规划API。CBS使用中心规划器寻找无碰撞路径，而无需关心API的具体实现方式。实验证明，该协议能够为完成独立任务的异构智能体团队实现多智能体运动规划，支持包括启发式搜索（如A*）、基于采样的搜索（如RRT）、优化（如直接配置）、扩散和强化学习等多种单智能体规划器。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体系统中，异构智能体（例如，来自不同制造商的机器人，使用不同的运动规划算法）如何在共享环境中高效、无碰撞地完成各自独立任务的问题。现有方法的痛点在于，不同智能体的运动规划器可能不兼容，难以直接进行协同规划。

**核心思路**：论文的核心思路是将冲突搜索（Conflict-Based Search, CBS）作为一种协议来使用。CBS的核心思想是首先为每个智能体独立规划路径，然后检测和解决智能体之间的冲突。通过将CBS作为一个协议，论文将多智能体规划问题分解为两个层次：高层的冲突解决和底层的单智能体路径规划。

**技术框架**：整体框架包含两个主要模块：高层冲突树搜索和底层单智能体路径规划。高层冲突树搜索负责检测和解决智能体之间的冲突，生成一系列约束条件。底层单智能体路径规划模块则负责在给定约束条件下，为每个智能体寻找一条无碰撞路径。该框架迭代进行，直到找到所有智能体的无冲突路径。

**关键创新**：最重要的技术创新点在于将CBS作为一种协议，实现了异构智能体之间的协同运动规划。与现有方法相比，该方法不需要所有智能体使用相同的运动规划器，而是允许每个智能体使用最适合自己的规划器。这大大提高了系统的灵活性和适应性。

**关键设计**：CBS协议的关键设计在于定义了一个统一的单智能体运动规划API，该API接受时空约束作为输入，并返回一条满足约束的无碰撞路径。高层冲突解决策略也至关重要，常见的策略包括选择冲突最严重的智能体对进行分解，以及使用启发式函数来指导搜索方向。此外，论文可能还涉及一些参数设置，例如冲突检测的阈值、搜索树的扩展策略等，但具体细节未知。

## 📊 实验亮点

论文展示了该协议能够支持多种单智能体规划器，包括A*、RRT、直接配置、扩散和强化学习等。虽然论文中没有给出具体的性能数据，但强调了该方法在异构智能体团队中的适用性和灵活性。具体的性能提升幅度未知，但该方法为异构智能体协同运动规划提供了一种有效的解决方案。

## 🎯 应用场景

该研究成果可广泛应用于多机器人协同作业场景，如智能仓储、自动化工厂、建筑工地、医院物流等。通过该方法，不同类型的机器人能够安全高效地协同完成任务，提高生产效率和服务质量。未来，该技术有望推动多智能体系统的发展，实现更复杂的机器人协作。

## 📄 摘要（原文）

> Imagine the future construction site, hospital, office, or even sophisticated household with dozens of robots bought from different manufacturers. How can we enable these different systems to effectively move in a shared environment, given that each robot may have its own independent motion planning system? This work shows how we can get efficient collision-free movements between algorithmically heterogeneous agents by using Conflict-Based Search (Sharon et al. 2015) as a protocol. At its core, the CBS Protocol requires one specific single-agent motion planning API; finding a collision-free path that satisfies certain space-time constraints. Given such an API, CBS uses a central planner to find collision-free paths - independent of how the API is implemented. We show how this protocol enables multi-agent motion planning for a heterogeneous team of agents completing independent tasks with a variety of single-agent planners including: Heuristic Search (e.g., A*), Sampling Based Search (e.g., RRT), Optimization (e.g., Direct Collocation), Diffusion, and Reinforcement Learning.

