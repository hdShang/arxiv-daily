---
layout: default
title: Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline
---

# Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20546" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20546v2</a>
  <a href="https://arxiv.org/pdf/2505.20546.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20546v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20546v2', 'Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Meng Lu, Ruochen Zhang, Carsten Eickhoff, Ellie Pavlick

**分类**: cs.CL

**发布日期**: 2025-05-26 (更新: 2025-05-28)

---

## 💡 一句话要点

**提出向量干预以解决多语言事实回忆不一致问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `事实回忆` `向量干预` `机制分析` `语言一致性` `自然语言处理`

## 📋 核心要点

1. 现有多语言大型语言模型在事实回忆任务中表现不一致，尤其在非英语语言中显著较差，原因尚不明确。
2. 论文提出两种向量干预方法，旨在改善模型在多语言查询中的事实回忆能力，增强其内部处理路径。
3. 实验结果显示，干预措施使最低表现语言的回忆准确率提升超过35%，有效提高了多语言模型的性能。

## 📝 摘要（中文）

多语言大型语言模型（LLMs）在不同语言间的事实一致性表现不佳，尤其在英语中的事实回忆任务上表现更为突出。本文通过机制分析技术揭示了LLMs的内部处理流程，发现主要错误源于对英语中心机制的不足利用及翻译过程中的错误。为此，提出了两种独立于语言和数据集的向量干预方法，旨在引导模型朝向更高的事实一致性路径。实验结果表明，这些干预措施使最低表现语言的回忆准确率提高了超过35%。

## 🔬 方法详解

**问题定义**：本文解决多语言大型语言模型在事实回忆任务中存在的语言间一致性差的问题，尤其是英语与其他语言之间的表现差异。现有方法未能充分利用英语中心的事实回忆机制，导致翻译后的答案不准确。

**核心思路**：通过引入两种向量干预方法，独立于语言和数据集，旨在引导模型更有效地利用其内部机制，从而提高多语言的事实一致性。

**技术框架**：整体流程包括：首先，模型接收多语言查询并使用英语中心机制进行处理；其次，生成英语答案并进行翻译；最后，通过向量干预调整模型的内部路径以提高最终答案的准确性。

**关键创新**：本研究的主要创新在于提出了两种向量干预方法，能够有效重定向模型的内部处理路径，与传统方法相比，显著提高了多语言的事实回忆能力。

**关键设计**：在设计中，干预方法的参数设置经过精心调整，以确保其对不同语言和数据集的普适性，损失函数和网络结构也进行了优化，以支持更高效的事实回忆机制。

## 📊 实验亮点

实验结果表明，提出的向量干预方法使最低表现语言的回忆准确率提升超过35%。这一显著提升不仅验证了干预方法的有效性，也展示了机制分析在多语言模型中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括多语言信息检索、跨语言问答系统和多语言内容生成等。通过提高多语言模型的事实一致性，能够为用户提供更准确的信息，提升用户体验，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Multilingual large language models (LLMs) often exhibit factual inconsistencies across languages, with significantly better performance in factual recall tasks in English than in other languages. The causes of these failures, however, remain poorly understood. Using mechanistic analysis techniques, we uncover the underlying pipeline that LLMs employ, which involves using the English-centric factual recall mechanism to process multilingual queries and then translating English answers back into the target language. We identify two primary sources of error: insufficient engagement of the reliable English-centric mechanism for factual recall, and incorrect translation from English back into the target language for the final answer. To address these vulnerabilities, we introduce two vector interventions, both independent of languages and datasets, to redirect the model toward better internal paths for higher factual consistency. Our interventions combined increase the recall accuracy by over 35 percent for the lowest-performing language. Our findings demonstrate how mechanistic insights can be used to unlock latent multilingual capabilities in LLMs.

