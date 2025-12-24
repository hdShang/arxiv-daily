---
layout: default
title: Bench4KE: Benchmarking Automated Competency Question Generation
---

# Bench4KE: Benchmarking Automated Competency Question Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24554" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24554v3</a>
  <a href="https://arxiv.org/pdf/2505.24554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24554v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24554v3', 'Bench4KE: Benchmarking Automated Competency Question Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anna Sofia Lippolis, Minh Davide Ragagni, Paolo Ciancarini, Andrea Giovanni Nuzzolese, Valentina Presutti

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-12-09)

---

## 💡 一句话要点

**提出Bench4KE以解决知识工程自动化评估标准化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识工程` `能力问题生成` `基准测试` `大型语言模型` `自动化工具` `评估标准化` `本体工程`

## 📋 核心要点

1. 现有的能力问题生成工具缺乏标准化评估，导致研究结果难以比较和复现。
2. Bench4KE是一个API基础的基准测试系统，旨在为自动生成能力问题的工具提供标准化评估。
3. 通过对6个基于LLM的能力问题生成系统进行比较分析，Bench4KE建立了未来研究的基准线。

## 📝 摘要（中文）

大型语言模型（LLMs）的出现为知识工程（KE）自动化研究带来了新的机遇。尽管已有基于LLM的工具用于自动生成能力问题（CQs），但缺乏标准化的评估方法，影响了研究的严谨性和结果的可比性。为此，本文提出了Bench4KE，一个基于API的可扩展基准测试系统，专注于自动生成CQs的工具评估。Bench4KE提供了来自17个真实世界本体工程项目的CQs数据集，并使用一套相似性度量来评估生成的CQs质量。此外，Bench4KE还支持其他KE自动化任务，如SPARQL查询生成和本体测试。代码和数据集已在Apache 2.0许可证下公开。

## 🔬 方法详解

**问题定义**：本文解决的是知识工程自动化工具评估缺乏标准化的问题，现有方法在结果比较和复现性方面存在不足。

**核心思路**：提出Bench4KE作为一个可扩展的基准测试系统，专注于能力问题的自动生成工具评估，通过提供标准化的数据集和评估指标来提升研究的严谨性。

**技术框架**：Bench4KE的整体架构包括数据集管理模块、评估指标计算模块和结果展示模块。数据集管理模块提供来自17个本体工程项目的CQs数据集，评估指标模块使用多种相似性度量来评估生成的CQs质量。

**关键创新**：Bench4KE的创新在于其提供的标准化评估框架和丰富的基准数据集，使得不同工具的评估结果可以直接比较，填补了现有研究中的空白。

**关键设计**：在设计中，Bench4KE采用了多种相似性度量来评估CQs的质量，确保评估结果的全面性和准确性，同时支持未来扩展其他KE自动化任务的能力。

## 📊 实验亮点

在对6个基于LLM的能力问题生成系统的比较分析中，Bench4KE建立了一个基准线，为未来的研究提供了参考。该系统通过使用标准化的评估指标，显著提高了生成CQs的质量评估的可靠性和有效性。

## 🎯 应用场景

Bench4KE的潜在应用领域包括本体工程、知识图谱构建和智能问答系统等。通过提供标准化的评估工具，研究人员和开发者可以更有效地比较和改进自动生成能力问题的工具，从而推动知识工程领域的发展。未来，Bench4KE可能会扩展到更多的知识工程自动化任务，进一步提升其实际价值。

## 📄 摘要（原文）

> The availability of Large Language Models (LLMs) presents a unique opportunity to reinvigorate research on Knowledge Engineering (KE) automation. This trend is already evident in recent efforts developing LLM-based methods and tools for the automatic generation of Competency Questions (CQs), natural language questions used by ontology engineers to define the functional requirements of an ontology. However, the evaluation of these tools lacks standardization. This undermines the methodological rigor and hinders the replication and comparison of results. To address this gap, we introduce Bench4KE, an extensible API-based benchmarking system for KE automation. The presented release focuses on evaluating tools that generate CQs automatically. Bench4KE provides a curated gold standard consisting of CQ datasets from 17 real-world ontology engineering projects and uses a suite of similarity metrics to assess the quality of the CQs generated. We present a comparative analysis of 6 recent CQ generation systems, which are based on LLMs, establishing a baseline for future research. Bench4KE is also designed to accommodate additional KE automation tasks, such as SPARQL query generation, ontology testing and drafting. Code and datasets are publicly available under the Apache 2.0 license.

