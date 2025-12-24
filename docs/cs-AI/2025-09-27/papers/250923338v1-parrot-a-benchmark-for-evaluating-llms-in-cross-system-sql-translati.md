---
layout: default
title: "PARROT: A Benchmark for Evaluating LLMs in Cross-System SQL Translation"
---

# PARROT: A Benchmark for Evaluating LLMs in Cross-System SQL Translation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23338" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23338v1</a>
  <a href="https://arxiv.org/pdf/2509.23338.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23338v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23338v1', 'PARROT: A Benchmark for Evaluating LLMs in Cross-System SQL Translation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Zhou, Guoliang Li, Haoyu Wang, Yuxing Han, Xufei Wu, Fan Wu, Xuanhe Zhou

**分类**: cs.DB, cs.AI, cs.CL, cs.IR, cs.LG

**发布日期**: 2025-09-27

**备注**: To appear in NeurIPS 2025. Welcome your submission to challenge our leaderboard at: https://code4db.github.io/parrot-bench/. Also visit our code repository at: https://github.com/weAIDB/PARROT

**🔗 代码/项目**: [PROJECT_PAGE](https://code4db.github.io/parrot-bench/)

---

## 💡 一句话要点

**PARROT：用于评估LLM跨系统SQL转换能力的基准测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `SQL转换` `跨系统数据库` `大型语言模型` `基准测试` `数据库迁移`

## 📋 核心要点

1. 现有的SQL基准测试在跨系统SQL转换任务中存在不足，无法充分评估LLM对不同数据库系统方言的理解能力。
2. PARROT基准测试旨在提供一个实用且真实的跨系统SQL转换评估平台，包含多种数据库系统和复杂的SQL方言。
3. 实验结果表明，现有LLM在PARROT基准测试上的性能较低，突显了跨系统SQL转换任务的挑战性。

## 📝 摘要（中文）

大型语言模型（LLM）在文本到SQL任务中表现出越来越高的有效性。然而，另一个密切相关的问题，即跨系统SQL转换（又称SQL到SQL），它将为一种数据库系统（例如，MySQL）编写的查询适配为另一种系统（例如，ClickHouse）的等效查询，具有重要的实际意义，但仍未得到充分探索。现有的SQL基准测试不太适合SQL到SQL的评估，因为它们（1）侧重于有限的数据库系统（通常只是SQLite），并且（2）无法捕获许多系统特定的SQL方言（例如，自定义函数、数据类型和语法规则）。因此，在本文中，我们介绍了PARROT，一个用于跨系统SQL转换的实用且真实的基准测试。PARROT包含来自38个开源基准测试和真实业务服务的598个翻译对，专门用于挑战系统特定的SQL理解（例如，LLM的平均准确率低于38.53%）。我们还提供了多个基准测试变体，包括包含28,003个翻译的PARROT-Diverse（用于广泛的语法测试）和包含5,306个代表性样本的PARROT-Simple（用于集中的压力测试），涵盖22个生产级数据库系统。为了促进未来的研究，我们发布了一个公共排行榜和源代码：https://code4db.github.io/parrot-bench/。

## 🔬 方法详解

**问题定义**：论文旨在解决跨系统SQL转换问题，即如何将一个数据库系统（如MySQL）的SQL查询转换为另一个数据库系统（如ClickHouse）的等效查询。现有方法主要基于单一数据库系统，无法有效处理不同数据库系统之间的SQL方言差异，导致转换准确率低。

**核心思路**：论文的核心思路是构建一个包含多种数据库系统和复杂SQL方言的基准测试数据集PARROT，用于全面评估LLM在跨系统SQL转换任务中的性能。通过PARROT，可以更准确地衡量LLM对不同数据库系统SQL语法的理解和转换能力。

**技术框架**：PARROT基准测试包含598个翻译对，来源于38个开源基准测试和真实业务服务。此外，还提供了PARROT-Diverse（28,003个翻译）和PARROT-Simple（5,306个翻译）两个变体，分别用于广泛的语法测试和集中的压力测试。该基准测试覆盖了22个生产级数据库系统。

**关键创新**：PARROT的关键创新在于其数据集的多样性和真实性，它包含了大量来自不同数据库系统的SQL查询，涵盖了各种系统特定的SQL方言，例如自定义函数、数据类型和语法规则。这使得PARROT能够更全面地评估LLM在跨系统SQL转换任务中的能力。

**关键设计**：PARROT的设计重点在于覆盖尽可能多的数据库系统和SQL方言。数据集的构建过程中，作者精心挑选了来自不同来源的SQL查询，并进行了人工验证，确保翻译的准确性和一致性。此外，PARROT还提供了多种评估指标，例如准确率和BLEU分数，以便更全面地评估LLM的性能。

## 📊 实验亮点

实验结果表明，现有LLM在PARROT基准测试上的平均准确率低于38.53%，这表明跨系统SQL转换任务对LLM来说仍然具有很大的挑战性。PARROT-Diverse和PARROT-Simple变体的引入，能够更全面地评估LLM在不同场景下的性能。

## 🎯 应用场景

该研究成果可应用于数据库迁移、多数据库系统集成、自动化SQL转换等领域。通过利用LLM进行跨系统SQL转换，可以降低数据库迁移的成本和复杂性，提高多数据库系统集成的效率，并实现SQL代码的自动化转换和优化。

## 📄 摘要（原文）

> Large language models (LLMS) have shown increasing effectiveness in Text-to-SQL tasks. However, another closely related problem, Cross-System SQL Translation (a.k.a., SQL-to-SQL), which adapts a query written for one database system (e.g., MySQL) into its equivalent one for another system (e.g., ClickHouse), is of great practical importance but remains underexplored. Existing SQL benchmarks are not well-suited for SQL-to-SQL evaluation, which (1) focus on a limited set of database systems (often just SQLite) and (2) cannot capture many system-specific SQL dialects (e.g., customized functions, data types, and syntax rules). Thus, in this paper, we introduce PARROT, a Practical And Realistic BenchmaRk for CrOss-System SQL Translation. PARROT comprises 598 translation pairs from 38 open-source benchmarks and real-world business services, specifically prepared to challenge system-specific SQL understanding (e.g., LLMS achieve lower than 38.53% accuracy on average). We also provide multiple benchmark variants, including PARROT-Diverse with 28,003 translations (for extensive syntax testing) and PARROT-Simple with 5,306 representative samples (for focused stress testing), covering 22 production-grade database systems. To promote future research, we release a public leaderboard and source code at: https://code4db.github.io/parrot-bench/.

