---
layout: default
title: Context-Picker: Dynamic context selection using multi-stage reinforcement learning
---

# Context-Picker: Dynamic context selection using multi-stage reinforcement learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14465" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14465v1</a>
  <a href="https://arxiv.org/pdf/2512.14465.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14465v1" onclick="toggleFavorite(this, '2512.14465v1', 'Context-Picker: Dynamic context selection using multi-stage reinforcement learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyuan Zhu, Chengdong Xu, Kaiqiang Ke, Chao Yu

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**Context-Picker：利用多阶段强化学习动态选择长文本问答的上下文**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长文本问答` `上下文选择` `强化学习` `多阶段学习` `证据提炼`

## 📋 核心要点

1. 长文本问答中，如何选择既包含关键信息又避免噪声干扰的最佳上下文是一个核心挑战。
2. Context-Picker采用两阶段强化学习，先召回所有可能相关的上下文，再精确地去除冗余信息，选择最小充分子集。
3. 实验表明，Context-Picker在多个长文本问答数据集上显著优于现有RAG模型，在保证准确率的同时减少了上下文长度。

## 📝 摘要（中文）

在长文本问答（LCQA）中，确定给定查询的最佳上下文数量是一个重大挑战。包含过少的段落可能遗漏关键信息，而包含过多的段落会引入噪声并降低答案质量。传统的Top-$K$检索和单阶段重排序等方法面临着选择合适段落数量的困境，对于通常只需要少量特定证据的事实性问题尤其如此。为了解决这个问题，我们引入了Context-Picker，这是一个推理感知的框架，它将范式从基于相似性的排序转变为最小充分子集选择。Context-Picker将上下文选择视为一个决策过程，通过受人类启发的两阶段强化学习方案进行优化：一个以召回为导向的阶段，优先考虑推理链的覆盖；然后是一个以精度为导向的阶段，积极地修剪冗余以提炼出一个紧凑的证据集。为了解决奖励稀疏性问题，我们提出了一个离线证据提炼流程，通过留一法（LOO）挖掘“最小充分集”，提供密集的、任务对齐的监督。在五个长文本和多跳问答基准上的实验表明，Context-Picker显著优于强大的RAG基线，以相当或更短的上下文长度实现了卓越的答案准确性。消融研究表明，由粗到精的优化方案、冗余感知的奖励塑造和以理由为指导的格式都对这些收益做出了重大贡献。

## 🔬 方法详解

**问题定义**：长文本问答（LCQA）任务中，现有方法如固定Top-K检索或单阶段重排序难以确定最佳上下文数量。包含上下文过少可能遗漏关键信息，过多则引入噪声，降低答案质量。尤其对于事实性问题，往往只需要少量关键证据，现有方法难以有效提取。

**核心思路**：将上下文选择视为一个决策过程，通过强化学习来优化。模仿人类阅读理解的过程，先广泛搜索相关信息（召回），再精简信息，去除冗余（精度）。通过两阶段强化学习，实现由粗到精的上下文选择。

**技术框架**：Context-Picker包含两个主要阶段：召回阶段和精度阶段。召回阶段旨在覆盖所有可能相关的推理链，使用强化学习策略选择上下文段落，最大化召回率。精度阶段则专注于去除冗余信息，进一步提炼上下文，提高答案的准确性。为了解决奖励稀疏性问题，采用离线证据提炼流程，挖掘“最小充分集”作为监督信号。

**关键创新**：Context-Picker的核心创新在于将上下文选择问题转化为一个可学习的决策过程，并采用两阶段强化学习策略。与传统的基于相似度排序的方法不同，Context-Picker关注于选择最小充分的证据子集，从而提高答案的准确性和效率。离线证据提炼流程为强化学习提供了密集的监督信号，解决了奖励稀疏性问题。

**关键设计**：Context-Picker使用两阶段强化学习，每个阶段都有独立的奖励函数和策略网络。召回阶段的奖励函数侧重于覆盖推理链，精度阶段的奖励函数侧重于去除冗余信息。离线证据提炼流程使用留一法（LOO）来挖掘最小充分集，为强化学习提供监督信号。具体网络结构和参数设置在论文中有详细描述（未知）。

## 📊 实验亮点

Context-Picker在五个长文本和多跳问答基准测试中显著优于强大的RAG基线。在保证或减少上下文长度的情况下，答案准确性得到了显著提升。消融实验表明，由粗到精的优化策略、冗余感知的奖励塑造以及以理由为指导的格式都对性能提升做出了重要贡献。（具体性能数据未知）

## 🎯 应用场景

Context-Picker可应用于各种需要从长文本中提取信息的场景，如智能客服、法律咨询、金融分析等。通过选择最相关的上下文，可以提高信息检索的准确性和效率，降低计算成本，并提升用户体验。该研究对于提升机器阅读理解能力具有重要意义。

## 📄 摘要（原文）

> In long-context question answering (LCQA), determining the optimal amount of context for a given query is a significant challenge. Including too few passages may omit critical information, while including too many can introduce noise and reduce the quality of the answer. Traditional approaches, such as fixed Top-$K$ retrieval and single-stage reranking, face the dilemma of selecting the right number of passages. This problem is particularly pronounced for factoid questions, which often require only a few specific pieces of evidence. To address this issue, we introduce \emph{Context-Picker}, a reasoning-aware framework that shifts the paradigm from similarity-based ranking to minimal sufficient subset selection. Context-Picker treats context selection as a decision-making process optimized via a human-inspired, two-stage reinforcement learning schedule: a \emph{recall-oriented} stage that prioritizes the coverage of reasoning chains, followed by a \emph{precision-oriented} stage that aggressively prunes redundancy to distill a compact evidence set. To resolve reward sparsity, we propose an offline evidence distillation pipeline that mines "minimal sufficient sets" via a Leave-One-Out (LOO) procedure, providing dense, task-aligned supervision. Experiments on five long-context and multi-hop QA benchmarks demonstrate that Context-Picker significantly outperforms strong RAG baselines, achieving superior answer accuracy with comparable or reduced context lengths. Ablation studies indicate that the coarse-to-fine optimization schedule, the redundancy-aware reward shaping, and the rationale-guided format all contribute substantially to these gains.

