---
layout: default
title: "Powering Job Search at Scale: LLM-Enhanced Query Understanding in Job Matching Systems"
---

# Powering Job Search at Scale: LLM-Enhanced Query Understanding in Job Matching Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09690" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09690v1</a>
  <a href="https://arxiv.org/pdf/2509.09690.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09690v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09690v1', 'Powering Job Search at Scale: LLM-Enhanced Query Understanding in Job Matching Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ping Liu, Jianqiang Shen, Qianqi Shen, Chunnan Yao, Kevin Kao, Dan Xu, Rajat Arora, Baofen Zheng, Caleb Johnson, Liangjie Hong, Jingwei Wu, Wenjing Zhang

**分类**: cs.IR, cs.LG

**发布日期**: 2025-08-19

**备注**: CIKM2025

**DOI**: [10.1145/3746252.3760913](https://doi.org/10.1145/3746252.3760913)

---

## 💡 一句话要点

**提出统一查询理解框架以提升招聘匹配系统的效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `查询理解` `大型语言模型` `招聘匹配` `个性化推荐` `系统复杂性`

## 📋 核心要点

1. 现有方法依赖多个任务特定的命名实体识别模型，导致系统脆弱且难以维护。
2. 提出的框架利用大型语言模型，联合建模用户查询和上下文信号，生成结构化解释。
3. 实验结果显示，该方法在相关性质量上有显著提升，并降低了系统复杂性。

## 📝 摘要（中文）

查询理解在现代相关性系统中至关重要，用户查询通常短小、模糊且高度依赖上下文。传统方法依赖多个特定任务的命名实体识别模型来提取结构化信息，导致架构脆弱、维护成本高且适应性差。本文提出了一种由大型语言模型（LLM）驱动的统一查询理解框架，旨在解决这些问题。该方法联合建模用户查询和上下文信号，如个人资料属性，以生成结构化解释，从而提供更准确和个性化的推荐。实验结果表明，该框架在在线A/B测试中显著提高了相关性质量，同时减少了系统复杂性和运营开销。

## 🔬 方法详解

**问题定义**：本文解决的是招聘匹配系统中查询理解的挑战，现有方法依赖多个特定任务的模型，导致系统脆弱且难以适应变化的语言模式和分类法。

**核心思路**：提出的统一查询理解框架通过大型语言模型（LLM）联合建模用户查询和上下文信息，旨在生成更准确的结构化解释，以提高推荐的个性化和相关性。

**技术框架**：框架包括用户查询输入、上下文信号提取和结构化解释生成三个主要模块。用户查询与个人资料属性等上下文信息共同输入LLM，生成结构化输出。

**关键创新**：最重要的创新在于将大型语言模型应用于查询理解，打破了传统方法的碎片化架构，实现了更高的适应性和可扩展性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化结构化输出的准确性，并通过调优模型参数以适应不同的查询类型和上下文信息。具体的网络结构和参数设置在实验中进行了详细验证。

## 📊 实验亮点

实验结果表明，提出的框架在在线A/B测试中显著提高了相关性质量，相较于传统方法，系统复杂性和运营开销大幅降低，展示了良好的可扩展性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括招聘平台、在线求职系统和其他需要高效查询理解的动态网络应用。通过提供更准确的推荐，该框架可以显著提升用户体验和满意度，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Query understanding is essential in modern relevance systems, where user queries are often short, ambiguous, and highly context-dependent. Traditional approaches often rely on multiple task-specific Named Entity Recognition models to extract structured facets as seen in job search applications. However, this fragmented architecture is brittle, expensive to maintain, and slow to adapt to evolving taxonomies and language patterns. In this paper, we introduce a unified query understanding framework powered by a Large Language Model (LLM), designed to address these limitations. Our approach jointly models the user query and contextual signals such as profile attributes to generate structured interpretations that drive more accurate and personalized recommendations. The framework improves relevance quality in online A/B testing while significantly reducing system complexity and operational overhead. The results demonstrate that our solution provides a scalable and adaptable foundation for query understanding in dynamic web applications.

