---
layout: default
title: "Schema Lineage Extraction at Scale: Multilingual Pipelines, Composite Evaluation, and Language-Model Benchmarks"
---

# Schema Lineage Extraction at Scale: Multilingual Pipelines, Composite Evaluation, and Language-Model Benchmarks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07179" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07179v1</a>
  <a href="https://arxiv.org/pdf/2508.07179.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07179v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07179v1', 'Schema Lineage Extraction at Scale: Multilingual Pipelines, Composite Evaluation, and Language-Model Benchmarks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Yin, Yi-Wei Chen, Meng-Lung Lee, Xiya Liu

**分类**: cs.CL, cs.AI, cs.DB

**发布日期**: 2025-08-10

---

## 💡 一句话要点

**提出自动化提取多语言企业数据管道的模式血统框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模式血统提取` `多语言数据管道` `语义漂移` `数据治理` `机器学习评估`

## 📋 核心要点

1. 现有企业数据管道在多语言环境下的复杂转换导致语义漂移，影响数据的可重复性和治理。
2. 提出了一种新框架，自动提取多语言企业管道中的模式血统，标准化数据转换表示。
3. 实验结果显示，模型规模和提示技术的复杂性显著提升了血统提取的性能，32B模型表现接近GPT系列。

## 📝 摘要（中文）

企业数据管道因多种编程语言的复杂转换，常导致原始元数据与下游数据之间的语义断裂。这种“语义漂移”影响数据的可重复性和治理，降低了检索增强生成（RAG）和文本到SQL系统的效用。为此，本文提出了一种新框架，自动提取多语言企业管道脚本中的细粒度模式血统，识别源模式、源表、转换逻辑和聚合操作，创建数据转换的标准化表示。为严格评估血统质量，本文引入了模式血统复合评估（SLiCE）指标，评估结构正确性和语义保真度，并提出了一个包含1700个手动标注血统的基准。实验表明，血统提取的性能随着模型规模和提示技术的复杂性而提升。

## 🔬 方法详解

**问题定义**：本文旨在解决企业数据管道中因多种编程语言引起的语义漂移问题，现有方法在提取模式血统时存在准确性和一致性不足的痛点。

**核心思路**：提出了一种自动化框架，通过识别源模式、源表、转换逻辑和聚合操作，来实现对数据转换的细粒度提取和标准化表示。

**技术框架**：整体架构包括数据解析模块、模式识别模块和评估模块。数据解析模块负责从多语言脚本中提取信息，模式识别模块进行血统提取，评估模块使用SLiCE指标进行质量评估。

**关键创新**：引入了模式血统复合评估（SLiCE）指标，综合考虑结构正确性和语义保真度，提供了一种新的评估方式，与现有方法相比，能够更全面地反映血统提取的质量。

**关键设计**：在实验中使用了12种不同规模的语言模型，特别是32B开源模型在单一推理轨迹下的表现与GPT系列相当，展示了模型规模与提取性能之间的正相关关系。

## 📊 实验亮点

实验结果表明，随着模型规模的增加，血统提取的性能显著提升。特别是32B开源模型在标准提示下的表现与GPT系列相当，显示出一种可扩展且经济的方案来部署模式感知代理。

## 🎯 应用场景

该研究的潜在应用领域包括企业数据治理、数据仓库管理和智能数据检索等。通过提供准确的模式血统提取，企业能够更好地管理数据流动，提高数据的可追溯性和可重复性，进而提升数据驱动决策的质量和效率。

## 📄 摘要（原文）

> Enterprise data pipelines, characterized by complex transformations across multiple programming languages, often cause a semantic disconnect between original metadata and downstream data. This "semantic drift" compromises data reproducibility and governance, and impairs the utility of services like retrieval-augmented generation (RAG) and text-to-SQL systems. To address this, a novel framework is proposed for the automated extraction of fine-grained schema lineage from multilingual enterprise pipeline scripts. This method identifies four key components: source schemas, source tables, transformation logic, and aggregation operations, creating a standardized representation of data transformations. For the rigorous evaluation of lineage quality, this paper introduces the Schema Lineage Composite Evaluation (SLiCE), a metric that assesses both structural correctness and semantic fidelity. A new benchmark is also presented, comprising 1,700 manually annotated lineages from real-world industrial scripts. Experiments were conducted with 12 language models, from 1.3B to 32B small language models (SLMs) to large language models (LLMs) like GPT-4o and GPT-4.1. The results demonstrate that the performance of schema lineage extraction scales with model size and the sophistication of prompting techniques. Specially, a 32B open-source model, using a single reasoning trace, can achieve performance comparable to the GPT series under standard prompting. This finding suggests a scalable and economical approach for deploying schema-aware agents in practical applications.

