---
layout: default
title: TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs
---

# TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14698" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14698</a>
  <a href="https://arxiv.org/pdf/2512.14698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14698" onclick="toggleFavorite(this, '2512.14698', 'TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**TimeLens：通过多模态LLM重新思考视频时序定位，构建高质量基线。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频时序定位` `多模态LLM` `高质量数据集` `强化学习` `视频理解` `时间表示` `数据重标注`

## 📋 核心要点

1. 现有视频时序定位基准测试存在数据质量问题，导致模型评估结果不可靠，阻碍了有效方法的发展。
2. TimeLens通过高质量数据构建和算法设计，系统性地研究了如何利用多模态LLM提升视频时序定位能力。
3. TimeLens模型在视频时序定位任务上取得了显著的性能提升，甚至超越了部分闭源模型，为开源社区提供了强大的基线。

## 📝 摘要（中文）

本文并非提出一种全新的方法，而是为视频理解中的核心能力——视频时序定位（VTG）建立了一个直接、增量但至关重要的基线。尽管多模态大型语言模型（MLLM）在各种视频理解任务中表现出色，但优化它们以用于VTG的方法仍未得到充分探索。本文提出了TimeLens，对构建具有强大VTG能力的MLLM进行了系统研究，主要关注数据质量和算法设计两个方面。首先，揭示了现有VTG基准测试中存在的关键质量问题，并引入了TimeLens-Bench，它包含经过严格质量标准重新注释的三个流行基准测试版本。分析表明，与传统基准相比，模型重新排序发生了巨大变化，证实了先前评估标准的不可靠性。还通过自动重新注释流程解决了嘈杂的训练数据问题，从而产生了大规模、高质量的训练数据集TimeLens-100K。在数据基础之上，深入探索了算法设计原则，产生了一系列有意义的见解和有效但高效的实践。这些包括用于时间表示的交错文本编码，一种无需思考的具有可验证奖励的强化学习（RLVR）方法作为训练范例，以及为RLVR训练精心设计的方案。这些努力最终促成了TimeLens模型，这是一系列MLLM，在开源模型中具有最先进的VTG性能，甚至超过了GPT-5和Gemini-2.5-Flash等专有模型。所有代码、数据和模型都将发布，以促进未来的研究。

## 🔬 方法详解

**问题定义**：视频时序定位（VTG）旨在从视频中定位与给定文本查询相关的特定时间片段。现有VTG方法受限于低质量的训练和评估数据，导致模型泛化能力差，且难以公平比较不同方法的优劣。现有方法缺乏针对MLLM在VTG任务上的优化策略。

**核心思路**：TimeLens的核心思路是通过高质量的数据和算法设计，充分利用多模态LLM的潜力，提升VTG的性能。具体来说，通过重新标注现有数据集，构建高质量的训练和评估基准，并探索有效的训练策略和模型结构。

**技术框架**：TimeLens包含以下几个主要模块：
1. **数据构建**：重新标注现有VTG数据集，构建高质量的TimeLens-Bench和TimeLens-100K数据集。
2. **模型结构**：采用多模态LLM作为基础模型，并引入交错文本编码用于时间表示。
3. **训练策略**：使用无需思考的强化学习与可验证奖励（RLVR）作为训练范例，并设计了相应的训练方案。

**关键创新**：TimeLens的关键创新在于：
1. **高质量数据**：通过严格的质量控制和重新标注，构建了高质量的VTG数据集，解决了现有数据集的质量问题。
2. **RLVR训练**：采用无需思考的强化学习与可验证奖励（RLVR）作为训练范例，避免了复杂的奖励函数设计，提高了训练效率和稳定性。

**关键设计**：
1. **交错文本编码**：将时间信息与文本查询交错编码，使模型能够更好地理解时间上下文。
2. **RLVR奖励函数**：设计了基于IoU（Intersection over Union）的可验证奖励函数，用于指导强化学习过程。
3. **训练方案**：精心设计了RLVR训练的超参数和训练流程，以保证模型的收敛性和性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14698/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14698/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14698/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TimeLens模型在TimeLens-Bench上取得了显著的性能提升，在多个指标上超越了现有的开源模型，甚至超过了GPT-5和Gemini-2.5-Flash等闭源模型。通过高质量数据和有效的训练策略，TimeLens证明了多模态LLM在VTG任务上的巨大潜力。

## 🎯 应用场景

TimeLens的研究成果可广泛应用于视频内容理解、智能视频搜索、视频编辑和智能监控等领域。高质量的VTG能力可以帮助用户更准确地定位视频中的关键时刻，提高信息检索效率，并为视频内容分析提供更精确的基础。

## 📄 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

