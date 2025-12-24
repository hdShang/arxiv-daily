---
layout: default
title: "REFINESTAT: Efficient Exploration for Probabilistic Program Synthesis"
---

# REFINESTAT: Efficient Exploration for Probabilistic Program Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01082" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01082v1</a>
  <a href="https://arxiv.org/pdf/2509.01082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01082v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01082v1', 'REFINESTAT: Efficient Exploration for Probabilistic Program Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Madhav Kanda, Shubham Ugare, Sasa Misailovic

**分类**: cs.LG, cs.PL

**发布日期**: 2025-09-01

**备注**: RefineStat constrains LM decoding with statistical validity checks and uses diagnostic-guided resampling (priors/likelihoods) to transform small LMs' drafts into correct, reliable probabilistic programs that can match or surpass closed-source models

---

## 💡 一句话要点

**提出RefineStat以解决概率程序合成中的语义约束问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `概率编程` `程序合成` `语义约束` `模型细化` `小型语言模型`

## 📋 核心要点

1. 现有的小型语言模型在生成概率程序时，常常出现语法和语义错误，导致生成的程序不可靠。
2. RefineStat通过引入语义约束和诊断感知的细化机制，确保合成程序的有效性和可靠性。
3. 实验表明，RefineStat在多个代码生成任务中表现优异，生成的程序在语法和统计上均优于现有大型语言模型。

## 📝 摘要（中文）

概率编程为建模不确定性提供了强大的框架，但在该领域进行统计模型发现时，需要在严格的领域特定约束下导航巨大的搜索空间。当小型语言模型生成概率程序时，常常会产生语法和语义错误。为了解决这一问题，本文提出了RefineStat，一个驱动于语言模型的框架，强制执行语义约束，确保合成的程序包含有效的分布和良构的参数，并在可靠性检查失败时通过重新采样先验或似然组件进行诊断感知的细化。实验结果表明，RefineStat在多个概率编程代码生成任务中表现出色，生成的程序在语法和统计上都可靠，常常超过闭源大型语言模型的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决概率程序合成中生成程序的语法和语义错误问题。现有方法在生成过程中缺乏有效的语义约束，导致生成的程序不可靠。

**核心思路**：RefineStat的核心思想是通过引入语义约束来确保生成程序的有效性，并在程序生成后进行诊断感知的细化，以修正潜在的错误。这样的设计使得生成的程序在语法和统计上都更为可靠。

**技术框架**：RefineStat的整体架构包括两个主要模块：语义约束模块和细化模块。语义约束模块负责确保生成程序的有效性，而细化模块则在发现错误时进行重新采样和修正。

**关键创新**：RefineStat的主要创新在于引入了语义约束和诊断感知的细化机制，这与现有方法的随机生成方式形成了鲜明对比，显著提高了生成程序的质量。

**关键设计**：在参数设置上，RefineStat使用了特定的损失函数来评估程序的有效性，并设计了适应性强的网络结构，以便在不同的生成任务中保持高效性和准确性。

## 📊 实验亮点

实验结果显示，RefineStat在多个概率编程代码生成任务中，生成的程序在语法和统计上均表现优异，常常与大型闭源语言模型（如OpenAI o3）相媲美，甚至在某些任务中超越了它们，展示了显著的性能提升。

## 🎯 应用场景

RefineStat的潜在应用场景包括自动化数据分析、机器学习模型的生成和优化，以及复杂系统的建模等领域。其实际价值在于能够提高程序生成的可靠性，降低人工干预的需求，未来可能推动智能编程助手的发展。

## 📄 摘要（原文）

> Probabilistic programming offers a powerful framework for modeling uncertainty, yet statistical model discovery in this domain entails navigating an immense search space under strict domain-specific constraints. When small language models are tasked with generating probabilistic programs, they frequently produce outputs that suffer from both syntactic and semantic errors, such as flawed inference constructs. Motivated by probabilistic programmers' domain expertise and debugging strategies, we introduce RefineStat, a language model--driven framework that enforces semantic constraints ensuring synthesized programs contain valid distributions and well-formed parameters, and then applies diagnostic-aware refinement by resampling prior or likelihood components whenever reliability checks fail. We evaluate RefineStat on multiple probabilistic-programming code-generation tasks using smaller language models (SLMs) and find that it produces programs that are both syntactically sound and statistically reliable, often matching or surpassing those from closed-source large language models (e.g., OpenAI o3).

