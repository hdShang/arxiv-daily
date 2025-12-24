---
layout: default
title: "ERank: Fusing Supervised Fine-Tuning and Reinforcement Learning for Effective and Efficient Text Reranking"
---

# ERank: Fusing Supervised Fine-Tuning and Reinforcement Learning for Effective and Efficient Text Reranking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00520" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00520v1</a>
  <a href="https://arxiv.org/pdf/2509.00520.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00520v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00520v1', 'ERank: Fusing Supervised Fine-Tuning and Reinforcement Learning for Effective and Efficient Text Reranking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuzheng Cai, Yanzhao Zhang, Dingkun Long, Mingxin Li, Pengjun Xie, Weiguo Zheng

**分类**: cs.IR, cs.CL

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出ERank以解决文本重排序中的效率与效果问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本重排序` `监督微调` `强化学习` `大语言模型` `信息检索` `推荐系统` `效率提升`

## 📋 核心要点

1. 现有的文本重排序方法在效率和效果之间存在权衡，尤其是基于大语言模型的重排序器。
2. 本文提出ERank，通过两阶段训练流程结合监督微调和强化学习，提升了模型的相关性区分能力和效率。
3. 在多个基准测试中，ERank表现出色，尤其在推理密集的BRIGHT基准上，达到了40.2的nDCG@10，超越了现有方法。

## 📝 摘要（中文）

文本重排序模型是现代系统（如检索增强生成）的关键组成部分，负责在生成之前选择最相关的文档。然而，当前基于大语言模型的重排序器面临着基本的权衡。一方面，基于监督微调的点对点方法将相关性视为二分类任务，缺乏必要的评分区分能力；另一方面，复杂推理设计的列表式方法虽然强大，但效率低下，不适合低延迟应用。为了解决这一困境，本文提出了ERank，这是一种高效且有效的点对点重排序器，基于推理大语言模型，能够在多种相关性场景中表现出色。我们提出了一种新颖的两阶段训练流程，首先进行监督微调，训练模型生成细粒度整数评分，显著增强相关性区分能力。随后，利用强化学习和新颖的列表式奖励进一步优化模型。我们在多个基准上评估ERank，结果显示其优越的效果和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有文本重排序方法在效率与效果之间的权衡问题。当前基于监督微调的点对点方法缺乏足够的评分区分能力，而复杂推理的列表式方法又效率低下，难以应用于低延迟场景。

**核心思路**：ERank通过引入两阶段训练流程，首先进行监督微调以生成细粒度的整数评分，增强相关性区分能力；然后利用强化学习进一步优化模型，提升全局排名意识。

**技术框架**：ERank的整体架构包括两个主要阶段：第一阶段为监督微调，模型生成细粒度评分；第二阶段为强化学习，使用列表式奖励进行进一步优化。

**关键创新**：ERank的核心创新在于将监督微调与强化学习相结合，克服了传统方法的局限性，尤其是在评分区分和效率方面的提升。

**关键设计**：在监督微调阶段，模型输出细粒度整数评分；在强化学习阶段，设计了新颖的列表式奖励机制，以增强模型的全局排名意识。

## 📊 实验亮点

在BRIGHT基准测试中，ERank-4B模型达到了38.7的nDCG@10，而更大的32B变体则达到了40.2，成为当前的最佳性能。这一成果显著优于现有的重排序方法，展示了ERank在复杂推理任务中的强大能力。

## 🎯 应用场景

ERank的研究成果可广泛应用于信息检索、推荐系统和自然语言处理等领域，尤其适用于需要快速响应的应用场景，如在线搜索和实时推荐。其高效性和准确性将为相关领域带来显著的实际价值，推动智能系统的发展。

## 📄 摘要（原文）

> Text reranking models are a crucial component in modern systems like Retrieval-Augmented Generation, tasked with selecting the most relevant documents prior to generation. However, current Large Language Models (LLMs) powered rerankers often face a fundamental trade-off. On one hand, Supervised Fine-Tuning based pointwise methods that frame relevance as a binary classification task lack the necessary scoring discrimination, particularly for those built on reasoning LLMs. On the other hand, approaches designed for complex reasoning often employ powerful yet inefficient listwise formulations, rendering them impractical for low latency applications. To resolve this dilemma, we introduce ERank, a highly effective and efficient pointwise reranker built from a reasoning LLM that excels across diverse relevance scenarios. We propose a novel two-stage training pipeline that begins with Supervised Fine-Tuning (SFT). In this stage, we move beyond binary labels and train the model generatively to output fine grained integer scores, which significantly enhances relevance discrimination. The model is then further refined using Reinforcement Learning (RL) with a novel, listwise derived reward. This technique instills global ranking awareness into the efficient pointwise architecture. We evaluate the ERank reranker on the BRIGHT, FollowIR, TREC DL, and BEIR benchmarks, demonstrating superior effectiveness and robustness compared to existing approaches. On the reasoning-intensive BRIGHT benchmark, our ERank-4B achieves an nDCG@10 of 38.7, while a larger 32B variant reaches a state of the art nDCG@10 of 40.2.

