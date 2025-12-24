---
layout: default
title: Can Past Experience Accelerate LLM Reasoning?
---

# Can Past Experience Accelerate LLM Reasoning?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20643" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20643v1</a>
  <a href="https://arxiv.org/pdf/2505.20643.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20643v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20643v1', 'Can Past Experience Accelerate LLM Reasoning?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bo Pan, Liang Zhao

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出SpeedupLLM框架以加速大语言模型推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理加速` `自适应计算` `记忆机制` `计算预算`

## 📋 核心要点

1. 现有方法在提升大语言模型推理效果的同时，往往导致推理时间的增加，效率低下。
2. 论文提出SpeedupLLM框架，通过自适应计算分配和记忆机制，系统性地加速LLMs的推理过程。
3. 实验结果表明，使用适当的记忆和推理方法，LLMs的推理速度可提高，计算成本降低56%。

## 📝 摘要（中文）

本论文探讨了大语言模型（LLMs）在推理过程中是否能够通过重复接触相关任务来加快推理速度。研究表明，尽管增加计算资源通常能提高LLMs的有效性，但也会导致推理时间增加。为此，论文提出了SpeedupLLM框架，系统性地定义了推理加速问题，并通过自适应计算分配和记忆机制进行实现与基准测试。实验结果显示，适当的记忆和推理方法可以使LLMs在过去经验的帮助下，推理速度提高，计算成本降低高达56%。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型推理速度提升的问题，现有方法在增加计算资源时，推理时间却未能有效降低，导致效率低下。

**核心思路**：论文提出的核心思路是通过重复接触相关任务来加速推理，借鉴人类通过经验提升效率的方式，设计自适应计算分配和记忆机制。

**技术框架**：SpeedupLLM框架包括任务相关性分析、计算预算计算、记忆方法和推理方法等模块，系统性地实现推理速度的提升。

**关键创新**：最重要的技术创新在于提出了一个理论上有保证的框架，能够有效地实现推理加速，与现有方法相比，强调了记忆机制的重要性。

**关键设计**：在设计中，关键参数包括计算预算的动态调整、记忆方法的选择（如短期记忆和长期记忆），以及推理方法的优化，以确保在不同任务相似性水平下的有效性。

## 📊 实验亮点

实验结果显示，使用SpeedupLLM框架后，LLMs在推理速度上有显著提升，计算成本降低高达56%。在不同问题相似性水平和记忆方法的测试中，均表现出优越的性能，验证了框架的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和人机交互等。通过加速大语言模型的推理过程，可以显著提升这些应用的响应速度和用户体验，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Allocating more compute to large language models (LLMs) reasoning has generally been demonstrated to improve their effectiveness, but also results in increased inference time. In contrast, humans can perform tasks faster and better with increased experience and exposure. Hence, this paper aims to investigate the question: Can LLMs also become faster at reasoning through recurrent exposure on relevant tasks, and if so, how can it be achieved? To address these questions, we first formalize the problem setting of LLM reasoning speedup systematically in the dimensions of task relevancy and compute budget calculation. We then propose SpeedupLLM, a theoretically guaranteed framework to implement and benchmark such reasoning speedup behaviour based on adaptive compute allocation and memory mechanisms. We further conduct comprehensive experiments to benchmark such behaviour across different question similarity levels, memory methods, and reasoning methods. Results show that LLMs can generally reason faster with past experience, achieving up to a 56% reduction in compute cost when equipped with appropriate memory and reasoning methods.

