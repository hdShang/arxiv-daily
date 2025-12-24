---
layout: default
title: "Revisiting Diffusion Q-Learning: From Iterative Denoising to One-Step Action Generation"
---

# Revisiting Diffusion Q-Learning: From Iterative Denoising to One-Step Action Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13904" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13904v2</a>
  <a href="https://arxiv.org/pdf/2508.13904.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13904v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13904v2', 'Revisiting Diffusion Q-Learning: From Iterative Denoising to One-Step Action Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thanh Nguyen, Chang D. Yoo

**分类**: cs.LG

**发布日期**: 2025-08-19 (更新: 2025-10-01)

---

## 💡 一句话要点

**提出One-Step Flow Q-Learning以解决DQL训练与推理效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散Q学习` `强化学习` `动作生成` `流匹配` `速度场` `离线学习` `机器人控制` `自动驾驶`

## 📋 核心要点

1. 现有的扩散Q学习方法依赖多步去噪，导致训练和推理效率低下，且过程脆弱。
2. 本文提出的One-Step Flow Q-Learning框架，能够在无需辅助模块的情况下实现有效的一步动作生成。
3. 实验结果显示，OFQL在D4RL基准测试中显著提升了性能，超越了所有基线方法，达到了最先进的水平。

## 📝 摘要（中文）

扩散Q学习（DQL）已成为离线强化学习的高效范式，但其依赖于多步去噪的动作生成方式导致训练和推理过程缓慢且脆弱。现有加速DQL的方法通常依赖辅助模块或策略蒸馏，牺牲了简单性或性能。为此，本文提出了一种新框架One-Step Flow Q-Learning（OFQL），实现了在训练和推理过程中有效的一步动作生成，无需辅助模块或蒸馏。OFQL在流匹配（FM）范式下重新构建DQL策略，通过学习平均速度场直接支持准确的一步动作生成，显著提高了学习速度和鲁棒性。实验结果表明，OFQL在D4RL基准测试中不仅显著减少了训练和推理的计算量，还大幅超越了多步DQL，达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散Q学习（DQL）在动作生成过程中对多步去噪的依赖，这导致了训练和推理的低效与脆弱性。现有方法通常需要辅助模块或策略蒸馏，造成了简单性与性能之间的权衡。

**核心思路**：提出One-Step Flow Q-Learning（OFQL）框架，旨在实现高效的一步动作生成。通过在流匹配（FM）范式下重新构建DQL策略，OFQL学习一个平均速度场，直接支持准确的一步动作生成，从而消除了多步去噪的需求。

**技术框架**：OFQL的整体架构包括策略学习模块和动作生成模块。策略学习模块负责学习平均速度场，而动作生成模块则利用该速度场进行高效的一步动作生成。整个过程不需要额外的辅助模块或蒸馏步骤。

**关键创新**：OFQL的核心创新在于通过学习平均速度场来实现直接的一步动作生成，这与传统的多步去噪方法本质上不同。此设计显著提高了学习的速度和鲁棒性。

**关键设计**：在技术细节上，OFQL采用了特定的损失函数来优化速度场的学习，并设计了高效的网络结构以支持快速的动作生成。

## 📊 实验亮点

在D4RL基准测试中，OFQL显著减少了训练和推理的计算量，且在性能上超越了多步DQL，达到了最先进的水平。具体而言，OFQL在多个任务上均表现出色，提升幅度达到XX%（具体数据待补充）。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、游戏智能等需要高效决策的场景。OFQL的高效性和鲁棒性使其在实际应用中具有较大的价值，能够显著提升智能体在复杂环境中的表现。未来，OFQL可能会推动更多基于强化学习的应用发展。

## 📄 摘要（原文）

> Diffusion Q-Learning (DQL) has established diffusion policies as a high-performing paradigm for offline reinforcement learning, but its reliance on multi-step denoising for action generation renders both training and inference slow and fragile. Existing efforts to accelerate DQL toward one-step denoising typically rely on auxiliary modules or policy distillation, sacrificing either simplicity or performance. It remains unclear whether a one-step policy can be trained directly without such trade-offs. To this end, we introduce One-Step Flow Q-Learning (OFQL), a novel framework that enables effective one-step action generation during both training and inference, without auxiliary modules or distillation. OFQL reformulates the DQL policy within the Flow Matching (FM) paradigm but departs from conventional FM by learning an average velocity field that directly supports accurate one-step action generation. This design removes the need for multi-step denoising and backpropagation-through-time updates, resulting in substantially faster and more robust learning. Extensive experiments on the D4RL benchmark show that OFQL, despite generating actions in a single step, not only significantly reduces computation during both training and inference but also outperforms multi-step DQL by a large margin. Furthermore, OFQL surpasses all other baselines, achieving state-of-the-art performance in D4RL.

