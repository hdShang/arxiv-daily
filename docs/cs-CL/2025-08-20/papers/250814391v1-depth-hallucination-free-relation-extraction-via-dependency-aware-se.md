---
layout: default
title: "DEPTH: Hallucination-Free Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement"
---

# DEPTH: Hallucination-Free Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14391" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14391v1</a>
  <a href="https://arxiv.org/pdf/2508.14391.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14391v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14391v1', 'DEPTH: Hallucination-Free Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yupei Yang, Fan Feng, Lin Yang, Wanxi Deng, Lin Qu, Biwei Huang, Shikui Tu, Lei Xu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出DEPTH框架以解决关系提取中的幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `关系提取` `知识图谱` `自然语言处理` `依赖感知` `强化学习` `句子简化` `结构化知识`

## 📋 核心要点

1. 现有关系提取方法在复杂句子结构下难以可靠判断关系的存在，导致幻觉现象频发。
2. DEPTH框架通过依赖感知句子简化和双层次精炼，减少语法噪声并提升关系提取的准确性。
3. 在六个基准测试中，DEPTH将幻觉率降低至7.0%，F1分数较最先进基线提升17.2%。

## 📝 摘要（中文）

关系提取是构建结构化知识的重要环节，尽管大型语言模型在此领域展现出良好潜力，但现有方法多集中于关系分类，难以可靠判断关系的存在，尤其在复杂句子结构下，容易产生幻觉，导致知识图谱中的噪声边缘。为此，本文提出DEPTH框架，结合依赖感知句子简化和双层次层次化精炼，分为两个阶段：首先通过最短依赖路径提取关系，简化句子以减少语法噪声；其次聚合局部预测并基于整体理解进行修正。实验表明，DEPTH将幻觉率降低至7.0%，F1分数提升17.2%。

## 🔬 方法详解

**问题定义**：本文旨在解决关系提取中存在的幻觉问题，现有方法在复杂句子结构下难以准确判断关系的存在，导致知识图谱中出现噪声边缘。

**核心思路**：DEPTH框架通过依赖感知句子简化和双层次精炼，旨在减少语法噪声并保留关键语义，从而提高关系提取的可靠性。

**技术框架**：DEPTH框架分为两个主要模块：第一阶段是Grounding模块，通过最短依赖路径提取关系，简化句子；第二阶段是Refinement模块，聚合局部预测并进行整体修正。

**关键创新**：DEPTH的创新在于引入了依赖感知的句子简化和双层次的精炼过程，显著降低了幻觉现象，提升了关系提取的准确性。

**关键设计**：在设计中，采用了基于因果关系的奖励模型，以减少奖励黑客现象，并通过人类反馈进行强化学习的稳健微调。

## 📊 实验亮点

DEPTH在六个基准测试中的实验结果显示，幻觉率降低至7.0%，同时F1分数较最先进基线提升17.2%，展现出显著的性能优势，证明了其在关系提取任务中的有效性。

## 🎯 应用场景

该研究在知识图谱构建、信息抽取和自然语言处理等领域具有广泛的应用潜力。通过提高关系提取的准确性，DEPTH能够为下游任务提供更可靠的结构化知识，进而提升智能系统的决策能力和推理能力。

## 📄 摘要（原文）

> Relation extraction enables the construction of structured knowledge for many downstream applications. While large language models (LLMs) have shown great promise in this domain, most existing methods concentrate on relation classification, which predicts the semantic relation type between a related entity pair. However, we observe that LLMs often struggle to reliably determine whether a relation exists, especially in cases involving complex sentence structures or intricate semantics, which leads to spurious predictions. Such hallucinations can introduce noisy edges in knowledge graphs, compromising the integrity of structured knowledge and downstream reliability. To address these challenges, we propose DEPTH, a framework that integrates Dependency-aware sEntence simPlification and Two-tiered Hierarchical refinement into the relation extraction pipeline. Given a sentence and its candidate entity pairs, DEPTH operates in two stages: (1) the Grounding module extracts relations for each pair by leveraging their shortest dependency path, distilling the sentence into a minimal yet coherent relational context that reduces syntactic noise while preserving key semantics; (2) the Refinement module aggregates all local predictions and revises them based on a holistic understanding of the sentence, correcting omissions and inconsistencies. We further introduce a causality-driven reward model that mitigates reward hacking by disentangling spurious correlations, enabling robust fine-tuning via reinforcement learning with human feedback. Experiments on six benchmarks demonstrate that DEPTH reduces the average hallucination rate to 7.0\% while achieving a 17.2\% improvement in average F1 score over state-of-the-art baselines.

