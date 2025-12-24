---
layout: default
title: "Divide, Discover, Deploy: Factorized Skill Learning with Symmetry and Style Priors"
---

# Divide, Discover, Deploy: Factorized Skill Learning with Symmetry and Style Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19953" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19953v2</a>
  <a href="https://arxiv.org/pdf/2508.19953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19953v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19953v2', 'Divide, Discover, Deploy: Factorized Skill Learning with Symmetry and Style Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rafael Cathomen, Mayank Mittal, Marin Vlastelica, Marco Hutter

**分类**: cs.RO

**发布日期**: 2025-08-27 (更新: 2025-08-28)

**备注**: Accepted to CoRL 2025. For code and videos, please check: https://leggedrobotics.github.io/d3-skill-discovery/

---

## 💡 一句话要点

**提出模块化无监督技能发现框架以解决机器人技能学习问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无监督技能发现` `模块化框架` `状态空间因子化` `对称性偏置` `风格因子` `机器人学习` `安全性` `可解释性`

## 📋 核心要点

1. 现有的无监督技能发现方法在现实机器人应用中面临安全性和可解释性不足的挑战。
2. 本文提出的模块化框架通过因子化状态空间，学习解耦的技能表示，并引入对称性和风格因子以增强技能的结构性和安全性。
3. 实验结果显示，该框架在仿真中实现了零-shot转移到真实硬件，学习的技能在下游任务中表现与手工奖励训练的策略相当。

## 📝 摘要（中文）

无监督技能发现（USD）使得智能体能够在没有特定任务奖励的情况下自主学习多样化行为。尽管近期的USD方法展现出良好前景，但其在现实机器人中的应用仍未得到充分探索。本文提出了一种模块化的USD框架，以应对学习技能的安全性、可解释性和可部署性等挑战。我们的方法利用用户定义的状态空间因子化来学习解耦的技能表示，并根据所需的内在奖励函数为每个因子分配不同的技能发现算法。通过引入基于对称性的归纳偏置和风格因子，我们促进了安全和鲁棒的行为。我们在仿真中评估了该框架，并展示了学习技能的零-shot转移到真实硬件的能力。实验结果表明，因子化和对称性促进了结构化的人类可解释行为的发现，而风格因子和惩罚则增强了安全性和多样性。

## 🔬 方法详解

**问题定义**：本文旨在解决无监督技能发现（USD）在现实机器人应用中的安全性、可解释性和可部署性不足的问题。现有方法往往缺乏对技能的结构化理解，导致学习的技能难以应用于实际场景。

**核心思路**：论文提出了一种模块化的USD框架，通过用户定义的状态空间因子化来学习解耦的技能表示。每个因子使用不同的技能发现算法，结合对称性和风格因子来促进安全和鲁棒的行为。

**技术框架**：整体框架包括状态空间因子化模块、技能发现算法选择模块、对称性偏置引入模块和风格因子正则化模块。通过这些模块的协同工作，学习到的技能能够在不同的环境中有效迁移。

**关键创新**：最重要的技术创新在于引入了基于对称性的归纳偏置和风格因子，这些设计使得学习的技能不仅结构化且具备更高的安全性和多样性。这与传统方法的单一技能发现算法形成了鲜明对比。

**关键设计**：在参数设置上，用户可以定义状态空间的因子化方式，损失函数中引入了对称性和风格因子的正则化项，以促进技能的多样性和安全性。网络结构上，采用了适应性算法选择机制，以便根据不同因子的特性选择最合适的技能发现算法。

## 📊 实验亮点

实验结果表明，提出的框架在仿真中实现了零-shot转移到真实硬件，学习的技能在下游任务中表现与手工奖励训练的策略相当。此外，因子化和对称性促进了结构化人类可解释行为的发现，风格因子和惩罚增强了安全性和多样性。

## 🎯 应用场景

该研究的潜在应用场景包括自主机器人、智能制造和人机协作等领域。通过模块化的技能学习框架，机器人能够在复杂环境中自主适应和执行多样化任务，提升了机器人在实际应用中的灵活性和安全性。未来，该方法有望推动更广泛的无监督学习技术在机器人领域的应用。

## 📄 摘要（原文）

> Unsupervised Skill Discovery (USD) allows agents to autonomously learn diverse behaviors without task-specific rewards. While recent USD methods have shown promise, their application to real-world robotics remains underexplored. In this paper, we propose a modular USD framework to address the challenges in the safety, interpretability, and deployability of the learned skills. Our approach employs user-defined factorization of the state space to learn disentangled skill representations. It assigns different skill discovery algorithms to each factor based on the desired intrinsic reward function. To encourage structured morphology-aware skills, we introduce symmetry-based inductive biases tailored to individual factors. We also incorporate a style factor and regularization penalties to promote safe and robust behaviors. We evaluate our framework in simulation using a quadrupedal robot and demonstrate zero-shot transfer of the learned skills to real hardware. Our results show that factorization and symmetry lead to the discovery of structured human-interpretable behaviors, while the style factor and penalties enhance safety and diversity. Additionally, we show that the learned skills can be used for downstream tasks and perform on par with oracle policies trained with hand-crafted rewards.

