---
layout: default
title: "Learning to Sample: Reinforcement Learning-Guided Sampling for Autonomous Vehicle Motion Planning"
---

# Learning to Sample: Reinforcement Learning-Guided Sampling for Autonomous Vehicle Motion Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24313" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24313v1</a>
  <a href="https://arxiv.org/pdf/2509.24313.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24313v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24313v1', 'Learning to Sample: Reinforcement Learning-Guided Sampling for Autonomous Vehicle Motion Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Korbinian Moller, Roland Stroop, Mattia Piccinini, Alexander Langmann, Johannes Betz

**分类**: cs.RO

**发布日期**: 2025-09-29

**备注**: 8 pages, submitted to the IEEE ICRA 2026, Vienna, Austria

**🔗 代码/项目**: [GITHUB](https://github.com/TUM-AVS/Learning-to-Sample)

---

## 💡 一句话要点

**提出基于强化学习引导采样的运动规划方法，提升自动驾驶在复杂城市环境中的决策效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动驾驶` `运动规划` `强化学习` `采样方法` `世界模型`

## 📋 核心要点

1. 在复杂城市环境中，传统基于采样的运动规划方法因均匀或启发式采样产生大量不可行或不相关的轨迹，效率较低。
2. 论文提出一种混合框架，利用强化学习智能体引导采样过程，使采样集中在更有可能产生可行轨迹的区域。
3. 实验结果表明，该方法显著减少了采样数量和运行时间，同时保持了规划质量，提升了自动驾驶车辆的决策效率。

## 📝 摘要（中文）

本文提出了一种混合框架，用于解决自动驾驶中基于采样的运动规划方法在复杂城市环境中效率低下的问题。该框架利用强化学习（RL）智能体引导采样过程，使其集中在更有可能产生可行轨迹的动作空间区域，同时保持轨迹生成和评估的解析性和可验证性。该方法结合了基于可解码深度集编码器的世界模型（WM），能够处理可变数量的交通参与者并重建潜在表示。在CommonRoad仿真环境中进行的评估表明，该方法能够减少高达99%的采样需求，并减少高达84%的运行时间，同时保持规划质量（成功率和无碰撞率）。这些改进使得自动驾驶车辆在城市环境中能够更快、更可靠地做出决策，从而在实际约束下实现更安全、更灵敏的导航。

## 🔬 方法详解

**问题定义**：在自动驾驶的运动规划中，基于采样的算法在复杂城市环境中面临挑战。传统的均匀采样或启发式采样策略往往会生成大量无效或不相关的轨迹，导致计算资源浪费和规划效率低下。现有方法难以在保证规划质量的同时，快速找到可行的轨迹。

**核心思路**：论文的核心思路是利用强化学习（RL）来指导采样过程。通过训练一个RL智能体，使其能够学习到哪些区域的采样更有可能产生可行的轨迹。这样，采样过程不再是盲目的，而是有针对性的，从而提高了采样效率和规划速度。

**技术框架**：该方法采用混合框架，包含以下几个主要模块：1) 基于可解码深度集编码器的世界模型（WM），用于对环境进行建模，处理可变数量的交通参与者，并生成环境的潜在表示；2) 强化学习智能体，根据世界模型的输出，指导采样过程，选择更有可能产生可行轨迹的动作；3) 轨迹生成器，根据RL智能体选择的动作，生成轨迹；4) 轨迹评估器，使用确定性的可行性检查和成本函数，评估轨迹的质量，并选择最优轨迹。

**关键创新**：该方法最重要的技术创新点在于将强化学习引入到采样过程中。与传统的均匀采样或启发式采样相比，RL引导的采样能够更有效地探索动作空间，找到可行的轨迹。此外，使用可解码深度集编码器构建世界模型，能够处理动态变化的交通环境。

**关键设计**：世界模型使用深度集编码器，能够处理可变数量的交通参与者。强化学习智能体使用策略梯度方法进行训练，目标是最大化生成可行轨迹的概率。奖励函数的设计至关重要，需要平衡探索和利用，鼓励智能体探索新的区域，同时利用已知的可行区域。具体参数设置和网络结构在论文中有详细描述（未知）。

## 📊 实验亮点

实验结果表明，该方法在CommonRoad仿真环境中能够显著提升运动规划的效率。与传统方法相比，该方法能够减少高达99%的采样需求，并减少高达84%的运行时间，同时保持规划质量（成功率和无碰撞率）。这些结果表明，该方法能够有效地解决复杂城市环境中的运动规划问题。

## 🎯 应用场景

该研究成果可应用于自动驾驶车辆的运动规划和决策控制，尤其是在复杂城市交通环境中。通过提高规划效率和安全性，可以提升自动驾驶系统的可靠性和用户体验。此外，该方法还可以扩展到其他机器人运动规划领域，例如无人机导航和工业机器人路径规划。

## 📄 摘要（原文）

> Sampling-based motion planning is a well-established approach in autonomous driving, valued for its modularity and analytical tractability. In complex urban scenarios, however, uniform or heuristic sampling often produces many infeasible or irrelevant trajectories. We address this limitation with a hybrid framework that learns where to sample while keeping trajectory generation and evaluation fully analytical and verifiable. A reinforcement learning (RL) agent guides the sampling process toward regions of the action space likely to yield feasible trajectories, while evaluation and final selection remains governed by deterministic feasibility checks and cost functions. We couple the RL sampler with a world model (WM) based on a decodable deep set encoder, enabling both variable numbers of traffic participants and reconstructable latent representations. The approach is evaluated in the CommonRoad simulation environment, showing up to 99% fewer required samples and a runtime reduction of up to 84% while maintaining planning quality in terms of success and collision-free rates. These improvements lead to faster, more reliable decision-making for autonomous vehicles in urban environments, achieving safer and more responsive navigation under real-world constraints. Code and trained artifacts are publicly available at: https://github.com/TUM-AVS/Learning-to-Sample

