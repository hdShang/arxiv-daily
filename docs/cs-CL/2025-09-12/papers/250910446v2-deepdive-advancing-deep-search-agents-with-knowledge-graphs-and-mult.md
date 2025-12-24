---
layout: default
title: "DeepDive: Advancing Deep Search Agents with Knowledge Graphs and Multi-Turn RL"
---

# DeepDive: Advancing Deep Search Agents with Knowledge Graphs and Multi-Turn RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10446" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10446v2</a>
  <a href="https://arxiv.org/pdf/2509.10446.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10446v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10446v2', 'DeepDive: Advancing Deep Search Agents with Knowledge Graphs and Multi-Turn RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Lu, Zhenyu Hou, Zihan Wang, Hanchen Zhang, Xiao Liu, Yujiang Li, Shi Feng, Jie Tang, Yuxiao Dong

**分类**: cs.CL

**发布日期**: 2025-09-12 (更新: 2025-10-14)

**🔗 代码/项目**: [GITHUB](https://github.com/THUDM/DeepDive)

---

## 💡 一句话要点

**DeepDive：利用知识图谱和多轮强化学习提升深度搜索Agent能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度搜索` `知识图谱` `强化学习` `大型语言模型` `信息检索`

## 📋 核心要点

1. 现有开放LLM在利用浏览工具进行深度搜索时，面临长程推理能力不足和缺乏高质量训练数据的挑战。
2. DeepDive通过从知识图谱自动生成复杂问题，并采用多轮强化学习来提升LLM的深度搜索和推理能力。
3. 实验结果表明，DeepDive在BrowseComp等基准测试中取得了显著的性能提升，验证了多轮强化学习的有效性。

## 📝 摘要（中文）

本文提出了DeepDive，旨在提升深度搜索Agent的能力。为了解决开放LLM在复杂现实任务中，由于浏览工具带来的长程推理能力不足以及缺乏足够困难的监督数据的问题，DeepDive首先提出了一种从开放知识图谱中自动合成复杂、困难且难以找到的问题的策略。其次，应用端到端的多轮强化学习（RL）来增强LLM在深度搜索中的长程推理能力。为了鼓励多样性并减少冗余，设计了一种冗余惩罚，以避免重复相似的查询。实验表明，DeepDive-32B在BrowseComp上取得了新的开源竞争结果，优于WebSailor、DeepSeek-R1-Browse和Search-o1。多轮RL训练提高了深度搜索能力，并显著促进了多个基准测试的性能提升。DeepDive还支持测试时工具调用的扩展和并行采样。所有数据集、模型和代码均已公开。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在进行深度搜索时，面临着两个主要的痛点。一是利用浏览工具进行长程推理的能力不足，难以处理需要多次交互和复杂推理的任务。二是缺乏足够困难和高质量的监督数据，导致模型在复杂场景下的泛化能力受限。

**核心思路**：DeepDive的核心思路是通过自动生成高质量的训练数据和采用多轮强化学习来提升LLM的深度搜索能力。具体来说，首先利用知识图谱自动生成复杂的问题，这些问题需要多次搜索和推理才能解决。然后，使用多轮强化学习来训练LLM，使其能够更好地利用浏览工具进行搜索和推理。

**技术框架**：DeepDive的整体框架包括以下几个主要模块：1) **问题生成模块**：从知识图谱中自动生成复杂、困难的问题。2) **搜索Agent模块**：基于LLM构建的搜索Agent，负责根据问题生成搜索查询，并解析搜索结果。3) **强化学习模块**：使用多轮强化学习来训练搜索Agent，使其能够更好地进行长程推理和搜索。4) **冗余惩罚模块**：通过引入冗余惩罚，鼓励Agent生成多样化的查询，避免重复搜索。

**关键创新**：DeepDive最重要的技术创新点在于结合了知识图谱的问题生成和多轮强化学习的训练方法。通过知识图谱生成高质量的训练数据，解决了现有方法缺乏足够训练数据的问题。通过多轮强化学习，提升了LLM的长程推理能力，使其能够更好地处理复杂搜索任务。

**关键设计**：在强化学习模块中，使用了Proximal Policy Optimization (PPO) 算法进行训练。为了鼓励多样性并减少冗余，设计了一种冗余惩罚项，该惩罚项基于查询之间的相似度计算，并将其添加到奖励函数中。具体而言，如果Agent生成的查询与之前的查询过于相似，则会受到惩罚。此外，DeepDive还支持测试时工具调用的扩展和并行采样，进一步提升了搜索效率。

## 📊 实验亮点

DeepDive-32B在BrowseComp基准测试中取得了新的开源领先结果，超越了WebSailor、DeepSeek-R1-Browse和Search-o1等现有方法。实验结果表明，多轮强化学习训练显著提升了深度搜索能力，并对多个基准测试的性能提升做出了重要贡献。此外，DeepDive还支持测试时工具调用的扩展和并行采样，进一步提升了搜索效率。

## 🎯 应用场景

DeepDive具有广泛的应用前景，可用于智能问答系统、信息检索、知识发现等领域。它可以帮助用户更高效地获取所需信息，解决复杂问题。未来，DeepDive有望应用于自动化研究、决策支持等更高级的任务中，提升人工智能的智能化水平。

## 📄 摘要（原文）

> Augmenting large language models (LLMs) with browsing tools substantially improves their potential as deep search agents to solve complex, real-world tasks. Yet, open LLMs still perform poorly in such settings due to limited long-horizon reasoning capacity with browsing tools and the lack of sufficiently difficult supervised data. To address these challenges, we present DeepDive to advance deep search agents. First, we propose a strategy to automatically synthesize complex, difficult, and hard-to-find questions from open knowledge graphs. Second, we apply end-to-end multi-turn reinforcement learning (RL) to enhance LLMs' long-horizon reasoning with deep search. To encourage diversity and reduce redundancy, we design a redundancy penalty that discourages repeated similar queries. Experiments show that DeepDive-32B achieves a new open-source competitive result on BrowseComp, outperforming WebSailor, DeepSeek-R1-Browse, and Search-o1. We demonstrate that multi-turn RL training improves deep search ability and significantly contributes to the performance improvements across multiple benchmarks. We observe that DeepDive enables test-time scaling of tool calls and parallel sampling. All datasets, models, and code are publicly available at https://github.com/THUDM/DeepDive.

