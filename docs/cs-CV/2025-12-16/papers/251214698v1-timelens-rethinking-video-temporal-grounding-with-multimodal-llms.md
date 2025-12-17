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

**TimeLens：利用多模态LLM重新思考视频时序定位任务，构建高质量基线。**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)**

**关键词**: `视频时序定位` `多模态LLM` `数据质量` `强化学习` `视频理解` `基准测试` `时间表示`

## 📋 核心要点

1. 现有视频时序定位基准测试存在数据质量问题，导致模型评估结果不可靠，阻碍了有效方法的发展。
2. TimeLens通过高质量数据重标注和算法设计，系统性地提升多模态LLM在视频时序定位任务上的性能。
3. TimeLens模型在开源模型中取得了最先进的视频时序定位性能，甚至超越了部分专有模型。

## 📝 摘要（中文）

本文并非提出一种全新的方法，而是为视频理解中的核心能力——视频时序定位（VTG）建立了一个直接、增量但至关重要的基线。尽管多模态大型语言模型（MLLM）在各种视频理解任务中表现出色，但优化它们以适应VTG的方法仍未得到充分探索。本文提出了TimeLens，系统地研究了构建具有强大VTG能力的MLLM，主要关注数据质量和算法设计两个方面。首先，揭示了现有VTG基准测试中存在的关键质量问题，并引入了TimeLens-Bench，它包含经过严格质量标准重新注释的三个流行的基准测试版本。我们的分析表明，与传统基准相比，模型排名发生了巨大变化，证实了先前评估标准的不可靠性。我们还通过自动重新注释流程解决了嘈杂的训练数据问题，从而产生了大规模、高质量的训练数据集TimeLens-100K。在数据基础之上，我们对算法设计原则进行了深入探索，产生了一系列有意义的见解和有效而高效的实践。这些包括用于时间表示的交错文本编码、一种无需思考的具有可验证奖励的强化学习（RLVR）方法作为训练范例，以及为RLVR训练精心设计的方案。这些努力最终产生了TimeLens模型，这是一系列MLLM，在开源模型中具有最先进的VTG性能，甚至超过了GPT-5和Gemini-2.5-Flash等专有模型。所有代码、数据和模型都将发布，以促进未来的研究。

## 🔬 方法详解

**问题定义**：视频时序定位（VTG）旨在根据给定的文本查询，在视频中找到对应的时间片段。现有VTG基准测试的数据质量参差不齐，标注存在噪声，导致模型训练和评估受到影响，无法真实反映模型的性能。此外，如何有效地利用多模态大型语言模型（MLLM）进行VTG任务仍是一个挑战。

**核心思路**：TimeLens的核心思路是“数据为王”，首先通过高质量的数据集构建可靠的基线，然后在此基础上探索有效的算法设计。具体来说，通过严格的质量控制流程重新标注现有数据集，并构建大规模高质量的训练数据集。同时，探索了时间表示方法、训练范式和训练策略，以充分利用MLLM的潜力。

**技术框架**：TimeLens的整体框架包括数据准备和模型训练两个主要阶段。在数据准备阶段，首先对现有VTG数据集进行质量评估，然后进行重新标注，构建高质量的TimeLens-Bench和TimeLens-100K数据集。在模型训练阶段，采用多模态LLM作为基础模型，并结合交错文本编码、强化学习训练等技术进行优化。

**关键创新**：TimeLens的关键创新在于其对数据质量的重视和系统性的算法设计探索。通过高质量的数据集，可以更准确地评估模型的性能，并为模型训练提供更可靠的指导。此外，TimeLens提出的交错文本编码和强化学习训练方法，可以有效地提升MLLM在VTG任务上的性能。

**关键设计**：TimeLens的关键设计包括：1) 使用交错文本编码来表示时间信息，将时间戳与文本查询交织在一起，使模型能够更好地理解时间关系。2) 采用无需思考的强化学习（RLVR）作为训练范式，通过可验证的奖励函数来指导模型的学习。3) 精心设计RLVR训练的方案，包括奖励函数的选择、探索策略的设置等。

## 📊 实验亮点

TimeLens模型在TimeLens-Bench上取得了显著的性能提升，超过了现有开源模型，甚至超越了GPT-5和Gemini-2.5-Flash等专有模型。实验结果表明，高质量的数据和有效的算法设计是提升VTG性能的关键。TimeLens-100K数据集的发布也将为未来的研究提供有力的支持。

## 🎯 应用场景

TimeLens的研究成果可应用于智能视频搜索、视频内容理解、智能客服等领域。例如，用户可以通过自然语言查询视频中的特定事件或片段，TimeLens可以帮助快速定位到相关内容。该研究有助于提升视频理解的智能化水平，并为相关应用提供更准确、高效的技术支持。

## 📄 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

