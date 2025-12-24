---
layout: default
title: "CORE: Measuring Multi-Agent LLM Interaction Quality under Game-Theoretic Pressures"
---

# CORE: Measuring Multi-Agent LLM Interaction Quality under Game-Theoretic Pressures

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11915" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11915v1</a>
  <a href="https://arxiv.org/pdf/2508.11915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11915v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11915v1', 'CORE: Measuring Multi-Agent LLM Interaction Quality under Game-Theoretic Pressures')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Punya Syon Pandey, Yongjin Yang, Jiarui Liu, Zhijing Jin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-16

**🔗 代码/项目**: [GITHUB](https://github.com/psyonp/core)

---

## 💡 一句话要点

**提出CORE指标以量化多智能体LLM交互质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `博弈论` `对话质量评估` `语言模型` `聚类熵` `词汇重复性` `语义相似性` `CORE指标`

## 📋 核心要点

1. 现有方法未能充分量化多智能体系统中基于博弈论的交互的语言多样性，导致对交互质量的理解不足。
2. 本文提出CORE指标，通过聚类熵、词汇重复性和语义相似性等多维度量化多智能体LLM的对话质量。
3. 实验结果表明，合作环境下的对话质量显著优于竞争环境，CORE为理解语言适应提供了新的视角。

## 📝 摘要（中文）

在多智能体系统中，基于博弈论的交互揭示了许多新兴能力，但这些交互的语言多样性尚未得到充分量化。本文提出了对话鲁棒性评估分数CORE，该指标用于量化多智能体系统中不同博弈论交互下的语言使用效果。CORE结合了聚类熵、词汇重复性和语义相似性等度量，为对话质量提供了直接的视角。通过在竞争、合作和中立环境下对成对LLM对话应用CORE，分析结果显示合作环境中存在更陡峭的Zipf分布和更高的Heap指数，表明更高的重复性和更大的词汇扩展。相反，竞争交互则显示出较低的Zipf和Heap指数，反映出较少的重复性和更受限的词汇。研究结果为社会激励如何影响语言适应提供了新见解，并强调了CORE作为多智能体LLM系统中语言鲁棒性测量的有效工具。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体系统中基于博弈论的交互语言多样性量化不足的问题，现有方法缺乏有效的度量工具来评估对话质量。

**核心思路**：提出CORE指标，通过结合聚类熵、词汇重复性和语义相似性，提供一个全面的对话质量评估框架，以量化不同博弈论交互下的语言使用效果。

**技术框架**：CORE的整体架构包括数据收集、特征提取和质量评估三个主要模块。首先收集多智能体对话数据，然后提取相关特征，最后计算CORE得分以评估对话质量。

**关键创新**：CORE的创新在于其综合性度量方法，能够同时考虑语言的多样性和重复性，与现有单一维度的评估方法相比，提供了更全面的视角。

**关键设计**：在参数设置上，CORE使用聚类熵来评估词汇的分布情况，词汇重复性通过计算相同词汇的出现频率来实现，语义相似性则通过预训练的语言模型进行计算，确保了评估的准确性和可靠性。

## 📊 实验亮点

实验结果显示，在合作环境下，CORE指标的Zipf分布陡峭度和Heap指数显著高于竞争环境，表明合作对话中存在更高的词汇重复性和扩展性。这些发现为理解社会激励对语言适应的影响提供了新的见解。

## 🎯 应用场景

CORE指标的提出为多智能体系统中的对话质量评估提供了新的工具，具有广泛的应用潜力。它可以用于智能客服、游戏AI、社交机器人等领域，帮助提升系统的语言适应能力和用户体验。未来，CORE还可能推动对话系统的进一步研究和优化。

## 📄 摘要（原文）

> Game-theoretic interactions between agents with Large Language Models (LLMs) have revealed many emergent capabilities, yet the linguistic diversity of these interactions has not been sufficiently quantified. In this paper, we present the Conversational Robustness Evaluation Score: CORE, a metric to quantify the effectiveness of language use within multi-agent systems across different game-theoretic interactions. CORE integrates measures of cluster entropy, lexical repetition, and semantic similarity, providing a direct lens of dialog quality. We apply CORE to pairwise LLM dialogs across competitive, cooperative, and neutral settings, further grounding our analysis in Zipf's and Heaps' Laws to characterize word frequency distributions and vocabulary growth. Our findings show that cooperative settings exhibit both steeper Zipf distributions and higher Heap exponents, indicating more repetition alongside greater vocabulary expansion. In contrast, competitive interactions display lower Zipf and Heaps exponents, reflecting less repetition and more constrained vocabularies. These results provide new insights into how social incentives influence language adaptation, and highlight CORE as a robust diagnostic for measuring linguistic robustness in multi-agent LLM systems. Our code is available at https://github.com/psyonp/core.

