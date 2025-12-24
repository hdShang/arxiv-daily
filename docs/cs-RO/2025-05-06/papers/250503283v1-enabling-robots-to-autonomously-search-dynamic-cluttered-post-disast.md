---
layout: default
title: Enabling Robots to Autonomously Search Dynamic Cluttered Post-Disaster Environments
---

# Enabling Robots to Autonomously Search Dynamic Cluttered Post-Disaster Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03283" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03283v1</a>
  <a href="https://arxiv.org/pdf/2505.03283.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03283v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03283v1', 'Enabling Robots to Autonomously Search Dynamic Cluttered Post-Disaster Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karlo Rado, Mirko Baglioni, Anahita Jamshidnejad

**分类**: cs.RO, eess.SY

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出集成控制框架以解决灾后动态环境中的自主搜索问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `自主导航` `搜索与救援` `动态环境` `运动规划` `机器人控制` `不确定性处理` `鲁棒控制`

## 📋 核心要点

1. 现有的搜索与救援机器人在动态和复杂环境中导航时面临安全性和效率的挑战，尤其是在存在静态和动态障碍物的情况下。
2. 本研究提出了一种集成控制框架，结合了启发式运动规划和稳健的运动跟踪，旨在提高机器人在不确定环境中的导航能力。
3. 通过多次计算机模拟实验，所提框架在安全性和效率上显著优于传统方法，达到了42.3%的性能提升。

## 📝 摘要（中文）

本论文探讨了如何使机器人在灾后响应中自主执行搜索与救援任务，尤其是在动态且复杂的环境中安全导航的挑战。我们提出了一种集成控制框架，包含高效的启发式运动规划系统和稳健的运动跟踪系统，能够在考虑不确定性的情况下引导机器人沿着无碰撞的参考轨迹移动。通过计算机模拟实验，结果显示该框架在安全、无碰撞和最短时间内到达目标方面，相较于现有的两种主流方法（快速扩展随机树和人工势场法）表现出高达42.3%的优越性。

## 🔬 方法详解

**问题定义**：本论文旨在解决自主搜索与救援机器人在动态、复杂环境中安全导航的问题。现有方法在处理不确定性和动态障碍物时，往往无法保证安全和效率。

**核心思路**：论文提出的解决方案是一个集成控制框架，结合了启发式运动规划和稳健的运动跟踪系统，能够在动态环境中有效应对不确定性，确保机器人沿着安全轨迹移动。

**技术框架**：整体架构包括两个主要模块：启发式运动规划系统负责生成无碰撞的参考轨迹，运动跟踪系统则根据环境的动态变化调整机器人的运动，以保持在安全轨迹上。

**关键创新**：最重要的技术创新在于集成了运动规划与跟踪的双重机制，能够实时应对环境变化，显著提高了机器人在复杂环境中的导航能力。与现有方法相比，该框架在处理动态障碍物时表现出更高的安全性和效率。

**关键设计**：在设计中，运动规划系统采用了高效的启发式算法，确保快速生成参考轨迹；运动跟踪系统则使用了鲁棒控制策略，以应对不确定性和动态变化，确保机器人能够稳定地跟踪参考轨迹。具体的参数设置和损失函数设计在实验中经过多次调优，以达到最佳性能。

## 📊 实验亮点

实验结果表明，所提出的集成控制框架在安全、无碰撞和最短时间内到达目标方面，相较于快速扩展随机树和人工势场法，性能提升高达42.3%。这一显著的提升展示了新方法在复杂环境中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括灾后搜索与救援、危险环境下的自动化操作以及智能机器人在动态环境中的自主导航。其实际价值在于提高救援效率，减少人类在危险环境中的风险，未来可能推动机器人技术在紧急响应领域的广泛应用。

## 📄 摘要（原文）

> Robots will bring search and rescue (SaR) in disaster response to another level, in case they can autonomously take over dangerous SaR tasks from humans. A main challenge for autonomous SaR robots is to safely navigate in cluttered environments with uncertainties, while avoiding static and moving obstacles. We propose an integrated control framework for SaR robots in dynamic, uncertain environments, including a computationally efficient heuristic motion planning system that provides a nominal (assuming there are no uncertainties) collision-free trajectory for SaR robots and a robust motion tracking system that steers the robot to track this reference trajectory, taking into account the impact of uncertainties. The control architecture guarantees a balanced trade-off among various SaR objectives, while handling the hard constraints, including safety. The results of various computer-based simulations, presented in this paper, showed significant out-performance (of up to 42.3%) of the proposed integrated control architecture compared to two commonly used state-of-the-art methods (Rapidly-exploring Random Tree and Artificial Potential Function) in reaching targets (e.g., trapped victims in SaR) safely, collision-free, and in the shortest possible time.

