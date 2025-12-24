---
layout: default
title: "GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control"
---

# GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03772" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03772v5</a>
  <a href="https://arxiv.org/pdf/2508.03772.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03772v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03772v5', 'GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marco Simoni, Aleksandar Fontana, Giulio Rossolini, Andrea Saracino, Paolo Mori

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-05 (更新: 2025-12-11)

---

## 💡 一句话要点

**提出GTPO以解决GRPO训练不稳定性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `群体相对策略优化` `训练稳定性` `大型语言模型` `熵过滤` `负更新` `策略崩溃` `性能提升`

## 📋 核心要点

1. 现有的GRPO方法在训练过程中存在不稳定性和收敛性差的问题，影响了大型语言模型的对齐效果。
2. GTPO通过跳过负更新并放大正更新来解决矛盾梯度问题，同时过滤高熵完成以防止策略崩溃。
3. 实验结果表明，GTPO在GSM8K、MATH等多个数据集上表现出更高的训练稳定性和性能提升。

## 📝 摘要（中文）

群体相对策略优化（GRPO）是一种有前景的基于策略的方法，用于大型语言模型的对齐，但其性能常常受到训练不稳定性和收敛不佳的限制。本文识别并分析了GRPO的两个主要问题：一是令牌级惩罚，导致不同响应中共享的有价值令牌收到矛盾的反馈信号；二是策略崩溃，负奖励的完成可能会惩罚自信的响应，进而使模型决策偏向不太可能的令牌。为了解决这些问题，我们提出了GTPO（基于轨迹的群体相对策略优化），通过跳过负更新并放大正更新来防止有价值令牌上的矛盾梯度，同时过滤掉熵超过可证明阈值的完成，以防止策略崩溃。与GRPO不同，GTPO不依赖于KL散度正则化，消除了训练过程中对参考模型的需求，同时确保了更大的训练稳定性和改进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决GRPO在训练过程中出现的两个主要问题：令牌级惩罚导致的矛盾梯度更新，以及负奖励完成引起的策略崩溃。这些问题会降低模型的训练稳定性和性能。

**核心思路**：GTPO的核心思想是通过跳过对有价值令牌的负更新来避免矛盾梯度，同时通过熵过滤机制防止策略崩溃。这种设计旨在增强模型对有价值信息的学习能力。

**技术框架**：GTPO的整体架构包括两个主要模块：一是对有价值令牌的正更新放大，二是熵过滤机制。通过这两个模块的结合，GTPO能够在训练过程中保持稳定性。

**关键创新**：GTPO的主要创新在于不依赖KL散度正则化，消除了对参考模型的需求。这一设计使得训练过程更加简化，同时提高了模型的稳定性和性能。

**关键设计**：在GTPO中，负更新被跳过，正更新被放大，熵过滤的阈值经过理论证明，以确保模型在训练过程中不会出现策略崩溃的现象。

## 📊 实验亮点

实验结果显示，GTPO在多个基准数据集（如GSM8K、MATH、AIME 2024、AIME 2025和AMC 2023）上均表现出显著的性能提升，训练稳定性明显增强，具体性能数据未提供，但相较于GRPO有明显改善。

## 🎯 应用场景

GTPO的研究成果在大型语言模型的训练和对齐中具有广泛的应用潜力，尤其是在需要高稳定性和高性能的任务中，如自然语言处理、对话系统和智能问答等领域。未来，GTPO可能会推动更高效的模型训练方法的发展，提升人工智能系统的可靠性和智能水平。

## 📄 摘要（原文）

> Group Relative Policy Optimization (GRPO) is a promising policy-based approach for Large Language Model alignment, yet its performance is often limited by training instability and suboptimal convergence. In this paper, we identify and analyze two main GRPO issues: (i) the token-level penalization, where valuable tokens shared across different responses receive contradictory feedback signals, leading to conflicting gradient updates that can reduce their likelihood; and (ii) the policy collapse, where negatively rewarded completions may penalize confident responses and shift model decisions toward unlikely tokens, destabilizing training process. To address these issues we introduce GTPO (Group-relative Trajectory-based Policy Optimization), which prevents conflicting gradients on valuable tokens by skipping negative updates while amplifying positive ones and filters out completions whose entropy exceeds a provable threshold, to prevent policy collapse. Unlike GRPO, GTPO does not rely on KL-divergence regularization, eliminating the need for a reference model during training, while still ensuring greater training stability and improved performance, as validated through multiple experiments on GSM8K, MATH, AIME 2024, AIME 2025 and AMC 2023.

