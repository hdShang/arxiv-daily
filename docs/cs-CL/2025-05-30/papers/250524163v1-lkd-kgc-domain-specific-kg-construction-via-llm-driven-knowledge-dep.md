---
layout: default
title: LKD-KGC: Domain-Specific KG Construction via LLM-driven Knowledge Dependency Parsing
---

# LKD-KGC: Domain-Specific KG Construction via LLM-driven Knowledge Dependency Parsing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24163" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24163v1</a>
  <a href="https://arxiv.org/pdf/2505.24163.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24163v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24163v1', 'LKD-KGC: Domain-Specific KG Construction via LLM-driven Knowledge Dependency Parsing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Sun, Shiyou Qian, Zhangchi Han, Wei Li, Zelin Qian, Dingyu Yang, Jian Cao, Guangtao Xue

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30

**备注**: Submitting to EDBT 2026

---

## 💡 一句话要点

**提出LKD-KGC以解决领域特定知识图谱构建的效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `领域特定` `无监督学习` `知识依赖推断` `大型语言模型` `信息提取` `机器学习`

## 📋 核心要点

1. 现有的知识图谱构建方法依赖于手动定义的模式和单文档处理，难以应对领域特定的复杂知识依赖关系。
2. LKD-KGC框架通过自主分析文档库推断知识依赖关系，利用LLM驱动的优先级确定处理顺序，生成实体模式。
3. 实验结果显示，LKD-KGC在精度和召回率上较最先进的基线方法提升了10%至20%，证明了其在构建高质量领域特定知识图谱的潜力。

## 📝 摘要（中文）

知识图谱（KGs）将现实世界的实体及其关系结构化为三元组，增强了机器推理能力。尽管领域特定的知识图谱具有显著优势，但其手动构建效率低下且需要专业知识。基于大型语言模型（LLMs）的知识图谱构建方法虽然高效，但受限于手动定义的模式和单文档处理，难以应对复杂的知识依赖关系。为此，本文提出了LKD-KGC，一个无监督的领域特定知识图谱构建框架，能够自主分析文档库推断知识依赖关系，并通过LLM驱动的优先级确定最佳处理顺序，最终生成实体模式。实验结果表明，LKD-KGC在精度和召回率上较现有方法普遍提升了10%至20%。

## 🔬 方法详解

**问题定义**：本文旨在解决领域特定知识图谱构建中的效率低下和知识依赖关系复杂的问题。现有方法依赖于手动定义的模式，无法有效处理特定领域的知识。

**核心思路**：LKD-KGC通过无监督方式分析文档库，推断知识依赖关系，并利用LLM驱动的优先级确定最佳处理顺序，从而生成实体模式，避免了对预定义结构的依赖。

**技术框架**：LKD-KGC的整体架构包括文档分析模块、知识依赖推断模块和实体模式生成模块。文档分析模块负责提取文档中的信息，知识依赖推断模块分析信息之间的关系，实体模式生成模块则根据推断结果生成知识图谱的结构。

**关键创新**：LKD-KGC的主要创新在于其无监督的知识依赖推断能力和基于LLM的优先级处理机制，这与传统方法的手动模式定义形成鲜明对比。

**关键设计**：在设计中，LKD-KGC采用了层次化的文档上下文集成方式，确保生成的实体模式能够有效反映文档间的知识关系，同时避免了对外部知识的依赖。

## 📊 实验亮点

LKD-KGC在实验中表现出色，相较于最先进的基线方法，精度和召回率普遍提升了10%至20%。这一结果表明，该框架在领域特定知识图谱构建中具有显著的优势和应用潜力。

## 🎯 应用场景

LKD-KGC的研究成果可广泛应用于医疗、法律、金融等领域的知识图谱构建，帮助专业人员更高效地提取和组织领域特定知识。未来，该方法有望推动自动化知识管理和智能决策支持系统的发展。

## 📄 摘要（原文）

> Knowledge Graphs (KGs) structure real-world entities and their relationships into triples, enhancing machine reasoning for various tasks. While domain-specific KGs offer substantial benefits, their manual construction is often inefficient and requires specialized knowledge. Recent approaches for knowledge graph construction (KGC) based on large language models (LLMs), such as schema-guided KGC and reference knowledge integration, have proven efficient. However, these methods are constrained by their reliance on manually defined schema, single-document processing, and public-domain references, making them less effective for domain-specific corpora that exhibit complex knowledge dependencies and specificity, as well as limited reference knowledge. To address these challenges, we propose LKD-KGC, a novel framework for unsupervised domain-specific KG construction. LKD-KGC autonomously analyzes document repositories to infer knowledge dependencies, determines optimal processing sequences via LLM driven prioritization, and autoregressively generates entity schema by integrating hierarchical inter-document contexts. This schema guides the unsupervised extraction of entities and relationships, eliminating reliance on predefined structures or external knowledge. Extensive experiments show that compared with state-of-the-art baselines, LKD-KGC generally achieves improvements of 10% to 20% in both precision and recall rate, demonstrating its potential in constructing high-quality domain-specific KGs.

