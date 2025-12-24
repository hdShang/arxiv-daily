---
layout: default
title: Interpretable Learning Dynamics in Unsupervised Reinforcement Learning
---

# Interpretable Learning Dynamics in Unsupervised Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06279" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06279v1</a>
  <a href="https://arxiv.org/pdf/2505.06279.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06279v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06279v1', 'Interpretable Learning Dynamics in Unsupervised Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shashwat Pandey

**分类**: cs.LG, stat.ML

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出可解释性框架以理解无监督强化学习中的内在动机**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无监督强化学习` `可解释性` `内在动机` `注意力机制` `代理行为分析` `探索策略` `深度学习` `动态学习`

## 📋 核心要点

1. 现有的无监督强化学习方法缺乏对代理内部动态的可解释性，难以理解内在动机如何影响其行为和学习过程。
2. 本文提出了一种可解释性框架，通过分析代理的注意力和行为，揭示内在动机对其学习动态的影响。
3. 实验结果表明，基于好奇心的代理在注意力和探索行为上表现出更广泛和动态的特征，Transformer-RND在多个指标上优于其他代理。

## 📝 摘要（中文）

本文提出了一种可解释性框架，旨在理解内在动机如何影响无监督强化学习（URL）代理的注意力、行为和表示学习。通过分析五种代理（DQN、RND、ICM、PPO和Transformer-RND变体），使用Grad-CAM、层次相关传播（LRP）、探索指标和潜在空间聚类，揭示了代理如何感知和适应环境。我们引入了注意力多样性和注意力变化率两个指标，发现好奇心驱动的代理表现出更广泛和动态的注意力及探索行为。Transformer-RND在注意力广度、探索覆盖率和紧凑结构的潜在表示方面表现优异。研究结果强调了架构归纳偏置和训练信号对代理内部动态的影响，提供了超越奖励中心评估的诊断工具，促进了RL代理的可解释性和泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决无监督强化学习代理的可解释性问题，现有方法往往无法揭示代理如何通过内在动机进行学习和适应环境。

**核心思路**：通过引入注意力多样性和注意力变化率两个新指标，分析代理在不同时间和空间上的注意力分布，进而理解内在动机对代理行为的影响。

**技术框架**：研究采用Grad-CAM和层次相关传播（LRP）等技术，结合探索指标和潜在空间聚类，对五种不同的代理进行分析，构建了一个综合的可解释性框架。

**关键创新**：提出的注意力多样性和注意力变化率指标是本研究的核心创新，能够有效捕捉代理在学习过程中的动态变化，与传统的奖励中心评估方法形成鲜明对比。

**关键设计**：在实验中，采用了多种代理架构（如DQN、RND、ICM、PPO和Transformer-RND），并通过精心设计的训练信号和损失函数，确保代理能够在程序生成的环境中有效学习。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，基于好奇心的代理在注意力多样性和探索覆盖率上显著优于其他代理，Transformer-RND在多个指标上表现最佳，展示了更广泛的注意力和更高的探索能力。这些发现为理解代理的学习动态提供了新的视角。

## 🎯 应用场景

该研究的可解释性框架可广泛应用于无监督强化学习领域，特别是在需要理解代理行为和决策过程的场景中，如机器人控制、游戏AI和自动驾驶等。未来，该框架有望推动RL代理的透明性和可解释性，促进其在实际应用中的信任度。

## 📄 摘要（原文）

> We present an interpretability framework for unsupervised reinforcement learning (URL) agents, aimed at understanding how intrinsic motivation shapes attention, behavior, and representation learning. We analyze five agents DQN, RND, ICM, PPO, and a Transformer-RND variant trained on procedurally generated environments, using Grad-CAM, Layer-wise Relevance Propagation (LRP), exploration metrics, and latent space clustering. To capture how agents perceive and adapt over time, we introduce two metrics: attention diversity, which measures the spatial breadth of focus, and attention change rate, which quantifies temporal shifts in attention. Our findings show that curiosity-driven agents display broader, more dynamic attention and exploratory behavior than their extrinsically motivated counterparts. Among them, TransformerRND combines wide attention, high exploration coverage, and compact, structured latent representations. Our results highlight the influence of architectural inductive biases and training signals on internal agent dynamics. Beyond reward-centric evaluation, the proposed framework offers diagnostic tools to probe perception and abstraction in RL agents, enabling more interpretable and generalizable behavior.

