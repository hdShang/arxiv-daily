---
layout: default
title: Vgent: Graph-based Retrieval-Reasoning-Augmented Generation For Long Video Understanding
---

# Vgent: Graph-based Retrieval-Reasoning-Augmented Generation For Long Video Understanding

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14032" target="_blank" class="toolbar-btn">arXiv: 2510.14032v1</a>
    <a href="https://arxiv.org/pdf/2510.14032.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14032v1" 
            onclick="toggleFavorite(this, '2510.14032v1', 'Vgent: Graph-based Retrieval-Reasoning-Augmented Generation For Long Video Understanding')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xiaoqian Shen, Wenxuan Zhang, Jun Chen, Mohamed Elhoseiny

**分类**: cs.CV

**发布日期**: 2025-10-15

**备注**: NeurIPS 2025 (Spotlight). Webpage at https://xiaoqian-shen.github.io/Vgent

**🔗 代码/项目**: [PROJECT_PAGE](https://xiaoqian-shen.github.io/Vgent)

---

## 💡 一句话要点

**提出Vgent，通过图结构检索-推理增强生成，提升长视频理解能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `图结构` `检索增强生成` `视频推理` `视频问答`

## 📋 核心要点

1. 现有LVLMs难以处理长视频中大量的tokens，并且难以保持长期的时序信息，导致理解和推理能力受限。
2. Vgent通过构建视频片段的图结构，并引入中间推理步骤，增强检索的有效性和推理的准确性，从而提升长视频理解能力。
3. 实验结果表明，Vgent在长视频理解基准测试中显著优于现有方法，并在MLVU上取得了3.0%~5.4%的性能提升。

## 📝 摘要（中文）

针对大型视频语言模型(LVLMs)在处理长视频时，因上下文窗口限制和长期序列信息保持困难而面临的挑战，本文提出了一种基于图结构的检索-推理增强生成框架Vgent，以提升LVLMs的长视频理解能力。该方法引入了两项关键创新：(i) 使用结构化图表示视频，保留视频片段之间的语义关系，从而提高检索效率。(ii) 引入中间推理步骤，缓解LVLMs的推理限制，利用结构化验证减少检索噪声，并促进跨片段相关信息的显式聚合，从而产生更准确和上下文感知的响应。在三个长视频理解基准测试中，对各种开源LVLMs进行了全面评估。结果表明，该方法在MLVU上相对于基线模型实现了3.0%~5.4%的整体性能提升，并且优于最先进的视频RAG方法8.6%。代码已公开。

## 🔬 方法详解

**问题定义**：长视频理解任务对LVLMs提出了挑战，因为它们难以处理超出上下文窗口限制的大量视频tokens，并且难以保持长期的时序信息。现有的检索增强生成(RAG)方法在处理长视频时，可能会破坏时间依赖性，并包含不相关的信息，从而阻碍准确的推理。

**核心思路**：Vgent的核心思路是利用图结构来表示视频，从而保留视频片段之间的语义关系，提高检索效率。此外，引入中间推理步骤，利用结构化验证来减少检索噪声，并促进跨片段相关信息的显式聚合，从而提高推理的准确性。

**技术框架**：Vgent框架包含以下主要模块：1) 视频片段提取和特征编码；2) 基于语义关系的图构建，节点代表视频片段，边代表片段间的关系；3) 基于图结构的检索，根据查询检索相关片段；4) 中间推理步骤，对检索结果进行结构化验证和信息聚合；5) 生成模块，根据推理结果生成最终答案。

**关键创新**：Vgent的关键创新在于：1) 使用图结构来表示视频，从而更好地保留视频片段之间的语义关系，提高检索效率；2) 引入中间推理步骤，利用结构化验证来减少检索噪声，并促进跨片段相关信息的显式聚合，从而提高推理的准确性。与现有方法的本质区别在于，Vgent更加注重视频片段之间的关系和信息的聚合。

**关键设计**：图结构的构建方式是关键设计之一，例如如何定义节点和边，如何计算边的权重等。中间推理步骤的具体实现方式，例如使用什么样的结构化验证方法，如何进行信息聚合等，也是关键设计。论文中可能还涉及一些超参数的设置，例如图的节点数量、边的权重阈值等，这些参数的设置也会影响最终的性能。

## 📊 实验亮点

Vgent在三个长视频理解基准测试中进行了评估，结果表明，Vgent在MLVU上相对于基线模型实现了3.0%~5.4%的整体性能提升，并且优于最先进的视频RAG方法8.6%。这些结果表明，Vgent能够有效地提高长视频理解能力。

## 🎯 应用场景

Vgent可应用于智能监控、视频搜索、视频摘要、视频问答等领域。例如，在智能监控中，可以利用Vgent对监控视频进行分析，快速定位异常事件。在视频搜索中，可以利用Vgent提高搜索的准确性和效率。在视频摘要中，可以利用Vgent提取视频的关键信息，生成简洁的摘要。在视频问答中，可以利用Vgent回答用户提出的关于视频内容的问题。

## 📄 摘要（原文）

> Understanding and reasoning over long videos pose significant challenges for large video language models (LVLMs) due to the difficulty in processing intensive video tokens beyond context window and retaining long-term sequential information. Retrieval-Augmented Generation (RAG) has demonstrated effectiveness in processing long context for Large Language Models (LLMs); however, applying RAG to long video faces challenges such as disrupted temporal dependencies and inclusion of irrelevant information that can hinder accurate reasoning. To address these limitations, we propose Vgent, a novel graph-based retrieval-reasoning-augmented generation framework to enhance LVLMs for long video understanding. Our approach introduces two key innovations: (i) It represents videos by structured graphs with semantic relationships across video clips preserved to improve retrieval effectiveness. (ii) It introduces an intermediate reasoning step to mitigate the reasoning limitation of LVLMs, which leverages structured verification to reduce retrieval noise and facilitate the explicit aggregation of relevant information across clips, resulting in more accurate and context-aware responses. We comprehensively evaluate our framework with various open-source LVLMs on three long-video understanding benchmarks. Our approach yielded an overall performance improvement of $3.0\%\sim 5.4\%$ over base models on MLVU, and outperformed state-of-the-art video RAG methods by $8.6\%$. Our code is publicly available at https://xiaoqian-shen.github.io/Vgent.

