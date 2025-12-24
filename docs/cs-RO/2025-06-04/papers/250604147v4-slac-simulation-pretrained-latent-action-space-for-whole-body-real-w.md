---
layout: default
title: "SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World RL"
---

# SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04147" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04147v4</a>
  <a href="https://arxiv.org/pdf/2506.04147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04147v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04147v4', 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaheng Hu, Peter Stone, Roberto Martín-Martín

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-06-04 (更新: 2025-08-16)

**备注**: CoRL 2025

---

## 💡 一句话要点

**提出SLAC以解决高自由度机器人控制的样本效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `机器人控制` `潜在动作空间` `无监督学习` `高自由度系统` `样本效率` `现实世界应用`

## 📋 核心要点

1. 现有的强化学习方法在高自由度机器人控制中面临样本效率低和安全探索难的问题。
2. SLAC通过低保真度模拟器预训练潜在动作空间，结合无监督技能发现方法，促进高效的下游学习。
3. SLAC在双手移动操作任务中实现了最先进的性能，能够快速学习复杂任务，且无需示范或先验知识。

## 📝 摘要（中文）

构建高效的家庭和工业机器人需要掌握高自由度系统的控制能力。尽管强化学习（RL）在自主获取机器人控制策略方面具有潜力，但在高自由度环境中应用仍面临挑战。直接在现实世界中进行RL需要安全探索和高样本效率，而这在实践中难以实现。本文提出SLAC，通过利用低保真度模拟器预训练任务无关的潜在动作空间，使得复杂机器人在现实世界中的RL变得可行。SLAC通过定制的无监督技能发现方法训练潜在动作空间，促进时间抽象、解耦和安全性，从而提高下游学习的效率。实验结果表明，SLAC在双手移动操作任务中表现出色，能够在不到一小时的现实世界交互中学习到接触丰富的全身任务，无需任何演示或手工设计的行为先验。

## 🔬 方法详解

**问题定义**：本文旨在解决高自由度机器人在现实世界中进行强化学习时的样本效率和安全探索问题。现有方法在这些方面表现不佳，导致学习过程缓慢且不稳定。

**核心思路**：SLAC的核心思路是利用低保真度模拟器预训练一个任务无关的潜在动作空间，通过无监督技能发现方法促进时间抽象和解耦，从而提高学习效率。

**技术框架**：SLAC的整体架构包括两个主要阶段：首先在模拟环境中训练潜在动作空间，然后在现实世界中使用该动作空间作为动作接口，通过新颖的离线策略强化学习算法进行下游任务学习。

**关键创新**：SLAC的主要创新在于其潜在动作空间的预训练方法和无监督技能发现策略，这与传统的直接RL方法有本质区别，后者往往依赖于大量的示范或手工设计的行为先验。

**关键设计**：在设计中，SLAC采用了特定的损失函数来促进技能的解耦和时间抽象，同时在网络结构上进行了优化，以适应高自由度的动作空间。

## 📊 实验亮点

SLAC在双手移动操作任务中实现了最先进的性能，能够在不到一小时的现实世界交互中学习到复杂的接触丰富的全身任务，相较于现有方法显著提升了学习效率，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

SLAC的研究成果在家庭和工业机器人领域具有广泛的应用潜力。通过提高高自由度机器人在复杂任务中的学习效率，SLAC可以加速机器人自主操作的实现，推动智能家居、自动化生产等领域的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Building capable household and industrial robots requires mastering the control of versatile, high-degree-of-freedom (DoF) systems such as mobile manipulators. While reinforcement learning (RL) holds promise for autonomously acquiring robot control policies, scaling it to high-DoF embodiments remains challenging. Direct RL in the real world demands both safe exploration and high sample efficiency, which are difficult to achieve in practice. Sim-to-real RL, on the other hand, is often brittle due to the reality gap. This paper introduces SLAC, a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space. SLAC trains this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety, thereby facilitating efficient downstream learning. Once a latent action space is learned, SLAC uses it as the action interface for a novel off-policy RL algorithm to autonomously learn downstream tasks through real-world interactions. We evaluate SLAC against existing methods on a suite of bimanual mobile manipulation tasks, where it achieves state-of-the-art performance. Notably, SLAC learns contact-rich whole-body tasks in under an hour of real-world interactions, without relying on any demonstrations or hand-crafted behavior priors. More information and robot videos at robo-rl.github.io

