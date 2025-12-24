---
layout: default
title: "BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent"
---

# BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06600" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06600v1</a>
  <a href="https://arxiv.org/pdf/2508.06600.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06600v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06600v1', 'BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping Nie, Kai Zou, Andrew Liu, Joshua Green, Kshama Patel, Ruoxi Meng, Mingyi Su, Sahel Sharifymoghaddam, Yanxi Li, Haoran Hong, Xinyu Shi, Xuye Liu, Nandan Thakur, Crystina Zhang, Luyu Gao, Wenhu Chen, Jimmy Lin

**分类**: cs.CL, cs.IR

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出BrowseComp-Plus以解决深度研究代理评估的公平性与透明性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度研究代理` `评估基准` `大型语言模型` `信息检索` `公平性` `透明性` `可控实验`

## 📋 核心要点

1. 现有的评估基准如BrowseComp依赖于动态的黑箱网络搜索API，导致公平性和透明性不足，难以进行可重复的实验。
2. 本文提出BrowseComp-Plus基准，通过使用固定的文档库和人工验证的支持文档，解决了现有方法的评估问题。
3. 实验结果显示，结合GPT-5与Qwen3-Embedding-8B检索器的模型准确性提升至70.1%，显著优于其他模型。

## 📝 摘要（中文）

深度研究代理通过整合大型语言模型与搜索工具，提升了处理复杂查询的能力。然而，现有的评估基准如BrowseComp存在公平性和透明性不足的问题。为此，本文提出了BrowseComp-Plus基准，采用固定的、精心策划的文档库，使得每个查询都包含经过人工验证的支持文档和具有挑战性的负样本，从而实现了可控实验。该基准有效区分了深度研究系统的性能，展示了不同模型的准确性提升，促进了对检索有效性和引用准确性的深入分析。

## 🔬 方法详解

**问题定义**：现有的深度研究代理评估方法依赖于动态的网络搜索API，导致公平性和透明性不足，难以进行有效的性能比较和可重复实验。

**核心思路**：本文提出BrowseComp-Plus基准，采用固定且经过精心策划的文档库，使得每个查询都能包含经过人工验证的支持文档和具有挑战性的负样本，从而实现可控实验。

**技术框架**：BrowseComp-Plus的整体架构包括固定文档库的构建、查询设计、支持文档的验证以及负样本的挖掘，确保每次实验的可控性和可重复性。

**关键创新**：该基准的最大创新在于通过固定文档库和人工验证的支持文档，解决了现有评估方法中的公平性和透明性问题，使得对深度研究代理的性能评估更加准确和可靠。

**关键设计**：在参数设置上，BrowseComp-Plus确保了文档库的多样性和代表性，损失函数设计上注重检索效果与引用准确性的平衡，网络结构则采用了先进的检索模型以提升整体性能。

## 📊 实验亮点

实验结果显示，使用BrowseComp-Plus基准的模型在准确性上有显著提升。例如，结合BM25检索器的开源模型Search-R1的准确性为3.86%，而GPT-5的准确性达到了55.9%。进一步结合Qwen3-Embedding-8B检索器后，准确性提升至70.1%，显示出该基准在评估深度研究代理性能方面的有效性。

## 🎯 应用场景

BrowseComp-Plus基准具有广泛的应用潜力，特别是在深度学习和自然语言处理领域的研究中。它可以用于评估和比较不同深度研究代理的性能，帮助研究人员更好地理解和改进检索系统的有效性。此外，该基准还可为相关领域的实际应用提供支持，如智能问答系统和信息检索。未来，该研究可能推动深度研究代理的标准化评估方法的发展。

## 📄 摘要（原文）

> Deep-Research agents, which integrate large language models (LLMs) with search tools, have shown success in improving the effectiveness of handling complex queries that require iterative search planning and reasoning over search results. Evaluations on current benchmarks like BrowseComp relies on black-box live web search APIs, have notable limitations in (1) fairness: dynamic and opaque web APIs hinder fair comparisons and reproducibility of deep research methods; (2) transparency: lack of control over the document corpus makes it difficult to isolate retriever contributions. In other words, the current evaluations may compare a complete deep research system at a given time, but they do not foster well-controlled experiments to provide insights into the capability of underlying deep research LLMs. To address these challenges, we introduce BrowseComp-Plus, a benchmark derived from BrowseComp, employing a fixed, carefully curated corpus. Each query in BrowseComp-Plus includes human-verified supporting documents and mined challenging negatives, enabling controlled experimentation. The benchmark is shown to be effective in distinguishing the performance of deep research systems. For instance, the open-source model Search-R1, when paired with the BM25 retriever, achieves 3.86% accuracy, whereas the GPT-5 achieves 55.9%. Integrating the GPT-5 with the Qwen3-Embedding-8B retriever further enhances its accuracy to 70.1% with fewer search calls. This benchmark allows comprehensive evaluation and disentangled analysis of deep research agents and retrieval methods, fostering insights into retrieval effectiveness, citation accuracy, and context engineering in Deep-Research system.

