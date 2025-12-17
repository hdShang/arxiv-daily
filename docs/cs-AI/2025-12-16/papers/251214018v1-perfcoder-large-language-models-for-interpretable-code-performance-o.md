---
layout: default
title: PerfCoder: Large Language Models for Interpretable Code Performance Optimization
---

# PerfCoder: Large Language Models for Interpretable Code Performance Optimization

**arXiv**: [2512.14018v1](https://arxiv.org/abs/2512.14018) | [PDF](https://arxiv.org/pdf/2512.14018.pdf)

**作者**: Jiuding Yang, Shengyao Lu, Hongxuan Liu, Shayan Shirahmad Gale Bagi, Zahra Fazel, Tomasz Czajkowski, Di Niu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出PerfCoder模型，通过可解释的定制化优化生成高性能代码，解决大语言模型在代码性能优化方面的不足。**

**关键词**: `代码性能优化` `大语言模型` `可解释优化` `强化微调` `代码生成` `软件工程` `自动化重构`

## 📋 核心要点

1. 现有大语言模型在代码生成中缺乏性能优化监督，导致生成代码效率低，难以满足实际软件需求。
2. PerfCoder通过微调真实优化轨迹和强化学习对齐偏好，实现可解释的定制化代码优化，无需迭代优化。
3. 在PIE基准测试中，PerfCoder在运行时加速和优化率上超越所有模型，并提升32B模型和GPT-5的优化性能。

## 📝 摘要（中文）

大语言模型在自动代码生成方面取得了显著进展，但在生成高性能代码方面仍存在局限，这是实际软件系统中的关键需求。我们认为当前大语言模型不仅因数据稀缺而受限，更重要的是缺乏指导可解释且有效性能改进的监督。本文介绍了PerfCoder，这是一系列专门设计用于通过可解释的定制化优化从源代码生成性能增强代码的大语言模型。PerfCoder在精选的真实世界优化轨迹集合上进行了微调，这些轨迹带有可读的人类注释，并通过使用运行时测量的强化微调进行偏好对齐，使其能够提出特定于输入的改进策略并直接应用，而无需依赖迭代优化。在PIE代码性能基准测试中，PerfCoder在运行时加速和有效优化率方面均超越了所有现有模型，表明性能优化不能仅通过规模实现，而需要优化策略意识。此外，PerfCoder可以生成关于源代码的可解释反馈，当在规划器与优化器协作工作流中作为更大语言模型的输入时，可以进一步改善结果。具体而言，我们将32B模型和GPT-5在代码优化方面的性能提升到新水平，显著超越了它们的原始性能。

## 🔬 方法详解

PerfCoder的整体框架基于大语言模型，通过两个关键步骤实现代码性能优化：首先，在精选的真实世界优化轨迹数据集上进行微调，这些轨迹包含人类可读的注释，以学习可解释的优化策略；其次，使用运行时测量进行强化微调，以对齐模型偏好，使其能够直接应用输入特定的改进。技术创新点在于结合了监督微调和强化学习，强调优化策略的可解释性。与现有方法的主要区别在于，PerfCoder不依赖迭代优化过程，而是通过一次性生成优化代码，并利用可解释反馈提升协作工作流中的性能。

## 📊 实验亮点

在PIE代码性能基准测试中，PerfCoder在运行时加速和有效优化率方面均超越所有现有模型，并将32B模型和GPT-5的代码优化性能提升到新水平，显著超越原始性能。

## 🎯 应用场景

该研究可应用于软件开发、编译器优化和自动化代码重构领域，帮助开发者生成高性能代码，提升软件系统效率，具有实际工程价值。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable progress in automatic code generation, yet their ability to produce high-performance code remains limited--a critical requirement in real-world software systems. We argue that current LLMs struggle not only due to data scarcity but, more importantly, because they lack supervision that guides interpretable and effective performance improvements. In this work, we introduce PerfCoder, a family of LLMs specifically designed to generate performance-enhanced code from source code via interpretable, customized optimizations. PerfCoder is fine-tuned on a curated collection of real-world optimization trajectories with human-readable annotations, and preference-aligned by reinforcement fine-tuning using runtime measurements, enabling it to propose input-specific improvement strategies and apply them directly without relying on iterative refinement. On the PIE code performance benchmark, PerfCoder surpasses all existing models in both runtime speedup and effective optimization rate, demonstrating that performance optimization cannot be achieved by scale alone but requires optimization stratetgy awareness. In addition, PerfCoder can generate interpretable feedback about the source code, which, when provided as input to a larger LLM in a planner-and-optimizer cooperative workflow, can further improve outcomes. Specifically, we elevate the performance of 32B models and GPT-5 to new levels on code optimization, substantially surpassing their original performance.

