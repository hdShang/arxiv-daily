---
layout: default
title: "TiMoE: Time-Aware Mixture of Language Experts"
---

# TiMoE: Time-Aware Mixture of Language Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08827" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08827v1</a>
  <a href="https://arxiv.org/pdf/2508.08827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08827v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08827v1', 'TiMoE: Time-Aware Mixture of Language Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Robin Faro, Dongyang Fan, Tamar Alphaidze, Martin Jaggi

**分类**: cs.CL

**发布日期**: 2025-08-12

**🔗 代码/项目**: [GITHUB](https://github.com/epfml/TiMoE)

---

## 💡 一句话要点

**提出TiMoE以解决语言模型的时间知识过时问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间感知` `语言模型` `专家混合` `因果推理` `NLP任务` `知识更新` `预训练`

## 📋 核心要点

1. 现有大型语言模型在固定快照上训练，导致知识过时和时间泄漏问题，影响预测准确性。
2. 本文提出TiMoE，通过对不同时间段的专家进行预训练，确保推理时的因果有效性，避免未来信息干扰。
3. 实验结果显示，TiMoE在多个NLP任务上表现优异，减少未来知识错误达15%，展示了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）通常在固定的网络快照上进行训练，这导致其知识可能过时，并且在预测时可能出现时间泄漏，即依赖于查询时间点之后的信息。为了解决这一问题，本文从头开始对一组GPT风格的专家进行预训练，使用2013-2024年语料库的不同两年切片，并通过TiMoE（时间感知语言专家混合模型）将它们结合起来。在推理时，TiMoE会屏蔽所有训练窗口在查询时间戳之后结束的专家，并合并剩余的对数概率，确保严格的因果有效性，同时保留多期知识的广度。我们还发布了TSQA，一个包含10,000个问题的基准，其选项被明确标记为过去、未来或无关，从而允许对时间幻觉进行细致的测量。实验结果表明，经过共同适应的TiMoE变体在八个标准NLP任务和TSQA上表现出色，匹配或超过了最佳单期专家，并将未来知识错误减少了多达15%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在固定快照训练下的知识过时和时间泄漏问题，现有方法无法有效处理时间相关性。

**核心思路**：论文提出的TiMoE模型通过对不同时间段的专家进行预训练，并在推理时屏蔽不相关的专家，从而确保因果有效性，避免未来信息的干扰。

**技术框架**：TiMoE的整体架构包括多个GPT风格的专家模型，这些模型分别在不同的时间段上进行训练。在推理时，模型会根据查询时间戳选择合适的专家进行预测，合并其输出的对数概率。

**关键创新**：TiMoE的主要创新在于其时间感知的专家混合机制，通过模块化的时间分段预训练和因果路由，显著提高了模型的时间相关性处理能力，与传统方法相比，避免了未来知识的干扰。

**关键设计**：在模型设计中，采用了分段训练的策略，确保每个专家只接触到其对应时间段的数据。此外，损失函数的设计也考虑了时间因素，以优化模型在不同时间段的表现。

## 📊 实验亮点

实验结果表明，TiMoE在八个标准NLP任务及TSQA基准上表现优异，特别是在减少未来知识错误方面，提升幅度达到15%。该模型的共同适应变体在性能上匹配或超过了最佳单期专家，展示了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括新闻生成、社交媒体分析和时间敏感的问答系统等。通过提高语言模型对时间信息的处理能力，TiMoE能够在动态环境中提供更准确的预测和响应，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) are typically trained on fixed snapshots of the web, which means that their knowledge becomes stale and their predictions risk temporal leakage: relying on information that lies in the future relative to a query. We tackle this problem by pre-training from scratch a set of GPT-style experts on disjoint two-year slices of a 2013-2024 corpus and combining them through TiMoE, a Time-aware Mixture of Language Experts. At inference time, TiMoE masks all experts whose training window ends after the query timestamp and merges the remaining log-probabilities in a shared space, guaranteeing strict causal validity while retaining the breadth of multi-period knowledge. We also release TSQA, a 10k-question benchmark whose alternatives are explicitly labelled as past, future or irrelevant, allowing fine-grained measurement of temporal hallucinations. Experiments on eight standard NLP tasks plus TSQA show that a co-adapted TiMoE variant matches or exceeds the best single-period expert and cuts future-knowledge errors by up to 15%. Our results demonstrate that modular, time-segmented pre-training paired with causal routing is a simple yet effective path toward LLMs that stay chronologically grounded without sacrificing general performance much. We open source our code at TiMoE (Github): https://github.com/epfml/TiMoE

