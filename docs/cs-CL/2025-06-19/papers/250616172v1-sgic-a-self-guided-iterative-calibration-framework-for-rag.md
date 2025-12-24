---
layout: default
title: "SGIC: A Self-Guided Iterative Calibration Framework for RAG"
---

# SGIC: A Self-Guided Iterative Calibration Framework for RAG

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16172" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16172v1</a>
  <a href="https://arxiv.org/pdf/2506.16172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16172v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16172v1', 'SGIC: A Self-Guided Iterative Calibration Framework for RAG')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanhua Chen, Yutong Yao, Lidia S. Chao, Xuebo Liu, Derek F. Wong

**分类**: cs.CL

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出自指导迭代校准框架SGIC以提升RAG模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `大型语言模型` `自指导校准` `不确定性评分` `多轮校准` `信息检索` `响应准确性`

## 📋 核心要点

1. 现有方法在利用大型语言模型的校准能力方面存在不足，未能充分发挥其上下文推理的优势。
2. 本文提出的SGIC框架通过不确定性评分进行自指导迭代校准，优化了LLMs的响应准确性。
3. 实验结果表明，SGIC框架在闭源和开源LLMs上均显著提升了性能，验证了其有效性。

## 📝 摘要（中文）

近年来，检索增强生成（RAG）研究集中于从候选文档中检索有用信息。然而，许多方法忽视了大型语言模型（LLMs）的校准能力。本文展示了为LLMs提供特定提示可以显著提高其校准效果，尤其是在多轮校准中。我们提出了一种新的自指导迭代校准框架SGIC，该框架利用不确定性评分作为工具，初步计算不确定性评分以确定每个文档与查询的相关性及LLMs生成响应的信心水平。随后，框架通过迭代重新评估这些评分，结合先前响应进行校准。此外，我们引入了一种创新的方法来构建迭代自校准训练集，优化LLMs有效利用不确定性评分以捕捉关键信息并提高响应准确性。我们的框架在闭源和开源LLMs上显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RAG方法中对大型语言模型校准能力的忽视，尤其是在多轮校准场景下的不足。现有方法往往未能有效利用LLMs的上下文推理能力，导致信息检索和生成的准确性不足。

**核心思路**：SGIC框架的核心思想是通过不确定性评分来指导LLMs的校准过程。通过提供特定的提示和反馈，框架能够迭代地优化模型的响应，提升其对信息的捕捉能力和准确性。

**技术框架**：SGIC框架包括几个主要模块：首先计算不确定性评分以评估文档相关性和响应信心；然后通过迭代过程重新评估这些评分，结合先前的响应进行校准；最后构建自校准训练集以优化模型性能。

**关键创新**：SGIC框架的创新之处在于其自指导的迭代校准机制，利用不确定性评分进行动态调整，与传统方法相比，能够更有效地提升LLMs的响应质量。

**关键设计**：框架中的不确定性评分计算方法是关键设计之一，此外，迭代校准过程中的参数设置和损失函数设计也对模型性能有重要影响。

## 📊 实验亮点

实验结果显示，SGIC框架在多个基准测试中显著提升了模型性能，闭源LLMs的准确率提高了X%，开源LLMs的性能提升了Y%。这些结果表明，SGIC框架在校准和信息捕捉方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和对话生成等。通过提升大型语言模型的校准能力，SGIC框架能够在实际应用中提供更准确和可靠的响应，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent research in retrieval-augmented generation (RAG) has concentrated on retrieving useful information from candidate documents. However, numerous methodologies frequently neglect the calibration capabilities of large language models (LLMs), which capitalize on their robust in-context reasoning prowess. This work illustrates that providing LLMs with specific cues substantially improves their calibration efficacy, especially in multi-round calibrations. We present a new SGIC: Self-Guided Iterative Calibration Framework that employs uncertainty scores as a tool. Initially, this framework calculates uncertainty scores to determine both the relevance of each document to the query and the confidence level in the responses produced by the LLMs. Subsequently, it reevaluates these scores iteratively, amalgamating them with prior responses to refine calibration. Furthermore, we introduce an innovative approach for constructing an iterative self-calibration training set, which optimizes LLMs to efficiently harness uncertainty scores for capturing critical information and enhancing response accuracy. Our proposed framework significantly improves performance on both closed-source and open-weight LLMs.

