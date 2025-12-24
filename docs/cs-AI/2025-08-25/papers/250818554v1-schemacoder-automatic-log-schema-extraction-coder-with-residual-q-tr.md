---
layout: default
title: "SchemaCoder: Automatic Log Schema Extraction Coder with Residual Q-Tree Boosting"
---

# SchemaCoder: Automatic Log Schema Extraction Coder with Residual Q-Tree Boosting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18554" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18554v1</a>
  <a href="https://arxiv.org/pdf/2508.18554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18554v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18554v1', 'SchemaCoder: Automatic Log Schema Extraction Coder with Residual Q-Tree Boosting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lily Jiaxin Wan, Chia-Tung Ho, Rongjian Liang, Cunxi Yu, Deming Chen, Haoxing Ren

**分类**: cs.AI

**发布日期**: 2025-08-25

**备注**: 18 pages, 16 figures, under review for AAAI2026

---

## 💡 一句话要点

**提出SchemaCoder以解决日志模式提取的自动化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `日志模式提取` `自动化` `大型语言模型` `残差问答树` `机器学习` `数据分析` `系统监控`

## 📋 核心要点

1. 现有的日志模式提取方法依赖于预定义的正则表达式，需人工干预，限制了自动化程度和效率。
2. SchemaCoder通过引入残差问答树增强机制，实现了对日志模式的完全自动化提取，避免了人工定制的需求。
3. 在LogHub-2.0基准测试中，SchemaCoder的表现优于现有技术，平均提升21.3%，显示出其有效性和优越性。

## 📝 摘要（中文）

日志模式提取是从大量日志数据中提取人类可读模板的过程，尽管这一过程至关重要，但却极为耗时。近期研究尝试利用大型语言模型（LLMs）来自动化这一任务，但现有方法依赖于预定义的正则表达式，需人工领域专业知识，严重限制了生产力提升。为根本解决这一问题，本文提出了SchemaCoder，这是首个完全自动化的模式提取框架，适用于多种日志文件格式，无需人工定制。SchemaCoder的核心是新颖的残差问答树（Q-Tree）增强机制，通过针对性、适应性查询迭代优化模式提取。实验验证显示，SchemaCoder在广泛使用的LogHub-2.0基准上优于现有方法，平均提升21.3%。

## 🔬 方法详解

**问题定义**：本文旨在解决日志模式提取中的自动化问题，现有方法依赖于人工定义的正则表达式，导致效率低下和适应性差。

**核心思路**：SchemaCoder通过引入残差问答树增强机制，利用大型语言模型（LLMs）进行迭代优化，自动提取日志模式，避免人工干预。

**技术框架**：SchemaCoder的整体架构包括几个主要模块：首先，通过上下文限制分割将日志划分为语义块；其次，使用基于嵌入的采样选择代表性模式；最后，通过分层的问答树驱动的LLM查询生成模式代码，并通过文本残差进化优化器和残差增强进行迭代优化。

**关键创新**：SchemaCoder的核心创新在于其残差问答树增强机制，能够通过适应性查询不断优化模式提取过程，与传统方法相比，显著提高了自动化程度和准确性。

**关键设计**：在设计中，SchemaCoder采用了上下文限制分割技术，确保语义块的准确性；同时，嵌入式采样策略用于选择最具代表性的模式，增强了提取的有效性。

## 📊 实验亮点

在LogHub-2.0基准测试中，SchemaCoder的平均性能提升达21.3%，显著优于现有的最先进技术，展示了其在日志模式提取任务中的有效性和优势。

## 🎯 应用场景

SchemaCoder的潜在应用场景包括日志分析、故障检测和系统监控等领域。其自动化的模式提取能力能够显著提高日志数据处理的效率，降低人工干预的需求，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Log schema extraction is the process of deriving human-readable templates from massive volumes of log data, which is essential yet notoriously labor-intensive. Recent studies have attempted to streamline this task by leveraging Large Language Models (LLMs) for automated schema extraction. However, existing methods invariably rely on predefined regular expressions, necessitating human domain expertise and severely limiting productivity gains. To fundamentally address this limitation, we introduce SchemaCoder, the first fully automated schema extraction framework applicable to a wide range of log file formats without requiring human customization within the flow. At its core, SchemaCoder features a novel Residual Question-Tree (Q-Tree) Boosting mechanism that iteratively refines schema extraction through targeted, adaptive queries driven by LLMs. Particularly, our method partitions logs into semantic chunks via context-bounded segmentation, selects representative patterns using embedding-based sampling, and generates schema code through hierarchical Q-Tree-driven LLM queries, iteratively refined by our textual-residual evolutionary optimizer and residual boosting. Experimental validation demonstrates SchemaCoder's superiority on the widely-used LogHub-2.0 benchmark, achieving an average improvement of 21.3% over state-of-the-arts.

