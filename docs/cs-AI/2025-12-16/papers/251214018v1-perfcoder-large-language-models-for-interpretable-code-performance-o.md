---
layout: default
title: PerfCoder: Large Language Models for Interpretable Code Performance Optimization
---

# PerfCoder: Large Language Models for Interpretable Code Performance Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14018" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14018v1</a>
  <a href="https://arxiv.org/pdf/2512.14018.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14018v1" onclick="toggleFavorite(this, '2512.14018v1', 'PerfCoder: Large Language Models for Interpretable Code Performance Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiuding Yang, Shengyao Lu, Hongxuan Liu, Shayan Shirahmad Gale Bagi, Zahra Fazel, Tomasz Czajkowski, Di Niu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**PerfCoder：基于大语言模型的可解释代码性能优化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码优化` `大语言模型` `性能提升` `强化学习` `代码生成`

## 📋 核心要点

1. 现有大语言模型在生成高性能代码方面存在不足，缺乏指导可解释和有效性能改进的监督。
2. PerfCoder通过在优化轨迹上微调LLM，并使用运行时测量进行强化学习，实现可解释的代码性能优化。
3. 实验表明，PerfCoder在代码性能基准测试中超越现有模型，并能提升更大规模LLM的优化能力。

## 📝 摘要（中文）

大语言模型（LLM）在自动代码生成方面取得了显著进展，但其生成高性能代码的能力仍然有限，这在实际软件系统中至关重要。我们认为，当前LLM的不足不仅在于数据稀缺，更重要的是缺乏指导可解释和有效性能改进的监督。本文提出了PerfCoder，一个专门设计用于通过可解释的、定制的优化从源代码生成性能增强代码的LLM家族。PerfCoder在一个精心策划的、带有可读注释的真实优化轨迹集合上进行微调，并通过使用运行时测量的强化微调进行偏好对齐，使其能够提出特定于输入的改进策略并直接应用它们，而无需依赖迭代改进。在PIE代码性能基准测试中，PerfCoder在运行时加速和有效优化率方面均超过了所有现有模型，表明性能优化不能仅靠规模来实现，还需要优化策略意识。此外，PerfCoder可以生成关于源代码的可解释反馈，当在规划器-优化器协同工作流程中作为较大LLM的输入提供时，可以进一步改善结果。具体而言，我们提升了32B模型和GPT-5在代码优化方面的性能至新的水平，大大超过了它们原来的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型（LLM）在生成高性能代码方面的不足。现有方法生成的代码性能不高，缺乏可解释的优化策略，难以满足实际软件系统的需求。现有LLM缺乏有效的监督信号，无法指导其进行可解释和有效的性能改进。

**核心思路**：论文的核心思路是训练一个专门用于代码性能优化的LLM（PerfCoder），使其能够生成可解释的优化策略并直接应用。通过在真实的优化轨迹上进行微调，并使用运行时测量进行强化学习，PerfCoder能够学习到有效的优化模式，并生成高性能的代码。

**技术框架**：PerfCoder的技术框架主要包括以下几个部分：1) 数据收集：收集真实世界中的代码优化轨迹，并进行人工标注，提供可解释的优化信息。2) 模型微调：在收集到的优化轨迹数据上对LLM进行微调，使其能够学习到代码优化的知识。3) 强化学习：使用运行时测量作为奖励信号，对模型进行强化学习，使其能够生成更高性能的代码。4) 规划器-优化器协同：将PerfCoder生成的优化建议提供给更大的LLM，以进一步提升代码性能。

**关键创新**：论文的关键创新在于：1) 提出了PerfCoder，一个专门用于代码性能优化的LLM。2) 使用优化轨迹和运行时测量进行监督学习和强化学习，使模型能够学习到有效的优化策略。3) 提出了规划器-优化器协同框架，将PerfCoder与更大的LLM结合，进一步提升代码性能。

**关键设计**：PerfCoder的关键设计包括：1) 优化轨迹的收集和标注：确保优化轨迹的质量和可解释性。2) 强化学习的奖励函数设计：使用运行时测量作为奖励信号，引导模型生成更高性能的代码。3) 模型架构的选择：选择合适的LLM架构作为基础模型，并进行微调。

## 📊 实验亮点

PerfCoder在PIE代码性能基准测试中超越了所有现有模型，在运行时加速和有效优化率方面均取得了显著提升。通过与更大的LLM（如32B模型和GPT-5）协同工作，PerfCoder能够进一步提升它们的性能，达到新的水平，大幅超过其原始性能。这表明PerfCoder不仅自身具有强大的优化能力，还能有效提升其他LLM的性能。

## 🎯 应用场景

PerfCoder可应用于各种软件开发场景，例如自动代码优化、编译器优化、性能分析和调试等。它可以帮助开发者快速生成高性能的代码，提高软件系统的效率和可靠性。未来，PerfCoder有望成为软件开发工具链中的重要组成部分，推动软件工程的自动化和智能化。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable progress in automatic code generation, yet their ability to produce high-performance code remains limited--a critical requirement in real-world software systems. We argue that current LLMs struggle not only due to data scarcity but, more importantly, because they lack supervision that guides interpretable and effective performance improvements. In this work, we introduce PerfCoder, a family of LLMs specifically designed to generate performance-enhanced code from source code via interpretable, customized optimizations. PerfCoder is fine-tuned on a curated collection of real-world optimization trajectories with human-readable annotations, and preference-aligned by reinforcement fine-tuning using runtime measurements, enabling it to propose input-specific improvement strategies and apply them directly without relying on iterative refinement. On the PIE code performance benchmark, PerfCoder surpasses all existing models in both runtime speedup and effective optimization rate, demonstrating that performance optimization cannot be achieved by scale alone but requires optimization stratetgy awareness. In addition, PerfCoder can generate interpretable feedback about the source code, which, when provided as input to a larger LLM in a planner-and-optimizer cooperative workflow, can further improve outcomes. Specifically, we elevate the performance of 32B models and GPT-5 to new levels on code optimization, substantially surpassing their original performance.

