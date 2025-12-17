---
layout: default
title: Manifold-constrained Hamilton-Jacobi Reachability Learning for Decentralized Multi-Agent Motion Planning
---

# Manifold-constrained Hamilton-Jacobi Reachability Learning for Decentralized Multi-Agent Motion Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03591" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03591v1</a>
  <a href="https://arxiv.org/pdf/2511.03591.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03591v1" onclick="toggleFavorite(this, '2511.03591v1', 'Manifold-constrained Hamilton-Jacobi Reachability Learning for Decentralized Multi-Agent Motion Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingyi Chen, Ruiqi Ni, Jun Kim, Ahmed H. Qureshi

**分类**: cs.RO, eess.SY

**发布日期**: 2025-11-05

---

## 💡 一句话要点

**提出流形约束Hamilton-Jacobi可达性学习，用于分散式多智能体运动规划**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多智能体运动规划` `流形约束` `Hamilton-Jacobi可达性` `分散式控制` `轨迹优化`

## 📋 核心要点

1. 现有分散式多智能体运动规划方法难以处理任务诱导的流形约束，例如服务机器人保持杯子直立。
2. 提出流形约束的Hamilton-Jacobi可达性学习框架，将任务相关的安全条件融入分散式轨迹优化中。
3. 实验结果表明，该方法优于现有约束运动规划器，并适用于高维多智能体操作的实时应用。

## 📝 摘要（中文）

本文提出了一种流形约束的Hamilton-Jacobi可达性(HJR)学习框架，用于分散式多智能体运动规划(MAMP)。该方法解决了流形约束下的HJR问题，以捕获任务相关的安全条件，并将其集成到分散式轨迹优化规划器中。这使得机器人能够在不需要假设其他智能体策略的情况下，生成既安全又任务可行的运动计划。该方法可以推广到各种流形约束任务，并有效地扩展到高维多智能体操作问题。实验表明，该方法优于现有的约束运动规划器，并以适合实际应用的速度运行。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体运动规划中，如何在满足任务诱导的流形约束（例如保持杯子直立）的同时，保证运动安全的问题。现有方法难以在高维空间中有效地处理此类约束，或者需要对其他智能体的策略做出假设，限制了其在复杂动态环境中的应用。

**核心思路**：论文的核心思路是将任务相关的安全条件通过求解流形约束下的Hamilton-Jacobi可达性(HJR)问题来显式地建模。然后，将这些安全条件集成到分散式轨迹优化规划器中，从而使每个智能体都能够在规划自身轨迹时考虑到任务约束和避免碰撞，而无需依赖其他智能体的策略。

**技术框架**：整体框架包含两个主要阶段：1) **流形约束HJR学习**：利用学习方法求解流形约束下的HJR方程，得到安全可达集，从而捕获任务相关的安全条件。2) **分散式轨迹优化**：将学习到的安全可达集作为约束条件，集成到分散式轨迹优化规划器中，每个智能体独立地优化自身的轨迹，同时避免碰撞和满足任务约束。

**关键创新**：最重要的技术创新点在于将流形约束的HJR问题与分散式轨迹优化相结合。通过HJR学习，显式地建模了任务相关的安全条件，避免了对其他智能体策略的假设，提高了规划的鲁棒性和适应性。与现有方法相比，该方法能够更好地处理高维空间中的复杂约束，并实现更安全、更高效的多智能体运动规划。

**关键设计**：论文的关键设计包括：1) 如何定义和表示流形约束，例如使用隐式曲面函数。2) 如何设计HJR学习算法，以有效地求解流形约束下的HJR方程，例如使用神经网络逼近值函数。3) 如何将学习到的安全可达集集成到轨迹优化器中，例如作为约束条件或惩罚项。具体的参数设置、损失函数和网络结构等细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

实验结果表明，该方法在多种流形约束任务中优于现有的约束运动规划器。具体性能数据（例如成功率、规划时间、碰撞率等）和提升幅度在论文中进行了详细展示（未知）。视频演示进一步验证了该方法在实际场景中的有效性和实时性。

## 🎯 应用场景

该研究成果可应用于服务机器人、自动驾驶、无人机编队等领域。例如，服务机器人可以在人群中安全地运送物品，自动驾驶车辆可以在复杂交通环境中安全行驶，无人机编队可以执行复杂的协同任务。该方法能够提高多智能体系统的安全性、可靠性和效率，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Safe multi-agent motion planning (MAMP) under task-induced constraints is a critical challenge in robotics. Many real-world scenarios require robots to navigate dynamic environments while adhering to manifold constraints imposed by tasks. For example, service robots must carry cups upright while avoiding collisions with humans or other robots. Despite recent advances in decentralized MAMP for high-dimensional systems, incorporating manifold constraints remains difficult. To address this, we propose a manifold-constrained Hamilton-Jacobi reachability (HJR) learning framework for decentralized MAMP. Our method solves HJR problems under manifold constraints to capture task-aware safety conditions, which are then integrated into a decentralized trajectory optimization planner. This enables robots to generate motion plans that are both safe and task-feasible without requiring assumptions about other agents' policies. Our approach generalizes across diverse manifold-constrained tasks and scales effectively to high-dimensional multi-agent manipulation problems. Experiments show that our method outperforms existing constrained motion planners and operates at speeds suitable for real-world applications. Video demonstrations are available at https://youtu.be/RYcEHMnPTH8 .

