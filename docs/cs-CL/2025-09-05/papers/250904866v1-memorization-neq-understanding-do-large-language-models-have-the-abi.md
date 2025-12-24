---
layout: default
title: "Memorization $\\neq$ Understanding: Do Large Language Models Have the Ability of Scenario Cognition?"
---

# Memorization $\neq$ Understanding: Do Large Language Models Have the Ability of Scenario Cognition?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04866" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04866v1</a>
  <a href="https://arxiv.org/pdf/2509.04866.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04866v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04866v1', 'Memorization $\neq$ Understanding: Do Large Language Models Have the Ability of Scenario Cognition?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boxiang Ma, Ru Li, Yuanlong Wang, Hongye Tan, Xiaoli Li

**分类**: cs.CL

**发布日期**: 2025-09-05

**备注**: EMNLP 2025 Main Conference

---

## 💡 一句话要点

**提出双视角评估框架以解决大语言模型场景认知能力问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `场景认知` `双视角评估` `语义理解` `自然语言处理`

## 📋 核心要点

1. 当前大型语言模型在场景认知能力上存在显著不足，主要依赖于对训练数据的表面记忆。
2. 本文提出了一种双视角评估框架，通过场景基础数据集评估模型的语义场景认知能力。
3. 实验结果显示，现有LLMs在场景认知任务中表现不佳，未能有效理解语义关联。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言处理任务中表现出色，但其泛化能力是否源于对训练数据的简单记忆，还是深层语义理解仍然是一个关键问题。为此，本文提出了一种双视角评估框架，旨在评估LLMs的场景认知能力，即将语义场景元素与上下文中的论据关联的能力。我们引入了一个新颖的基于场景的数据集，包含多样的虚构事实文本描述，并对场景元素进行了注释。通过评估模型输出和内部表示，我们的实验表明，当前的LLMs主要依赖于表面的记忆，未能在简单情况下实现稳健的语义场景认知。这些发现揭示了LLMs在语义理解方面的关键局限性，并为提升其能力提供了认知洞察。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在场景认知能力方面的不足，现有方法往往无法有效区分记忆与理解的差异，导致模型在实际应用中的局限性。

**核心思路**：通过引入双视角评估框架，结合模型输出与内部表示的分析，全面评估LLMs的场景认知能力，探讨其在语义理解上的深度。

**技术框架**：整体架构包括两个主要模块：一是基于场景的数据集构建，二是双视角评估机制，分别从模型输出和内部表示两个方面进行分析。

**关键创新**：最重要的技术创新在于提出了双视角评估框架，能够同时考察模型的输出能力与内部表示的语义关联，揭示了模型在场景认知上的深层次问题。

**关键设计**：在数据集构建中，设计了多样的虚构事实文本，并对场景元素进行了详细注释；在评估过程中，采用了特定的损失函数和参数设置，以确保模型在场景认知任务上的有效性。

## 📊 实验亮点

实验结果表明，当前的LLMs在场景认知任务中表现不佳，主要依赖表面记忆，未能有效理解语义关联。具体而言，模型在简单场景问题上的准确率未达到预期，显示出其在语义理解方面的关键局限性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、对话系统和自动文本生成等。通过提升大型语言模型的场景认知能力，可以增强其在复杂语境下的理解和推理能力，从而提高实际应用的效果和用户体验。未来，该研究可能推动更深层次的语义理解模型的开发。

## 📄 摘要（原文）

> Driven by vast and diverse textual data, large language models (LLMs) have demonstrated impressive performance across numerous natural language processing (NLP) tasks. Yet, a critical question persists: does their generalization arise from mere memorization of training data or from deep semantic understanding? To investigate this, we propose a bi-perspective evaluation framework to assess LLMs' scenario cognition - the ability to link semantic scenario elements with their arguments in context. Specifically, we introduce a novel scenario-based dataset comprising diverse textual descriptions of fictional facts, annotated with scenario elements. LLMs are evaluated through their capacity to answer scenario-related questions (model output perspective) and via probing their internal representations for encoded scenario elements-argument associations (internal representation perspective). Our experiments reveal that current LLMs predominantly rely on superficial memorization, failing to achieve robust semantic scenario cognition, even in simple cases. These findings expose critical limitations in LLMs' semantic understanding and offer cognitive insights for advancing their capabilities.

