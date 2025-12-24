---
layout: default
title: "QUPID: Quantified Understanding for Enhanced Performance, Insights, and Decisions in Korean Search Engines"
---

# QUPID: Quantified Understanding for Enhanced Performance, Insights, and Decisions in Korean Search Engines

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07345" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07345v1</a>
  <a href="https://arxiv.org/pdf/2505.07345.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07345v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07345v1', 'QUPID: Quantified Understanding for Enhanced Performance, Insights, and Decisions in Korean Search Engines')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ohjoon Kwon, Changsu Lee, Jihye Back, Lim Sun Suk, Inho Kang, Donghyeon Jeon

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-05-12

**期刊**: ACL 2025 Industry Track

---

## 💡 一句话要点

**提出QUPID以提升韩国搜索引擎的相关性评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息检索` `相关性评估` `小型语言模型` `模型组合` `计算效率` `搜索引擎` `架构设计`

## 📋 核心要点

1. 现有的相关性评估方法主要依赖大型语言模型，但在计算效率和准确性上存在不足。
2. QUPID通过结合生成式SLM与嵌入式SLM，提出了一种新颖的模型组合策略，以提高相关性评估的准确性。
3. 实验结果显示，QUPID在多个文档类型上表现出一致的性能提升，推理速度显著加快，且在实际应用中提升了nDCG@5分数。

## 📝 摘要（中文）

大型语言模型（LLMs）在信息检索中的相关性评估中得到了广泛应用。然而，本研究表明，结合两种不同架构的小型语言模型（SLMs）可以在这一任务中超越LLMs。我们的方法QUPID将生成式SLM与基于嵌入的SLM相结合，取得了更高的相关性判断准确率，同时相比于最先进的LLM解决方案降低了计算成本。这种计算效率使得QUPID在处理每日数百万查询的实际搜索系统中具有高度可扩展性。在不同文档类型的实验中，我们的方法表现出一致的性能提升（Cohen's Kappa为0.646，相较于领先的LLMs的0.387），并且推理速度提高了60倍。此外，当集成到生产搜索管道中时，QUPID将nDCG@5分数提高了1.9%。这些发现强调了模型组合中的架构多样性如何显著增强信息检索系统的搜索相关性和操作效率。

## 🔬 方法详解

**问题定义**：本论文旨在解决信息检索中相关性评估的准确性和计算效率问题。现有方法主要依赖大型语言模型（LLMs），但在处理大量查询时，计算成本高且效率低下。

**核心思路**：论文提出的QUPID方法通过结合两种不同架构的小型语言模型（SLMs），即生成式SLM与基于嵌入的SLM，旨在提高相关性判断的准确性，同时降低计算开销。这样的设计能够充分利用不同模型的优势，提升整体性能。

**技术框架**：QUPID的整体架构包括两个主要模块：生成式SLM用于生成候选答案，嵌入式SLM用于对候选答案进行相关性评分。通过这两个模块的协同工作，QUPID能够在保证准确性的同时实现高效的推理。

**关键创新**：QUPID的最重要创新在于模型组合的架构设计，通过将两种小型语言模型结合，克服了单一大型语言模型在计算效率上的不足。这种架构多样性显著提升了信息检索系统的性能。

**关键设计**：在模型设计中，QUPID采用了特定的损失函数来优化相关性评分，并在网络结构上进行了精细调整，以确保生成式和嵌入式模型之间的有效协作。

## 📊 实验亮点

实验结果显示，QUPID在Cohen's Kappa指标上达到了0.646，相较于领先的LLMs的0.387有显著提升。同时，QUPID的推理速度提高了60倍，并在生产环境中将nDCG@5分数提升了1.9%，展示了其在实际应用中的有效性。

## 🎯 应用场景

QUPID的研究成果在实际搜索引擎中具有广泛的应用潜力，尤其是在需要处理大量查询的场景，如电子商务、社交媒体和在线内容平台。其高效的计算性能和准确的相关性评估能够显著提升用户体验，帮助用户更快速地找到所需信息。未来，QUPID的架构设计也可能为其他领域的信息检索任务提供新的思路。

## 📄 摘要（原文）

> Large language models (LLMs) have been widely used for relevance assessment in information retrieval. However, our study demonstrates that combining two distinct small language models (SLMs) with different architectures can outperform LLMs in this task. Our approach -- QUPID -- integrates a generative SLM with an embedding-based SLM, achieving higher relevance judgment accuracy while reducing computational costs compared to state-of-the-art LLM solutions. This computational efficiency makes QUPID highly scalable for real-world search systems processing millions of queries daily. In experiments across diverse document types, our method demonstrated consistent performance improvements (Cohen's Kappa of 0.646 versus 0.387 for leading LLMs) while offering 60x faster inference times. Furthermore, when integrated into production search pipelines, QUPID improved nDCG@5 scores by 1.9%. These findings underscore how architectural diversity in model combinations can significantly enhance both search relevance and operational efficiency in information retrieval systems.

