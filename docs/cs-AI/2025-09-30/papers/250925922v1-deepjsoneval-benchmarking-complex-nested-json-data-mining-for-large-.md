---
layout: default
title: "DeepJSONEval: Benchmarking Complex Nested JSON Data Mining for Large Language Models"
---

# DeepJSONEval: Benchmarking Complex Nested JSON Data Mining for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25922" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25922v1</a>
  <a href="https://arxiv.org/pdf/2509.25922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25922v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25922v1', 'DeepJSONEval: Benchmarking Complex Nested JSON Data Mining for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhicheng Zhou, Jing Li, Suming Qiu, Junjie Huang, Linyuan Qiu, Zhijie Sun

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/GTS-AI-Infra-Lab-SotaS/DeepJSONEval)

---

## 💡 一句话要点

**DeepJSONEval：提出用于评估LLM在复杂嵌套JSON数据挖掘能力的新基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `JSON数据挖掘` `基准测试` `数据理解` `信息抽取` `嵌套数据结构` `Web数据挖掘`

## 📋 核心要点

1. 现有LLM的JSON生成评估基准侧重于纯JSON生成，忽略了数据理解和提取能力，与实际Web数据挖掘任务脱节。
2. DeepJSONEval提出一个包含2100个多领域、深度嵌套JSON结构的基准，用于更真实地评估LLM的数据挖掘能力。
3. 实验结果表明，现有LLM在处理DeepJSONEval基准中的复杂JSON结构时存在显著的性能差距，突显了该基准的价值。

## 📝 摘要（中文）

互联网充斥着低密度、高冗余的信息，如社交媒体评论、重复新闻和冗长的讨论，难以高效提取有价值的见解。多层嵌套JSON结构通过将此类信息压缩成语义丰富的分层表示来提供有效的解决方案，它将数据组织成键值对、数组和嵌套对象，保留上下文关系并实现高效的存储、检索和语义查询。例如，在新闻聚合中，JSON对象可以分层嵌套文章的元数据（标题、作者、日期）、内容（文本、多媒体）和多媒体信息（多媒体类型、标题）。大型语言模型（LLM）通过解析非结构化文本并将结构化结果直接输出到复杂的JSON模式中，在Web数据挖掘中发挥着变革性作用。然而，当前用于评估LLM的JSON输出能力的基准过分强调纯JSON生成，而不是评估数据理解和提取能力，这种局限性缺乏与实际Web数据挖掘任务的相关性。为了解决这个问题，我们引入了DeepJSONEval，这是一个新颖的基准，具有2100个多领域实例，具有深度嵌套结构，按难度分类。实验表明，LLM在处理这种复杂性方面存在显着的性能差距。我们的基准和数据集是开源的，旨在推进结构化JSON生成的研究。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在处理Web数据挖掘任务时，需要将非结构化的文本数据转换为结构化的JSON格式。然而，现有的JSON生成评估基准主要关注纯粹的JSON生成能力，而忽略了LLM对数据本身的理解和提取能力。这导致评估结果与实际应用场景存在偏差，无法准确反映LLM在真实Web数据挖掘任务中的性能。现有方法的痛点在于缺乏一个能够有效评估LLM在处理复杂嵌套JSON数据挖掘能力的基准。

**核心思路**：DeepJSONEval的核心思路是构建一个包含多领域、深度嵌套JSON结构的基准数据集，以此来模拟真实Web数据挖掘场景中遇到的复杂数据结构。通过评估LLM在解析和生成这些复杂JSON结构时的性能，可以更全面地了解LLM的数据理解和提取能力。这种设计旨在弥合现有评估方法与实际应用之间的差距，为LLM在Web数据挖掘领域的应用提供更可靠的评估依据。

**技术框架**：DeepJSONEval基准包含以下主要组成部分：
1.  **数据集构建**：收集来自多个领域的数据，并将其转换为深度嵌套的JSON结构。
2.  **难度分级**：根据JSON结构的复杂程度，将数据集中的实例分为不同的难度等级。
3.  **评估指标**：设计合适的评估指标，用于衡量LLM在解析和生成JSON结构时的准确性和效率。
4.  **实验评估**：使用不同的LLM在DeepJSONEval基准上进行实验，并分析实验结果。

**关键创新**：DeepJSONEval最重要的技术创新点在于其基准数据集的构建方式。该数据集包含多领域、深度嵌套的JSON结构，能够更真实地模拟Web数据挖掘场景中遇到的复杂数据结构。与现有基准相比，DeepJSONEval更侧重于评估LLM的数据理解和提取能力，而不仅仅是JSON生成能力。这种创新使得DeepJSONEval能够更准确地反映LLM在真实Web数据挖掘任务中的性能。

**关键设计**：DeepJSONEval的关键设计包括：
1.  **嵌套深度**：JSON结构的嵌套深度是衡量其复杂程度的重要指标。DeepJSONEval中的JSON结构具有较深的嵌套深度，能够有效地挑战LLM的数据处理能力。
2.  **领域多样性**：数据集包含来自多个领域的数据，例如新闻、社交媒体等。这种领域多样性可以确保评估结果的泛化能力。
3.  **难度分级**：根据JSON结构的复杂程度，将数据集中的实例分为不同的难度等级。这有助于更细致地评估LLM在不同难度级别下的性能。

## 📊 实验亮点

DeepJSONEval基准的实验结果表明，现有LLM在处理复杂嵌套JSON结构时存在显著的性能差距。具体来说，某些LLM在处理高难度级别的JSON实例时，准确率明显下降，表明其数据理解和提取能力不足。这些实验结果突显了DeepJSONEval基准的价值，证明了其能够有效区分不同LLM在处理复杂JSON数据方面的能力。

## 🎯 应用场景

DeepJSONEval的研究成果可广泛应用于Web数据挖掘、信息抽取、知识图谱构建等领域。通过更准确地评估LLM在处理复杂JSON数据方面的能力，可以帮助研究人员和开发者选择更适合特定任务的LLM模型，并优化模型在实际应用中的性能。此外，该基准的开源也有助于推动相关领域的研究进展，促进LLM在结构化数据处理方面的应用。

## 📄 摘要（原文）

> The internet is saturated with low-density, high-redundancy information, such as social media comments, repetitive news, and lengthy discussions, making it difficult to extract valuable insights efficiently. Multi-layer nested JSON structures provide an effective solution by compressing such information into semantically rich, hierarchical representations, which organize data into key-value pairs, arrays, and nested objects, preserving contextual relationships and enabling efficient storage, retrieval, and semantic querying. For instance, in news aggregation, a JSON object can nest an article's metadata (title, author, date), content (text, multimedia), and multimedia information (multimedia type, caption) hierarchically. Large Language Models (LLMs) play a transformative role in web data mining by parsing unstructured text and outputting structured results directly into complex JSON schemas. However, current benchmarks for evaluating LLMs' JSON output capabilities overemphasize pure JSON generation rather than assessing data comprehension and extraction abilities, a limitation that lacks relevance to practical web data mining tasks. To address this, we introduce DeepJSONEval, a novel benchmark featuring 2100 multi-domain instances with deep nested structures, categorized by difficulty. Experiments show significant performance gaps among LLMs in handling such complexity. Our benchmark and datasets are open-sourced to advance research in structured JSON generation.(https://github.com/GTS-AI-Infra-Lab-SotaS/DeepJSONEval).

