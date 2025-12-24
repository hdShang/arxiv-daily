---
layout: default
title: "HarmMetric Eval: Benchmarking Metrics and Judges for LLM Harmfulness Assessment"
---

# HarmMetric Eval: Benchmarking Metrics and Judges for LLM Harmfulness Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24384" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24384v1</a>
  <a href="https://arxiv.org/pdf/2509.24384.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24384v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24384v1', 'HarmMetric Eval: Benchmarking Metrics and Judges for LLM Harmfulness Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Langqi Yang, Tianhang Zheng, Kedong Xiu, Yixuan Chen, Di Wang, Puning Zhao, Zhan Qin, Kui Ren

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/qusgo)

---

## 💡 一句话要点

**提出HarmMetric Eval，用于全面评估LLM有害性评估指标与判别器的质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `有害性评估` `越狱攻击` `基准测试` `安全对齐`

## 📋 核心要点

1. 现有评估LLM有害性的指标和判别器缺乏系统性的质量评估，影响了越狱攻击有效性评估的可信度。
2. HarmMetric Eval旨在提供一个全面的基准，用于整体和细粒度地评估有害性指标和判别器的有效性。
3. 实验结果表明，传统指标METEOR和ROUGE-1在评估模型响应有害性方面优于基于LLM的判别器。

## 📝 摘要（中文）

大型语言模型（LLM）与人类价值观的对齐对其安全部署至关重要，然而，越狱攻击会破坏这种对齐，从而引诱LLM产生有害输出。近年来，涌现了大量的越狱攻击，同时也出现了各种用于评估LLM输出有害性的指标和判别器。然而，缺乏一个系统的基准来评估这些指标和判别器的质量和有效性，这削弱了已报告的越狱有效性和其他风险的可信度。为了解决这一差距，我们推出了HarmMetric Eval，这是一个全面的基准，旨在支持对有害性指标和判别器的整体和细粒度评估。我们的基准包括一个高质量的数据集，其中包含具有代表性的有害提示以及各种有害和非有害的模型响应，以及一个灵活的评分机制，与各种指标和判别器兼容。通过HarmMetric Eval，我们的大量实验揭示了一个令人惊讶的结果：两个传统的指标——METEOR和ROUGE-1——在评估模型响应的有害性方面优于基于LLM的判别器，这挑战了关于LLM在该领域优越性的普遍看法。我们的数据集可在https://huggingface.co/datasets/qusgo/HarmMetric_Eval公开获取，代码可在https://anonymous.4open.science/r/HarmMetric-Eval-4CBE获取。

## 🔬 方法详解

**问题定义**：论文旨在解决如何系统性地评估用于衡量大型语言模型（LLM）有害性的各种指标和判别器的质量和有效性的问题。现有方法缺乏统一的评估标准，导致对LLM安全性的评估结果难以比较和验证，同时也难以确定哪些指标和判别器真正有效。

**核心思路**：论文的核心思路是构建一个高质量的基准数据集，包含各种有害提示以及对应的有害和非有害模型响应，并设计一个灵活的评分机制，使得不同的有害性指标和判别器可以在同一基准上进行评估和比较。通过对各种指标和判别器在基准数据集上的表现进行分析，从而确定其优劣。

**技术框架**：HarmMetric Eval基准主要包含以下几个部分：1) 高质量的有害提示数据集；2) 针对每个提示，收集LLM生成的有害和非有害响应；3) 灵活的评分机制，允许不同的有害性指标和判别器对响应进行评分；4) 评估指标，用于衡量不同指标和判别器的性能，例如准确率、召回率等。

**关键创新**：该论文的关键创新在于构建了一个专门用于评估LLM有害性评估指标和判别器的基准数据集。与以往的研究不同，该研究不仅关注LLM本身的安全问题，更关注用于评估LLM安全性的工具的质量。此外，研究结果表明，传统的文本相似度指标在某些情况下优于基于LLM的判别器，这挑战了以往的认知。

**关键设计**：数据集包含了多种类型的有害提示，例如涉及仇恨言论、暴力、歧视等。对于每个提示，收集了多个LLM生成的响应，并人工标注了这些响应的有害程度。评分机制允许不同的指标和判别器对响应进行评分，并根据评分结果计算评估指标。研究中使用了METEOR和ROUGE-1等传统指标，以及基于LLM的判别器，例如GPT-3和BERT等。

## 📊 实验亮点

实验结果表明，传统的文本相似度指标METEOR和ROUGE-1在评估模型响应的有害性方面，表现优于基于LLM的判别器。这一发现挑战了当前普遍认为LLM在有害性评估方面具有优势的观点，为未来的研究方向提供了新的思路。

## 🎯 应用场景

该研究成果可应用于LLM的安全评估和风险管理。开发者可以使用HarmMetric Eval来评估和选择合适的有害性评估指标和判别器，从而提高LLM的安全性。此外，该基准还可以用于比较不同LLM的安全性，并促进LLM安全领域的研究。

## 📄 摘要（原文）

> The alignment of large language models (LLMs) with human values is critical for their safe deployment, yet jailbreak attacks can subvert this alignment to elicit harmful outputs from LLMs. In recent years, a proliferation of jailbreak attacks has emerged, accompanied by diverse metrics and judges to assess the harmfulness of the LLM outputs. However, the absence of a systematic benchmark to assess the quality and effectiveness of these metrics and judges undermines the credibility of the reported jailbreak effectiveness and other risks. To address this gap, we introduce HarmMetric Eval, a comprehensive benchmark designed to support both overall and fine-grained evaluation of harmfulness metrics and judges. Our benchmark includes a high-quality dataset of representative harmful prompts paired with diverse harmful and non-harmful model responses, alongside a flexible scoring mechanism compatible with various metrics and judges. With HarmMetric Eval, our extensive experiments uncover a surprising result: two conventional metrics--METEOR and ROUGE-1--outperform LLM-based judges in evaluating the harmfulness of model responses, challenging prevailing beliefs about LLMs' superiority in this domain. Our dataset is publicly available at https://huggingface.co/datasets/qusgo/HarmMetric_Eval, and the code is available at https://anonymous.4open.science/r/HarmMetric-Eval-4CBE.

