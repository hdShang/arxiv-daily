---
layout: default
title: One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion
---

# One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18780" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18780v2</a>
  <a href="https://arxiv.org/pdf/2505.18780.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18780v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18780v2', 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yahao Fan, Tianxiang Gui, Kaiyang Ji, Shutong Ding, Chixuan Zhang, Jiayuan Gu, Jingyi Yu, Jingya Wang, Ye Shi

**分类**: cs.RO, cs.LG

**发布日期**: 2025-05-24 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出DreamPolicy以解决人形机器人运动的可扩展性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人形机器人` `强化学习` `运动合成` `数据驱动` `可扩展性` `策略优化` `离线学习`

## 📋 核心要点

1. 现有的强化学习方法在处理多样地形时需要特定的奖励设计，难以利用扩展的数据集，导致可扩展性不足。
2. 我们提出的DreamPolicy框架通过整合离线数据和扩散驱动的运动合成，允许单一策略在多种地形上进行学习和泛化。
3. 实验结果显示，DreamPolicy在训练环境中的成功率达到90%，并在未见地形上比传统方法提高了20%的成功率。

## 📝 摘要（中文）

人形机器人运动面临可扩展性挑战：传统强化学习方法需要特定任务的奖励，且难以利用不断增长的数据集。我们提出了DreamPolicy，一个统一框架，使单一策略能够掌握多样的地形，并通过系统整合离线数据和扩散驱动的运动合成，实现对未见场景的零-shot泛化。DreamPolicy引入了人形运动图像（HMI），通过自回归的地形感知扩散规划器合成未来状态预测，直接捕捉人形运动学，避免了繁琐的重定向过程。实验表明，DreamPolicy在训练环境中平均成功率达到90%，在未见地形上比现有方法高出20%。

## 🔬 方法详解

**问题定义**：本论文旨在解决人形机器人运动中的可扩展性问题，现有方法在面对多样化地形时，往往需要特定的任务奖励，难以有效利用不断增长的数据集。

**核心思路**：DreamPolicy框架的核心思想是通过整合离线数据和扩散驱动的运动合成，创建一个统一的策略，使其能够在多种地形上进行学习和泛化，避免了繁琐的手动奖励设计。

**技术框架**：DreamPolicy的整体架构包括三个主要模块：离线数据整合、扩散驱动的运动合成和策略优化。离线数据通过聚合不同地形的策略回放，生成未来状态预测，供策略学习使用。

**关键创新**：最重要的技术创新在于引入了人形运动图像（HMI），通过扩散规划器合成的“梦境”轨迹，直接捕捉人形运动学，显著提高了策略的泛化能力。

**关键设计**：在设计上，HMI的生成依赖于自回归的地形感知扩散规划器，避免了传统方法中的重定向需求，且通过动态目标设置，简化了奖励工程的复杂性。

## 📊 实验亮点

实验结果显示，DreamPolicy在训练环境中的平均成功率达到90%，在未见地形上比现有方法提高了20%的成功率。此外，该方法在扰动和复合场景中表现出色，克服了传统方法的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括人形机器人在复杂环境中的自主导航、救援任务和人机协作等场景。通过实现高效的运动控制，DreamPolicy能够提升机器人在多样化和未知环境中的适应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Humanoid locomotion faces a critical scalability challenge: traditional reinforcement learning (RL) methods require task-specific rewards and struggle to leverage growing datasets, even as more training terrains are introduced. We propose DreamPolicy, a unified framework that enables a single policy to master diverse terrains and generalize zero-shot to unseen scenarios by systematically integrating offline data and diffusion-driven motion synthesis. At its core, DreamPolicy introduces Humanoid Motion Imagery (HMI) - future state predictions synthesized through an autoregressive terrain-aware diffusion planner curated by aggregating rollouts from specialized policies across various distinct terrains. Unlike human motion datasets requiring laborious retargeting, our data directly captures humanoid kinematics, enabling the diffusion planner to synthesize "dreamed" trajectories that encode terrain-specific physical constraints. These trajectories act as dynamic objectives for our HMI-conditioned policy, bypassing manual reward engineering and enabling cross-terrain generalization. DreamPolicy addresses the scalability limitations of prior methods: while traditional RL fails to exploit growing datasets, our framework scales seamlessly with more offline data. As the dataset expands, the diffusion prior learns richer locomotion skills, which the policy leverages to master new terrains without retraining. Experiments demonstrate that DreamPolicy achieves average 90% success rates in training environments and an average of 20% higher success on unseen terrains than the prevalent method. It also generalizes to perturbed and composite scenarios where prior approaches collapse. By unifying offline data, diffusion-based trajectory synthesis, and policy optimization, DreamPolicy overcomes the "one task, one policy" bottleneck, establishing a paradigm for scalable, data-driven humanoid control.

