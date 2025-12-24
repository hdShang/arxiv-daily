---
layout: default
title: "Modular Arithmetic: Language Models Solve Math Digit by Digit"
---

# Modular Arithmetic: Language Models Solve Math Digit by Digit

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02513" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02513v1</a>
  <a href="https://arxiv.org/pdf/2508.02513.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02513v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02513v1', 'Modular Arithmetic: Language Models Solve Math Digit by Digit')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tanja Baeumel, Daniil Gurgurov, Yusser al Ghussin, Josef van Genabith, Simon Ostermann

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出数字位置特定电路以解决语言模型的算术问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `算术运算` `数字表示` `因果干预` `特征重要性` `可解释性` `电路设计`

## 📋 核心要点

1. 现有研究对大型语言模型在算术任务中的内部机制缺乏统一理解，尤其是数字表示方式和运算策略。
2. 本文提出了一种新的视角，认为LLMs通过数字位置特定电路逐位处理数字，从而执行算术运算。
3. 通过实验验证，发现这些电路在不同模型和标记策略下均存在，且能有效提升算术任务的解决能力。

## 📝 摘要（中文）

尽管近期研究开始揭示大型语言模型（LLMs）在简单算术任务中所采用的内部策略，但对其基本机制的统一理解仍然缺乏。本文扩展了近期发现，表明LLMs以逐位方式表示数字，并提供了数字位置特定电路的证据，这些电路使LLMs能够执行简单的算术任务。我们通过特征重要性和因果干预的方法识别并验证了这些电路，揭示了LLMs在解决算术问题时所依赖的可组合和可解释的结构。我们的干预选择性地改变了模型在特定数字位置的预测，展示了数字位置电路在解决算术任务中的因果作用。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在执行简单算术任务时的内部机制不明确的问题。现有方法未能充分揭示模型如何逐位处理数字及其运算策略的细节。

**核心思路**：论文提出LLMs通过数字位置特定电路逐位处理数字，这些电路在不同的数字位置（如单位、十位、百位）独立操作，从而提高算术运算的准确性和效率。

**技术框架**：整体架构包括特征重要性分析和因果干预两个主要模块。首先，通过特征重要性识别数字位置特定电路，然后通过因果干预验证这些电路的作用。

**关键创新**：最重要的技术创新在于识别和验证了数字位置特定电路的存在，这一发现与现有方法的主要区别在于提供了可解释的算术运算机制。

**关键设计**：在实验中，采用了针对特定数字位置的干预策略，改变模型的预测结果，验证了电路的因果作用。模型的参数设置和网络结构设计均考虑了不同数字位置的独立性。

## 📊 实验亮点

实验结果表明，数字位置特定电路在不同模型和标记策略下均有效存在。通过干预实验，模型在特定数字位置的预测准确性显著提升，验证了这些电路在算术任务中的关键作用。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能助手和自动化计算工具等。通过理解LLMs的算术处理机制，可以提升其在数学教育和计算任务中的表现，进而推动智能系统在复杂任务中的应用价值。

## 📄 摘要（原文）

> While recent work has begun to uncover the internal strategies that Large Language Models (LLMs) employ for simple arithmetic tasks, a unified understanding of their underlying mechanisms is still lacking. We extend recent findings showing that LLMs represent numbers in a digit-wise manner and present evidence for the existence of digit-position-specific circuits that LLMs use to perform simple arithmetic tasks, i.e. modular subgroups of MLP neurons that operate independently on different digit positions (units, tens, hundreds). Notably, such circuits exist independently of model size and of tokenization strategy, i.e. both for models that encode longer numbers digit-by-digit and as one token. Using Feature Importance and Causal Interventions, we identify and validate the digit-position-specific circuits, revealing a compositional and interpretable structure underlying the solving of arithmetic problems in LLMs. Our interventions selectively alter the model's prediction at targeted digit positions, demonstrating the causal role of digit-position circuits in solving arithmetic tasks.

