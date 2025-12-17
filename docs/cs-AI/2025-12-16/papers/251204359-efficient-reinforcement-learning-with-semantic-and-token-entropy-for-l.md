---
layout: default
title: Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning
---

# Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04359" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04359</a>
  <a href="https://arxiv.org/pdf/2512.04359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04359" onclick="toggleFavorite(this, '2512.04359', 'Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongye Cao, Zhixin Bai, Ziyue Peng, Boyan Wang, Tianpei Yang, Jing Huo, Yuyao Zhang, Yang Gao

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于语义和Token熵的强化学习框架，提升LLM推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `推理能力` `熵正则化` `课程学习`

## 📋 核心要点

1. 现有基于可验证奖励的强化学习方法易出现熵坍塌，限制了策略探索和推理能力。
2. 提出一种利用语义和Token熵信号的强化学习框架，从数据和算法层面缓解熵坍塌。
3. 实验表明，该方法在多个基准测试中优于其他基于熵的方法，提升了LLM推理能力。

## 📝 摘要（中文）

本文提出了一种高效的强化学习框架，该框架利用语义和Token层面的熵信号来提升大型语言模型（LLM）的推理能力。针对现有基于可验证奖励的强化学习（RLVR）方法中存在的熵坍塌问题，本文从数据和算法两个角度入手。在数据层面，引入了语义熵引导的课程学习，按照语义熵从小到大的顺序组织训练数据，引导模型从易到难地进行优化。在算法层面，采用非均匀的Token处理方式，对低熵Token施加KL正则化，并对这些Token内的高协方差部分施加更强的约束，以促进策略探索。通过联合优化数据组织和算法设计，有效缓解了熵坍塌问题，提升了LLM的推理能力。在6个基准测试和3个不同参数规模的基础模型上的实验结果表明，本文方法优于其他基于熵的方法。

## 🔬 方法详解

**问题定义**：现有基于可验证奖励的强化学习（RLVR）方法在提升大型语言模型（LLM）推理能力方面表现出色，但常常面临熵坍塌的问题。熵坍塌会导致策略探索不足，从而限制了LLM的推理能力。现有方法难以有效平衡探索与利用，导致模型容易陷入局部最优解。

**核心思路**：本文的核心思路是通过引入语义和Token层面的熵信号来促进策略探索，缓解熵坍塌。具体而言，从数据层面，利用语义熵引导课程学习，让模型先学习简单的任务，再逐步学习复杂的任务。从算法层面，对不同熵值的Token采取不同的处理方式，对低熵Token进行正则化，以鼓励探索。

**技术框架**：该框架包含两个主要组成部分：语义熵引导的课程学习和非均匀Token处理的强化学习算法。首先，计算训练数据的语义熵，并按照语义熵从小到大的顺序组织数据。然后，使用强化学习算法训练LLM，在训练过程中，对低熵Token施加KL正则化，并对这些Token内的高协方差部分施加更强的约束。整体流程是从简单到复杂地训练模型，同时鼓励模型探索不同的策略。

**关键创新**：本文的关键创新在于联合优化数据组织和算法设计，利用语义熵和Token熵两种信息来缓解熵坍塌。与现有方法相比，本文方法不仅考虑了数据的难度，还考虑了Token的重要性，从而更有效地促进了策略探索。非均匀Token处理是另一个创新点，它允许对不同的Token采取不同的处理方式，从而更精细地控制策略的探索。

**关键设计**：语义熵的计算方式未知，但应该是基于某种语义表示的距离或差异性。KL正则化的系数需要根据实验进行调整，以平衡探索和利用。对低熵Token内的高协方差部分施加更强的约束的具体实现方式未知，可能涉及到对损失函数的修改或对网络结构的调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.04359/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.04359/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.04359/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，本文方法在6个基准测试中优于其他基于熵的方法。具体而言，在某些基准测试中，本文方法相比于基线方法取得了显著的性能提升，例如在XXX数据集上提升了X%。此外，实验还验证了语义熵引导的课程学习和非均匀Token处理的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要LLM进行复杂推理的场景，例如问答系统、对话生成、代码生成等。通过提升LLM的推理能力，可以提高这些应用的准确性和可靠性。此外，该方法还可以用于训练其他类型的语言模型，提升其在各种任务上的表现。未来，该方法有望推动LLM在更多领域的应用。

## 📄 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has demonstrated superior performance in enhancing the reasoning capability of large language models (LLMs). However, this accuracy-oriented learning paradigm often suffers from entropy collapse, which reduces policy exploration and limits reasoning capabilities. To address this challenge, we propose an efficient reinforcement learning framework that leverages entropy signals at both the semantic and token levels to improve reasoning. From the data perspective, we introduce semantic entropy-guided curriculum learning, organizing training data from low to high semantic entropy to guide progressive optimization from easier to more challenging tasks. For the algorithmic design, we adopt non-uniform token treatment by imposing KL regularization on low-entropy tokens that critically impact policy exploration and applying stronger constraints on high-covariance portions within these tokens. By jointly optimizing data organization and algorithmic design, our method effectively mitigates entropy collapse and enhances LLM reasoning. Experimental results across 6 benchmarks with 3 different parameter-scale base models demonstrate that our method outperforms other entropy-based approaches in improving reasoning.

