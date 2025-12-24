---
layout: default
title: "FormaRL: Enhancing Autoformalization with no Labeled Data"
---

# FormaRL: Enhancing Autoformalization with no Labeled Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18914" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18914v1</a>
  <a href="https://arxiv.org/pdf/2508.18914.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18914v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18914v1', 'FormaRL: Enhancing Autoformalization with no Labeled Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanxing Huang, Xinling Jin, Sijie Liang, Peng Li, Yang Liu

**分类**: cs.AI

**发布日期**: 2025-08-26

**备注**: Conference paper at COLM2025

**🔗 代码/项目**: [GITHUB](https://github.com/THUNLP-MT/FormaRL)

---

## 💡 一句话要点

**提出FormaRL以解决自动形式化数据稀缺问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动形式化` `强化学习` `数据稀缺` `形式验证` `定理证明` `数学教育` `无标注数据`

## 📋 核心要点

1. 现有的自动形式化方法受限于标注数据的稀缺，导致其性能提升缓慢。
2. FormaRL通过强化学习框架，利用少量未标记数据进行自动形式化，结合语法和一致性检查来优化过程。
3. 实验结果显示，FormaRL在多个基准测试中显著提升了自动形式化的准确率，尤其是在out-of-distribution性能上表现优异。

## 📝 摘要（中文）

自动形式化是形式验证中的核心任务，但由于数据稀缺和缺乏有效方法，其进展受到限制。本文提出了FormaRL，一个简单而高效的强化学习框架，仅需少量未标记数据。FormaRL结合了Lean编译器的语法检查和大型语言模型的一致性检查来计算奖励，并采用GRPO算法更新形式化器。我们还从本科数学材料中整理了一个名为uproof的证明问题数据集，以促进自动形式化和高级数学中的定理证明的探索。实验表明，FormaRL能将Qwen2.5-Coder-7B-Instruct的pass@1自动形式化准确率提高4至6倍。

## 🔬 方法详解

**问题定义**：自动形式化任务在形式验证中至关重要，但现有方法依赖大量标注数据，导致数据稀缺时性能受限。

**核心思路**：FormaRL通过强化学习框架，利用少量未标记数据，结合Lean编译器的语法检查和大型语言模型的一致性检查来计算奖励，从而优化自动形式化过程。

**技术框架**：FormaRL的整体架构包括数据输入模块、奖励计算模块和形式化器更新模块。数据输入模块负责处理未标记数据，奖励计算模块结合语法和一致性检查，形式化器更新模块采用GRPO算法进行优化。

**关键创新**：FormaRL的主要创新在于其能够在没有标注数据的情况下，通过强化学习有效提升自动形式化的准确率，这与传统方法依赖大量标注数据的本质区别显著。

**关键设计**：在设计中，FormaRL使用了GRPO算法进行策略更新，奖励函数结合了语法和一致性检查的结果，确保了形式化过程的高效性和准确性。

## 📊 实验亮点

实验结果显示，FormaRL在ProofNet上将Qwen2.5-Coder-7B-Instruct的pass@1准确率从4.04%提升至26.15%，在uproof上从2.4%提升至9.6%。此外，FormaRL在out-of-distribution性能上也表现出色，pass@1准确率从6.2%提升至9.6%，pass@16准确率从24.4%提升至33.6%。

## 🎯 应用场景

该研究的潜在应用领域包括形式验证、自动定理证明和数学教育等。通过提供一种无需大量标注数据的自动形式化方法，FormaRL可以帮助研究人员和开发者在更广泛的数学问题上进行验证和证明，推动相关领域的发展。

## 📄 摘要（原文）

> Autoformalization is one of the central tasks in formal verification, while its advancement remains hindered due to the data scarcity and the absence efficient methods. In this work we propose \textbf{FormaRL}, a simple yet efficient reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. FormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer. We also curated a proof problem dataset from undergraduate-level math materials, named \textbf{uproof}, in the hope to facilitate the exploration of autoformalization and theorem proving in advanced math. Experiments show that FormaRL can increase the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4 $\sim$ 6x (4.04\% $\to$ 26.15\% on ProofNet and 2.4\% $\to$ 9.6\% on uproof) with merely 859 unlabeled data. And on uproof our method also achieved a strong improvement in out-of-distribution performance compared to existing open-source state-of-the-art autoformalizers on both pass@1 accuracy (6.2\% $\to$ 9.6\%) and pass@16 accuracy (24.4\% $\to$ 33.6\%). Training code of FormaRL is open-sourced at https://github.com/THUNLP-MT/FormaRL.

