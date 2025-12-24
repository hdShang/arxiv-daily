---
layout: default
title: "RelationalFactQA: A Benchmark for Evaluating Tabular Fact Retrieval from Large Language Models"
---

# RelationalFactQA: A Benchmark for Evaluating Tabular Fact Retrieval from Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21409" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21409v1</a>
  <a href="https://arxiv.org/pdf/2505.21409.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21409v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21409v1', 'RelationalFactQA: A Benchmark for Evaluating Tabular Fact Retrieval from Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dario Satriani, Enzo Veltri, Donatello Santoro, Paolo Papotti

**分类**: cs.CL, cs.AI, cs.DB

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出RelationalFactQA以评估大型语言模型的表格事实检索能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `事实检索` `结构化数据` `自然语言处理` `SQL生成` `评估基准` `知识检索`

## 📋 核心要点

1. 核心问题：现有基准评估短小答案，忽视了生成结构化、多记录表格输出的能力，导致LLMs在复杂查询中表现不佳。
2. 方法要点：提出RelationalFactQA基准，通过多样的自然语言问题和SQL配对，系统评估LLMs的知识检索能力。
3. 实验或效果：实验显示，最先进的LLMs在生成关系输出时的事实准确率未超过25%，且随着输出维度增加，性能显著下降。

## 📝 摘要（中文）

大型语言模型（LLMs）在事实性方面面临持续挑战。现有基准通常评估短小的事实答案，忽视了从参数知识中生成结构化、多记录表格输出的关键能力。我们展示了这种关系事实检索比孤立的点查询要困难得多，甚至在模型已知单个事实的情况下，也暴露出对输出维度（如属性或记录数量）敏感的不同失败模式。为系统评估这一未被充分探索的能力，我们引入了RelationalFactQA，一个新基准，包含多样的自然语言问题（配对SQL）和黄金标准的表格答案，专门设计用于评估结构化格式中的知识检索。实验表明，即使是最先进的LLMs在生成关系输出时也显著挣扎，事实准确率未超过25%，且随着输出维度的增加，性能显著下降。这些发现凸显了当前LLMs在合成结构化事实知识方面的关键局限性，并确立了RelationalFactQA作为衡量未来LLM事实性进展的重要资源。

## 🔬 方法详解

**问题定义**：论文要解决的问题是大型语言模型在生成结构化、多记录表格输出时的事实性不足。现有方法主要集中在短小答案的评估，未能有效应对复杂查询的挑战。

**核心思路**：论文的核心解决思路是引入RelationalFactQA基准，通过设计多样的自然语言问题和SQL配对，系统性地评估LLMs在结构化知识检索中的能力。这样的设计旨在揭示LLMs在处理复杂输出时的局限性。

**技术框架**：整体架构包括问题生成模块、SQL生成模块和表格答案生成模块。首先生成自然语言问题，然后将其转换为SQL查询，最后与黄金标准表格答案进行对比，评估模型的输出质量。

**关键创新**：最重要的技术创新点在于引入了一个专门针对关系事实检索的基准，RelationalFactQA，填补了现有评估方法的空白，使得对LLMs的评估更加全面和系统。

**关键设计**：在设计中，采用了多样化的问题类型和复杂度，设置了不同的输出维度，并使用了标准的损失函数来优化模型的生成能力，确保评估的准确性和可靠性。

## 📊 实验亮点

实验结果显示，当前最先进的LLMs在生成关系输出时的事实准确率未超过25%。随着输出维度的增加，模型性能显著下降，揭示了LLMs在处理复杂结构化数据时的关键局限性，为未来的研究指明了方向。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、数据分析工具和信息检索等。通过提升LLMs在结构化知识检索方面的能力，可以显著改善用户体验，推动自然语言处理技术在实际场景中的应用，未来可能影响教育、商业和科研等多个领域。

## 📄 摘要（原文）

> Factuality in Large Language Models (LLMs) is a persistent challenge. Current benchmarks often assess short factual answers, overlooking the critical ability to generate structured, multi-record tabular outputs from parametric knowledge. We demonstrate that this relational fact retrieval is substantially more difficult than isolated point-wise queries, even when individual facts are known to the model, exposing distinct failure modes sensitive to output dimensionality (e.g., number of attributes or records). To systematically evaluate this under-explored capability, we introduce RelationalFactQA, a new benchmark featuring diverse natural language questions (paired with SQL) and gold-standard tabular answers, specifically designed to assess knowledge retrieval in a structured format. RelationalFactQA enables analysis across varying query complexities, output sizes, and data characteristics. Our experiments reveal that even state-of-the-art LLMs struggle significantly, not exceeding 25% factual accuracy in generating relational outputs, with performance notably degrading as output dimensionality increases. These findings underscore critical limitations in current LLMs' ability to synthesize structured factual knowledge and establish RelationalFactQA as a crucial resource for measuring future progress in LLM factuality.

