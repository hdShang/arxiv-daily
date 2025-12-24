---
layout: default
title: WirelessMathBench: A Mathematical Modeling Benchmark for LLMs in Wireless Communications
---

# WirelessMathBench: A Mathematical Modeling Benchmark for LLMs in Wireless Communications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14354" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14354v1</a>
  <a href="https://arxiv.org/pdf/2505.14354.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14354v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14354v1', 'WirelessMathBench: A Mathematical Modeling Benchmark for LLMs in Wireless Communications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Li, Mengbing Liu, Li Wei, Jiancheng An, Mérouane Debbah, Chau Yuen

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-20

**备注**: Accepted to ACL 2025 Findings

---

## 💡 一句话要点

**提出WirelessMathBench以评估LLMs在无线通信中的数学建模能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `无线通信` `数学建模` `评估基准` `方程补全` `深度学习` `工程应用`

## 📋 核心要点

1. 现有的LLMs在复杂的数学推理，尤其是无线通信领域表现不佳，缺乏有效的评估基准。
2. 本文提出WirelessMathBench基准，专注于无线通信中的数学建模挑战，包含多种类型的问题。
3. 实验结果显示，当前LLMs在复杂方程补全任务中的表现有限，最高准确率仅为38.05%。

## 📝 摘要（中文）

大型语言模型（LLMs）在多种任务中取得了显著成果，但在复杂的领域特定数学推理，尤其是无线通信方面的能力仍未得到充分探索。本文介绍了WirelessMathBench，这是一个专门设计的基准，用于评估LLMs在无线通信工程中的数学建模挑战。该基准包含来自40篇前沿研究论文的587个精心策划的问题，涵盖从基本的选择题到复杂的方程补全任务，所有问题都严格遵循物理和维度约束。通过对领先的LLMs进行广泛实验，我们发现尽管许多模型在基本回忆任务中表现良好，但在重建部分或完全遮蔽的方程时性能显著下降，暴露了当前LLMs的基本局限性。即使是表现最佳的DeepSeek-R1，在我们的基准上平均准确率也仅为38.05%，完全方程补全的成功率仅为7.83%。通过公开发布WirelessMathBench及评估工具包，我们旨在推动更强大、领域感知的LLMs在无线系统分析和更广泛工程应用中的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在无线通信领域的数学建模能力不足的问题。现有方法在处理复杂数学推理时表现不佳，缺乏针对性的评估工具。

**核心思路**：论文提出WirelessMathBench基准，通过精心设计的问题集来评估LLMs在无线通信中的数学建模能力，特别关注方程补全任务的表现。

**技术框架**：WirelessMathBench包含587个问题，涵盖从基础选择题到复杂方程补全的多种任务，所有问题均遵循物理和维度约束。评估工具包与基准一同发布，便于研究者使用。

**关键创新**：该基准的创新之处在于其专注于无线通信领域的数学建模，填补了现有LLMs评估工具的空白，提供了针对性强的评估标准。

**关键设计**：问题设计涵盖基本和复杂任务，确保了多样性和挑战性。实验中使用的评估指标包括准确率和成功率，特别关注方程的部分和完全补全任务。

## 📊 实验亮点

实验结果显示，尽管许多LLMs在基本任务中表现良好，但在复杂方程补全任务中，DeepSeek-R1的平均准确率仅为38.05%，完全方程补全的成功率仅为7.83%。这些结果揭示了当前模型在处理复杂数学问题时的局限性。

## 🎯 应用场景

WirelessMathBench的潜在应用领域包括无线通信系统的分析与优化、工程教育中的数学建模训练，以及推动更强大LLMs的研究与开发。该基准的发布将促进学术界和工业界在无线通信领域的进一步探索与应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved impressive results across a broad array of tasks, yet their capacity for complex, domain-specific mathematical reasoning-particularly in wireless communications-remains underexplored. In this work, we introduce WirelessMathBench, a novel benchmark specifically designed to evaluate LLMs on mathematical modeling challenges to wireless communications engineering. Our benchmark consists of 587 meticulously curated questions sourced from 40 state-of-the-art research papers, encompassing a diverse spectrum of tasks ranging from basic multiple-choice questions to complex equation completion tasks, including both partial and full completions, all of which rigorously adhere to physical and dimensional constraints. Through extensive experimentation with leading LLMs, we observe that while many models excel in basic recall tasks, their performance degrades significantly when reconstructing partially or fully obscured equations, exposing fundamental limitations in current LLMs. Even DeepSeek-R1, the best performer on our benchmark, achieves an average accuracy of only 38.05%, with a mere 7.83% success rate in full equation completion. By publicly releasing WirelessMathBench along with the evaluation toolkit, we aim to advance the development of more robust, domain-aware LLMs for wireless system analysis and broader engineering applications.

