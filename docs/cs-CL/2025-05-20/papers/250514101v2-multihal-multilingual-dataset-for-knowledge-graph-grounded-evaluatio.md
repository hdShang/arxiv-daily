---
layout: default
title: MultiHal: Multilingual Dataset for Knowledge-Graph Grounded Evaluation of LLM Hallucinations
---

# MultiHal: Multilingual Dataset for Knowledge-Graph Grounded Evaluation of LLM Hallucinations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14101" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14101v2</a>
  <a href="https://arxiv.org/pdf/2505.14101.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14101v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14101v2', 'MultiHal: Multilingual Dataset for Knowledge-Graph Grounded Evaluation of LLM Hallucinations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ernests Lavrinovics, Russa Biswas, Katja Hose, Johannes Bjerva

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-23)

---

## 💡 一句话要点

**提出MultiHal以解决多语言知识图谱基础的LLM幻觉评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识图谱` `幻觉评估` `多语言处理` `结构化数据` `自然语言处理` `事实核查`

## 📋 核心要点

1. 现有的幻觉评估基准主要集中在英语数据集上，缺乏多语言和知识图谱路径的支持，导致评估的局限性。
2. 本文提出MultiHal，一个基于知识图谱的多语言多跳评估基准，旨在通过结构化事实资源改善幻觉评估。
3. 实验结果表明，KG集成在语义相似度、NLI蕴涵和幻觉检测方面相较于传统QA方法有显著提升，得分提高幅度在0.12到0.42之间。

## 📝 摘要（中文）

大型语言模型（LLMs）固有的忠实性和事实性限制，通常被称为幻觉。现有的评估基准主要集中在英语数据集上，依赖于补充信息上下文而忽视了结构化事实资源。为此，知识图谱（KGs）被认为是减轻幻觉的有效工具。本文提出了一个基于知识图谱的多语言多跳评估基准MultiHal，旨在改善生成文本的评估。我们从开放域知识图谱中挖掘了14万条KG路径，筛选出高质量的2.59万条。基线评估显示，KG集成在多个语言和模型上显著提高了语义相似度、NLI蕴涵和幻觉检测的得分，展示了其潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成文本时的幻觉问题，现有方法多依赖于英语数据集和非结构化信息，缺乏多语言和知识图谱的支持，导致评估效果不佳。

**核心思路**：提出MultiHal基准，通过引入知识图谱提供结构化事实，增强多语言幻觉评估的有效性，旨在改善现有评估方法的局限性。

**技术框架**：整体架构包括数据收集、KG路径挖掘与筛选、评估基准构建等阶段。首先从开放域知识图谱中挖掘KG路径，然后筛选出高质量的路径以构建评估基准。

**关键创新**：最重要的创新在于将知识图谱与多语言评估结合，填补了现有评估基准在多语言和结构化事实支持方面的空白，显著提升了评估的准确性和可靠性。

**关键设计**：在数据收集过程中，挖掘了14万条KG路径，并经过筛选保留了2.59万条高质量路径，确保了评估基准的有效性和准确性。

## 📊 实验亮点

实验结果显示，MultiHal在多个语言和模型上相较于传统QA方法，语义相似度得分提高了0.12到0.36，NLI蕴涵得分提高了0.16到0.36，幻觉检测得分提高了0.29到0.42，证明了知识图谱集成的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括多语言生成模型的评估、知识图谱在自然语言处理中的应用以及幻觉检测与事实核查任务。通过提供一个结构化的评估基准，MultiHal有助于推动相关领域的研究进展，提升生成模型的可靠性和实用性。

## 📄 摘要（原文）

> Large Language Models (LLMs) have inherent limitations of faithfulness and factuality, commonly referred to as hallucinations. Several benchmarks have been developed that provide a test bed for factuality evaluation within the context of English-centric datasets, while relying on supplementary informative context like web links or text passages but ignoring the available structured factual resources. To this end, Knowledge Graphs (KGs) have been identified as a useful aid for hallucination mitigation, as they provide a structured way to represent the facts about entities and their relations with minimal linguistic overhead. We bridge the lack of KG paths and multilinguality for factual language modeling within the existing hallucination evaluation benchmarks and propose a KG-based multilingual, multihop benchmark called MultiHal framed for generative text evaluation. As part of our data collection pipeline, we mined 140k KG-paths from open-domain KGs, from which we pruned noisy KG-paths, curating a high-quality subset of 25.9k. Our baseline evaluation shows an absolute scale improvement by approximately 0.12 to 0.36 points for the semantic similarity score, 0.16 to 0.36 for NLI entailment and 0.29 to 0.42 for hallucination detection in KG-RAG over vanilla QA across multiple languages and multiple models, demonstrating the potential of KG integration. We anticipate MultiHal will foster future research towards several graph-based hallucination mitigation and fact-checking tasks.

