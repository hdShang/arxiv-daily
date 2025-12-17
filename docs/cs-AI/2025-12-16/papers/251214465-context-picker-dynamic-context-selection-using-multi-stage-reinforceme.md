---
layout: default
title: Context-Picker: Dynamic context selection using multi-stage reinforcement learning
---

# Context-Picker: Dynamic context selection using multi-stage reinforcement learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14465" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14465</a>
  <a href="https://arxiv.org/pdf/2512.14465.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14465" onclick="toggleFavorite(this, '2512.14465', 'Context-Picker: Dynamic context selection using multi-stage reinforcement learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyuan Zhu, Chengdong Xu, Kaiqiang Ke, Chao Yu

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Context-Picker：利用多阶段强化学习动态选择长文本问答的上下文**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长文本问答` `上下文选择` `强化学习` `多阶段学习` `证据提炼`

## 📋 核心要点

1. 长文本问答中，固定数量的上下文检索方法难以平衡信息覆盖和噪声抑制，影响答案质量。
2. Context-Picker采用两阶段强化学习，先召回关键信息，再精简冗余上下文，选择最小充分证据集。
3. 实验表明，Context-Picker在多个基准测试中优于现有RAG模型，提升了答案准确性并减少了上下文长度。

## 📝 摘要（中文）

在长文本问答（LCQA）中，确定给定查询的最佳上下文数量是一个重大挑战。包含过少的段落可能遗漏关键信息，而包含过多的段落会引入噪声并降低答案质量。传统的Top-$K$检索和单阶段重排序等方法面临着选择合适段落数量的困境，对于通常只需要少量特定证据的事实性问题尤其如此。为了解决这个问题，我们引入了Context-Picker，这是一个推理感知的框架，它将范式从基于相似性的排序转变为最小充分子集选择。Context-Picker将上下文选择视为一个决策过程，通过受人类启发的两阶段强化学习方案进行优化：一个以召回为导向的阶段，优先考虑推理链的覆盖；然后是一个以精确为导向的阶段，积极地修剪冗余以提炼出一个紧凑的证据集。为了解决奖励稀疏性问题，我们提出了一个离线证据提炼流程，通过留一法（LOO）程序挖掘“最小充分集”，提供密集的、任务对齐的监督。在五个长文本和多跳问答基准上的实验表明，Context-Picker显著优于强大的RAG基线，以相当或更短的上下文长度实现了卓越的答案准确性。消融研究表明，由粗到精的优化方案、冗余感知的奖励塑造和基于理由的格式都对这些收益做出了重大贡献。

## 🔬 方法详解

**问题定义**：长文本问答（LCQA）任务中，如何为给定的问题选择最佳数量和质量的上下文段落是一个关键问题。现有方法，如固定Top-K检索，要么可能遗漏关键信息，要么引入过多噪声，导致答案质量下降。特别是对于事实性问题，通常只需要少量关键证据，但现有方法难以精确选择。

**核心思路**：Context-Picker的核心思路是将上下文选择视为一个决策过程，通过强化学习来优化。它借鉴人类的阅读理解习惯，首先尽可能召回所有相关信息，然后再逐步去除冗余信息，最终选择一个最小但充分的证据子集。这种由粗到精的策略旨在提高答案的准确性和效率。

**技术框架**：Context-Picker采用一个两阶段强化学习框架。第一阶段是“召回导向”阶段，目标是尽可能覆盖所有可能包含答案的上下文段落。第二阶段是“精确导向”阶段，目标是去除冗余和噪声段落，提炼出一个紧凑的证据集。为了解决强化学习中的奖励稀疏性问题，论文还提出了一个离线证据提炼流程，用于生成密集的、任务对齐的监督信号。

**关键创新**：Context-Picker的关键创新在于将上下文选择问题转化为一个可学习的决策过程，并采用两阶段强化学习策略进行优化。与传统的基于相似度排序的方法不同，Context-Picker关注的是选择一个最小但充分的证据子集，而不是简单地选择Top-K个最相似的段落。此外，离线证据提炼流程有效地解决了奖励稀疏性问题，提高了学习效率。

**关键设计**：在第一阶段，奖励函数侧重于召回率，鼓励模型选择更多可能包含答案的段落。在第二阶段，奖励函数侧重于精确率，惩罚模型选择冗余段落。离线证据提炼流程使用留一法（LOO）来挖掘“最小充分集”，即移除任何一个段落都会导致答案错误的最小段落集合。这些“最小充分集”被用作强化学习的监督信号，引导模型学习如何选择最佳上下文。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14465/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14465/figures/overview-2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14465/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Context-Picker在五个长文本和多跳问答基准测试中显著优于现有的RAG基线模型。实验结果表明，Context-Picker在保持或减少上下文长度的同时，显著提高了答案的准确性。消融实验验证了由粗到精的优化策略、冗余感知的奖励塑造以及基于理由的格式对性能提升的贡献。

## 🎯 应用场景

Context-Picker可应用于各种需要从长文本中提取信息的场景，如智能客服、法律文档分析、金融报告解读等。通过更精确地选择上下文，可以提高信息检索的效率和准确性，减少计算资源消耗，并提升用户体验。该研究对于提升长文本处理能力具有重要意义。

## 📄 摘要（原文）

> In long-context question answering (LCQA), determining the optimal amount of context for a given query is a significant challenge. Including too few passages may omit critical information, while including too many can introduce noise and reduce the quality of the answer. Traditional approaches, such as fixed Top-$K$ retrieval and single-stage reranking, face the dilemma of selecting the right number of passages. This problem is particularly pronounced for factoid questions, which often require only a few specific pieces of evidence. To address this issue, we introduce \emph{Context-Picker}, a reasoning-aware framework that shifts the paradigm from similarity-based ranking to minimal sufficient subset selection. Context-Picker treats context selection as a decision-making process optimized via a human-inspired, two-stage reinforcement learning schedule: a \emph{recall-oriented} stage that prioritizes the coverage of reasoning chains, followed by a \emph{precision-oriented} stage that aggressively prunes redundancy to distill a compact evidence set. To resolve reward sparsity, we propose an offline evidence distillation pipeline that mines "minimal sufficient sets" via a Leave-One-Out (LOO) procedure, providing dense, task-aligned supervision. Experiments on five long-context and multi-hop QA benchmarks demonstrate that Context-Picker significantly outperforms strong RAG baselines, achieving superior answer accuracy with comparable or reduced context lengths. Ablation studies indicate that the coarse-to-fine optimization schedule, the redundancy-aware reward shaping, and the rationale-guided format all contribute substantially to these gains.

