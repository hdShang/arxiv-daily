---
layout: default
title: "DynamicBench: Evaluating Real-Time Report Generation in Large Language Models"
---

# DynamicBench: Evaluating Real-Time Report Generation in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21343" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21343v1</a>
  <a href="https://arxiv.org/pdf/2506.21343.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21343v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21343v1', 'DynamicBench: Evaluating Real-Time Report Generation in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyao Li, Hao Sun, Zile Qiao, Yong Jiang, Pengjun Xie, Fei Huang, Hong Xu, Jiaya Jia

**分类**: cs.LG

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出DynamicBench以解决实时信息处理评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `实时信息处理` `动态评估` `报告生成` `双路径检索` `领域特定知识` `性能提升`

## 📋 核心要点

1. 核心问题：现有的基准测试方法无法满足实时信息处理的动态需求，导致评估结果不够全面。
2. 方法要点：DynamicBench通过双路径检索管道，结合网络搜索与本地数据库，评估LLMs在动态数据处理中的能力。
3. 实验或效果：实验结果显示，DynamicBench在无文档和有文档场景下的性能分别比GPT4o提升了7.0%和5.8%。

## 📝 摘要（中文）

传统的大型语言模型（LLMs）基准测试通常依赖于静态评估，如讲故事或表达观点，这无法捕捉当代应用中实时信息处理的动态需求。为了解决这一局限性，我们提出了DynamicBench，一个旨在评估LLMs在存储和处理最新数据方面能力的基准。DynamicBench利用双路径检索管道，将网络搜索与本地报告数据库相结合，要求领域特定知识，以确保在专业领域内生成准确的响应报告。通过在提供或不提供外部文档的场景中评估模型，DynamicBench有效衡量它们独立处理最新信息或利用上下文增强的能力。此外，我们还引入了一种先进的报告生成系统，能够有效管理动态信息的综合。实验结果表明，我们的方法在无文档和有文档的场景中分别超越GPT4o 7.0%和5.8%的表现，验证了其有效性。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统基准测试无法有效评估大型语言模型在实时信息处理中的能力这一问题。现有方法主要依赖静态评估，无法反映模型在动态环境中的表现。

**核心思路**：DynamicBench的核心思路是通过双路径检索管道，将网络搜索与本地报告数据库结合，确保模型能够在特定领域内生成准确的报告，并有效处理最新信息。

**技术框架**：DynamicBench的整体架构包括两个主要模块：一是实时网络搜索模块，二是本地数据库检索模块。模型在这两个模块之间切换，以获取最新信息或依赖已有数据进行报告生成。

**关键创新**：最重要的技术创新在于引入了双路径检索机制，使得模型能够在不同场景下灵活应对信息需求。这一设计与传统的静态评估方法有本质区别，能够更好地适应动态信息处理的需求。

**关键设计**：在技术细节上，DynamicBench采用了特定领域的知识图谱，以提高信息检索的准确性。同时，损失函数设计上考虑了实时反馈机制，以优化模型在动态环境下的表现。

## 📊 实验亮点

实验结果显示，DynamicBench在无文档和有文档的场景下分别超越了GPT4o 7.0%和5.8%的性能，验证了其在实时信息处理中的有效性。这一成果为大型语言模型的评估提供了新的视角和方法。

## 🎯 应用场景

该研究的潜在应用领域包括新闻报道、实时数据分析和智能客服等场景，能够帮助相关领域的从业者更高效地生成和处理信息。未来，DynamicBench有望推动大型语言模型在动态信息处理方面的进一步发展，提升其在实际应用中的价值。

## 📄 摘要（原文）

> Traditional benchmarks for large language models (LLMs) typically rely on static evaluations through storytelling or opinion expression, which fail to capture the dynamic requirements of real-time information processing in contemporary applications. To address this limitation, we present DynamicBench, a benchmark designed to evaluate the proficiency of LLMs in storing and processing up-to-the-minute data. DynamicBench utilizes a dual-path retrieval pipeline, integrating web searches with local report databases. It necessitates domain-specific knowledge, ensuring accurate responses report generation within specialized fields. By evaluating models in scenarios that either provide or withhold external documents, DynamicBench effectively measures their capability to independently process recent information or leverage contextual enhancements. Additionally, we introduce an advanced report generation system adept at managing dynamic information synthesis. Our experimental results confirm the efficacy of our approach, with our method achieving state-of-the-art performance, surpassing GPT4o in document-free and document-assisted scenarios by 7.0% and 5.8%, respectively. The code and data will be made publicly available.

