---
layout: default
title: "TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs"
---

# TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14698" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14698v1</a>
  <a href="https://arxiv.org/pdf/2512.14698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14698v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14698v1', 'TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-12-16

**备注**: Project Page: https://timelens-arc-lab.github.io/

---

## 💡 一句话要点

**TimeLens：利用多模态LLM重新思考视频时序定位任务，构建高质量基线。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频时序定位` `多模态LLM` `数据质量` `强化学习` `视频理解` `基准测试` `时间表示`

## 📋 核心要点

1. 现有视频时序定位基准测试存在数据质量问题，导致模型评估结果不可靠，阻碍了有效方法的发展。
2. TimeLens通过高质量数据构建和算法设计，系统性地提升多模态LLM在视频时序定位任务上的性能。
3. TimeLens模型在开源模型中取得了最先进的视频时序定位性能，甚至超越了GPT-5和Gemini-2.5-Flash等专有模型。

## 📝 摘要（中文）

本文并非提出一种全新的方法，而是为视频理解中的核心能力——视频时序定位(VTG)建立了一个直接、增量但至关重要的基线。尽管多模态大型语言模型(MLLM)在各种视频理解任务中表现出色，但优化它们以适应VTG的方法仍未被充分探索。本文提出了TimeLens，对构建具有强大VTG能力的MLLM进行了系统研究，主要关注数据质量和算法设计两个方面。首先，揭示了现有VTG基准测试中的关键质量问题，并引入了TimeLens-Bench，其中包含经过严格质量标准重新注释的三个流行基准测试版本。我们的分析表明，与传统基准相比，模型重新排序发生了巨大变化，证实了先前评估标准的不可靠性。我们还通过自动重新注释管道解决了嘈杂的训练数据问题，从而产生了大规模、高质量的训练数据集TimeLens-100K。在数据基础上，我们对算法设计原则进行了深入探索，产生了一系列有意义的见解和有效但高效的实践。这些包括用于时间表示的交错文本编码、一种无需思考的具有可验证奖励的强化学习(RLVR)方法作为训练范例，以及为RLVR训练精心设计的方案。这些努力最终产生了TimeLens模型，这是一系列MLLM，在开源模型中具有最先进的VTG性能，甚至超过了GPT-5和Gemini-2.5-Flash等专有模型。所有代码、数据和模型都将发布，以促进未来的研究。

## 🔬 方法详解

**问题定义**：视频时序定位（VTG）旨在从视频中找到与给定文本查询相对应的时间片段。现有方法受限于低质量的训练和评估数据，导致模型泛化能力差，且难以公平比较不同方法的优劣。

**核心思路**：TimeLens的核心思路是“数据为王”，首先构建高质量的训练和评估数据集，然后探索有效的算法设计，从而提升多模态LLM在VTG任务上的性能。通过高质量的数据，模型可以学习到更准确的时序定位知识，从而提高泛化能力。

**技术框架**：TimeLens的技术框架主要包含三个部分：1) TimeLens-Bench：高质量的VTG评估基准，通过严格的质量控制流程重新标注现有数据集；2) TimeLens-100K：大规模高质量的训练数据集，通过自动重新标注流程清洗噪声数据；3) TimeLens模型：基于多模态LLM，采用交错文本编码、RLVR训练等技术，提升VTG性能。

**关键创新**：TimeLens的关键创新在于其对数据质量的重视，以及将强化学习与可验证奖励相结合的训练范式（RLVR）。传统方法往往忽略数据质量，导致模型性能受限。RLVR方法则可以更有效地训练模型，使其更好地理解视频内容和文本查询之间的关系。

**关键设计**：TimeLens的关键设计包括：1) 交错文本编码：将时间信息与文本查询交错编码，使模型更好地理解时间上下文；2) RLVR训练：使用可验证的奖励函数，引导模型学习更准确的时序定位；3) 数据增强：采用多种数据增强技术，提高模型的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14698v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14698v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14698v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TimeLens模型在TimeLens-Bench上取得了显著的性能提升，超过了现有的开源模型，甚至超越了GPT-5和Gemini-2.5-Flash等专有模型。实验结果表明，高质量的数据和有效的算法设计是提升视频时序定位性能的关键。TimeLens-Bench的引入也为未来的研究提供了一个更可靠的评估基准。

## 🎯 应用场景

TimeLens的研究成果可广泛应用于视频搜索、视频编辑、智能监控、教育视频分析等领域。高质量的视频时序定位能力可以提升用户体验，提高工作效率，并为更高级的视频理解任务奠定基础。未来，该技术有望应用于自动驾驶、机器人导航等领域。

## 📄 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

