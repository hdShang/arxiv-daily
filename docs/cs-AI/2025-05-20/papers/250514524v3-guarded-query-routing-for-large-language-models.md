---
layout: default
title: Guarded Query Routing for Large Language Models
---

# Guarded Query Routing for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14524" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14524v3</a>
  <a href="https://arxiv.org/pdf/2505.14524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14524v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14524v3', 'Guarded Query Routing for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Richard Šléher, William Brach, Tibor Sloboda, Kristián Košťál, Lukas Galke

**分类**: cs.AI

**发布日期**: 2025-05-20 (更新: 2025-10-25)

**DOI**: [10.3233/FAIA251304](https://doi.org/10.3233/FAIA251304)

**🔗 代码/项目**: [GITHUB](https://github.com/williambrach/gqr)

---

## 💡 一句话要点

**提出受保护的查询路由方法以解决大语言模型的查询分类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `查询路由` `大语言模型` `分布外检测` `机器学习` `数据集构建` `模型对比` `法律` `金融`

## 📋 核心要点

1. 现有的查询路由方法在处理分布外查询时存在不足，可能导致不相关或不安全的响应。
2. 本文提出了受保护查询路由基准（GQR-Bench），通过多种模型对比，探索有效的查询路由机制。
3. 实验结果表明，WideMLP在准确性和速度上表现最佳，而LLM模型虽然准确性高，但速度较慢。

## 📝 摘要（中文）

查询路由是将用户查询分配到不同的大语言模型（LLM）端点的任务，可以视为文本分类问题。然而，必须妥善处理分布外查询，这些查询可能涉及不相关的领域、其他语言或包含不安全文本。本文研究了一种受保护的查询路由问题，首次引入了受保护查询路由基准（GQR-Bench），涵盖法律、金融和医疗三个示例目标领域，以及七个数据集以测试对分布外查询的鲁棒性。通过GQR-Bench，我们对比了多种路由机制的有效性和效率，结果显示，增强了分布外检测能力的WideMLP在准确性（88%）和速度（<4ms）之间取得了最佳平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在查询路由中对分布外查询的处理问题。现有方法在面对不相关领域或不安全内容时，可能无法有效分类和路由查询。

**核心思路**：提出受保护的查询路由基准（GQR-Bench），通过引入分布外检测能力，提升查询路由的准确性和安全性。设计的核心在于结合传统机器学习与现代LLM的优势，以实现更高效的查询处理。

**技术框架**：整体架构包括数据集构建、模型训练与评估三个主要阶段。首先构建GQR-Bench数据集，然后对比多种模型的路由效果，最后评估其在不同查询类型下的表现。

**关键创新**：最重要的创新在于引入了分布外检测能力的WideMLP模型，显著提升了查询路由的准确性和处理速度，打破了对LLM的自动依赖。

**关键设计**：在模型设计中，WideMLP采用了特定的损失函数和网络结构，以优化对分布外查询的检测能力，同时保持较低的计算延迟。

## 📊 实验亮点

实验结果显示，WideMLP在准确性上达到88%，处理速度低于4毫秒，优于其他模型。相比之下，LLM模型的准确性最高（91%），但处理速度较慢（本地Llama-3.1:8B为62毫秒，远程GPT-4o-mini为669毫秒），挑战了对LLM的自动依赖。

## 🎯 应用场景

该研究的潜在应用领域包括法律、金融和医疗等行业，能够有效提升查询路由的准确性和安全性，降低不相关或不安全内容的风险。未来，该方法可扩展至更多领域，推动智能问答系统的安全性与可靠性。

## 📄 摘要（原文）

> Query routing, the task to route user queries to different large language model (LLM) endpoints, can be considered as a text classification problem. However, out-of-distribution queries must be handled properly, as those could be about unrelated domains, queries in other languages, or even contain unsafe text. Here, we thus study a guarded query routing problem, for which we first introduce the Guarded Query Routing Benchmark (GQR-Bench, released as Python package gqr), covers three exemplary target domains (law, finance, and healthcare), and seven datasets to test robustness against out-of-distribution queries. We then use GQR-Bench to contrast the effectiveness and efficiency of LLM-based routing mechanisms (GPT-4o-mini, Llama-3.2-3B, and Llama-3.1-8B), standard LLM-based guardrail approaches (LlamaGuard and NVIDIA NeMo Guardrails), continuous bag-of-words classifiers (WideMLP, fastText), and traditional machine learning models (SVM, XGBoost). Our results show that WideMLP, enhanced with out-of-domain detection capabilities, yields the best trade-off between accuracy (88%) and speed (<4ms). The embedding-based fastText excels at speed (<1ms) with acceptable accuracy (80%), whereas LLMs yield the highest accuracy (91%) but are comparatively slow (62ms for local Llama-3.1:8B and 669ms for remote GPT-4o-mini calls). Our findings challenge the automatic reliance on LLMs for (guarded) query routing and provide concrete recommendations for practical applications. Source code is available: https://github.com/williambrach/gqr.

