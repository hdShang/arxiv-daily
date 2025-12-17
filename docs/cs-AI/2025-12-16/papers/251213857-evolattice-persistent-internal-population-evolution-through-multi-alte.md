---
layout: default
title: EvoLattice: Persistent Internal-Population Evolution through Multi-Alternative Quality-Diversity Graph Representations for LLM-Guided Program Discovery
---

# EvoLattice: Persistent Internal-Population Evolution through Multi-Alternative Quality-Diversity Graph Representations for LLM-Guided Program Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13857" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13857</a>
  <a href="https://arxiv.org/pdf/2512.13857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13857" onclick="toggleFavorite(this, '2512.13857', 'EvoLattice: Persistent Internal-Population Evolution through Multi-Alternative Quality-Diversity Graph Representations for LLM-Guided Program Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kamer Ali Yuksel

**分类**: cs.AI, cs.CL, cs.LG, cs.MA, cs.NE

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**EvoLattice：通过多替代质量多样性图表示实现LLM引导的程序发现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `程序演化` `大型语言模型` `质量多样性` `图表示` `智能体设计`

## 📋 核心要点

1. 现有LLM引导的程序演化方法依赖于单候选覆盖式突变，易丢失有用变体并导致结构性问题。
2. EvoLattice使用有向无环图表示候选程序群体，节点存储多个替代方案，实现组合搜索空间。
3. EvoLattice通过评估替代方案对全局性能的影响，为LLM提供数据驱动的反馈，并保证结构正确性。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地用于演化程序和多智能体系统，但现有方法大多依赖于基于覆盖的突变，每次只维护一个候选方案。这些方法丢弃了有用的变体，遭受破坏性编辑，并探索了一个脆弱的搜索空间，容易出现结构性故障。我们引入了EvoLattice，一个在单个有向无环图中表示候选程序或智能体行为群体的框架。每个节点存储多个持久性替代方案，并且通过图的每个有效路径定义了一个不同的可执行候选方案，从而产生一个大的组合搜索空间，而无需复制结构。EvoLattice通过对每个替代方案在其出现的所有路径上进行评分，从而实现细粒度的替代方案级别评估，从而产生统计数据，揭示局部设计选择如何影响全局性能。这些统计数据为LLM引导的突变、重组和修剪提供了密集的数据驱动反馈信号，同时保留了成功的组件。结构正确性由确定性的自修复机制保证，该机制独立于LLM强制执行非循环性和依赖性一致性。EvoLattice通过将替代方案解释为提示片段或子智能体行为，自然地扩展到智能体演化。在程序合成（代理和优化器元学习）中，EvoLattice比先前的LLM引导方法产生更稳定的演化、更大的表达性和更强的改进轨迹。由此产生的动态类似于质量多样性优化，从EvoLattice的内部多替代表示中隐式地出现，而不是显式的外部存档。

## 🔬 方法详解

**问题定义**：现有基于LLM的程序演化方法通常采用单候选方案的迭代更新策略，即每次只保留一个最佳候选方案，并对其进行突变。这种方法的痛点在于：1) 容易丢失有用的中间变体，导致搜索效率低下；2) 突变操作可能引入破坏性修改，导致程序结构崩溃；3) 搜索空间脆弱，容易陷入局部最优。

**核心思路**：EvoLattice的核心思路是构建一个有向无环图，将整个候选程序群体表示在一个统一的结构中。图中的每个节点代表程序的一个组成部分，每个节点可以存储多个替代方案。通过图的每一条有效路径，可以生成一个完整的可执行程序。这种设计允许同时探索多个候选方案，并保留有用的中间变体，从而提高搜索效率和鲁棒性。

**技术框架**：EvoLattice框架包含以下主要模块：1) **图构建模块**：负责构建和维护有向无环图，包括添加节点、添加替代方案、连接节点等操作。2) **评估模块**：负责评估每个替代方案的性能，并生成反馈信号。评估过程考虑了该替代方案在所有包含它的路径上的表现。3) **LLM引导模块**：利用LLM根据评估结果，指导图的演化，包括突变、重组和修剪等操作。4) **自修复模块**：负责保证图的结构正确性，包括强制执行非循环性和依赖性一致性。

**关键创新**：EvoLattice最重要的技术创新点在于其内部多替代方案表示。与传统的单候选方案方法不同，EvoLattice能够同时维护和评估多个替代方案，从而实现更高效的搜索和更鲁棒的演化。此外，EvoLattice的自修复机制能够保证程序结构的正确性，避免了因突变操作导致的结构性问题。

**关键设计**：EvoLattice的关键设计包括：1) **替代方案的表示**：每个节点存储多个替代方案，每个替代方案可以是程序代码片段、智能体行为等。2) **评估指标**：评估指标用于衡量每个替代方案的性能，并生成反馈信号。3) **LLM提示工程**：设计合适的LLM提示，引导LLM进行有效的突变、重组和修剪操作。4) **自修复规则**：定义一组规则，用于保证图的结构正确性，例如强制执行非循环性和依赖性一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13857/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，EvoLattice在程序合成任务（代理和优化器元学习）中，比现有的LLM引导方法表现出更稳定的演化过程、更大的表达能力和更强的性能提升。EvoLattice能够隐式地实现质量多样性优化，而无需显式的外部存档。

## 🎯 应用场景

EvoLattice可应用于程序合成、机器人控制、智能体设计等领域。通过高效地探索程序或智能体行为空间，EvoLattice能够自动发现高性能的解决方案。该研究的潜在价值在于降低程序开发和智能体设计的成本，并加速人工智能技术的应用。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used to evolve programs and multi-agent systems, yet most existing approaches rely on overwrite-based mutations that maintain only a single candidate at a time. Such methods discard useful variants, suffer from destructive edits, and explore a brittle search space prone to structural failure. We introduce EvoLattice, a framework that represents an entire population of candidate programs or agent behaviors within a single directed acyclic graph. Each node stores multiple persistent alternatives, and every valid path through the graph defines a distinct executable candidate, yielding a large combinatorial search space without duplicating structure. EvoLattice enables fine-grained alternative-level evaluation by scoring each alternative across all paths in which it appears, producing statistics that reveal how local design choices affect global performance. These statistics provide a dense, data-driven feedback signal for LLM-guided mutation, recombination, and pruning, while preserving successful components. Structural correctness is guaranteed by a deterministic self-repair mechanism that enforces acyclicity and dependency consistency independently of the LLM. EvoLattice naturally extends to agent evolution by interpreting alternatives as prompt fragments or sub-agent behaviors. Across program synthesis (proxy and optimizer meta-learning), EvoLattice yields more stable evolution, greater expressivity, and stronger improvement trajectories than prior LLM-guided methods. The resulting dynamics resemble quality-diversity optimization, emerging implicitly from EvoLattice's internal multi-alternative representation rather than an explicit external archive.

