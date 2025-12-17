---
layout: default
title: HEADER: Hierarchical Robot Exploration via Attention-Based Deep Reinforcement Learning with Expert-Guided Reward
---

# HEADER: Hierarchical Robot Exploration via Attention-Based Deep Reinforcement Learning with Expert-Guided Reward

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15679" target="_blank" class="toolbar-btn">arXiv: 2510.15679v1</a>
    <a href="https://arxiv.org/pdf/2510.15679.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15679v1" 
            onclick="toggleFavorite(this, '2510.15679v1', 'HEADER: Hierarchical Robot Exploration via Attention-Based Deep Reinforcement Learning with Expert-Guided Reward')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yuhong Cao, Yizhuo Wang, Jingsong Liang, Shuhao Liao, Yifeng Zhang, Peizhuo Li, Guillaume Sartoretti

**分类**: cs.RO

**发布日期**: 2025-10-17

---

## 💡 一句话要点

**HEADER：基于注意力深度强化学习和专家引导奖励的分层机器人探索方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人探索` `深度强化学习` `注意力机制` `分层图` `自主导航`

## 📋 核心要点

1. 现有基于学习的机器人自主探索方法在大型复杂环境中面临可扩展性和探索效率的挑战。
2. HEADER提出了一种基于注意力机制的深度强化学习方法，结合分层图表示和专家引导奖励，提升探索效率。
3. 实验结果表明，HEADER在模拟和真实环境中均优于现有方法，探索效率提升高达20%，并具有良好的可扩展性。

## 📝 摘要（中文）

本文旨在提升基于学习的自主机器人探索方法在环境规模和探索效率方面的性能。我们提出了HEADER，一种基于注意力的强化学习方法，利用分层图进行大规模环境中的高效探索。HEADER沿用传统方法构建机器人置信度/地图的分层表示，并设计了一种新颖的基于社区的算法来构建和更新全局图，该算法保持完全增量式、形状自适应，并以线性复杂度运行。我们的规划器基于注意力网络，能够精细地推理局部范围内的置信度，并粗略地利用全局范围内的远距离信息，从而做出考虑多尺度空间依赖性的最佳视点决策。此外，我们引入了一种无参数的特权奖励，通过避免手工设计的奖励塑造造成的训练目标偏差，显著提高了模型性能并产生了接近最优的探索行为。在具有挑战性的大规模探索模拟场景中，HEADER展示了比大多数现有学习和非学习方法更好的可扩展性，同时在探索效率方面比最先进的基线提高了高达20%。我们还在硬件上部署了HEADER，并在复杂的、大规模的真实场景中对其进行了验证，包括一个300m*230m的校园环境。

## 🔬 方法详解

**问题定义**：现有基于学习的机器人自主探索方法难以兼顾大规模环境的可扩展性和探索效率。传统方法依赖手工设计的奖励函数，容易产生偏差，导致次优的探索行为。此外，如何有效地利用全局信息进行局部决策也是一个挑战。

**核心思路**：HEADER的核心思路是利用分层图表示环境，并结合注意力机制的深度强化学习，使机器人能够同时考虑局部和全局信息，做出更明智的探索决策。通过引入无参数的特权奖励，避免了手工设计奖励函数带来的偏差，从而提升了探索效率。

**技术框架**：HEADER的整体框架包括以下几个主要模块：1) 分层图构建模块，用于构建和更新环境的分层表示；2) 基于注意力机制的深度强化学习规划器，用于根据当前状态选择下一个最佳视点；3) 专家引导奖励模块，用于提供无偏差的奖励信号。该框架采用增量式更新策略，能够适应动态变化的环境。

**关键创新**：HEADER的关键创新在于：1) 提出了一种基于社区的算法来构建和更新全局图，该算法具有线性复杂度，能够处理大规模环境；2) 引入了注意力机制，使规划器能够同时考虑局部和全局信息；3) 采用了无参数的特权奖励，避免了手工设计奖励函数带来的偏差。

**关键设计**：全局图的构建采用基于社区的算法，保证了线性复杂度。注意力机制采用Transformer结构，能够有效地捕捉多尺度空间依赖性。特权奖励基于专家知识，无需人工调整参数。深度强化学习模型采用Actor-Critic结构，Actor网络负责选择动作，Critic网络负责评估状态价值。

## 📊 实验亮点

HEADER在模拟环境中比现有方法提高了高达20%的探索效率，并在真实校园环境中成功部署。实验结果表明，HEADER具有良好的可扩展性和鲁棒性，能够适应复杂、大规模的环境。无参数特权奖励的引入显著提高了模型性能，避免了手工设计奖励函数带来的偏差。

## 🎯 应用场景

HEADER可应用于各种需要自主探索的场景，如室内机器人导航、无人机巡检、灾后救援、矿山勘探等。该方法能够提高探索效率，降低人工干预，并为机器人提供更可靠的环境感知能力，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> This work pushes the boundaries of learning-based methods in autonomous robot exploration in terms of environmental scale and exploration efficiency. We present HEADER, an attention-based reinforcement learning approach with hierarchical graphs for efficient exploration in large-scale environments. HEADER follows existing conventional methods to construct hierarchical representations for the robot belief/map, but further designs a novel community-based algorithm to construct and update a global graph, which remains fully incremental, shape-adaptive, and operates with linear complexity. Building upon attention-based networks, our planner finely reasons about the nearby belief within the local range while coarsely leveraging distant information at the global scale, enabling next-best-viewpoint decisions that consider multi-scale spatial dependencies. Beyond novel map representation, we introduce a parameter-free privileged reward that significantly improves model performance and produces near-optimal exploration behaviors, by avoiding training objective bias caused by handcrafted reward shaping. In simulated challenging, large-scale exploration scenarios, HEADER demonstrates better scalability than most existing learning and non-learning methods, while achieving a significant improvement in exploration efficiency (up to 20%) over state-of-the-art baselines. We also deploy HEADER on hardware and validate it in complex, large-scale real-life scenarios, including a 300m*230m campus environment.

