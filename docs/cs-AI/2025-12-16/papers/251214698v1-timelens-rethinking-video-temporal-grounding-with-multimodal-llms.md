---
layout: default
title: TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs
---

# TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs

**arXiv**: [2512.14698v1](https://arxiv.org/abs/2512.14698) | [PDF](https://arxiv.org/pdf/2512.14698.pdf)

**作者**: Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-12-16

**备注**: Project Page: https://timelens-arc-lab.github.io/

---

## 💡 一句话要点

**提出TimeLens基准与模型，通过高质量数据和算法设计提升多模态大语言模型的视频时序定位能力**

🎯 **匹配领域**: **强化学习**

**关键词**: `视频时序定位` `多模态大语言模型` `数据质量基准` `强化学习训练` `时间表示编码` `视频理解` `开源模型` `算法设计`

## 📋 核心要点

1. 现有VTG基准存在严重质量问题，导致模型评估不可靠，且训练数据噪声大，限制了MLLMs在视频时序定位中的性能提升。
2. 论文从数据质量和算法设计双维度入手，构建高质量基准TimeLens-Bench和训练集TimeLens-100K，并设计交替文本编码和RLVR训练范式。
3. TimeLens模型在开源模型中达到最先进水平，超越GPT-5等专有模型，显著提升了VTG任务的准确性和可靠性。

## 📝 摘要（中文）

本文并未提出全新方法，而是为视频理解的核心能力——视频时序定位（VTG）建立了一个直接、渐进但至关重要的基线。尽管多模态大语言模型（MLLMs）在多种视频理解任务中表现出色，但优化其VTG能力的方案仍未被充分探索。本文提出TimeLens，从数据质量和算法设计两个主要维度，系统性地研究如何构建具有强大VTG能力的MLLMs。我们首先揭示了现有VTG基准中的关键质量问题，并引入了TimeLens-Bench，它包含三个流行基准的精心重新标注版本，遵循严格的质量标准。我们的分析显示，与旧基准相比，模型排名发生了显著变化，证实了先前评估标准的不可靠性。我们还通过自动重新标注流程解决了训练数据中的噪声问题，生成了TimeLens-100K，这是一个大规模、高质量的训练数据集。基于我们的数据基础，我们深入探索了算法设计原则，得出一系列有意义的见解和有效且高效的实践。这些包括用于时间表示的交替文本编码、作为训练范式的免思考强化学习与可验证奖励（RLVR）方法，以及精心设计的RLVR训练方案。这些努力最终形成了TimeLens模型系列，这是一组在开源模型中具有最先进VTG性能的MLLMs，甚至超越了GPT-5和Gemini-2.5-Flash等专有模型。所有代码、数据和模型都将发布以促进未来研究。

## 🔬 方法详解

**问题定义**：论文旨在解决视频时序定位（VTG）任务中，由于现有基准数据质量低和训练数据噪声大，导致多模态大语言模型（MLLMs）性能评估不可靠且优化困难的问题。现有方法的痛点包括标注错误、评估标准不一致，以及缺乏系统性的算法设计指导。

**核心思路**：论文的核心思路是通过提升数据质量和优化算法设计，系统性地构建具有强大VTG能力的MLLMs。这包括重新标注基准以消除噪声、创建高质量训练集，并探索有效的编码和训练策略，以确保模型能准确理解视频中的时间信息。

**技术框架**：整体框架分为数据构建和算法设计两阶段。首先，通过人工审核和自动流程，生成TimeLens-Bench（高质量评估基准）和TimeLens-100K（高质量训练数据集）。然后，基于这些数据，设计MLLM模型，采用交替文本编码处理时间表示，并使用RLVR作为训练范式，结合可验证奖励进行优化。

**关键创新**：最重要的技术创新是提出了TimeLens-Bench和TimeLens-100K，解决了数据质量问题；同时，引入了交替文本编码和RLVR训练方法，这些设计显著提升了VTG性能，与现有方法相比，更注重数据可靠性和算法效率。

**关键设计**：关键设计包括：交替文本编码将时间信息嵌入文本序列，增强时间感知；RLVR训练范式免除了复杂思考步骤，直接基于可验证奖励（如定位准确性）进行强化学习；训练方案中可能涉及奖励函数设计、学习率调度等超参数优化，具体细节需参考论文代码。

## 📊 实验亮点

TimeLens模型在TimeLens-Bench上评估，显示出与旧基准相比的模型排名巨变，证实了先前标准的不可靠性。具体性能上，TimeLens在开源模型中达到最先进水平，甚至超越了GPT-5和Gemini-2.5-Flash等专有模型，提升了VTG任务的准确率，具体数据需参考论文实验部分。

## 🎯 应用场景

该研究可应用于视频内容分析、智能监控、视频检索和编辑等领域，通过提升视频时序定位的准确性，助力自动化视频理解系统的发展。其高质量数据和算法设计为未来VTG研究提供了可靠基线，推动多模态AI在真实场景中的落地，如教育、娱乐和安防。

## 📄 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

