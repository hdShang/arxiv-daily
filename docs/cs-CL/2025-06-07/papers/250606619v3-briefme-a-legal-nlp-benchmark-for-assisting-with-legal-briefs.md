---
layout: default
title: "BriefMe: A Legal NLP Benchmark for Assisting with Legal Briefs"
---

# BriefMe: A Legal NLP Benchmark for Assisting with Legal Briefs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06619" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06619v3</a>
  <a href="https://arxiv.org/pdf/2506.06619.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06619v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06619v3', 'BriefMe: A Legal NLP Benchmark for Assisting with Legal Briefs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jesse Woo, Fateme Hashemi Chaleshtori, Ana Marasović, Kenneth Marino

**分类**: cs.CL

**发布日期**: 2025-06-07 (更新: 2025-06-19)

**备注**: ACL Findings 2025; 10 pages main, 5 pages references, 37 pages appendix

---

## 💡 一句话要点

**提出BRIEFME数据集以解决法律文书撰写辅助问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律NLP` `数据集` `法律文书` `语言模型` `论点补全` `案例检索` `任务设计`

## 📋 核心要点

1. 法律文书撰写在法律NLP中被忽视，现有模型在相关任务上表现不足。
2. 提出BRIEFME数据集，包含论点摘要、补全和案例检索三项任务，旨在辅助法律专业人士。
3. 实验表明，当前大型语言模型在摘要和补全任务上表现优异，但在论点补全和案例检索上仍有待提升。

## 📝 摘要（中文）

法律自然语言处理（NLP）领域中，法律文书的撰写与编辑尚未得到充分探索。撰写法律文书不仅需要对法律条款有深入理解，还需具备提出新论点的能力。为此，本文提出了BRIEFME数据集，专注于法律文书的三项任务：论点摘要、论点补全和案例检索。通过对这些任务的创建与分析，展示了当前模型的表现，发现大型语言模型在摘要和引导补全任务上表现良好，但在现实论点补全和相关法律案例检索上表现不佳。希望该数据集能促进法律NLP的发展，帮助法律工作者更好地完成工作。

## 🔬 方法详解

**问题定义**：论文旨在解决法律文书撰写中的辅助问题，现有方法在论点补全和案例检索方面表现不佳，无法满足法律专业人士的需求。

**核心思路**：通过构建BRIEFME数据集，设计三项任务以评估和提升语言模型在法律文书撰写中的能力，特别是论点的创造性和相关性。

**技术框架**：整体架构包括数据集的构建、任务设计和模型评估三个主要模块。数据集涵盖法律文书的多样性，任务设计则针对法律文书的特定需求。

**关键创新**：BRIEFME数据集的创建是本研究的核心创新，特别是在法律文书撰写的任务设计上，与现有的法律NLP数据集相比，更加注重论点的创造性和实用性。

**关键设计**：在任务设计中，采用了特定的评估标准和损失函数，以确保模型在法律文书撰写中的表现，特别是在论点补全和案例检索的准确性和相关性上。

## 📊 实验亮点

实验结果显示，当前大型语言模型在论点摘要和引导补全任务上表现优异，甚至超越了人类生成的标题。然而，在现实论点补全和案例检索任务上，模型的表现仍显不足，提示未来研究的方向。

## 🎯 应用场景

该研究的潜在应用领域包括法律文书撰写、法律咨询和法庭辩论等。通过提供高效的法律文书撰写辅助工具，能够显著提高法律专业人士的工作效率，降低文书撰写的时间成本，未来可能影响法律行业的工作流程和效率。

## 📄 摘要（原文）

> A core part of legal work that has been under-explored in Legal NLP is the writing and editing of legal briefs. This requires not only a thorough understanding of the law of a jurisdiction, from judgments to statutes, but also the ability to make new arguments to try to expand the law in a new direction and make novel and creative arguments that are persuasive to judges. To capture and evaluate these legal skills in language models, we introduce BRIEFME, a new dataset focused on legal briefs. It contains three tasks for language models to assist legal professionals in writing briefs: argument summarization, argument completion, and case retrieval. In this work, we describe the creation of these tasks, analyze them, and show how current models perform. We see that today's large language models (LLMs) are already quite good at the summarization and guided completion tasks, even beating human-generated headings. Yet, they perform poorly on other tasks in our benchmark: realistic argument completion and retrieving relevant legal cases. We hope this dataset encourages more development in Legal NLP in ways that will specifically aid people in performing legal work.

