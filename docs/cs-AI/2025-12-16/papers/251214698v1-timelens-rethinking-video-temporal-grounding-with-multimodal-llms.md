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

**关键词**: `视频时序定位` `多模态大语言模型` `基准评估` `高质量数据` `强化学习训练` `视频理解` `开源模型` `算法设计`

## 📋 核心要点

1. 现有VTG基准存在质量问题，导致模型评估不可靠，且训练数据噪声大，限制了MLLMs在视频时序定位中的性能提升。
2. 论文从数据质量和算法设计入手，构建高质量基准TimeLens-Bench和训练集TimeLens-100K，并设计交替文本编码和RLVR训练范式。
3. TimeLens模型在VTG任务中达到开源模型最优，超越GPT-5等专有模型，验证了高质量数据和算法设计的有效性。

## 📝 摘要（中文）

本文并未提出新方法，而是为视频理解的核心能力——视频时序定位（VTG）建立了一个直接、渐进但至关重要的基线。尽管多模态大语言模型（MLLMs）在多种视频理解任务中表现出色，但优化其VTG能力的方案仍未被充分探索。本文提出TimeLens，从数据质量和算法设计两个主要维度，系统性地研究如何构建具有强大VTG能力的MLLMs。我们首先揭示了现有VTG基准中的关键质量问题，并引入了TimeLens-Bench，它包含三个流行基准的精心重新标注版本，遵循严格的质量标准。我们的分析显示，与旧基准相比，模型排名发生了显著变化，证实了先前评估标准的不可靠性。我们还通过自动重新标注流程解决了训练数据中的噪声问题，生成了TimeLens-100K，这是一个大规模、高质量的训练数据集。基于我们的数据基础，我们深入探索了算法设计原则，得出一系列有意义的见解和有效且高效的实践。这些包括用于时间表示的交替文本编码、作为训练范式的免思考强化学习与可验证奖励（RLVR）方法，以及精心设计的RLVR训练方案。这些努力最终形成了TimeLens模型系列，这是一组在开源模型中具有最先进VTG性能的MLLMs，甚至超越了GPT-5和Gemini-2.5-Flash等专有模型。所有代码、数据和模型都将发布以促进未来研究。

## 🔬 方法详解

TimeLens的整体框架基于多模态大语言模型，专注于提升视频时序定位能力。关键技术创新点包括：在数据层面，通过严格标准重新标注现有基准，构建TimeLens-Bench以解决评估问题，并利用自动流程生成高质量训练集TimeLens-100K；在算法层面，引入交替文本编码来有效表示时间信息，并采用免思考强化学习与可验证奖励（RLVR）作为训练范式，优化模型输出。与现有方法的主要区别在于，它系统性地整合了高质量数据构建和算法设计，而非单一技术改进，强调基准可靠性和训练效率，为VTG任务提供了可复现的基线方案。

## 📊 实验亮点

TimeLens模型在VTG任务中达到开源模型最优性能，超越GPT-5和Gemini-2.5-Flash等专有模型；TimeLens-Bench基准揭示了旧基准的不可靠性，导致模型排名显著变化；高质量数据集TimeLens-100K有效提升了训练效果。

## 🎯 应用场景

该研究可应用于视频内容分析、智能监控、视频检索和编辑等领域，通过提升视频时序定位精度，支持更准确的视频理解任务，如事件检测、场景分割和问答系统，具有实际价值。

## 📄 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

