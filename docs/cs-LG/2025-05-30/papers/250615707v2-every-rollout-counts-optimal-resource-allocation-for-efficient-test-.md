---
layout: default
title: "Every Rollout Counts: Optimal Resource Allocation for Efficient Test-Time Scaling"
---

# Every Rollout Counts: Optimal Resource Allocation for Efficient Test-Time Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15707" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15707v2</a>
  <a href="https://arxiv.org/pdf/2506.15707.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15707v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15707v2', 'Every Rollout Counts: Optimal Resource Allocation for Efficient Test-Time Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinglin Wang, Yiwei Li, Shaoxiong Feng, Peiwen Yuan, Yueqi Zhang, Jiayi Shi, Chuyi Tan, Boyuan Pan, Yao Hu, Kan Li

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-10-20)

**备注**: Accepted at NeurIPS2025

---

## 💡 一句话要点

**提出DORA以优化测试时间资源分配问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `测试时间缩放` `资源分配` `大型语言模型` `推理路径` `方向导向资源分配`

## 📋 核心要点

1. 现有的测试时间缩放方法在固定预算下的资源分配效率低，导致计算资源的浪费。
2. 本文提出方向导向资源分配（DORA）方法，通过在方向级别进行资源分配，优化了推理路径的选择。
3. DORA在MATH500、AIME2024和AIME2025等数学推理基准上表现优异，超越了强基线，达到了最新的准确率。

## 📝 摘要（中文）

测试时间缩放（TTS）通过在推理时使用额外的计算来探索多个推理路径，从而提升大型语言模型（LLMs）的性能。然而，如何在搜索过程中有效分配固定的回滚预算仍然未得到充分研究，常导致计算资源的低效使用。为此，本文将测试时间搜索形式化为资源分配问题，并推导出最大化正确解概率的最优分配策略。我们提出了方向导向资源分配（DORA）方法，通过在方向级别分配资源，减轻了现有方法的偏见。实验结果表明，DORA在多个数学推理基准上表现优异，达到了最新的准确率。

## 🔬 方法详解

**问题定义**：本文要解决的问题是如何在测试时间缩放中有效分配固定的回滚预算，以提高大型语言模型的推理性能。现有方法往往倾向于选择候选数量较多的推理方向，导致计算资源的低效使用。

**核心思路**：论文的核心思路是将测试时间搜索视为资源分配问题，提出DORA方法，通过在方向级别进行资源分配，避免了现有方法的偏见，从而提高了正确解的概率。

**技术框架**：整体架构包括资源分配模型和推理路径选择模块。首先，模型根据方向质量评估每个推理方向的潜力，然后在方向级别分配计算资源，最后进行推理路径的选择和验证。

**关键创新**：DORA的主要创新在于将资源分配从候选数量解耦，专注于方向质量，这与现有方法的本质区别在于其优化了资源的使用效率。

**关键设计**：在DORA中，关键参数包括方向质量评估函数和资源分配策略，损失函数设计为最大化正确解概率，确保在固定预算下的最优资源使用。具体的网络结构和参数设置在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，DORA在MATH500、AIME2024和AIME2025等基准上均超越了强基线，达到了最新的准确率，且在计算成本相当的情况下，提升幅度显著，证明了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化推理系统和智能问答等。通过优化测试时间资源分配，DORA可以显著提升大型语言模型在复杂推理任务中的表现，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Test-Time Scaling (TTS) improves the performance of Large Language Models (LLMs) by using additional inference-time computation to explore multiple reasoning paths through search. Yet how to allocate a fixed rollout budget most effectively during search remains underexplored, often resulting in inefficient use of compute at test time. To bridge this gap, we formulate test-time search as a resource allocation problem and derive the optimal allocation strategy that maximizes the probability of obtaining a correct solution under a fixed rollout budget. Within this formulation, we reveal a core limitation of existing search methods: solution-level allocation tends to favor reasoning directions with more candidates, leading to theoretically suboptimal and inefficient use of compute. To address this, we propose Direction-Oriented Resource Allocation (DORA), a provably optimal method that mitigates this bias by decoupling direction quality from candidate count and allocating resources at the direction level. To demonstrate DORA's effectiveness, we conduct extensive experiments on challenging mathematical reasoning benchmarks including MATH500, AIME2024, and AIME2025. The empirical results show that DORA consistently outperforms strong baselines with comparable computational cost, achieving state-of-the-art accuracy. We hope our findings contribute to a broader understanding of optimal TTS for LLMs.

