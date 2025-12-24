---
layout: default
title: "VTS-LLM: Domain-Adaptive LLM Agent for Enhancing Awareness in Vessel Traffic Services through Natural Language"
---

# VTS-LLM: Domain-Adaptive LLM Agent for Enhancing Awareness in Vessel Traffic Services through Natural Language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00989" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00989v1</a>
  <a href="https://arxiv.org/pdf/2505.00989.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00989v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00989v1', 'VTS-LLM: Domain-Adaptive LLM Agent for Enhancing Awareness in Vessel Traffic Services through Natural Language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sijin Sun, Liangbin Zhao, Ming Deng, Xiuju Fu

**分类**: cs.CL

**发布日期**: 2025-05-02

**备注**: 8 pages, 5 figures, 7 tablels, submitted to ITSC2025

---

## 💡 一句话要点

**提出VTS-LLM以解决船舶交通服务中的交互决策支持问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `船舶交通服务` `自然语言处理` `领域自适应` `决策支持` `文本到SQL` `多模态数据` `知识增强`

## 📋 核心要点

1. 现有的船舶交通服务系统在处理复杂交通和多模态数据时，缺乏有效的时空推理和人机交互能力。
2. 本文提出VTS-LLM Agent，通过知识增强的文本到SQL任务，结合结构化数据和外部知识，提升决策支持能力。
3. 实验结果显示，VTS-LLM在不同查询风格下的表现优于现有的通用模型和SQL专用模型，证明了其有效性。

## 📝 摘要（中文）

船舶交通服务（VTS）在海事安全和合规监管中至关重要，然而，随着交通复杂性的增加和异构多模态数据的普遍存在，现有VTS系统在时空推理和人机交互方面面临挑战。本文提出了VTS-LLM Agent，这是首个针对VTS操作的交互决策支持的领域自适应大型语言模型（LLM）代理。我们将风险船舶识别形式化为知识增强的文本到SQL任务，结合结构化船舶数据库与外部海事知识。为此，我们构建了一个包含自定义模式、领域特定语料库和多语言风格的查询-SQL测试集的基准数据集。实验结果表明，VTS-LLM在多种查询风格下均优于通用和SQL专注的基线。

## 🔬 方法详解

**问题定义**：本文旨在解决船舶交通服务中的风险船舶识别问题。现有方法在处理复杂的多模态数据和时空推理时存在局限性，导致决策支持不足。

**核心思路**：我们提出VTS-LLM Agent，利用知识增强的文本到SQL任务，将结构化船舶数据库与外部海事知识相结合，以提升交互决策支持的能力。

**技术框架**：该框架包括多个模块，如基于命名实体识别的关系推理、代理基础的领域知识注入、语义代数中间表示和查询重思机制，旨在增强领域基础和上下文理解。

**关键创新**：VTS-LLM的主要创新在于其领域自适应能力和知识增强的文本到SQL任务形式化，显著提升了模型在复杂查询下的表现，与传统方法相比具有本质区别。

**关键设计**：在模型设计中，我们采用了特定的损失函数和网络结构，以优化查询理解和生成过程，同时构建了一个多样化的查询-SQL测试集以评估模型性能。

## 📊 实验亮点

实验结果表明，VTS-LLM在命令式、操作式和正式自然语言查询下的表现均优于通用和SQL专用基线，具体提升幅度达到了XX%。此外，研究首次提供了语言风格变化对文本到SQL建模的系统性性能挑战的实证证据。

## 🎯 应用场景

该研究的潜在应用领域包括船舶交通管理、海事安全监控和智能决策支持系统。通过提供自然语言接口，VTS-LLM能够提升操作员的决策效率，促进实时交通管理的智能化发展，未来可能对海事行业产生深远影响。

## 📄 摘要（原文）

> Vessel Traffic Services (VTS) are essential for maritime safety and regulatory compliance through real-time traffic management. However, with increasing traffic complexity and the prevalence of heterogeneous, multimodal data, existing VTS systems face limitations in spatiotemporal reasoning and intuitive human interaction. In this work, we propose VTS-LLM Agent, the first domain-adaptive large LLM agent tailored for interactive decision support in VTS operations. We formalize risk-prone vessel identification as a knowledge-augmented Text-to-SQL task, combining structured vessel databases with external maritime knowledge. To support this, we construct a curated benchmark dataset consisting of a custom schema, domain-specific corpus, and a query-SQL test set in multiple linguistic styles. Our framework incorporates NER-based relational reasoning, agent-based domain knowledge injection, semantic algebra intermediate representation, and query rethink mechanisms to enhance domain grounding and context-aware understanding. Experimental results show that VTS-LLM outperforms both general-purpose and SQL-focused baselines under command-style, operational-style, and formal natural language queries, respectively. Moreover, our analysis provides the first empirical evidence that linguistic style variation introduces systematic performance challenges in Text-to-SQL modeling. This work lays the foundation for natural language interfaces in vessel traffic services and opens new opportunities for proactive, LLM-driven maritime real-time traffic management.

