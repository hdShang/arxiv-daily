---
layout: default
title: "GRILE: A Benchmark for Grammar Reasoning and Explanation in Romanian LLMs"
---

# GRILE: A Benchmark for Grammar Reasoning and Explanation in Romanian LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14279" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14279v1</a>
  <a href="https://arxiv.org/pdf/2508.14279.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14279v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14279v1', 'GRILE: A Benchmark for Grammar Reasoning and Explanation in Romanian LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adrian-Marius Dumitran, Alexandra-Mihaela Danila, Angela-Liliana Dumitran

**分类**: cs.CL, cs.CY, cs.LG

**发布日期**: 2025-08-19

**备注**: Accepted as long paper @RANLP2025

---

## 💡 一句话要点

**提出GRILE基准以解决罗马尼亚LLMs的语法推理与解释问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大规模语言模型` `自然语言处理` `教育技术` `语法推理` `低资源语言` `模型评估` `错误分析`

## 📋 核心要点

1. 现有的LLMs在低资源语言的教育应用中存在准确性不足和解释质量差的问题。
2. GRILE基准通过提供1151道多项选择题，评估LLMs在选择答案和生成解释方面的能力。
3. 实验表明，Gemini 2.5 Pro在准确性上表现优异，而大多数模型的表现则显著低于预期，揭示了教育NLP中的挑战。

## 📝 摘要（中文）

大规模语言模型（LLMs）在自然语言处理领域引发了革命，但其在低资源语言中的教育价值尚不明确。本文提出GRILE（罗马尼亚语推理与语言解释），这是第一个开放基准，包含从罗马尼亚高风险考试中收集的1151道多项选择题。GRILE旨在探测七种最先进的多语言和罗马尼亚特定LLMs的两种互补能力：选择正确答案和生成语言学上准确的解释。实验结果显示，Gemini 2.5 Pro的准确率达到83%，而大多数开放权重模型的准确率低于65%，且48%的解释存在事实或教学缺陷。详细的错误分析揭示了形态学和最新DOOM3正字法规范应用中的系统性弱点。所有数据、代码和公共网络演示均已发布，以促进未来研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大规模语言模型在罗马尼亚语教育应用中的准确性和解释质量不足的问题。现有方法在低资源语言的语法推理和解释生成方面存在明显的挑战。

**核心思路**：论文提出GRILE基准，通过设计多项选择题和评估模型的推理与解释能力，来系统性地分析和提升LLMs在教育场景中的表现。

**技术框架**：GRILE基准包含题库构建、模型评估和错误分析三个主要模块。题库由高风险考试题目构成，模型评估则通过准确性和解释质量进行。

**关键创新**：GRILE是首个针对罗马尼亚语的开放基准，提供了系统的评估框架，能够揭示LLMs在教育应用中的潜在缺陷，与现有方法相比，具有更强的针对性和实用性。

**关键设计**：在模型评估中，采用了多项选择题的形式，并通过专家审查来评估解释的准确性和教学有效性，确保了结果的可靠性和有效性。实验中还使用了最新的DOOM3正字法规范作为评估标准。

## 📊 实验亮点

实验结果显示，Gemini 2.5 Pro在GRILE基准上达到了83%的准确率，而大多数开放权重模型的准确率低于65%。此外，48%的模型生成的解释被专家评审认为存在事实或教学缺陷，揭示了当前模型在教育应用中的不足。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、语言学习和智能辅导系统。GRILE基准的建立为低资源语言的教育NLP提供了新的研究方向，能够帮助开发更可靠的语言模型，提升教育质量和学习效果。未来，GRILE可能成为其他低资源语言的基准参考，推动相关领域的研究进展。

## 📄 摘要（原文）

> LLMs (Large language models) have revolutionized NLP (Natural Language Processing), yet their pedagogical value for low-resource languages remains unclear. We present GRILE (Grammar Romanian Inference and Language Explanations) , the first open benchmark of 1,151 multiple-choice questions harvested from Romanian high-stakes exams (National Evaluation, Baccalaureate, university admissions). GRILE enables us to probe two complementary abilities of seven state-of-the-art multilingual and Romanian-specific LLMs: (i) selecting the correct answer, and (ii) producing linguistically accurate explanations. While Gemini 2.5 Pro reaches 83% accuracy, most open-weight models stay below 65%, and 48% of their explanations contain factual or pedagogical flaws according to expert review. A detailed error analysis pinpoints systematic weaknesses in morphology and in applying the latest DOOM3 orthographic norms. All data, code and a public web demo are released to catalyze future research. Our findings expose open challenges for trustworthy educational NLP in low-resource settings and establish GRILE as a new test-bed for controllable explanation generation and evaluation.

