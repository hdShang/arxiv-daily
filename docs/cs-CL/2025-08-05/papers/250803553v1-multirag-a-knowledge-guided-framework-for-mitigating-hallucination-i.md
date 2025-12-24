---
layout: default
title: "MultiRAG: A Knowledge-guided Framework for Mitigating Hallucination in Multi-source Retrieval Augmented Generation"
---

# MultiRAG: A Knowledge-guided Framework for Mitigating Hallucination in Multi-source Retrieval Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03553" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03553v1</a>
  <a href="https://arxiv.org/pdf/2508.03553.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03553v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03553v1', 'MultiRAG: A Knowledge-guided Framework for Mitigating Hallucination in Multi-source Retrieval Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenlong Wu, Haofen Wang, Bohan Li, Peixuan Huang, Xinzhe Zhao, Lei Liang

**分类**: cs.IR, cs.CL

**发布日期**: 2025-08-05

**备注**: Accepted by ICDE 2025 Research Paper

**期刊**: In 2025 IEEE 41st International Conference on Data Engineering (ICDE), Hong Kong, 2025, pp. 3070-3083

**DOI**: [10.1109/ICDE65448.2025.00230](https://doi.org/10.1109/ICDE65448.2025.00230)

**🔗 代码/项目**: [GITHUB](https://github.com/wuwenlong123/MultiRAG)

---

## 💡 一句话要点

**提出MultiRAG以解决多源检索增强生成中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `多源数据` `幻觉问题` `知识引导` `多层次置信度` `信息检索` `智能问答`

## 📋 核心要点

1. 现有的检索增强生成方法在多源数据整合时面临稀疏分布和信息冲突等挑战，导致幻觉现象加剧。
2. 本文提出MultiRAG框架，通过知识引导的方法，利用多源线图和多层次置信度计算来解决幻觉问题。
3. 在四个多领域查询数据集和两个多跳问答数据集上的实验结果表明，MultiRAG在知识检索的可靠性和效率上有显著提升。

## 📝 摘要（中文）

检索增强生成（RAG）已成为解决大型语言模型（LLMs）幻觉问题的有前景的解决方案。然而，多源检索的整合虽然可能提供更多信息，却也引入了新的挑战，反而可能加剧幻觉问题。这些挑战主要体现在两个方面：多源数据的稀疏分布妨碍了逻辑关系的捕捉，以及不同来源之间固有的不一致性导致信息冲突。为了解决这些挑战，本文提出了MultiRAG，一个通过知识引导的方法来减轻多源检索增强生成中的幻觉问题的框架。我们的框架引入了两个关键创新：一是知识构建模块，利用多源线图有效聚合不同知识源之间的逻辑关系，解决稀疏数据分布问题；二是复杂的检索模块，实现多层次的置信度计算机制，进行图层和节点级评估，以识别和消除不可靠的信息节点，从而减少由源间不一致性引起的幻觉。大量实验表明，MultiRAG显著提高了复杂多源场景下知识检索的可靠性和效率。

## 🔬 方法详解

**问题定义**：本文旨在解决多源检索增强生成中的幻觉问题，现有方法在整合多源数据时，因数据稀疏和信息冲突而导致生成内容的不可靠性。

**核心思路**：MultiRAG框架通过知识引导的方式，利用多源线图聚合逻辑关系，并通过多层次置信度计算机制来识别和消除不可靠信息，从而减轻幻觉现象。

**技术框架**：MultiRAG的整体架构包括两个主要模块：知识构建模块和检索模块。知识构建模块负责聚合不同知识源的逻辑关系，而检索模块则进行信息的评估和筛选。

**关键创新**：MultiRAG的创新在于引入了多源线图来有效聚合逻辑关系，并实现了图层和节点级的置信度计算机制，这与现有方法的单一源检索和简单置信度评估有本质区别。

**关键设计**：在设计上，MultiRAG使用了多源线图结构来表示知识源之间的关系，并通过设置合理的置信度阈值来筛选信息节点，确保生成内容的可靠性。

## 📊 实验亮点

在实验中，MultiRAG在四个多领域查询数据集和两个多跳问答数据集上表现出色，相较于基线方法，其知识检索的可靠性和效率显著提升，具体性能数据未提供，但提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和对话生成等。通过提高多源信息整合的可靠性，MultiRAG能够在复杂场景中提供更准确的生成结果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Retrieval Augmented Generation (RAG) has emerged as a promising solution to address hallucination issues in Large Language Models (LLMs). However, the integration of multiple retrieval sources, while potentially more informative, introduces new challenges that can paradoxically exacerbate hallucination problems. These challenges manifest primarily in two aspects: the sparse distribution of multi-source data that hinders the capture of logical relationships and the inherent inconsistencies among different sources that lead to information conflicts. To address these challenges, we propose MultiRAG, a novel framework designed to mitigate hallucination in multi-source retrieval-augmented generation through knowledge-guided approaches. Our framework introduces two key innovations: (1) a knowledge construction module that employs multi-source line graphs to efficiently aggregate logical relationships across different knowledge sources, effectively addressing the sparse data distribution issue; and (2) a sophisticated retrieval module that implements a multi-level confidence calculation mechanism, performing both graph-level and node-level assessments to identify and eliminate unreliable information nodes, thereby reducing hallucinations caused by inter-source inconsistencies. Extensive experiments on four multi-domain query datasets and two multi-hop QA datasets demonstrate that MultiRAG significantly enhances the reliability and efficiency of knowledge retrieval in complex multi-source scenarios. \textcolor{blue}{Our code is available in https://github.com/wuwenlong123/MultiRAG.

