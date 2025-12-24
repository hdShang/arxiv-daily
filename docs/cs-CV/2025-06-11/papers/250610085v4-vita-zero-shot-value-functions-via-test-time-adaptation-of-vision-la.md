---
layout: default
title: "VITA: Zero-Shot Value Functions via Test-Time Adaptation of Vision-Language Models"
---

# VITA: Zero-Shot Value Functions via Test-Time Adaptation of Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10085" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10085v4</a>
  <a href="https://arxiv.org/pdf/2506.10085.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10085v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10085v4', 'VITA: Zero-Shot Value Functions via Test-Time Adaptation of Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christos Ziakas, Alessandra Russo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-11-26)

---

## 💡 一句话要点

**提出VITA以解决视觉语言模型的零-shot价值函数问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉语言模型` `零-shot学习` `价值函数` `测试时适应` `机器人操作` `元学习` `自监督学习`

## 📋 核心要点

1. 现有的视觉语言模型在零-shot任务中表现出色，但其固定的预训练表示限制了对新环境的适应能力和时间推理能力。
2. VITA通过在推理时进行轻量级的适应，利用元学习的自监督损失来动态更新价值函数，从而增强模型的泛化能力。
3. 在真实的机器人操作任务中，VITA展示了从单一训练环境到多样化任务的优秀泛化能力，超越了当前最先进的零-shot方法。

## 📝 摘要（中文）

视觉语言模型（VLMs）在零-shot目标条件价值函数方面展现出潜力，但其冻结的预训练表示限制了泛化能力和时间推理。本文提出VITA，一种通过测试时适应增强这两种能力的零-shot价值函数学习方法。在推理阶段，轻量级适应模块通过在元学习的自监督损失上进行梯度更新，从而改善价值估计。VITA通过在轨迹上顺序更新，编码历史信息，解决了时间推理的局限性。为减轻捷径学习，提出了一种基于相异性的采样策略，在训练期间选择语义多样的轨迹片段。在真实的机器人操作任务中，VITA从单一训练环境泛化到多样的分布外任务、环境和体现，超越了使用自回归VLMs的最先进零-shot方法。此外，VITA的零-shot价值估计可用于离线强化学习中的奖励塑造，导致在Meta-World基准上的多任务策略超越了使用模糊逻辑密集奖励训练的策略。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在零-shot任务中的泛化能力不足和时间推理能力弱的问题。现有方法由于固定的预训练表示，难以适应新的环境和任务。

**核心思路**：VITA的核心思路是通过测试时适应，利用轻量级的适应模块在推理阶段进行动态更新，从而改善价值估计并增强模型的适应能力。

**技术框架**：VITA的整体架构包括一个轻量级适应模块，该模块在每次推理时通过梯度更新来优化价值函数。此外，VITA采用了一种基于相异性的采样策略，以选择语义多样的轨迹片段进行训练。

**关键创新**：VITA的主要创新在于引入了测试时适应机制，使得模型能够在推理阶段根据历史信息动态调整参数，从而有效解决时间推理的局限性。

**关键设计**：VITA使用元学习的自监督损失作为优化目标，设计了轻量级的适应模块，并在训练过程中采用了相异性采样策略，以确保模型能够学习到多样化的轨迹信息。

## 📊 实验亮点

在实验中，VITA在真实的机器人操作任务中表现优异，能够从单一训练环境泛化到多样的分布外任务，超越了当前最先进的零-shot方法，具体性能提升幅度显著。此外，VITA的零-shot价值估计在离线强化学习中用于奖励塑造，表现出色，提升了多任务策略的性能。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化任务执行和智能代理系统。通过提高模型的泛化能力，VITA可以在多种环境和任务中有效应用，推动智能机器人技术的发展。未来，VITA的理念也可能扩展到其他领域，如自然语言处理和计算机视觉中的零-shot学习任务。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) show promise as zero-shot goal-conditioned value functions, but their frozen pre-trained representations limit generalization and temporal reasoning. We introduce VITA, a zero-shot value function learning method that enhances both capabilities via test-time adaptation. At inference, a lightweight adaptation module is updated via a gradient step on a meta-learned self-supervised loss, such that each test-time update improves value estimation. By updating sequentially over a trajectory, VITA encodes history into its parameters, addressing the temporal reasoning limitations. To mitigate shortcut learning, we propose a dissimilarity-based sampling strategy that selects semantically diverse segments of the trajectory during training. In real-world robotic manipulation tasks, VITA generalizes from a single training environment to diverse out-of-distribution tasks, environments, and embodiments, outperforming the state-of-the-art zero-shot method using autoregressive VLMs. Furthermore, we demonstrate that VITA's zero-shot value estimates can be utilized for reward shaping in offline reinforcement learning, resulting in multi-task policies on the Meta-World benchmark that exceed the performance of those trained with the simulation's fuzzy-logic dense rewards.

