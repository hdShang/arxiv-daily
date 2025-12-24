---
layout: default
title: SwiftEval: Developing a Language-Specific Benchmark for LLM-generated Code Evaluation
---

# SwiftEval: Developing a Language-Specific Benchmark for LLM-generated Code Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24324" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24324v1</a>
  <a href="https://arxiv.org/pdf/2505.24324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24324v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24324v1', 'SwiftEval: Developing a Language-Specific Benchmark for LLM-generated Code Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ivan Petrukha, Yana Kurliak, Nataliia Stulova

**分类**: cs.LG, cs.CL, cs.PL, cs.SE

**发布日期**: 2025-05-30

**备注**: Accepted to FORGE'25 Benchmarking on 15.01.2025, to be published by IEEE under the CC BY-NC-ND 4.0 license. This is the accepted version of the article (5 pages, 2 figures, 1 table). DOI will be added upon publication

---

## 💡 一句话要点

**提出SwiftEval以解决Swift代码评估的不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `大型语言模型` `Swift评估` `多语言基准` `机器学习`

## 📋 核心要点

1. 现有的代码评估基准主要集中在Python，导致对Swift等其他语言的评估质量不足。
2. 论文提出了SwiftEval基准，包含28个手工设计的问题，专注于Swift语言特性。
3. 实验结果表明，LLM在需要语言特定特征的问题上得分显著下降，尤其是小型模型。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在代码生成方面取得了显著进展。然而，现有的评估基准主要集中在Python上，这使得对其他编程语言（如Swift）的高质量评估变得困难。通过对HumanEval-XL和MultiPL-E等多语言基准的分析，我们发现其Swift组件存在关键问题，导致其在评估LLM编码能力时不够充分或甚至无关。与这些现有方法不同，我们采用了质量优先的策略，提出了SwiftEval，这是第一个以Swift为导向的基准，包含28个精心设计的问题，并在此基础上评估了44个流行的代码LLM。我们的结果显示，对于需要语言特定特征的问题，LLM的得分显著下降，尤其是在较小模型中表现最为明显。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多语言代码评估基准在Swift语言评估中的不足，特别是HumanEval-XL和MultiPL-E在Swift组件上的关键问题，使得评估结果不够准确。

**核心思路**：我们提出了SwiftEval基准，专注于Swift语言的特性，采用质量优先的策略，设计了28个手工制作的问题，以更好地评估LLM在Swift代码生成中的能力。

**技术框架**：SwiftEval的整体架构包括问题设计、LLM评估和结果分析三个主要模块。首先，设计问题以涵盖Swift特有的语言特性；其次，使用44个流行的代码LLM进行评估；最后，分析模型在不同问题上的表现。

**关键创新**：SwiftEval是第一个专注于Swift的代码评估基准，区别于现有方法的地方在于其手工设计的问题能够更好地反映Swift语言的特性，而不仅仅是通过翻译Python基准来实现。

**关键设计**：在问题设计中，我们特别关注Swift的语法和特性，确保每个问题都能有效评估LLM在Swift编程中的能力。

## 📊 实验亮点

实验结果显示，LLM在需要特定语言特征的问题上得分显著下降，尤其是小型模型的表现最为明显。这表明现有模型在处理Swift语言特性时存在显著的不足，为未来的模型改进提供了方向。

## 🎯 应用场景

该研究的潜在应用领域包括教育、软件开发和自动化测试等。通过提供一个专门针对Swift的评估基准，开发者和研究人员可以更准确地评估和改进LLM在Swift代码生成方面的能力，从而推动相关技术的发展。

## 📄 摘要（原文）

> In recent years, large language models (LLMs) have showcased significant advancements in code generation. However, most evaluation benchmarks are primarily oriented towards Python, making it difficult to evaluate other programming languages, such as Swift, with high quality. By examining widely established multilingual benchmarks like HumanEval-XL and MultiPL-E, we identified critical issues specific to their Swift components, making them insufficient or even irrelevant for assessing LLM coding capabilities on Swift. Unlike these existing approaches, which prioritize rapid scaling and generalization by automatically translating Python-centric benchmarks with LLMs, we adopt a quality-over-quantity methodology. We present SwiftEval, the first Swift-oriented benchmark consisting of 28 carefully hand-crafted problems, and evaluate 44 popular Code LLMs on it. Our results show significant LLM scores drop for problems requiring language-specific features, most noticeable in the models of smaller sizes.

