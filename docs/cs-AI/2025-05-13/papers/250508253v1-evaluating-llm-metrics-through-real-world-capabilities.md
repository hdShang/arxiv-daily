---
layout: default
title: Evaluating LLM Metrics Through Real-World Capabilities
---

# Evaluating LLM Metrics Through Real-World Capabilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08253" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08253v1</a>
  <a href="https://arxiv.org/pdf/2505.08253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08253v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08253v1', 'Evaluating LLM Metrics Through Real-World Capabilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Justin K Miller, Wenjia Tang

**分类**: cs.AI

**发布日期**: 2025-05-13

**备注**: 14 pages main text, 5 pages references, 20 pages appendix; includes 3 figures and 4 tables

---

## 💡 一句话要点

**提出基于真实世界能力评估LLM性能的新方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `性能评估` `用户效用` `真实世界应用` `核心能力` `基准测试`

## 📋 核心要点

1. 现有的评估基准主要集中于代码生成和事实回忆，未能全面反映用户在实际任务中的需求。
2. 论文通过分析用户使用数据，提出了六种核心能力，并基于这些能力评估现有基准的覆盖情况。
3. 研究发现Google Gemini在用户效用指标上表现优于其他主流模型，显示出其在实际应用中的优势。

## 📝 摘要（中文）

随着生成式人工智能日益融入日常工作流程，评估其性能的方式应反映真实使用情况，而非抽象的智能概念。本文提出了一种关注实际效用的评估方法，分析了用户在日常任务中对大型语言模型（LLMs）的使用情况。通过对大规模调查数据和使用日志的分析，识别出六种核心能力，包括摘要、技术支持、工作审查、数据结构化、生成和信息检索。研究发现现有基准在覆盖这些能力方面存在显著差距，并提出了以人本标准为基础的评估框架。最终，研究表明Google Gemini在这些效用导向的指标上优于其他模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有评估基准未能充分反映大型语言模型在真实世界应用中的效用问题，尤其是在用户日常任务中的表现不足。

**核心思路**：通过分析用户的实际使用情况，识别出六种核心能力，并评估现有基准在这些能力上的覆盖程度，以此提出更符合用户需求的评估标准。

**技术框架**：研究首先收集大规模的用户调查数据和使用日志，识别出六种核心能力。接着，评估现有基准在这些能力上的表现，并提出人本标准进行比较。

**关键创新**：本研究的创新在于将评估重点从抽象智能转向实际效用，识别出用户在日常任务中真正需要的能力，并提出相应的评估标准。

**关键设计**：在评估过程中，采用了五个实用标准：连贯性、准确性、清晰性、相关性和效率，以确保评估结果能够真实反映用户的需求。具体的基准选择和比较方法也经过精心设计，以确保结果的可靠性。

## 📊 实验亮点

实验结果显示，Google Gemini在六种核心能力的效用评估中表现优于其他模型，包括OpenAI的GPT、xAI的Grok、Meta的LLaMA等。具体而言，Google Gemini在效率和准确性方面的提升幅度显著，表明其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括教育、内容创作、技术支持等多个行业。通过更准确地评估大型语言模型的实际效用，能够帮助企业和开发者优化AI工具的设计与应用，提高用户体验和工作效率。未来，该方法可能推动更符合用户需求的AI评估标准的建立。

## 📄 摘要（原文）

> As generative AI becomes increasingly embedded in everyday workflows, it is important to evaluate its performance in ways that reflect real-world usage rather than abstract notions of intelligence. Unlike many existing benchmarks that assess general intelligence, our approach focuses on real-world utility, evaluating how well models support users in everyday tasks. While current benchmarks emphasize code generation or factual recall, users rely on AI for a much broader range of activities-from writing assistance and summarization to citation formatting and stylistic feedback. In this paper, we analyze large-scale survey data and usage logs to identify six core capabilities that represent how people commonly use Large Language Models (LLMs): Summarization, Technical Assistance, Reviewing Work, Data Structuring, Generation, and Information Retrieval. We then assess the extent to which existing benchmarks cover these capabilities, revealing significant gaps in coverage, efficiency measurement, and interpretability. Drawing on this analysis, we use human-centered criteria to identify gaps in how well current benchmarks reflect common usage that is grounded in five practical criteria: coherence, accuracy, clarity, relevance, and efficiency. For four of the six capabilities, we identify the benchmarks that best align with real-world tasks and use them to compare leading models. We find that Google Gemini outperforms other models-including OpenAI's GPT, xAI's Grok, Meta's LLaMA, Anthropic's Claude, DeepSeek, and Qwen from Alibaba-on these utility-focused metrics.

