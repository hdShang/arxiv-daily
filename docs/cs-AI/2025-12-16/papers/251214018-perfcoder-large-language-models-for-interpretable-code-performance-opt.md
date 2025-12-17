---
layout: default
title: PerfCoder: Large Language Models for Interpretable Code Performance Optimization
---

# PerfCoder: Large Language Models for Interpretable Code Performance Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14018" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14018</a>
  <a href="https://arxiv.org/pdf/2512.14018.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14018" onclick="toggleFavorite(this, '2512.14018', 'PerfCoder: Large Language Models for Interpretable Code Performance Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiuding Yang, Shengyao Lu, Hongxuan Liu, Shayan Shirahmad Gale Bagi, Zahra Fazel, Tomasz Czajkowski, Di Niu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**PerfCoder：利用大语言模型实现可解释的代码性能优化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码优化` `大语言模型` `性能提升` `可解释性` `强化学习`

## 📋 核心要点

1. 现有大语言模型在生成高性能代码方面存在不足，缺乏有效的性能优化指导。
2. PerfCoder通过在优化轨迹上微调，并使用运行时测量进行强化学习，实现可解释的代码性能优化。
3. 实验表明，PerfCoder在代码性能基准测试中超越现有模型，并能提升更大模型的优化能力。

## 📝 摘要（中文）

大语言模型（LLMs）在自动代码生成方面取得了显著进展，但其生成高性能代码的能力仍然有限，这在实际软件系统中至关重要。我们认为，当前LLMs的不足不仅在于数据稀缺，更重要的是，它们缺乏指导可解释和有效性能改进的监督。本文提出了PerfCoder，一个专门设计用于通过可解释的、定制的优化从源代码生成性能增强代码的LLM家族。PerfCoder在一个精心策划的、带有可读注释的真实优化轨迹集合上进行微调，并通过使用运行时测量的强化微调进行偏好对齐，使其能够提出特定于输入的改进策略并直接应用它们，而无需依赖迭代细化。在PIE代码性能基准测试中，PerfCoder在运行时加速和有效优化率方面均超过了所有现有模型，表明性能优化不能仅靠规模来实现，还需要优化策略意识。此外，PerfCoder可以生成关于源代码的可解释反馈，当在规划器-优化器协同工作流程中作为较大LLM的输入提供时，可以进一步改善结果。具体来说，我们提升了32B模型和GPT-5在代码优化方面的性能至新的水平，大大超过了它们原来的性能。

## 🔬 方法详解

**问题定义**：现有的大语言模型在代码生成方面取得了进展，但生成高性能代码的能力仍然不足。它们缺乏对代码性能优化的有效指导，难以产生可解释的优化策略，导致生成的代码在实际应用中性能受限。

**核心思路**：PerfCoder的核心思路是通过学习真实世界的代码优化轨迹，使模型能够理解和应用有效的优化策略。通过可解释的优化过程，模型能够生成性能增强的代码，并提供关于源代码的反馈，从而提升代码质量。

**技术框架**：PerfCoder的技术框架主要包括以下几个部分：1) 数据收集：构建包含真实世界代码优化轨迹的数据集，并进行人工标注，提供可解释的优化信息。2) 模型微调：在收集的数据集上对大语言模型进行微调，使模型学习优化策略。3) 强化学习：使用运行时测量作为奖励信号，通过强化学习对模型进行偏好对齐，使其能够生成性能更优的代码。4) 规划器-优化器协同：将PerfCoder生成的反馈提供给更大的LLM，协同完成代码优化任务。

**关键创新**：PerfCoder的关键创新在于其专注于可解释的性能优化策略学习。与以往依赖大规模数据和模型的方法不同，PerfCoder通过学习优化轨迹，使模型能够理解优化背后的原理，并生成可解释的优化建议。此外，PerfCoder还通过强化学习，将运行时测量纳入优化过程，从而更好地提升代码性能。

**关键设计**：PerfCoder的关键设计包括：1) 优化轨迹数据集的构建，需要精心选择和标注真实的优化案例。2) 强化学习奖励函数的设计，需要准确反映代码性能的提升。3) 规划器-优化器协同工作流程的设计，需要有效地利用PerfCoder生成的反馈信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14018/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14018/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14018/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PerfCoder在PIE代码性能基准测试中超越了所有现有模型，在运行时加速和有效优化率方面均取得了显著提升。此外，PerfCoder生成的反馈信息能够有效提升更大模型的代码优化能力，例如将32B模型和GPT-5的性能提升到新的水平，大幅超过了它们原始的性能表现。

## 🎯 应用场景

PerfCoder可应用于各种软件开发场景，例如编译器优化、代码重构和性能调优。它可以帮助开发者自动生成高性能代码，并提供可解释的优化建议，从而提高开发效率和软件质量。未来，PerfCoder有望成为自动化代码优化工具的核心组件，并推动软件工程领域的智能化发展。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable progress in automatic code generation, yet their ability to produce high-performance code remains limited--a critical requirement in real-world software systems. We argue that current LLMs struggle not only due to data scarcity but, more importantly, because they lack supervision that guides interpretable and effective performance improvements. In this work, we introduce PerfCoder, a family of LLMs specifically designed to generate performance-enhanced code from source code via interpretable, customized optimizations. PerfCoder is fine-tuned on a curated collection of real-world optimization trajectories with human-readable annotations, and preference-aligned by reinforcement fine-tuning using runtime measurements, enabling it to propose input-specific improvement strategies and apply them directly without relying on iterative refinement. On the PIE code performance benchmark, PerfCoder surpasses all existing models in both runtime speedup and effective optimization rate, demonstrating that performance optimization cannot be achieved by scale alone but requires optimization stratetgy awareness. In addition, PerfCoder can generate interpretable feedback about the source code, which, when provided as input to a larger LLM in a planner-and-optimizer cooperative workflow, can further improve outcomes. Specifically, we elevate the performance of 32B models and GPT-5 to new levels on code optimization, substantially surpassing their original performance.

