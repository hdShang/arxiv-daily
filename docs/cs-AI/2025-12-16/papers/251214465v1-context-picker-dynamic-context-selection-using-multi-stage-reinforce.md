---
layout: default
title: Context-Picker: Dynamic context selection using multi-stage reinforcement learning
---

# Context-Picker: Dynamic context selection using multi-stage reinforcement learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14465" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14465v1</a>
  <a href="https://arxiv.org/pdf/2512.14465.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14465v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14465v1', 'Context-Picker: Dynamic context selection using multi-stage reinforcement learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyuan Zhu, Chengdong Xu, Kaiqiang Ke, Chao Yu

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**Context-Picker：利用多阶段强化学习动态选择长文本问答上下文**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长文本问答` `上下文选择` `强化学习` `多阶段学习` `证据提炼`

## 📋 核心要点

1. 长文本问答中，固定数量的上下文检索易引入噪声或遗漏关键信息，现有方法难以平衡。
2. Context-Picker采用两阶段强化学习，先召回关键信息，再精简冗余，选择最小充分上下文子集。
3. 实验表明，Context-Picker在多个基准测试中超越了RAG基线，提高了答案准确性并减少了上下文长度。

## 📝 摘要（中文）

在长文本问答（LCQA）中，确定给定查询的最佳上下文数量是一个重要的挑战。包含过少的段落可能会遗漏关键信息，而包含过多的段落可能会引入噪声并降低答案的质量。传统的Top-$K$检索和单阶段重排序等方法面临着选择合适段落数量的困境，对于通常只需要少量特定证据的事实性问题尤其如此。为了解决这个问题，我们引入了Context-Picker，这是一个推理感知的框架，它将范式从基于相似性的排序转变为最小充分子集选择。Context-Picker将上下文选择视为一个决策过程，通过受人类启发的两阶段强化学习策略进行优化：一个以召回为导向的阶段，优先考虑推理链的覆盖；然后是一个以精确为导向的阶段，积极地修剪冗余以提炼出一个紧凑的证据集。为了解决奖励稀疏性问题，我们提出了一个离线证据提炼流程，通过留一法（LOO）挖掘“最小充分集”，提供密集的、任务对齐的监督。在五个长文本和多跳问答基准上的实验表明，Context-Picker显著优于强大的RAG基线，以相当或更短的上下文长度实现了卓越的答案准确性。消融研究表明，由粗到精的优化策略、冗余感知的奖励塑造和以原理为指导的格式都对这些收益做出了重大贡献。

## 🔬 方法详解

**问题定义**：论文旨在解决长文本问答（LCQA）中上下文选择的问题。现有方法，如固定Top-K检索和单阶段重排序，无法有效地确定最佳上下文数量。包含过少信息可能导致遗漏关键证据，而包含过多信息则会引入噪声，降低答案质量，尤其是在需要少量精确证据的事实性问题中。

**核心思路**：论文的核心思路是将上下文选择视为一个决策过程，并采用强化学习来优化这个过程。通过模仿人类的推理过程，Context-Picker分两个阶段进行上下文选择：首先，以召回为导向，确保覆盖所有必要的推理链；然后，以精确为导向，去除冗余信息，最终得到一个最小且充分的上下文子集。

**技术框架**：Context-Picker框架包含两个主要的强化学习阶段：1) **召回阶段**：该阶段的目标是尽可能多地召回与问题相关的上下文段落，确保覆盖所有可能的推理路径。2) **精简阶段**：该阶段的目标是在召回的段落中去除冗余和噪声，选择最相关的最小上下文子集。为了解决奖励稀疏性问题，论文还提出了一个离线证据提炼流程，用于挖掘“最小充分集”，并提供密集的监督信号。

**关键创新**：Context-Picker的关键创新在于其两阶段强化学习策略和离线证据提炼流程。与传统的基于相似性的排序方法不同，Context-Picker采用推理感知的上下文选择方法，能够更准确地选择与问题相关的最小上下文子集。离线证据提炼流程通过留一法（LOO）挖掘最小充分集，为强化学习提供了更有效的监督信号。

**关键设计**：Context-Picker使用两阶段强化学习，每个阶段都有自己的奖励函数。召回阶段的奖励函数侧重于覆盖推理链，而精简阶段的奖励函数侧重于去除冗余。离线证据提炼流程使用留一法（LOO）来确定每个段落的重要性，并生成密集的奖励信号。具体的网络结构和参数设置在论文中有详细描述，但此处未提供详细信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14465v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14465v1/figures/overview-2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14465v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Context-Picker在五个长文本和多跳问答基准测试中显著优于强大的RAG基线。实验结果表明，Context-Picker在答案准确性方面取得了显著提升，同时保持了相当或更短的上下文长度。消融研究表明，由粗到精的优化策略、冗余感知的奖励塑造和以原理为指导的格式都对性能提升做出了重要贡献。

## 🎯 应用场景

Context-Picker可应用于各种需要从大量文本中提取信息的场景，如智能客服、法律咨询、医学诊断等。通过选择最相关的上下文，可以提高问答系统的准确性和效率，减少噪声干扰，并为用户提供更精确的答案。该研究对提升长文本问答系统的性能具有重要意义。

## 📄 摘要（原文）

> In long-context question answering (LCQA), determining the optimal amount of context for a given query is a significant challenge. Including too few passages may omit critical information, while including too many can introduce noise and reduce the quality of the answer. Traditional approaches, such as fixed Top-$K$ retrieval and single-stage reranking, face the dilemma of selecting the right number of passages. This problem is particularly pronounced for factoid questions, which often require only a few specific pieces of evidence. To address this issue, we introduce \emph{Context-Picker}, a reasoning-aware framework that shifts the paradigm from similarity-based ranking to minimal sufficient subset selection. Context-Picker treats context selection as a decision-making process optimized via a human-inspired, two-stage reinforcement learning schedule: a \emph{recall-oriented} stage that prioritizes the coverage of reasoning chains, followed by a \emph{precision-oriented} stage that aggressively prunes redundancy to distill a compact evidence set. To resolve reward sparsity, we propose an offline evidence distillation pipeline that mines "minimal sufficient sets" via a Leave-One-Out (LOO) procedure, providing dense, task-aligned supervision. Experiments on five long-context and multi-hop QA benchmarks demonstrate that Context-Picker significantly outperforms strong RAG baselines, achieving superior answer accuracy with comparable or reduced context lengths. Ablation studies indicate that the coarse-to-fine optimization schedule, the redundancy-aware reward shaping, and the rationale-guided format all contribute substantially to these gains.

