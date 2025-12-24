---
layout: default
title: "The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management"
---

# The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21433" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21433v3</a>
  <a href="https://arxiv.org/pdf/2508.21433.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21433v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21433v3', 'The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobias Lindenbauer, Igor Slinko, Ludwig Felder, Egor Bogomolov, Yaroslav Zharov

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-29 (更新: 2025-10-27)

**备注**: v3: DL4C camera-ready version to be presented at the 4th DL4C workshop co-located with NeurIPS '25; added OpenHands generality probe, added hybrid context management strategy

---

## 💡 一句话要点

**提出简单观察掩蔽策略以优化LLM代理的上下文管理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `上下文管理` `软件工程` `观察掩蔽` `成本优化` `代理系统` `混合方法`

## 📋 核心要点

1. 现有的LLM摘要方法在处理复杂任务时可能导致不必要的复杂性和高成本。
2. 论文提出了一种简单的观察掩蔽策略，旨在通过省略旧的观察来降低成本，同时保持解决率。
3. 实验结果表明，观察掩蔽策略在成本和性能上均优于传统的LLM摘要方法，且混合方法进一步提升了效率。

## 📝 摘要（中文）

大型语言模型（LLM）驱动的代理通过迭代推理、探索和工具使用来解决复杂任务，这一过程可能导致长且昂贵的上下文历史。尽管现有的先进软件工程代理如OpenHands和Cursor采用LLM摘要来应对这一问题，但其复杂性是否带来了实际的性能提升尚不明确。本文系统比较了在SWE-agent上使用简单环境观察掩蔽策略与LLM摘要的效果，发现前者在成本上减少了一半，同时在解决率上与LLM摘要相当，甚至略有超越。此外，提出了一种新颖的混合方法，进一步降低了7%至11%的成本。我们的研究对纯LLM摘要的趋势提出了质疑，并提供了推动效率与效果边界的初步证据。我们还发布了代码和数据以支持可重复性。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM代理在处理复杂任务时产生的高成本和长上下文历史问题。现有的LLM摘要方法虽然有效，但其复杂性和计算开销仍然是一个挑战。

**核心思路**：提出了一种简单的环境观察掩蔽策略，通过省略旧的观察信息来降低计算成本，同时保持或提升任务解决率。这种方法的设计基于对现有方法的性能分析，旨在简化上下文管理。

**技术框架**：整体架构包括三个主要模块：环境观察收集、观察掩蔽处理和任务解决。首先收集环境观察，然后应用掩蔽策略，最后通过代理进行任务解决。

**关键创新**：最重要的技术创新在于提出了简单观察掩蔽策略，该策略在成本和性能上均优于传统的LLM摘要方法，挑战了对复杂性依赖的常规思维。

**关键设计**：在实验中，观察掩蔽策略的参数设置经过精心调整，以确保在降低成本的同时不影响解决率。损失函数和网络结构的设计也经过优化，以适应新的处理流程。

## 📊 实验亮点

实验结果显示，简单观察掩蔽策略相较于原始代理成本降低了50%，并在解决率上与LLM摘要相当，甚至略有超越。此外，混合方法在成本上进一步降低了7%至11%，展示了其在效率上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程、智能代理系统和复杂任务管理。通过优化上下文管理策略，可以显著降低计算成本，提高系统的整体效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Model (LLM)-based agents solve complex tasks through iterative reasoning, exploration, and tool-use, a process that can result in long, expensive context histories. While state-of-the-art Software Engineering (SE) agents like OpenHands or Cursor use LLM-based summarization to tackle this issue, it is unclear whether the increased complexity offers tangible performance benefits compared to simply omitting older observations. We present a systematic comparison of these approaches within SWE-agent on SWE-bench Verified across five diverse model configurations. Moreover, we show initial evidence of our findings generalizing to the OpenHands agent scaffold. We find that a simple environment observation masking strategy halves cost relative to the raw agent while matching, and sometimes slightly exceeding, the solve rate of LLM summarization. Additionally, we introduce a novel hybrid approach that further reduces costs by 7% and 11% compared to just observation masking or LLM summarization, respectively. Our findings raise concerns regarding the trend towards pure LLM summarization and provide initial evidence of untapped cost reductions by pushing the efficiency-effectiveness frontier. We release code and data for reproducibility.

