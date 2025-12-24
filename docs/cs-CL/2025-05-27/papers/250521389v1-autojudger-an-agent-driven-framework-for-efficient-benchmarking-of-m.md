---
layout: default
title: "AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs"
---

# AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21389" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21389v1</a>
  <a href="https://arxiv.org/pdf/2505.21389.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21389v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21389v1', 'AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuanwen Ding, Chengjun Pan, Zejun Li, Jiwen Zhang, Siyuan Wang, Zhongyu Wei

**分类**: cs.CL

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出AutoJudger以解决多模态大语言模型评估成本高的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `评估框架` `项目反应理论` `动态选择` `语义感知检索` `动态记忆` `评估效率` `机器学习`

## 📋 核心要点

1. 现有的多模态大语言模型评估方法面临高昂的成本和复杂性，难以高效处理。
2. AutoJudger通过引入项目反应理论和自主评估代理，动态选择最具信息量的问题，提升评估效率。
3. 实验结果显示，AutoJudger仅使用4%的数据便可实现超过90%的排名准确率，显著降低评估开销。

## 📝 摘要（中文）

随着多模态大语言模型（MLLMs）基准测试规模和跨模态复杂性的增加，评估成本日益高昂。为了解决这一难题，本文提出了AutoJudger，一个基于代理的高效自适应评估框架。AutoJudger采用项目反应理论（IRT）来估计问题难度，并通过自主评估代理动态选择最具信息量的测试问题。该框架包含两个关键组件：语义感知检索机制确保所选问题涵盖视觉和语言模态中的多样化和挑战性场景，以及动态记忆模块维护先前评估问题的上下文统计，以指导整个评估过程中的一致性和全局信息问题选择。大量实验表明，AutoJudger在四个代表性多模态基准上显著降低了评估成本，仅使用4%的数据便可在MMT-Bench的完整评估中实现超过90%的排名准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型评估中成本高、效率低的问题。现有方法在处理复杂基准测试时，往往需要大量的评分资源，导致评估过程不够高效。

**核心思路**：AutoJudger的核心思路是通过引入项目反应理论（IRT）和自主评估代理，动态选择最具挑战性和信息量的问题，从而降低评估成本并提高评估效率。

**技术框架**：AutoJudger的整体架构包括两个主要模块：语义感知检索机制和动态记忆模块。前者确保所选问题覆盖多样化的场景，后者维护上下文统计以指导问题选择。

**关键创新**：AutoJudger的创新点在于其动态选择问题的能力，通过实时性能反馈来优化评估过程。这一方法与传统静态评估方法本质上不同，能够更灵活地应对不同模型的表现。

**关键设计**：在设计上，AutoJudger使用IRT来评估问题难度，并通过动态记忆模块记录先前问题的统计信息，以确保问题选择的连贯性和有效性。

## 📊 实验亮点

实验结果显示，AutoJudger在四个多模态基准上仅使用4%的数据便实现了超过90%的排名准确率，相较于传统方法显著降低了评估开销，展现出极高的评估效率。

## 🎯 应用场景

该研究的潜在应用领域包括多模态人工智能系统的评估、教育领域的自适应测试以及机器学习模型的性能监测。通过降低评估成本，AutoJudger能够使得更广泛的研究者和开发者能够高效地评估和优化其模型，推动相关技术的进步。

## 📄 摘要（原文）

> Evaluating multimodal large language models (MLLMs) is increasingly expensive, as the growing size and cross-modality complexity of benchmarks demand significant scoring efforts. To tackle with this difficulty, we introduce AutoJudger, an agent-driven framework for efficient and adaptive benchmarking of MLLMs that tackles this escalating cost. AutoJudger employs the Item Response Theory (IRT) to estimate the question difficulty and an autonomous evaluation agent to dynamically select the most informative test questions based on the model's real-time performance. Specifically, AutoJudger incorporates two pivotal components: a semantic-aware retrieval mechanism to ensure that selected questions cover diverse and challenging scenarios across both vision and language modalities, and a dynamic memory that maintains contextual statistics of previously evaluated questions to guide coherent and globally informed question selection throughout the evaluation process. Extensive experiments on four representative multimodal benchmarks demonstrate that our adaptive framework dramatically reduces evaluation expenses, i.e. AutoJudger uses only 4% of the data to achieve over 90% ranking accuracy with the full benchmark evaluation on MMT-Bench.

