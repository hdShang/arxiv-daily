---
layout: default
title: "LLMs Can't Handle Peer Pressure: Crumbling under Multi-Agent Social Interactions"
---

# LLMs Can't Handle Peer Pressure: Crumbling under Multi-Agent Social Interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18321" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18321v3</a>
  <a href="https://arxiv.org/pdf/2508.18321.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18321v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18321v3', 'LLMs Can\'t Handle Peer Pressure: Crumbling under Multi-Agent Social Interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maojia Song, Tej Deep Pala, Ruiwen Zhou, Weisheng Jin, Amir Zadeh, Chuan Li, Dorien Herremans, Soujanya Poria

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-24 (更新: 2025-12-09)

---

## 💡 一句话要点

**提出KAIROS基准以解决LLMs在多智能体社交互动中的脆弱性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多智能体系统` `社交互动` `决策能力` `群体相对策略优化` `融洽关系` `信息整合` `从众偏见`

## 📋 核心要点

1. 现有研究主要集中于从众偏见，未能全面探讨LLMs在多智能体社交互动中的表现和脆弱性。
2. 论文提出KAIROS基准，通过模拟测验式协作，系统分析融洽关系和同伴行为对决策的影响。
3. 实验结果显示，模型规模影响社会影响的易感性，较大模型更具韧性，而小模型需通过GRPO训练提升性能。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被集成到多智能体系统（MAS）中，其中同伴互动影响个体决策。虽然之前的研究主要关注从众偏见，但我们扩展了视角，探讨LLMs如何从先前的互动中建立融洽关系、识别和整合高质量的同伴信息，以及抵抗误导性输入的能力。我们引入了KAIROS，一个模拟测验式协作的基准，能够精确控制同伴代理的融洽水平和行为。这一统一的设置使得我们能够系统分析融洽关系、同伴行为和模型自信心如何共同影响决策。使用KAIROS，我们评估了提示、监督微调和通过群体相对策略优化（GRPO）的强化学习。结果表明，模型规模是调节社会影响易感性的主要因素：较大的模型更具韧性，并从基于提示的缓解中受益，而较小的模型则仍然脆弱。只有经过精心配置的GRPO训练才能为小模型带来一致的鲁棒性和性能提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在多智能体社交互动中脆弱性的问题，现有方法主要关注从众偏见，未能充分考虑融洽关系和信息整合的影响。

**核心思路**：通过引入KAIROS基准，模拟同伴代理的互动，研究如何通过历史互动建立融洽关系以及如何抵抗误导性输入，从而提升LLMs在复杂社交动态下的决策能力。

**技术框架**：KAIROS基准包括多个模块，首先是同伴代理的行为控制，其次是融洽关系的建立，最后是决策过程的分析。模型通过不同的训练方式（提示、微调、GRPO）进行评估。

**关键创新**：引入KAIROS基准是本研究的核心创新，它提供了一个统一的实验环境，能够系统地分析融洽关系、同伴行为和模型自信心对决策的影响，这在现有研究中尚属首次。

**关键设计**：在GRPO训练中，设计了特定的参数配置，以确保小模型在面对社交影响时能够获得一致的鲁棒性和性能提升。

## 📊 实验亮点

实验结果表明，模型规模是影响社会影响易感性的关键因素。较大模型在面对社交影响时表现出更强的韧性，并且通过提示方法能够显著提升其性能，而小模型则需要经过精心配置的GRPO训练才能获得一致的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、智能助手和多智能体协作系统等。通过提升LLMs在社交互动中的决策能力，可以增强其在复杂环境中的适应性和有效性，推动人机协作的进步。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly integrated into multi-agent systems (MAS), where peer interactions shape individual decisions. While prior work has mainly examined conformity bias, we broaden the view to include how LLMs build rapport from prior interactions, discern and integrate high-quality peer information, and resist misleading inputs-abilities essential for achieving collective intelligence under complex social dynamics. We introduce KAIROS, a benchmark that simulates quiz-style collaboration with peer agents whose rapport levels and behaviours can be precisely controlled in both historical interactions and the current round. This unified setup enables systematic analysis of how rapport, peer actions, and the model's self-confidence jointly influence decision-making. Using KAIROS, we evaluate prompting, supervised fine-tuning, and reinforcement learning via Group Relative Policy Optimisation (GRPO). Results show that model scale is a primary factor moderating susceptibility to social influence: larger models are more resilient and benefit from prompting-based mitigation, whereas smaller models remain vulnerable. Only carefully configured GRPO training yields consistent robustness and performance gains for small models.

