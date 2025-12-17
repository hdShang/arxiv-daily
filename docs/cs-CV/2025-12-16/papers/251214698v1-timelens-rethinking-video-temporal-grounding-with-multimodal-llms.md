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

**提出TimeLens基准与训练方法，通过高质量数据和算法设计提升多模态大语言模型的视频时序定位能力。**

🎯 **匹配领域**: **强化学习**

**关键词**: `视频时序定位` `多模态大语言模型` `基准评估` `数据质量` `强化学习` `视频理解` `开源模型` `算法设计`

## 📋 核心要点

1. 现有VTG基准存在质量问题，导致模型评估不可靠，限制了多模态大语言模型在视频时序定位中的优化。
2. 论文从数据质量和算法设计入手，构建高质量基准和训练集，并引入交替文本编码和RLVR训练范式。
3. TimeLens模型在开源模型中达到SOTA性能，超越GPT-5等专有模型，验证了方法的有效性。

## 📝 摘要（中文）

本文并未提出新方法，而是为视频理解的核心能力——视频时序定位（VTG）建立了一个直接、渐进但至关重要的基线。尽管多模态大语言模型（MLLMs）在多种视频理解任务中表现出色，但优化其VTG能力的方案仍待探索。本文提出TimeLens，从数据质量和算法设计两个主要维度，系统性地研究如何构建具有强大VTG能力的MLLMs。我们首先揭示了现有VTG基准中的关键质量问题，并引入TimeLens-Bench，包含三个流行基准的精心重新标注版本，遵循严格的质量标准。分析显示，与旧基准相比，模型排名发生显著变化，证实了先前评估标准的不可靠性。我们还通过自动重新标注流程处理噪声训练数据，生成了TimeLens-100K，一个大规模、高质量的训练数据集。基于数据基础，我们深入探索算法设计原则，获得了一系列有意义的见解和高效实用的实践。这些包括用于时间表示的交替文本编码、作为训练范式的免思考强化学习与可验证奖励（RLVR）方法，以及精心设计的RLVR训练方案。这些努力最终形成了TimeLens模型系列，在开源模型中实现了最先进的VTG性能，甚至超越了GPT-5和Gemini-2.5-Flash等专有模型。所有代码、数据和模型都将发布以促进未来研究。

## 🔬 方法详解

TimeLens的整体框架基于多模态大语言模型，通过系统优化数据质量和算法设计来提升视频时序定位能力。关键技术创新包括：构建TimeLens-Bench高质量基准和TimeLens-100K训练数据集以解决数据噪声问题；采用交替文本编码有效表示时间信息；提出免思考强化学习与可验证奖励（RLVR）作为训练范式，结合精心设计的训练方案。与现有方法的主要区别在于，它不引入新模型架构，而是聚焦于数据清洗和算法优化，提供可复现的基线，强调评估可靠性和训练效率。

## 📊 实验亮点

TimeLens模型在开源模型中实现最先进的VTG性能，超越GPT-5和Gemini-2.5-Flash等专有模型；重新标注的基准导致模型排名显著变化，凸显了先前评估标准的问题；高质量数据和算法优化共同贡献了性能提升。

## 🎯 应用场景

该研究可应用于视频内容分析、智能监控、教育视频检索和自动驾驶场景理解等领域，通过提升视频时序定位精度，增强多模态AI系统在现实世界中的实用性和可靠性。

## 📄 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

