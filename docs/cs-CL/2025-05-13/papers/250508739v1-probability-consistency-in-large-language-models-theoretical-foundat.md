---
layout: default
title: Probability Consistency in Large Language Models: Theoretical Foundations Meet Empirical Discrepancies
---

# Probability Consistency in Large Language Models: Theoretical Foundations Meet Empirical Discrepancies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08739" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08739v1</a>
  <a href="https://arxiv.org/pdf/2505.08739.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08739v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08739v1', 'Probability Consistency in Large Language Models: Theoretical Foundations Meet Empirical Discrepancies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoliang Luo, Xinyi Xu, Michael Ramscar, Bradley C. Love

**分类**: cs.CL

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出一致性概率学习方法以解决LLMs的偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `概率分布` `自回归模型` `位置偏见` `自注意力机制` `实验评估` `模型一致性`

## 📋 核心要点

1. 现有研究未能有效评估LLMs在不同令牌顺序下学习概率分布的一致性，导致方法论缺陷。
2. 论文提出了一种理论基础，证明序列困惑度在不同排列下不变，并定义了经验评估协议。
3. 实验结果表明，GPT-2模型在不同顺序下的训练存在系统性偏差，揭示了自注意力机制中的位置偏见。

## 📝 摘要（中文）

本研究探讨自回归大型语言模型（LLMs）在不同令牌顺序下是否能够学习一致的概率分布。我们正式证明，对于任何良定义的概率分布，序列困惑度在任何因式分解下都是不变的，包括前向、后向或任意排列。这一结果为研究LLMs如何从数据中学习奠定了严格的理论基础，并定义了经验评估的原则性协议。通过应用这些协议，我们发现先前研究在排序效应的考察中存在关键的 методологические недостатки。我们对GPT-2模型进行了重新训练，结果显示在所有顺序中都存在系统性偏差，任意排列的模型与前向和后向模型之间的偏差显著，尽管它们在很大程度上（但并非完全）一致。这些偏差可追溯到自注意力机制中的位置和局部性偏见。我们的理论和实证结果为理解LLMs中的位置偏见提供了新思路，并提出了检测LLMs概率分布不一致的方法。

## 🔬 方法详解

**问题定义**：本研究旨在解决自回归大型语言模型在不同令牌顺序下学习概率分布一致性的问题。现有方法未能有效识别和评估这种一致性，导致模型在实际应用中的不可靠性。

**核心思路**：论文通过理论证明序列困惑度在不同排列下保持不变，建立了LLMs学习过程的理论基础，并提出了系统的经验评估协议，以检测模型的概率分布一致性。

**技术框架**：研究首先定义了概率分布的一致性，然后通过重新训练GPT-2模型，分别在前向、后向和任意排列的顺序下进行实验，比较不同模型的表现。

**关键创新**：本研究的创新在于提供了一个理论框架，证明了序列困惑度的不变性，并通过系统的实验验证了这一理论，揭示了LLMs在处理不同顺序时的偏差。

**关键设计**：在实验中，采用了不同的训练顺序和自注意力机制，重点分析了位置和局部性偏见对模型输出的一致性影响。

## 📊 实验亮点

实验结果显示，在不同的训练顺序下，GPT-2模型表现出系统性偏差，任意排列模型的输出与前向和后向模型之间存在显著差异。这些发现强调了自注意力机制中的位置偏见，提供了对模型一致性的重要见解。

## 🎯 应用场景

该研究为大型语言模型的训练和评估提供了新的理论基础和方法论，具有广泛的应用潜力，尤其是在自然语言处理、机器翻译和文本生成等领域。通过识别和修正模型中的偏差，可以提高模型的可靠性和可信度，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Can autoregressive large language models (LLMs) learn consistent probability distributions when trained on sequences in different token orders? We prove formally that for any well-defined probability distribution, sequence perplexity is invariant under any factorization, including forward, backward, or arbitrary permutations. This result establishes a rigorous theoretical foundation for studying how LLMs learn from data and defines principled protocols for empirical evaluation. Applying these protocols, we show that prior studies examining ordering effects suffer from critical methodological flaws. We retrain GPT-2 models across forward, backward, and arbitrary permuted orders on scientific text. We find systematic deviations from theoretical invariance across all orderings with arbitrary permutations strongly deviating from both forward and backward models, which largely (but not completely) agreed with one another. Deviations were traceable to differences in self-attention, reflecting positional and locality biases in processing. Our theoretical and empirical results provide novel avenues for understanding positional biases in LLMs and suggest methods for detecting when LLMs' probability distributions are inconsistent and therefore untrustworthy.

