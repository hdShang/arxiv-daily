---
layout: default
title: Scaling Laws for State Dynamics in Large Language Models
---

# Scaling Laws for State Dynamics in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14892" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14892v1</a>
  <a href="https://arxiv.org/pdf/2505.14892.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14892v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14892v1', 'Scaling Laws for State Dynamics in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jacob X Li, Shreyas S Raman, Jessica Wan, Fahad Samman, Jazlyn Lin

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20

**备注**: 16 pages; 23 figures

---

## 💡 一句话要点

**探讨大语言模型状态动态的规模法则**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `状态动态` `激活补丁` `注意力机制` `状态跟踪`

## 📋 核心要点

1. 现有的大语言模型在状态动态建模方面的能力尚不明确，尤其是在复杂任务中表现不佳。
2. 论文通过评估LLMs在多个领域的状态动态捕捉能力，提出了激活补丁的方法来识别关键的注意力头。
3. 实验结果显示，GPT-2 XL和Pythia-1B在状态数量增加时准确率显著下降，揭示了状态跟踪的局限性。

## 📝 摘要（中文）

大语言模型（LLMs）在需要内部状态跟踪的任务中越来越多地被使用，但它们对状态转移动态的建模能力仍然不够清晰。本文评估了LLMs在三个领域（盒子跟踪、抽象DFA序列和复杂文本游戏）中捕捉确定性状态动态的能力。研究发现，随着状态空间大小和稀疏转移的增加，下一状态预测的准确性下降。GPT-2 XL在低复杂度设置下的准确率约为70%，但当盒子或状态数量超过5或10时，准确率降至30%以下。在DFA任务中，Pythia-1B在状态数量超过10且转移少于30时，准确率未能超过50%。通过激活补丁，我们识别出负责传播状态信息的注意力头，表明LLMs的状态跟踪是通过下一标记头的分布式交互而非显式符号计算实现的。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在状态动态建模中的不足，尤其是在状态空间增大时预测准确性下降的问题。现有方法未能有效捕捉复杂状态转移的动态特性。

**核心思路**：论文提出通过激活补丁技术识别出在状态信息传播中起关键作用的注意力头，进而分析其在状态跟踪中的表现。这样的设计旨在揭示LLMs在状态动态建模中的潜在机制。

**技术框架**：研究分为三个主要部分：首先是对不同任务（盒子跟踪、DFA序列、复杂文本游戏）的状态动态进行评估；其次是通过激活补丁技术识别关键注意力头；最后是分析这些头在状态信息传播中的作用。

**关键创新**：最重要的创新在于通过激活补丁识别出特定的注意力头，这些头在状态信息的传播中起到了重要作用，而不是依赖于传统的符号计算方法。

**关键设计**：在实验中，使用了不同的状态数量和转移稀疏度设置，以评估模型的表现。同时，关注了GPT-2 XL的第22层第20个头和Pythia-1B的第10、11、12和14层的头的激活情况。通过这些设计，研究揭示了LLMs在状态跟踪中的局限性。

## 📊 实验亮点

实验结果显示，GPT-2 XL在低复杂度设置下的准确率达到70%，但当状态数量超过5时，准确率降至30%以下。Pythia-1B在状态数量超过10且转移少于30时，准确率未能超过50%，揭示了状态跟踪的显著挑战。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、游戏AI和自动化决策系统等。通过深入理解大语言模型的状态动态，能够提升其在复杂任务中的表现，从而推动更智能的交互和决策支持系统的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly used in tasks requiring internal state tracking, yet their ability to model state transition dynamics remains poorly understood. We evaluate how well LLMs capture deterministic state dynamics across 3 domains: Box Tracking, Abstract DFA Sequences, and Complex Text Games, each formalizable as a finite-state system. Across tasks, we find that next-state prediction accuracy degrades with increasing state-space size and sparse transitions. GPT-2 XL reaches about 70% accuracy in low-complexity settings but drops below 30% when the number of boxes or states exceeds 5 or 10, respectively. In DFA tasks, Pythia-1B fails to exceed 50% accuracy when the number of states is > 10 and transitions are < 30. Through activation patching, we identify attention heads responsible for propagating state information: GPT-2 XL Layer 22 Head 20, and Pythia-1B Heads at Layers 10, 11, 12, and 14. While these heads successfully move relevant state features, action information is not reliably routed to the final token, indicating weak joint state-action reasoning. Our results suggest that state tracking in LLMs emerges from distributed interactions of next-token heads rather than explicit symbolic computation.

