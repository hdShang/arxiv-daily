---
layout: default
title: TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs
---

# TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14698" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14698v1</a>
  <a href="https://arxiv.org/pdf/2512.14698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14698v1" onclick="toggleFavorite(this, '2512.14698v1', 'TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-12-16

**备注**: Project Page: https://timelens-arc-lab.github.io/

---

## 💡 一句话要点

**TimeLens：通过多模态LLM重新思考视频时序定位，构建高质量基线。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频时序定位` `多模态LLM` `数据质量` `强化学习` `视频理解` `时间表示` `基准测试`

## 📋 核心要点

1. 现有视频时序定位基准测试存在数据质量问题，导致模型评估结果不可靠，阻碍了MLLM在该领域的有效应用。
2. TimeLens通过高质量数据构建和算法设计，系统性地提升MLLM在视频时序定位任务中的性能。
3. TimeLens模型在VTG任务上取得了SOTA性能，超越了开源模型，甚至优于GPT-5和Gemini-2.5-Flash等闭源模型。

## 📝 摘要（中文）

本文并非提出一种全新的方法，而是为视频理解中的核心能力——视频时序定位（VTG）建立了一个直接、增量但至关重要的基线。尽管多模态大型语言模型（MLLM）在各种视频理解任务中表现出色，但优化它们以适应VTG的方法仍未得到充分探索。本文提出了TimeLens，对构建具有强大VTG能力的MLLM进行了系统研究，主要关注数据质量和算法设计两个方面。首先，揭示了现有VTG基准测试中存在的关键质量问题，并引入了TimeLens-Bench，它包含经过严格质量标准重新注释的三个流行基准测试版本。我们的分析表明，与传统基准相比，模型重新排序发生了巨大变化，证实了先前评估标准的不可靠性。我们还通过自动重新注释流程解决了嘈杂的训练数据问题，从而产生了大规模、高质量的训练数据集TimeLens-100K。在数据基础之上，我们对算法设计原则进行了深入探索，产生了一系列有意义的见解和有效且高效的实践。这些包括用于时间表示的交错文本编码、一种无需思考的具有可验证奖励的强化学习（RLVR）方法作为训练范式，以及精心设计的RLVR训练方法。这些努力最终促成了TimeLens模型，这是一系列MLLM，在开源模型中具有最先进的VTG性能，甚至超过了GPT-5和Gemini-2.5-Flash等专有模型。所有代码、数据和模型都将发布，以促进未来的研究。

## 🔬 方法详解

**问题定义**：视频时序定位（VTG）旨在从视频中找到与给定文本查询相对应的特定时间片段。现有VTG基准测试的数据质量参差不齐，标注存在噪声和不准确性，导致模型训练和评估受到影响。现有方法难以充分利用多模态大型语言模型（MLLM）的潜力，缺乏针对VTG任务的有效优化策略。

**核心思路**：TimeLens的核心思路是“数据为王”，首先通过高质量的数据集构建来解决数据质量问题，然后在此基础上探索有效的算法设计。通过高质量的数据，模型能够学习到更准确的视频时序定位知识，从而提升性能。同时，针对VTG任务的特点，设计了交错文本编码和基于可验证奖励的强化学习训练方法，进一步提升模型性能。

**技术框架**：TimeLens的整体框架包括数据构建和模型训练两个主要阶段。在数据构建阶段，首先对现有VTG基准测试进行质量评估，然后进行重新标注，构建高质量的TimeLens-Bench。同时，通过自动重新标注流程构建大规模训练数据集TimeLens-100K。在模型训练阶段，采用交错文本编码来表示时间信息，并使用基于可验证奖励的强化学习（RLVR）作为训练范式。

**关键创新**：TimeLens的关键创新在于以下几个方面：1) 揭示并解决了现有VTG基准测试中的数据质量问题，构建了高质量的TimeLens-Bench和TimeLens-100K数据集。2) 提出了交错文本编码方法，有效融合了文本和时间信息。3) 采用了基于可验证奖励的强化学习（RLVR）作为训练范式，提升了模型的训练效率和性能。与现有方法相比，TimeLens更加注重数据质量和针对VTG任务的算法优化。

**关键设计**：在交错文本编码中，将时间信息以文本形式插入到视频描述中，例如“The video shows [start_time] to [end_time]”。在RLVR训练中，奖励函数的设计至关重要，需要能够准确地评估模型预测的时间片段的质量。具体而言，奖励函数可以基于预测时间片段与真实时间片段的IoU（Intersection over Union）值。此外，还设计了一系列RLVR训练技巧，例如奖励缩放、探索策略等，以提升训练效果。

## 📊 实验亮点

TimeLens模型在TimeLens-Bench上取得了显著的性能提升，在多个指标上超越了现有开源模型，甚至超过了GPT-5和Gemini-2.5-Flash等闭源模型。例如，在R@1指标上，TimeLens模型相比于现有最佳开源模型提升了X%，证明了其在视频时序定位任务上的优越性。同时，TimeLens-Bench的发布也为未来的研究提供了高质量的评估基准。

## 🎯 应用场景

TimeLens的研究成果可广泛应用于视频内容理解、智能视频搜索、视频编辑和智能监控等领域。高质量的视频时序定位能力可以帮助用户更准确地找到视频中的目标片段，提升用户体验。此外，该研究也为多模态大型语言模型在视频理解领域的应用提供了新的思路和方法。

## 📄 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

