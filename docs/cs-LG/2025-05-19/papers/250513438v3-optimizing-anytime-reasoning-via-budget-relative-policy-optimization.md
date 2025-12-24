---
layout: default
title: Optimizing Anytime Reasoning via Budget Relative Policy Optimization
---

# Optimizing Anytime Reasoning via Budget Relative Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13438" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13438v3</a>
  <a href="https://arxiv.org/pdf/2505.13438.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13438v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13438v3', 'Optimizing Anytime Reasoning via Budget Relative Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Penghui Qi, Zichen Liu, Tianyu Pang, Chao Du, Wee Sun Lee, Min Lin

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-19 (更新: 2025-11-07)

---

## 💡 一句话要点

**提出AnytimeReasoner以优化大语言模型的即时推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `即时推理` `强化学习` `大语言模型` `可验证奖励` `策略优化` `数学推理` `令牌预算` `效率提升`

## 📋 核心要点

1. 现有方法在固定令牌预算下优化推理性能，导致训练和部署效率低下。
2. 提出AnytimeReasoner框架，通过截断思考过程并引入可验证奖励来优化即时推理性能。
3. 实验证明该方法在数学推理任务中超越GRPO，提升了训练和令牌效率。

## 📝 摘要（中文）

在提升大型语言模型（LLMs）推理能力的过程中，测试时计算资源的扩展至关重要。现有方法通常采用强化学习（RL）来最大化在推理轨迹结束时获得的可验证奖励，但这些方法仅在固定的令牌预算下优化最终性能，限制了训练和部署的效率。本文提出了一种新颖的框架AnytimeReasoner，旨在优化即时推理性能，提高令牌效率和在不同令牌预算约束下的推理灵活性。通过从先验分布中抽样令牌预算，截断完整的思考过程，促使模型为每个截断的思考总结最佳答案并进行验证，从而引入可验证的密集奖励，促进RL优化中的有效信用分配。实验证明，该方法在数学推理任务中在各种思考预算下均优于GRPO，提升了训练和令牌效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在固定令牌预算下优化推理性能的不足，导致训练和部署效率低下的问题。

**核心思路**：提出AnytimeReasoner框架，通过截断思考过程并引入可验证的密集奖励，促使模型在不同令牌预算下进行有效推理。

**技术框架**：整体架构包括思考过程的截断、奖励的引入和优化策略的解耦。主要模块包括思考策略和总结策略的优化。

**关键创新**：引入了预算相对策略优化（BRPO）技术，增强了学习过程的鲁棒性和效率，与现有方法相比，能够更有效地进行信用分配。

**关键设计**：在损失函数设计上，采用了可验证的密集奖励机制，参数设置上根据先验分布进行令牌预算的抽样，确保模型在不同预算下的灵活性和效率。

## 📊 实验亮点

实验结果表明，AnytimeReasoner在数学推理任务中，在所有思考预算下均优于GRPO，提升幅度显著，具体性能数据未提供，但整体训练和令牌效率均有所提高。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和实时决策支持等。通过优化推理过程，提升了大语言模型在实际应用中的效率和灵活性，未来可能对智能助手和自动化系统产生深远影响。

## 📄 摘要（原文）

> Scaling test-time compute is crucial for enhancing the reasoning capabilities of large language models (LLMs). Existing approaches typically employ reinforcement learning (RL) to maximize a verifiable reward obtained at the end of reasoning traces. However, such methods optimize only the final performance under a large and fixed token budget, which hinders efficiency in both training and deployment. In this work, we present a novel framework, AnytimeReasoner, to optimize anytime reasoning performance, which aims to improve token efficiency and the flexibility of reasoning under varying token budget constraints. To achieve this, we truncate the complete thinking process to fit within sampled token budgets from a prior distribution, compelling the model to summarize the optimal answer for each truncated thinking for verification. This introduces verifiable dense rewards into the reasoning process, facilitating more effective credit assignment in RL optimization. We then optimize the thinking and summary policies in a decoupled manner to maximize the cumulative reward. Additionally, we introduce a novel variance reduction technique, Budget Relative Policy Optimization (BRPO), to enhance the robustness and efficiency of the learning process when reinforcing the thinking policy. Empirical results in mathematical reasoning tasks demonstrate that our method consistently outperforms GRPO across all thinking budgets under various prior distributions, enhancing both training and token efficiency.

