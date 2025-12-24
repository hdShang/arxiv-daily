---
layout: default
title: "ArgCMV: An Argument Summarization Benchmark for the LLM-era"
---

# ArgCMV: An Argument Summarization Benchmark for the LLM-era

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19580" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19580v1</a>
  <a href="https://arxiv.org/pdf/2508.19580.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19580v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19580v1', 'ArgCMV: An Argument Summarization Benchmark for the LLM-era')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Omkar Gurjar, Agam Goyal, Eshwar Chandrasekharan

**分类**: cs.CL

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出ArgCMV数据集以解决现有论点摘要基准不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `论点摘要` `关键点提取` `大型语言模型` `数据集构建` `在线辩论` `复杂性分析` `基准测试`

## 📋 核心要点

1. 现有的关键点提取方法在ArgKP21数据集上评估，存在代表性不足和复杂性低的问题。
2. 本文提出了ArgCMV数据集，包含来自真实在线辩论的12K个论点，覆盖更广泛的主题和复杂性。
3. 实验结果表明，现有方法在ArgCMV数据集上的表现不佳，推动了对新基准的需求和研究方向的探索。

## 📝 摘要（中文）

关键点提取是论点摘要中的重要任务，涉及从论点中提取高层次的简短摘要。现有的关键点提取方法主要在流行的ArgKP21数据集上进行评估。本文指出了ArgKP21数据集的一些主要局限性，并展示了需要更具代表性的新基准。我们使用最先进的大型语言模型（LLMs），策划了一个新的论点关键点提取数据集ArgCMV，包含约12K个来自实际在线人类辩论的论点，覆盖3000多个主题。我们的数据集展现了更高的复杂性，包括更长的共指论点、更高的主观话语单元的存在，以及比ArgKP21更广泛的主题范围。我们展示了现有方法在ArgCMV上适应性不佳，并通过对现有基线和最新开源模型的实验提供了广泛的基准结果。此项工作为长上下文在线讨论的关键点提取数据集引入了新视角，为下一代基于LLM的摘要研究奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决现有论点摘要基准（ArgKP21）在代表性和复杂性方面的不足，现有方法在处理真实人类对话时表现不佳。

**核心思路**：通过使用最先进的大型语言模型（LLMs），本文策划了一个新的数据集ArgCMV，以更好地反映实际在线辩论的复杂性和多样性。

**技术框架**：ArgCMV数据集的构建流程包括数据收集、筛选和标注，确保涵盖多样的主题和复杂的论点结构。

**关键创新**：ArgCMV数据集的最大创新在于其高复杂性和多样性，包含长篇共指论点和主观话语单元，显著区别于ArgKP21的简单结构。

**关键设计**：在数据集构建过程中，采用了严格的筛选标准和标注指南，以确保数据的质量和代表性，同时使用了最新的开源模型进行基准测试。

## 📊 实验亮点

实验结果显示，现有的关键点提取方法在ArgCMV数据集上的性能显著低于预期，表明现有技术在处理复杂在线讨论时的局限性。这一发现强调了ArgCMV作为新基准的重要性，并为未来的研究提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括在线辩论分析、社交媒体内容摘要和自动化信息提取等。通过提供更具代表性和复杂性的数据集，ArgCMV为未来的LLM驱动的摘要研究奠定了基础，推动了相关领域的进步与发展。

## 📄 摘要（原文）

> Key point extraction is an important task in argument summarization which involves extracting high-level short summaries from arguments. Existing approaches for KP extraction have been mostly evaluated on the popular ArgKP21 dataset. In this paper, we highlight some of the major limitations of the ArgKP21 dataset and demonstrate the need for new benchmarks that are more representative of actual human conversations. Using SoTA large language models (LLMs), we curate a new argument key point extraction dataset called ArgCMV comprising of around 12K arguments from actual online human debates spread across over 3K topics. Our dataset exhibits higher complexity such as longer, co-referencing arguments, higher presence of subjective discourse units, and a larger range of topics over ArgKP21. We show that existing methods do not adapt well to ArgCMV and provide extensive benchmark results by experimenting with existing baselines and latest open source models. This work introduces a novel KP extraction dataset for long-context online discussions, setting the stage for the next generation of LLM-driven summarization research.

