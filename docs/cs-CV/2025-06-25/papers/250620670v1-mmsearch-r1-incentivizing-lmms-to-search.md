---
layout: default
title: "MMSearch-R1: Incentivizing LMMs to Search"
---

# MMSearch-R1: Incentivizing LMMs to Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20670" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20670v1</a>
  <a href="https://arxiv.org/pdf/2506.20670.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20670v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20670v1', 'MMSearch-R1: Incentivizing LMMs to Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinming Wu, Zihao Deng, Wei Li, Yiding Liu, Bo You, Bo Li, Zejun Ma, Ziwei Liu

**分类**: cs.CV, cs.CL

**发布日期**: 2025-06-25

**备注**: Code: https://github.com/EvolvingLMMs-Lab/multimodal-search-r1

---

## 💡 一句话要点

**提出MMSearch-R1以解决多模态模型搜索效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `强化学习` `信息检索` `搜索效率` `知识获取`

## 📋 核心要点

1. 现有方法如RAG在处理复杂和动态的现实信息时，往往依赖固定管道，导致搜索效率低下。
2. MMSearch-R1通过强化学习框架，支持LMMs在互联网环境中进行按需多轮搜索，集成图像和文本搜索工具。
3. 实验结果显示，MMSearch-R1在知识密集型和信息检索VQA任务中超越了同规模的RAG基线，并减少了30%以上的搜索调用。

## 📝 摘要（中文）

大规模多模态模型（LMMs）在现实场景中的稳健部署需要访问外部知识源，然而现有方法如检索增强生成（RAG）和提示工程搜索代理依赖于固定的管道，常导致搜索行为低效或过度。本文提出MMSearch-R1，这是第一个端到端的强化学习框架，使LMMs能够在现实互联网环境中按需进行多轮搜索。该框架集成了图像和文本搜索工具，允许模型根据基于结果的奖励和搜索惩罚来推理何时以及如何调用这些工具。通过半自动化管道收集的多模态搜索VQA数据集，涵盖了多样的视觉和文本知识需求，并策划了一个搜索平衡的子集，证明对塑造高效的按需搜索行为至关重要。大量实验表明，模型不仅超越了同等模型规模的RAG基线，还在减少超过30%的搜索调用的同时，匹配了更大RAG模型的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模多模态模型在现实场景中搜索效率低下的问题。现有方法如RAG依赖于固定的检索管道，常常导致不必要的搜索调用和信息获取的低效。

**核心思路**：MMSearch-R1的核心思路是通过强化学习框架，使模型能够根据环境反馈动态决定何时以及如何进行搜索。这种设计使得模型能够在复杂的互联网环境中灵活应对多样化的信息需求。

**技术框架**：该框架包含多个模块，包括图像和文本搜索工具、强化学习策略模块以及奖励机制。模型通过与环境的交互学习，优化搜索策略。

**关键创新**：MMSearch-R1的主要创新在于其端到端的强化学习设计，使得LMMs能够在多轮搜索中自适应调整搜索策略，与传统的固定管道方法形成鲜明对比。

**关键设计**：模型采用基于结果的奖励机制和搜索惩罚，确保在训练过程中优化搜索效率。此外，数据集的构建也注重平衡搜索需求，以支持模型的有效学习。

## 📊 实验亮点

实验结果表明，MMSearch-R1在知识密集型和信息检索VQA任务中表现优异，超越了同规模的RAG基线，并且在减少搜索调用方面提升超过30%。这一结果显示了该方法在提升搜索效率方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和多模态交互等。通过提高多模态模型的搜索效率，MMSearch-R1能够在实际应用中提供更快速、准确的信息获取，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Robust deployment of large multimodal models (LMMs) in real-world scenarios requires access to external knowledge sources, given the complexity and dynamic nature of real-world information. Existing approaches such as retrieval-augmented generation (RAG) and prompt engineered search agents rely on rigid pipelines, often leading to inefficient or excessive search behaviors. We present MMSearch-R1, the first end-to-end reinforcement learning framework that enables LMMs to perform on-demand, multi-turn search in real-world Internet environments. Our framework integrates both image and text search tools, allowing the model to reason about when and how to invoke them guided by an outcome-based reward with a search penalty. To support training, We collect a multimodal search VQA dataset through a semi-automated pipeline that covers diverse visual and textual knowledge needs and curate a search-balanced subset with both search-required and search-free samples, which proves essential for shaping efficient and on-demand search behavior. Extensive experiments on knowledge-intensive and info-seeking VQA tasks show that our model not only outperforms RAG-based baselines of the same model size, but also matches the performance of a larger RAG-based model while reducing search calls by over 30%. We further analyze key empirical findings to offer actionable insights for advancing research in multimodal search.

