---
layout: default
title: Context-Picker: Dynamic context selection using multi-stage reinforcement learning
---

# Context-Picker: Dynamic context selection using multi-stage reinforcement learning

**arXiv**: [2512.14465v1](https://arxiv.org/abs/2512.14465) | [PDF](https://arxiv.org/pdf/2512.14465.pdf)

**作者**: Siyuan Zhu, Chengdong Xu, Kaiqiang Ke, Chao Yu

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Context-Picker框架，通过多阶段强化学习动态选择最小充分证据集，以解决长上下文问答中的噪声与信息不足问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `长上下文问答` `强化学习` `证据选择` `多阶段优化` `推理感知` `最小充分集` `噪声剪枝` `问答系统`

## 📋 核心要点

1. 长上下文问答中，传统固定Top-K检索和单阶段重排序方法难以平衡噪声与信息不足，尤其在事实型问题中。
2. 提出Context-Picker框架，采用两阶段强化学习：先召回覆盖推理链，再精确剪枝冗余，实现最小充分证据集选择。
3. 在五个基准测试中，Context-Picker显著超越RAG基线，答案准确性更高，同时上下文长度相当或更短。

## 📝 摘要（中文）

在长上下文问答（LCQA）中，为给定查询确定最优的上下文量是一个重大挑战。包含过少段落可能遗漏关键信息，而包含过多则会引入噪声并降低答案质量。传统方法如固定Top-K检索和单阶段重排序面临选择适当段落数量的困境，这一问题在事实型问题中尤为突出，这类问题通常只需要少量特定证据。为解决此问题，我们引入了Context-Picker，这是一个推理感知框架，将范式从基于相似性的排序转向最小充分子集选择。Context-Picker将上下文选择视为一个决策过程，通过受人类启发的两阶段强化学习计划进行优化：一个以召回为导向的阶段，优先覆盖推理链；随后是一个以精确为导向的阶段，积极剪枝冗余以提炼紧凑的证据集。为解决奖励稀疏性问题，我们提出了一个离线证据蒸馏流程，通过留一法（LOO）挖掘“最小充分集”，提供密集、任务对齐的监督。在五个长上下文和多跳问答基准上的实验表明，Context-Picker显著优于强大的RAG基线，在可比或更短的上下文长度下实现了更优的答案准确性。消融研究表明，从粗到细的优化计划、冗余感知的奖励塑造和推理引导的格式都对这一增益有实质性贡献。

## 🔬 方法详解

Context-Picker是一个推理感知框架，将上下文选择视为决策过程，通过多阶段强化学习优化。整体框架包括：以召回为导向的阶段，优先覆盖推理链；以精确为导向的阶段，积极剪枝冗余，提炼紧凑证据集。关键技术创新点包括：采用两阶段强化学习计划，模拟人类推理过程；提出离线证据蒸馏流程，通过留一法挖掘最小充分集，解决奖励稀疏性问题；引入冗余感知奖励塑造和推理引导格式。与现有方法的主要区别在于，它从相似性排序转向最小充分子集选择，动态调整上下文量，而非固定数量或单阶段处理。

## 📊 实验亮点

在五个长上下文和多跳问答基准上，Context-Picker显著优于RAG基线，答案准确性更高，同时上下文长度相当或更短，消融研究证实优化计划和奖励塑造的关键作用。

## 🎯 应用场景

该研究可应用于长文档问答、多跳推理、事实核查和智能助手等领域，通过动态选择最小充分证据集，提高答案准确性并减少计算开销，具有实际价值。

## 📄 摘要（原文）

> In long-context question answering (LCQA), determining the optimal amount of context for a given query is a significant challenge. Including too few passages may omit critical information, while including too many can introduce noise and reduce the quality of the answer. Traditional approaches, such as fixed Top-$K$ retrieval and single-stage reranking, face the dilemma of selecting the right number of passages. This problem is particularly pronounced for factoid questions, which often require only a few specific pieces of evidence. To address this issue, we introduce \emph{Context-Picker}, a reasoning-aware framework that shifts the paradigm from similarity-based ranking to minimal sufficient subset selection. Context-Picker treats context selection as a decision-making process optimized via a human-inspired, two-stage reinforcement learning schedule: a \emph{recall-oriented} stage that prioritizes the coverage of reasoning chains, followed by a \emph{precision-oriented} stage that aggressively prunes redundancy to distill a compact evidence set. To resolve reward sparsity, we propose an offline evidence distillation pipeline that mines "minimal sufficient sets" via a Leave-One-Out (LOO) procedure, providing dense, task-aligned supervision. Experiments on five long-context and multi-hop QA benchmarks demonstrate that Context-Picker significantly outperforms strong RAG baselines, achieving superior answer accuracy with comparable or reduced context lengths. Ablation studies indicate that the coarse-to-fine optimization schedule, the redundancy-aware reward shaping, and the rationale-guided format all contribute substantially to these gains.

