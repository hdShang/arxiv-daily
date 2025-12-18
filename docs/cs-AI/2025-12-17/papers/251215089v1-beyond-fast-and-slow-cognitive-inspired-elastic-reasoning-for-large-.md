---
layout: default
title: Beyond Fast and Slow: Cognitive-Inspired Elastic Reasoning for Large Language Models
---

# Beyond Fast and Slow: Cognitive-Inspired Elastic Reasoning for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15089" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15089v1</a>
  <a href="https://arxiv.org/pdf/2512.15089.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15089v1" onclick="toggleFavorite(this, '2512.15089v1', 'Beyond Fast and Slow: Cognitive-Inspired Elastic Reasoning for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinwu Hu, Dongjin Yang, Langyu Bian, Zhiquan Wen, Yufeng Wang, Yaofo Chen, Bin Xiao, Yuanqing Li, Mingkui Tan

**分类**: cs.AI

**发布日期**: 2025-12-17

**备注**: under review

---

## 💡 一句话要点

**提出CogER框架，通过认知启发的弹性推理提升大语言模型在不同难度问题上的效率与准确性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `弹性推理` `认知启发` `强化学习` `工具调用`

## 📋 核心要点

1. 现有大语言模型推理策略难以兼顾效率与精度，无法根据问题难度动态调整推理模式。
2. CogER框架模拟人类分层推理，通过评估问题难度，动态选择最优推理策略，实现资源高效利用。
3. 实验结果表明，CogER在领域内和领域外任务上均显著优于现有方法，提升效果明显。

## 📝 摘要（中文）

大型语言模型（LLMs）在各种语言任务中表现出了令人印象深刻的性能。然而，现有的LLM推理策略主要依赖于LLM自身，采用快速或慢速模式（如o1思维），因此难以在不同难度的查询中平衡推理效率和准确性。本文提出了认知启发的弹性推理（CogER）框架，该框架受到人类分层推理的启发，能够为每个查询动态选择最合适的推理策略。具体来说，CogER首先评估输入查询的复杂性，并将其分配到几个预定义的级别之一，每个级别对应于量身定制的处理策略，从而解决不可观察的查询难度带来的挑战。为了实现自动策略选择，我们将该过程建模为马尔可夫决策过程，并使用强化学习训练CogER-Agent。该Agent由平衡解决方案质量和计算成本的奖励函数引导，确保资源高效的推理。此外，对于需要外部工具的查询，我们引入了认知工具辅助推理，使LLM能够在思维链中自主调用外部工具。大量实验表明，CogER优于最先进的测试时缩放方法，在领域内任务上的平均精确匹配率至少提高了13%，在领域外任务上的平均精确匹配率至少提高了8%。

## 🔬 方法详解

**问题定义**：现有的大语言模型推理方法，例如快速模式和慢速模式，无法根据问题的难度自适应地调整推理策略。对于简单的问题，慢速模式会浪费计算资源；而对于复杂的问题，快速模式则难以保证准确性。因此，需要一种能够根据问题难度动态选择推理策略的方法，以在效率和准确性之间取得平衡。

**核心思路**：CogER的核心思路是模拟人类的认知过程，将推理过程分为多个层次，每个层次对应不同的推理策略。首先，评估输入问题的难度，然后根据难度级别选择相应的推理策略。对于需要外部工具的问题，CogER还能够自主调用外部工具进行辅助推理。这种分层和自适应的推理方式能够有效地提高推理效率和准确性。

**技术框架**：CogER框架主要包含以下几个模块：1) 难度评估模块：用于评估输入问题的难度级别。2) 策略选择模块：根据难度级别选择相应的推理策略。3) 推理执行模块：执行选定的推理策略，并生成答案。4) 认知工具辅助推理模块：对于需要外部工具的问题，该模块负责调用外部工具进行辅助推理。整个过程被建模成马尔可夫决策过程，使用强化学习训练一个CogER-Agent来自动选择策略。

**关键创新**：CogER的关键创新在于其认知启发的弹性推理机制。与现有的方法相比，CogER能够根据问题的难度动态选择推理策略，从而在效率和准确性之间取得更好的平衡。此外，CogER还引入了认知工具辅助推理，使LLM能够自主调用外部工具进行辅助推理，进一步提高了推理能力。

**关键设计**：难度评估模块可以使用各种机器学习模型，例如分类器或回归器，来预测问题的难度级别。策略选择模块可以使用强化学习算法，例如Q-learning或Policy Gradient，来训练一个Agent，使其能够根据问题的难度级别选择最优的推理策略。奖励函数的设计至关重要，需要平衡解决方案的质量和计算成本。认知工具辅助推理模块需要定义一套API，用于调用各种外部工具。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15089v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CogER在领域内任务上的平均精确匹配率至少提高了13%，在领域外任务上的平均精确匹配率至少提高了8%，显著优于现有的测试时缩放方法。这些结果表明，CogER框架能够有效地提高大语言模型在不同难度问题上的推理能力。

## 🎯 应用场景

CogER框架可应用于各种需要大语言模型进行推理的场景，例如问答系统、机器翻译、文本摘要、代码生成等。通过动态调整推理策略，CogER能够提高推理效率和准确性，降低计算成本，从而提升用户体验和系统性能。该研究对于推动大语言模型在实际应用中的普及具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated impressive performance across various language tasks. However, existing LLM reasoning strategies mainly rely on the LLM itself with fast or slow mode (like o1 thinking) and thus struggle to balance reasoning efficiency and accuracy across queries of varying difficulties. In this paper, we propose Cognitive-Inspired Elastic Reasoning (CogER), a framework inspired by human hierarchical reasoning that dynamically selects the most suitable reasoning strategy for each query. Specifically, CogER first assesses the complexity of incoming queries and assigns them to one of several predefined levels, each corresponding to a tailored processing strategy, thereby addressing the challenge of unobservable query difficulty. To achieve automatic strategy selection, we model the process as a Markov Decision Process and train a CogER-Agent using reinforcement learning. The agent is guided by a reward function that balances solution quality and computational cost, ensuring resource-efficient reasoning. Moreover, for queries requiring external tools, we introduce Cognitive Tool-Assisted Reasoning, which enables the LLM to autonomously invoke external tools within its chain-of-thought. Extensive experiments demonstrate that CogER outperforms state-of-the-art Test-Time scaling methods, achieving at least a 13% relative improvement in average exact match on In-Domain tasks and an 8% relative gain on Out-of-Domain tasks.

