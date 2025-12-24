---
layout: default
title: Evaluating the Retrieval Robustness of Large Language Models
---

# Evaluating the Retrieval Robustness of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21870" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21870v1</a>
  <a href="https://arxiv.org/pdf/2505.21870.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21870v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21870v1', 'Evaluating the Retrieval Robustness of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuyang Cao, Karthik Radhakrishnan, David Rosenberg, Steven Lu, Pengxiang Cheng, Lu Wang, Shiyue Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-28

**备注**: 19 pages

---

## 💡 一句话要点

**评估大语言模型在检索增强生成中的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `大语言模型` `鲁棒性评估` `知识密集型任务` `开放域问题`

## 📋 核心要点

1. 现有的检索增强生成方法在检索不完美时可能导致性能下降，限制了大语言模型的应用效果。
2. 本研究通过建立基准和引入鲁棒性指标，系统评估了大语言模型在RAG设置下的表现。
3. 实验结果表明，尽管大语言模型在检索鲁棒性上表现良好，但仍存在不完美鲁棒性的问题，影响其性能发挥。

## 📝 摘要（中文）

检索增强生成（RAG）通常提升大语言模型（LLMs）解决知识密集型任务的能力。然而，由于检索不完美及模型利用检索内容的能力有限，RAG可能导致性能下降。本研究评估了LLMs在实际RAG设置中的鲁棒性，重点关注三个研究问题：RAG是否总是优于非RAG？更多检索文档是否总能提升性能？文档顺序是否影响结果？为此，我们建立了一个包含1500个开放域问题的基准，并引入了三种鲁棒性指标。实验结果显示，所有LLMs展现出较高的检索鲁棒性，但不同程度的不完美鲁棒性限制了它们充分利用RAG的优势。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型在检索增强生成（RAG）中可能出现的性能下降问题，尤其是在检索不完美的情况下，现有方法未能充分利用检索内容的能力。

**核心思路**：通过建立一个包含1500个开放域问题的基准，论文评估了不同大语言模型在RAG设置下的鲁棒性，提出了三种鲁棒性指标来分析模型表现。

**技术框架**：整体架构包括数据集构建、鲁棒性指标设计和实验评估三个主要模块。首先，构建基准数据集；其次，设计评估指标；最后，通过实验对11个大语言模型进行评估。

**关键创新**：论文的主要创新在于引入了鲁棒性指标，系统性地评估了大语言模型在RAG中的表现，填补了现有研究的空白。

**关键设计**：在实验中，使用了三种不同的提示策略，评估了文档数量和顺序对模型性能的影响，确保了实验的全面性和准确性。

## 📊 实验亮点

实验结果显示，所有评估的大语言模型在检索鲁棒性上表现出色，尽管存在不同程度的不完美鲁棒性。具体而言，模型在面对不同数量和顺序的检索文档时，性能波动较小，表明其在实际应用中的可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括知识问答系统、智能助手和信息检索等。通过提升大语言模型在检索增强生成中的鲁棒性，可以显著提高这些系统在实际应用中的表现和用户体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Retrieval-augmented generation (RAG) generally enhances large language models' (LLMs) ability to solve knowledge-intensive tasks. But RAG may also lead to performance degradation due to imperfect retrieval and the model's limited ability to leverage retrieved content. In this work, we evaluate the robustness of LLMs in practical RAG setups (henceforth retrieval robustness). We focus on three research questions: (1) whether RAG is always better than non-RAG; (2) whether more retrieved documents always lead to better performance; (3) and whether document orders impact results. To facilitate this study, we establish a benchmark of 1500 open-domain questions, each with retrieved documents from Wikipedia. We introduce three robustness metrics, each corresponds to one research question. Our comprehensive experiments, involving 11 LLMs and 3 prompting strategies, reveal that all of these LLMs exhibit surprisingly high retrieval robustness; nonetheless, different degrees of imperfect robustness hinders them from fully utilizing the benefits of RAG.

