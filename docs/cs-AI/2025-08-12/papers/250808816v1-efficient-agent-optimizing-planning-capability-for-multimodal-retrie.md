---
layout: default
title: "Efficient Agent: Optimizing Planning Capability for Multimodal Retrieval Augmented Generation"
---

# Efficient Agent: Optimizing Planning Capability for Multimodal Retrieval Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08816" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08816v1</a>
  <a href="https://arxiv.org/pdf/2508.08816.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08816v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08816v1', 'Efficient Agent: Optimizing Planning Capability for Multimodal Retrieval Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuechen Wang, Yuming Qiao, Dan Meng, Jun Yang, Haonan Lu, Zhenyu Yang, Xudong Zhang

**分类**: cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出E-Agent以优化多模态检索增强生成的规划能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `增强生成` `规划能力` `动态决策` `信息检索` `E-Agent` `RemPlan基准` `工具感知执行`

## 📋 核心要点

1. 现有mRAG方法在检索策略上较为僵化，且未能充分利用视觉信息，导致性能受限。
2. 本文提出E-Agent框架，通过动态协调多模态工具和优化执行顺序，提升mRAG的规划能力。
3. 实验结果表明，E-Agent在准确率上较现有方法提升13%，同时减少冗余搜索37%，显示出显著的性能改进。

## 📝 摘要（中文）

多模态检索增强生成（mRAG）作为解决多模态大型语言模型（MLLMs）在现实场景中时间限制的有效方案，面临着检索策略僵化和视觉信息利用不足的问题。为此，本文提出了E-Agent框架，包含两个关键创新：一个基于上下文推理动态协调多模态工具的mRAG规划器，以及一个采用工具感知执行顺序的任务执行器，以优化mRAG工作流。E-Agent采用一次性mRAG规划策略，实现高效信息检索，减少冗余工具调用。为严格评估mRAG系统的规划能力，本文引入了真实世界mRAG规划（RemPlan）基准，包含检索依赖和独立问题类型，系统标注每个实例所需的检索工具。实验结果显示，E-Agent在RemPlan及三个已建立基准上表现优越，准确率较最先进的mRAG方法提升13%，冗余搜索减少37%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态检索增强生成（mRAG）方法在检索策略僵化和视觉信息利用不足的问题，这限制了其在实际应用中的有效性。

**核心思路**：E-Agent框架通过引入动态规划和工具感知执行顺序，优化了mRAG的工作流，使其能够在上下文推理的基础上更有效地调用多模态工具。

**技术框架**：E-Agent的整体架构包括两个主要模块：mRAG规划器和任务执行器。规划器负责根据上下文动态选择工具，而执行器则确保按照优化的顺序执行任务，从而提高效率。

**关键创新**：E-Agent的核心创新在于其一次性mRAG规划策略和工具感知执行顺序，这与现有方法的静态检索策略形成鲜明对比，显著提升了信息检索的效率和准确性。

**关键设计**：在设计中，E-Agent采用了明确的mRAG规划注释和多样化的问题设计，以增强其实用性，并通过RemPlan基准对其性能进行严格评估。

## 📊 实验亮点

E-Agent在RemPlan基准测试中表现出色，较最先进的mRAG方法准确率提升13%，同时冗余搜索减少37%。这一结果表明E-Agent在多模态信息检索和生成任务中的显著优势，具有较高的实用价值。

## 🎯 应用场景

E-Agent框架在新闻分析、趋势话题处理等多模态信息检索场景中具有广泛的应用潜力。其优化的规划能力能够有效提升信息检索的效率和准确性，未来可扩展至更多需要动态决策的领域，如智能客服和自动化内容生成等。

## 📄 摘要（原文）

> Multimodal Retrieval-Augmented Generation (mRAG) has emerged as a promising solution to address the temporal limitations of Multimodal Large Language Models (MLLMs) in real-world scenarios like news analysis and trending topics. However, existing approaches often suffer from rigid retrieval strategies and under-utilization of visual information. To bridge this gap, we propose E-Agent, an agent framework featuring two key innovations: a mRAG planner trained to dynamically orchestrate multimodal tools based on contextual reasoning, and a task executor employing tool-aware execution sequencing to implement optimized mRAG workflows. E-Agent adopts a one-time mRAG planning strategy that enables efficient information retrieval while minimizing redundant tool invocations. To rigorously assess the planning capabilities of mRAG systems, we introduce the Real-World mRAG Planning (RemPlan) benchmark. This novel benchmark contains both retrieval-dependent and retrieval-independent question types, systematically annotated with essential retrieval tools required for each instance. The benchmark's explicit mRAG planning annotations and diverse question design enhance its practical relevance by simulating real-world scenarios requiring dynamic mRAG decisions. Experiments across RemPlan and three established benchmarks demonstrate E-Agent's superiority: 13% accuracy gain over state-of-the-art mRAG methods while reducing redundant searches by 37%.

