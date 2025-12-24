---
layout: default
title: "Play Favorites: A Statistical Method to Measure Self-Bias in LLM-as-a-Judge"
---

# Play Favorites: A Statistical Method to Measure Self-Bias in LLM-as-a-Judge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06709" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06709v1</a>
  <a href="https://arxiv.org/pdf/2508.06709.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06709v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06709v1', 'Play Favorites: A Statistical Method to Measure Self-Bias in LLM-as-a-Judge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Evangelia Spiliopoulou, Riccardo Fogliato, Hanna Burnsky, Tamer Soliman, Jie Ma, Graham Horwood, Miguel Ballesteros

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出统计方法以测量大型语言模型的自我偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我偏见` `大型语言模型` `统计方法` `模型评估` `公平性分析`

## 📋 核心要点

1. 现有研究常常将模型质量的真实差异与偏见混淆，导致对模型性能的错误评估。
2. 本文提出了一种统计框架，能够明确识别和量化LLM的自我偏见，确保评估的准确性。
3. 通过对超过5000个提示-完成对的实证分析，发现某些模型存在系统性的自我偏见和家族偏见。

## 📝 摘要（中文）

大型语言模型（LLMs）可以作为评判者，快速可靠地评估其他LLM的输出。然而，模型可能会系统性地对自身输出给予过于宽松的评分，这种现象称为自我偏见，可能会扭曲对模型真实性能的评估。本文提出了一种统计框架，明确了识别和估计自我偏见的假设。该方法建模LLM作为评判者对自身完成的评分分布与其他模型的差异，同时考虑独立第三方评判者（如人类）提供的完成质量。我们在一个包含超过5000个提示-完成对的数据集上进行了实证分析，发现某些模型（如GPT-4o和Claude 3.5 Sonnet）系统性地对自身输出给予更高的评分。我们的研究强调了使用LLM评判者的潜在陷阱，并提供了减轻偏见的实用指导。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在自我评估时可能存在的自我偏见问题。现有方法未能有效区分模型质量与偏见，导致评估结果的不准确性。

**核心思路**：我们提出的统计框架通过建模LLM对自身输出与其他模型输出的评分分布差异，明确识别自我偏见，同时考虑第三方评判者的质量评估。

**技术框架**：该方法包括数据收集、评分分布建模、偏见识别与量化等主要模块。首先收集大量提示-完成对，然后通过统计分析比较不同模型的评分分布。

**关键创新**：本研究的创新点在于提出了一种系统化的统计方法来量化自我偏见，避免了以往方法对模型质量与偏见的混淆。

**关键设计**：在模型设计中，我们设置了多个参数以优化评分分布的比较，采用了适合的损失函数来确保偏见的准确识别。

## 📊 实验亮点

实验结果表明，某些模型（如GPT-4o和Claude 3.5 Sonnet）在自我评分时系统性地给予更高的分数，且存在家族偏见。这些发现为使用LLM作为评判者提供了重要的警示，并提出了减轻偏见的实用建议。

## 🎯 应用场景

该研究的潜在应用领域包括自动化评估系统、模型性能监测和公平性分析等。通过识别和减轻自我偏见，可以提高LLM在实际应用中的可靠性和公正性，促进其在教育、法律和内容创作等领域的应用。

## 📄 摘要（原文）

> Large language models (LLMs) can serve as judges that offer rapid and reliable assessments of other LLM outputs. However, models may systematically assign overly favorable ratings to their own outputs, a phenomenon known as self-bias, which can distort evaluations of true model performance. Previous studies often conflate genuine differences in model quality with bias or incorrectly assume that evaluations from LLMs and humans follow the same rating distributions. In this work, we present a statistical framework that explicitly formalizes assumptions under which self-bias can be identified and estimated. Our method models the difference in the scoring distribution that LLM-as-a-judge assigns to its own completions compared to other models, while accounting for the underlying quality of the completions provided by an independent, third-party judge (e.g., humans). Our method reliably isolates and quantifies self-bias, even when models vary in ability, ensuring that genuine performance differences are not mistaken for self-bias. We conduct an empirical analysis of self-bias on a large dataset (>5000 prompt-completion pairs) consisting of expert human annotations and judgments from nine different LLM judges. We find that some models, such as GPT-4o and Claude 3.5 Sonnet, systematically assign higher scores to their own outputs. These models also display family-bias; systematically assigning higher ratings to outputs produced by other models of the same family. Our findings highlight potential pitfalls of using LLM judges and offer practical guidance to mitigate biases when interpreting automated evaluations.

