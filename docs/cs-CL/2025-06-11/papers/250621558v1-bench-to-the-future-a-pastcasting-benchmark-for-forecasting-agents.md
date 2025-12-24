---
layout: default
title: "Bench to the Future: A Pastcasting Benchmark for Forecasting Agents"
---

# Bench to the Future: A Pastcasting Benchmark for Forecasting Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21558" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21558v1</a>
  <a href="https://arxiv.org/pdf/2506.21558.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21558v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21558v1', 'Bench to the Future: A Pastcasting Benchmark for Forecasting Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: FutureSearch, :, Jack Wildman, Nikos I. Bosse, Daniel Hnyk, Peter Mühlbacher, Finn Hambly, Jon Evans, Dan Schwarz, Lawrence Phillips

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出BTF基准以解决预测代理评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `预测基准` `人工智能评估` `大型语言模型` `历史事件预测` `过去预测`

## 📋 核心要点

1. 现有的预测基准缺乏一个现实、封闭且可重复的环境，限制了对AI系统的有效评估。
2. 本文提出了Bench To the Future (BTF)基准，通过提供已知答案的问题和相关网页，支持对过去事件的预测。
3. 实验表明，BTF能够产生与基于互联网的实时预测相当的结果，展示了其在评估预测能力方面的有效性。

## 📝 摘要（中文）

预测是一项具有挑战性的任务，提供了一种可量化的方式来研究人工智能系统。然而，现有的预测基准缺乏一个现实、封闭且可重复的环境。本文提出了Bench To the Future (BTF)，一个“过去预测”基准，包含数百个已知答案的高质量问题，并配有数万个相关网页的离线语料库。这使得从大型语言模型（LLM）中引出对过去事件的现实“预测”成为可能。实验结果表明，BTF环境下的预测结果与基于互联网的实时预测结果相当，展示了其在跟踪预测能力进展方面的有效性。我们希望这个基准能够不断更新，以适应不断增加的训练数据截止日期。

## 🔬 方法详解

**问题定义**：本文旨在解决现有预测基准缺乏现实性和可重复性的问题，导致对AI系统的评估不够准确。

**核心思路**：提出了一个“过去预测”基准，通过提供已知答案的问题和相关的离线网页语料库，使得LLM能够对历史事件进行预测，从而提高评估的可靠性。

**技术框架**：BTF基准包含数百个高质量问题，每个问题都配有大量相关网页，整体流程包括问题生成、数据收集和LLM预测。

**关键创新**：BTF的最大创新在于其“过去预测”方法，允许研究者在已知结果的情况下评估预测能力，这与传统的实时预测方法有本质区别。

**关键设计**：在设计中，选择了数万个相关网页作为语料库，并通过特定的评估指标来衡量LLM的预测能力，确保了实验的有效性和可靠性。

## 📊 实验亮点

实验结果显示，BTF基准下的预测结果与基于互联网的实时预测结果相当，验证了其有效性。特别是，在使用Claude 4模型进行评估时，BTF展示了持续的预测能力进展，提供了重要的基准数据。

## 🎯 应用场景

该研究的潜在应用领域包括人工智能系统的评估、预测模型的开发以及教育领域的历史事件分析。BTF基准的建立将为研究者提供一个可靠的工具，以更好地理解和改进预测能力，推动相关领域的发展。

## 📄 摘要（原文）

> Forecasting is a challenging task that offers a clearly measurable way to study AI systems. Forecasting requires a large amount of research on the internet, and evaluations require time for events to happen, making the development of forecasting benchmarks challenging. To date, no forecasting benchmark provides a realistic, hermetic, and repeatable environment for LLM forecasters. We introduce Bench To the Future (BTF), a "pastcasting" benchmark with hundreds of high-quality questions for which the resolution is already known. Each question is accompanied by a large offline corpus of tens of thousands of relevant web pages, enabling a way to elicit realistic "forecasts" on past events from LLMs. Results suggest that our pastcasting environment can produce results comparable to those based on forecasts using the internet on at-the-time unresolved questions. We show results benchmarking agent and chain-of-thought forecasting approaches using several LLMs, including the recently-released Claude 4 models, and demonstrate BTF's ability to track steady forecasting capability progress over time. We intend this to be a living benchmark, with new questions added continually to account for increasing training data cutoff dates. We invite researchers to contact us at hello@futuresearch.ai to utilize our benchmark or tooling for their own research.

