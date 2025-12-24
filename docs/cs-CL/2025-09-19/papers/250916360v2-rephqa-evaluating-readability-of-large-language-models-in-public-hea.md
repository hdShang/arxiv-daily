---
layout: default
title: "RephQA: Evaluating Readability of Large Language Models in Public Health Question Answering"
---

# RephQA: Evaluating Readability of Large Language Models in Public Health Question Answering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16360" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16360v2</a>
  <a href="https://arxiv.org/pdf/2509.16360.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16360v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16360v2', 'RephQA: Evaluating Readability of Large Language Models in Public Health Question Answering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weikang Qiu, Tinglin Huang, Ryan Rullo, Yucheng Kuang, Ali Maatouk, S. Raquel Ramos, Rex Ying

**分类**: cs.CL

**发布日期**: 2025-09-19 (更新: 2025-10-03)

**备注**: ACM KDD Health Track 2025 Blue Sky Best Paper

---

## 💡 一句话要点

**RephQA：评估大型语言模型在公共健康问答中的可读性，并提出优化策略。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可读性评估` `公共健康问答` `RephQA基准` `Group Relative Policy Optimization`

## 📋 核心要点

1. 现有大型语言模型在公共健康问答中，虽然具备一定的推理能力，但生成回复的可读性不足，难以被非医学背景人士理解。
2. 论文提出RephQA基准，用于评估LLM在公共健康问答中的可读性，并探索多种策略来提升LLM生成文本的可读性。
3. 实验结果表明，现有LLM在可读性方面存在差距，而token-adapted GRPO策略能够有效提升LLM生成文本的可读性。

## 📝 摘要（中文）

大型语言模型（LLMs）在解决复杂的医疗问题方面展现出潜力。然而，现有研究主要集中在提高准确性和推理能力，而忽略了LLM生成回复的可读性，尤其是在向非医学背景的人群清晰简洁地回答公共健康问题方面的能力。本文提出了RephQA，一个用于评估LLM在公共健康问答（QA）中可读性的基准。它包含来自13个主题的27个来源的533个专家评审的QA对，并包括一个代理多项选择任务来评估信息量，以及两个可读性指标：Flesch-Kincaid grade level和专业评分。对25个LLM的评估表明，大多数模型未能达到可读性标准，突出了推理和有效沟通之间的差距。为了解决这个问题，我们探索了四种提高可读性的策略——标准提示、思维链提示、Group Relative Policy Optimization (GRPO)以及token-adapted变体。Token-adapted GRPO取得了最佳结果，推动了更实用和用户友好的公共健康代理的开发。这些结果代表了朝着构建更实用的公共健康代理迈出的一步。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在公共健康问答领域生成文本可读性差的问题。现有方法主要关注准确性和推理能力，忽略了面向非专业人士的清晰简洁表达，导致LLM难以有效服务于大众。

**核心思路**：论文的核心思路是通过构建RephQA基准来量化评估LLM的可读性，并探索不同的优化策略，特别是token-adapted GRPO，以提升LLM生成文本的清晰度和简洁性，使其更易于理解。

**技术框架**：整体框架包含三个主要部分：1) 构建RephQA基准，包括收集QA对、进行专家评审、设计代理任务和可读性指标；2) 评估现有LLM在RephQA上的表现；3) 探索和优化可读性提升策略，包括标准提示、思维链提示、GRPO和token-adapted GRPO。

**关键创新**：最重要的技术创新点在于token-adapted GRPO策略。该策略针对LLM生成的每个token，动态调整优化目标，从而更精细地控制生成文本的可读性。与传统的GRPO相比，token-adapted GRPO能够更好地平衡准确性和可读性。

**关键设计**：RephQA基准的关键设计包括：1) 选取来自多个来源和主题的QA对，保证基准的覆盖性和多样性；2) 采用Flesch-Kincaid grade level和专业评分作为可读性指标，全面评估文本的易读性；3) 设计代理多项选择任务，评估LLM生成文本的信息量。

## 📊 实验亮点

实验结果表明，现有25个LLM在RephQA基准上的可读性表现不佳，未能达到标准。通过应用token-adapted GRPO策略，LLM生成文本的可读性得到了显著提升，在Flesch-Kincaid grade level和专业评分上均取得了最佳结果，证明了该策略的有效性。

## 🎯 应用场景

该研究成果可应用于开发用户友好的公共健康助手，帮助非专业人士获取准确、易懂的健康信息。通过提升LLM生成文本的可读性，可以有效改善医患沟通，提高公众健康素养，并为公共卫生决策提供更可靠的支持。

## 📄 摘要（原文）

> Large Language Models (LLMs) hold promise in addressing complex medical problems. However, while most prior studies focus on improving accuracy and reasoning abilities, a significant bottleneck in developing effective healthcare agents lies in the readability of LLM-generated responses, specifically, their ability to answer public health problems clearly and simply to people without medical backgrounds. In this work, we introduce RephQA, a benchmark for evaluating the readability of LLMs in public health question answering (QA). It contains 533 expert-reviewed QA pairs from 27 sources across 13 topics, and includes a proxy multiple-choice task to assess informativeness, along with two readability metrics: Flesch-Kincaid grade level and professional score. Evaluation of 25 LLMs reveals that most fail to meet readability standards, highlighting a gap between reasoning and effective communication. To address this, we explore four readability-enhancing strategies-standard prompting, chain-of-thought prompting, Group Relative Policy Optimization (GRPO), and a token-adapted variant. Token-adapted GRPO achieves the best results, advancing the development of more practical and user-friendly public health agents. These results represent a step toward building more practical agents for public health.

