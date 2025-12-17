---
layout: default
title: DREAMer-VXS: A Latent World Model for Sample-Efficient AGV Exploration in Stochastic, Unobserved Environments
---

# DREAMer-VXS: A Latent World Model for Sample-Efficient AGV Exploration in Stochastic, Unobserved Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00005" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00005v1</a>
  <a href="https://arxiv.org/pdf/2512.00005.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00005v1" onclick="toggleFavorite(this, '2512.00005v1', 'DREAMer-VXS: A Latent World Model for Sample-Efficient AGV Exploration in Stochastic, Unobserved Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Agniprabha Chakraborty

**分类**: cs.RO

**发布日期**: 2025-10-06

---

## 💡 一句话要点

**提出DREAMer-VXS以解决AGV在随机未知环境中的样本效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自主驾驶` `强化学习` `模型学习` `探索效率` `机器人技术` `动态环境` `样本效率`

## 📋 核心要点

1. 现有的无模型强化学习算法在样本效率和适应性方面表现不佳，限制了其在真实环境中的应用。
2. DREAMer-VXS通过构建一个基于部分LiDAR观测的世界模型，利用想象中的轨迹进行高效的策略学习，减少了对真实环境交互的依赖。
3. 实验结果表明，该方法在未知环境中的探索效率提高了45%，并且在动态障碍物面前表现出更强的鲁棒性。

## 📝 摘要（中文）

学习型机器人领域具有巨大的潜力，但传统的无模型强化学习算法在样本效率和脆弱性方面存在严重问题。本文提出了DREAMer-VXS，一个基于模型的自主地面车辆（AGV）探索框架，通过想象潜在轨迹进行规划。该方法从部分高维LiDAR观测中学习全面的世界模型，结合卷积变分自编码器（VAE）和递归状态空间模型（RSSM），实现了高效的导航策略训练。与最先进的无模型SAC基线相比，DREAMer-VXS在达到专家级性能时减少了90%的环境交互需求，并在未知环境中提高了45%的探索效率，展现出更强的鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决自主地面车辆（AGV）在随机和未知环境中进行探索时的样本效率低下和脆弱性问题。现有的无模型强化学习方法在实际应用中往往需要大量的环境交互，导致学习过程缓慢且不稳定。

**核心思路**：DREAMer-VXS的核心思路是通过构建一个世界模型，从部分高维LiDAR观测中学习环境的结构，并利用该模型进行想象中的轨迹规划，从而实现高效的策略学习。这样设计的目的是将策略学习与真实环境交互解耦，显著提高样本效率。

**技术框架**：该方法的整体架构包括两个主要模块：卷积变分自编码器（VAE）用于学习环境的紧凑表示，递归状态空间模型（RSSM）用于建模复杂的时间动态。通过将学习到的模型作为高效的模拟器，代理可以在想象中训练其导航策略。

**关键创新**：DREAMer-VXS的主要创新在于将模型学习与策略优化相结合，通过想象轨迹进行训练，减少了对真实环境交互的需求。这一方法与传统的无模型方法本质上不同，后者依赖于大量的实际交互来学习有效的策略。

**关键设计**：在技术细节方面，VAE和RSSM的网络结构经过精心设计，以确保能够有效捕捉环境的复杂特征。此外，代理的行为由一个优化的演员-评论家策略引导，该策略使用复合奖励函数，平衡任务目标与内在好奇心奖励，促进对未知空间的系统探索。

## 📊 实验亮点

实验结果显示，DREAMer-VXS在实现专家级性能时，环境交互需求减少了90%。此外，在未知环境中的探索效率提高了45%，并且在面对动态障碍物时展现出更强的鲁棒性，显著优于最先进的无模型SAC基线。

## 🎯 应用场景

DREAMer-VXS的研究成果在自主驾驶、机器人探索和智能物流等领域具有广泛的应用潜力。通过提高样本效率和探索能力，该方法能够加速机器人在复杂和动态环境中的学习过程，提升其在实际应用中的表现和可靠性。未来，该技术可能推动更智能的自动化系统的发展，改善人机协作和自主决策能力。

## 📄 摘要（原文）

> The paradigm of learning-based robotics holds immense promise, yet its translation to real-world applications is critically hindered by the sample inefficiency and brittleness of conventional model-free reinforcement learning algorithms. In this work, we address these challenges by introducing DREAMer-VXS, a model-based framework for Autonomous Ground Vehicle (AGV) exploration that learns to plan from imagined latent trajectories. Our approach centers on learning a comprehensive world model from partial and high-dimensional LiDAR observations. This world model is composed of a Convolutional Variational Autoencoder (VAE), which learns a compact representation of the environment's structure, and a Recurrent State-Space Model (RSSM), which models complex temporal dynamics. By leveraging this learned model as a high-speed simulator, the agent can train its navigation policy almost entirely in imagination. This methodology decouples policy learning from real-world interaction, culminating in a 90% reduction in required environmental interactions to achieve expert-level performance when compared to state-of-the-art model-free SAC baselines. The agent's behavior is guided by an actor-critic policy optimized with a composite reward function that balances task objectives with an intrinsic curiosity bonus, promoting systematic exploration of unknown spaces. We demonstrate through extensive simulated experiments that DREAMer-VXS not only learns orders of magnitude faster but also develops more generalizable and robust policies, achieving a 45% increase in exploration efficiency in unseen environments and superior resilience to dynamic obstacles.

