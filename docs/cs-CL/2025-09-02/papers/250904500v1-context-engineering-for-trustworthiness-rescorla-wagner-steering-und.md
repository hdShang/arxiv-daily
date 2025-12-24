---
layout: default
title: "Context Engineering for Trustworthiness: Rescorla Wagner Steering Under Mixed and Inappropriate Contexts"
---

# Context Engineering for Trustworthiness: Rescorla Wagner Steering Under Mixed and Inappropriate Contexts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04500" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04500v1</a>
  <a href="https://arxiv.org/pdf/2509.04500.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04500v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04500v1', 'Context Engineering for Trustworthiness: Rescorla Wagner Steering Under Mixed and Inappropriate Contexts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rushi Wang, Jiateng Liu, Cheng Qian, Yifan Shen, Yanzhou Pan, Zhaozhuo Xu, Ahmed Abbasi, Heng Ji, Denghui Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-02

**备注**: 36 pages, 7 figures

---

## 💡 一句话要点

**提出RW-Steering，通过上下文工程提升LLM在混合和不当上下文中的可信度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `上下文工程` `可信度` `Rescorla-Wagner模型` `微调` `混合上下文` `不当内容` `安全性`

## 📋 核心要点

1. 现有LLM在真实世界中面临混合上下文的挑战，其中少量不当内容会显著降低响应质量。
2. 论文提出RW-Steering方法，通过微调使模型能够识别并忽略不当上下文信号，提升模型鲁棒性。
3. 实验表明，RW-Steering能显著提高LLM在混合上下文中的响应质量，提升幅度达39.8%。

## 📝 摘要（中文）

本文研究了大型语言模型（LLM）在包含相关和不当内容的混合上下文中的处理和优先级排序方式。为此，作者提出了一个名为“中毒上下文测试平台”（Poisoned Context Testbed）的测试基准，将查询与包含相关和不当内容的真实世界上下文配对。受动物联想学习的启发，作者将神经科学中的Rescorla-Wagner（RW）模型进行调整，以量化竞争性上下文信号如何影响LLM的输出。结果表明，LLM倾向于整合上下文中不太普遍的信息。为了解决这个问题，作者提出了一种基于两阶段微调的方法RW-Steering，使模型能够在内部识别和忽略不适当的信号。实验表明，RW-Steering能够显著提高LLM在真实世界场景中的安全性，最佳微调模型将响应质量提高了39.8%。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在真实场景中，由于上下文包含少量不当信息而导致输出质量下降的问题。现有方法通常依赖于大量监督数据，且泛化能力较弱，无法有效处理不同比例的不当内容。

**核心思路**：论文的核心思路是借鉴神经科学中的Rescorla-Wagner (RW) 模型，模拟LLM对上下文信息的学习和权重分配过程。通过调整模型内部对不同上下文信号的敏感度，使其能够识别并抑制不当信息的影响，从而提高输出质量。

**技术框架**：RW-Steering方法包含两个主要阶段：首先，使用中毒上下文测试平台（Poisoned Context Testbed）评估LLM对混合上下文的敏感度，并利用RW模型量化不同上下文信号的影响。然后，通过两阶段微调，使模型学习区分和忽略不当信号。第一阶段侧重于识别不当内容，第二阶段则优化模型在忽略不当内容后的响应质量。

**关键创新**：RW-Steering的关键创新在于其基于神经科学的建模方法和两阶段微调策略。与传统的依赖大量监督数据的微调方法不同，RW-Steering能够更有效地利用少量数据，并具有更好的泛化能力，可以适应不同比例的不当内容。

**关键设计**：RW-Steering的关键设计包括：1) Poisoned Context Testbed的构建，用于评估LLM对混合上下文的敏感度；2) RW模型的适配，用于量化不同上下文信号的影响；3) 两阶段微调策略，第一阶段使用对比学习损失，鼓励模型区分适当和不当内容，第二阶段使用标准语言模型损失，优化模型在忽略不当内容后的响应质量。

## 📊 实验亮点

实验结果表明，RW-Steering方法能够显著提高LLM在混合上下文中的响应质量，最佳微调模型将响应质量提高了39.8%。此外，RW-Steering还能够逆转LLM对少量不当内容的过度敏感行为，使其能够更有效地忽略不当信息，从而提高模型的鲁棒性和安全性。该方法在不同比例的不当内容下均表现出良好的泛化能力。

## 🎯 应用场景

该研究成果可应用于各种需要LLM处理复杂、可能包含噪声或不当信息的真实世界场景，例如在线客服、内容审核、信息检索等。通过提高LLM在这些场景下的可靠性和安全性，可以降低错误信息传播的风险，提升用户体验，并为LLM的更广泛应用奠定基础。

## 📄 摘要（原文）

> Incorporating external context can significantly enhance the response quality of Large Language Models (LLMs). However, real-world contexts often mix relevant information with disproportionate inappropriate content, posing reliability risks. How do LLMs process and prioritize mixed context? To study this, we introduce the Poisoned Context Testbed, pairing queries with real-world contexts containing relevant and inappropriate content. Inspired by associative learning in animals, we adapt the Rescorla-Wagner (RW) model from neuroscience to quantify how competing contextual signals influence LLM outputs. Our adapted model reveals a consistent behavioral pattern: LLMs exhibit a strong tendency to incorporate information that is less prevalent in the context. This susceptibility is harmful in real-world settings, where small amounts of inappropriate content can substantially degrade response quality. Empirical evaluations on our testbed further confirm this vulnerability. To tackle this, we introduce RW-Steering, a two-stage finetuning-based approach that enables the model to internally identify and ignore inappropriate signals. Unlike prior methods that rely on extensive supervision across diverse context mixtures, RW-Steering generalizes robustly across varying proportions of inappropriate content. Experiments show that our best fine-tuned model improves response quality by 39.8% and reverses the undesirable behavior curve, establishing RW-Steering as a robust, generalizable context engineering solution for improving LLM safety in real-world use.

