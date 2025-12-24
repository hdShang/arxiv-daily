---
layout: default
title: SEM: Reinforcement Learning for Search-Efficient Large Language Models
---

# SEM: Reinforcement Learning for Search-Efficient Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07903" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07903v1</a>
  <a href="https://arxiv.org/pdf/2505.07903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07903v1', 'SEM: Reinforcement Learning for Search-Efficient Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyang Sha, Shiwen Cui, Weiqiang Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出SEM框架以优化大语言模型的搜索效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `强化学习` `搜索优化` `推理效率` `信息检索` `MuSiQue` `MMLU`

## 📋 核心要点

1. 现有方法在教会模型何时调用搜索与何时依赖内部知识方面存在显著挑战，导致冗余搜索行为。
2. 本文提出SEM框架，通过后训练强化学习优化大语言模型的搜索使用，提升推理效率。
3. 实验结果显示，SEM显著减少冗余搜索操作，同时在多个基准测试中保持或提高了回答准确性。

## 📝 摘要（中文）

近年来，大语言模型（LLMs）在推理和调用外部工具（特别是搜索引擎）方面取得了显著进展。然而，如何教会模型判断何时调用搜索、何时依赖内部知识仍然是一个重大挑战。现有的强化学习方法往往导致冗余的搜索行为，造成效率低下和成本过高。本文提出了一种新颖的后训练强化学习框架SEM，明确训练LLMs优化搜索使用。通过构建结合MuSiQue和MMLU的平衡数据集，创建模型必须学习区分可直接回答的问题和需要外部检索的问题的场景。我们设计了结构化推理模板，并采用群体相对策略优化（GRPO）对模型的搜索行为进行后训练。实验结果表明，该方法显著减少了冗余搜索操作，同时在多个具有挑战性的基准上保持或提高了回答准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在搜索使用上的效率问题，现有方法常导致冗余搜索，影响性能和成本。

**核心思路**：提出SEM框架，通过后训练强化学习明确训练模型优化搜索使用，帮助模型更好地判断何时调用外部搜索。

**技术框架**：整体架构包括数据集构建、结构化推理模板设计和群体相对策略优化（GRPO）三个主要模块，形成完整的训练流程。

**关键创新**：SEM框架的核心创新在于结合MuSiQue和MMLU数据集，创建特定场景以训练模型区分可直接回答的问题与需要检索的问题。

**关键设计**：设计了奖励函数以鼓励准确回答而不进行不必要的搜索，同时在需要时促进有效检索，确保模型的搜索行为更加高效。

## 📊 实验亮点

实验结果表明，SEM框架显著减少了冗余搜索操作，提升了模型在多个基准测试中的回答准确性，具体性能提升幅度达到X%（具体数据需根据实验结果填写）。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、虚拟助手和信息检索等。通过优化搜索使用，SEM框架可以显著提升模型的推理效率和用户体验，未来可能在多种实际场景中发挥重要作用。

## 📄 摘要（原文）

> Recent advancements in Large Language Models(LLMs) have demonstrated their capabilities not only in reasoning but also in invoking external tools, particularly search engines. However, teaching models to discern when to invoke search and when to rely on their internal knowledge remains a significant challenge. Existing reinforcement learning approaches often lead to redundant search behaviors, resulting in inefficiencies and over-cost. In this paper, we propose SEM, a novel post-training reinforcement learning framework that explicitly trains LLMs to optimize search usage. By constructing a balanced dataset combining MuSiQue and MMLU, we create scenarios where the model must learn to distinguish between questions it can answer directly and those requiring external retrieval. We design a structured reasoning template and employ Group Relative Policy Optimization(GRPO) to post-train the model's search behaviors. Our reward function encourages accurate answering without unnecessary search while promoting effective retrieval when needed. Experimental results demonstrate that our method significantly reduces redundant search operations while maintaining or improving answer accuracy across multiple challenging benchmarks. This framework advances the model's reasoning efficiency and extends its capability to judiciously leverage external knowledge.

