---
layout: default
title: "Automated Algorithmic Discovery for Scientific Computing through LLM-Guided Evolutionary Search: A Case Study in Gravitational-Wave Detection"
---

# Automated Algorithmic Discovery for Scientific Computing through LLM-Guided Evolutionary Search: A Case Study in Gravitational-Wave Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03661" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03661v3</a>
  <a href="https://arxiv.org/pdf/2508.03661.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03661v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03661v3', 'Automated Algorithmic Discovery for Scientific Computing through LLM-Guided Evolutionary Search: A Case Study in Gravitational-Wave Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: He Wang, Liang Zeng

**分类**: cs.AI, astro-ph.HE, astro-ph.IM, gr-qc

**发布日期**: 2025-08-05 (更新: 2025-11-16)

**备注**: 76 pages (28 main), with 6+6 figures and 2 tables, substantially revised with improved structure and clarity

---

## 💡 一句话要点

**提出Evo-MCTS框架以解决科学计算中的算法自动发现问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `算法自动发现` `进化搜索` `引力波检测` `可解释性` `大型语言模型`

## 📋 核心要点

1. 现有的自动算法发现方法在面对广泛的设计空间和高昂的评估成本时，缺乏有效的解决方案。
2. 本文提出的Evo-MCTS框架通过结合LLMs与进化搜索，提供了一种新的可解释算法发现方法。
3. 在引力波检测实验中，Evo-MCTS实现了20.2%的性能提升，显示出其在复杂领域中的有效性。

## 📝 摘要（中文）

科学计算中的自动算法发现面临着设计空间广泛、评估成本高、领域特定物理约束及可解释性需求等基本挑战。本文提出了Evo-MCTS（进化蒙特卡洛树搜索）框架，将大型语言模型（LLMs）与树结构进化搜索相结合，以实现可解释的算法发现。Evo-MCTS结合了反思性代码合成、结构化代码表示上的多尺度进化操作，以及通过树导向探索产生的可解释算法路径。在引力波检测这一具有连续参数空间和严格物理约束的挑战性领域中，Evo-MCTS相较于领域特定方法提升了20.2%，相较于基于LLM的优化框架提升了59.1%。这一提升源于其能够持续收敛于集成多个功能组件的可解释算法结构。

## 🔬 方法详解

**问题定义**：本文旨在解决科学计算中算法自动发现的挑战，尤其是在设计空间广泛且评估成本高的情况下，现有方法往往缺乏可解释性和有效性。

**核心思路**：Evo-MCTS框架通过将大型语言模型与树结构进化搜索相结合，利用LLM的领域知识进行反思性代码合成，从而实现可解释的算法发现。

**技术框架**：Evo-MCTS的整体架构包括三个主要模块：反思性代码合成、结构化代码表示的多尺度进化操作，以及树导向探索生成的可解释算法路径。

**关键创新**：Evo-MCTS的核心创新在于其结合了LLMs与进化搜索的能力，使得算法不仅具备高效性，还能保持可解释性，这与传统方法的黑箱特性形成鲜明对比。

**关键设计**：在设计中，Evo-MCTS采用了多尺度进化操作，以适应不同层次的代码结构，同时确保生成的算法在物理约束下的有效性和可验证性。

## 📊 实验亮点

在引力波检测的实验中，Evo-MCTS相较于领域特定方法实现了20.2%的性能提升，相较于基于LLM的优化框架则提升了59.1%。这一显著的性能提升表明Evo-MCTS在处理复杂科学计算问题时的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括科学计算、物理模拟和工程优化等。Evo-MCTS框架的通用性使其能够适应不同领域的算法发现需求，未来可能在多个科学研究和工业应用中发挥重要作用，推动自动化算法设计的发展。

## 📄 摘要（原文）

> Automated algorithm discovery in scientific computing faces fundamental challenges: vast design spaces with expensive evaluations, domain-specific physical constraints requiring expert knowledge, and the necessity for interpretable solutions that scientists can validate and understand. We present the Evo-MCTS (Evolutionary Monte Carlo Tree Search) framework, integrating large language models (LLMs) with tree-structured evolutionary search for interpretable algorithm discovery. Evo-MCTS combines reflective code synthesis leveraging LLM domain knowledge, multi-scale evolutionary operations on structured code representations, and interpretable algorithmic pathways emerging from tree-guided exploration. When applied to gravitational wave detection-a challenging domain with continuous parameter spaces and strict physical constraints-Evo-MCTS achieves 20.2% improvement over domain-specific methods and 59.1% over LLM-based optimization frameworks. This improvement arises from its ability to consistently converge toward interpretable algorithmic structures that integrate multiple functional components. Our domain-agnostic architecture establishes a generalizable methodology for automated algorithm discovery in scientific computing, where algorithmic transparency and physical validity are as essential as performance optimization.

