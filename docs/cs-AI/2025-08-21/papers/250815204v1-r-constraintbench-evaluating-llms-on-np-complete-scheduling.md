---
layout: default
title: "R-ConstraintBench: Evaluating LLMs on NP-Complete Scheduling"
---

# R-ConstraintBench: Evaluating LLMs on NP-Complete Scheduling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15204" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15204v1</a>
  <a href="https://arxiv.org/pdf/2508.15204.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15204v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15204v1', 'R-ConstraintBench: Evaluating LLMs on NP-Complete Scheduling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raj Jain, Marc Wetter

**分类**: cs.AI

**发布日期**: 2025-08-21

---

## 💡 一句话要点

**提出R-ConstraintBench以评估LLMs在NP完全调度问题上的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `调度问题` `大型语言模型` `资源约束` `约束交互` `性能评估` `数据中心迁移` `可行性分析`

## 📋 核心要点

1. 现有方法对大型语言模型在高约束条件下的推理能力评估不足，导致其可靠性未得到充分验证。
2. 本文提出R-ConstraintBench框架，通过逐步增加约束来评估模型在资源约束调度问题上的表现。
3. 实验结果显示，强模型在简单场景中表现良好，但在复杂约束交互下性能显著下降，揭示了约束交互的影响。

## 📝 摘要（中文）

有效的调度在资本项目、制造、物流和IT舰队过渡等多个领域中至关重要。然而，现有的大型语言模型（LLMs）在高约束条件下的推理能力尚未得到充分评估。为此，本文提出了R-ConstraintBench，这是一个可扩展的框架，用于评估模型在资源约束项目调度问题（RCPSP）上的表现。该框架通过线性增加约束的方式逐步提高难度，并在有向无环图（DAG）中引入非冗余的优先约束、停机时间、时间窗口和选择性约束。通过在数据中心迁移场景中的实例化，评估了多种LLMs的可行性和错误分析，识别出与失败最相关的约束类型。实验证明，强模型在仅有优先约束的DAG上表现接近极限，但在停机时间、时间窗口和选择性约束交互时，表现显著下降，表明约束交互是主要瓶颈。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在资源约束调度问题（RCPSP）中的推理能力不足，现有方法未能充分评估其在高约束条件下的表现。

**核心思路**：R-ConstraintBench框架通过逐步增加非冗余优先约束、停机时间、时间窗口和选择性约束，系统性地评估模型在复杂调度问题上的表现。这样的设计旨在揭示约束交互对模型性能的影响。

**技术框架**：该框架的整体架构包括多个阶段：首先在DAG中引入优先约束，然后逐步增加其他约束类型，最后进行可行性和错误分析。每个阶段的设计都旨在逐步提高问题的复杂性。

**关键创新**：R-ConstraintBench的主要创新在于其系统性地评估LLMs在NP完全调度问题上的表现，特别是通过约束交互的方式揭示模型性能的瓶颈。这与现有方法的评估方式有本质区别。

**关键设计**：在框架中，关键参数包括约束的类型和数量，损失函数设计用于评估可行性，网络结构则需适应不同约束条件下的调度问题。

## 📊 实验亮点

实验结果表明，强模型在仅有优先约束的DAG上表现接近极限，但在引入停机时间、时间窗口和选择性约束后，性能显著下降，显示出约束交互的影响。具体而言，模型在复杂约束下的可行性性能崩溃，揭示了约束交互而非图深度是主要瓶颈。

## 🎯 应用场景

该研究的潜在应用领域包括资本项目管理、制造业调度、物流优化和IT系统迁移等。通过提高大型语言模型在复杂调度问题上的可靠性，R-ConstraintBench能够为实际应用提供更有效的决策支持，推动相关领域的智能化进程。

## 📄 摘要（原文）

> Effective scheduling under tight resource, timing, and operational constraints underpins large-scale planning across sectors such as capital projects, manufacturing, logistics, and IT fleet transitions. However, the reliability of large language models (LLMs) when reasoning under high-constraint regimes is insufficiently characterized. To address this gap, we present R-ConstraintBench, a scalable framework that evaluates models on Resource-Constrained Project Scheduling Problems (RCPSP), an NP-Complete feasibility class, while difficulty increases via linear growth in constraints. R-ConstraintBench incrementally increases non-redundant precedence constraints in Directed Acyclic Graphs (DAGs) and then introduces downtime, temporal windows, and disjunctive constraints. As an illustrative example, we instantiate the benchmark in a data center migration setting and evaluate multiple LLMs using feasibility and error analysis, identifying degradation thresholds and constraint types most associated with failure. Empirically, strong models are near-ceiling on precedence-only DAGs, but feasibility performance collapses when downtime, temporal windows, and disjunctive constraints interact, implicating constraint interaction, not graph depth, as the principal bottleneck. Performance on clean synthetic ramps also does not guarantee transfer to domain-grounded scenarios, underscoring limited generalization.

