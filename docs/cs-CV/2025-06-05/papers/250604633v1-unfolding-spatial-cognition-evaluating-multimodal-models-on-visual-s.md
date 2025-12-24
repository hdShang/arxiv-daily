---
layout: default
title: "Unfolding Spatial Cognition: Evaluating Multimodal Models on Visual Simulations"
---

# Unfolding Spatial Cognition: Evaluating Multimodal Models on Visual Simulations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04633" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04633v1</a>
  <a href="https://arxiv.org/pdf/2506.04633.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04633v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04633v1', 'Unfolding Spatial Cognition: Evaluating Multimodal Models on Visual Simulations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linjie Li, Mahtab Bigverdi, Jiawei Gu, Zixian Ma, Yinuo Yang, Ziang Li, Yejin Choi, Ranjay Krishna

**分类**: cs.CV

**发布日期**: 2025-06-05

**备注**: STARE is available at https://github.com/STARE-bench/STARE

---

## 💡 一句话要点

**提出STARE基准以评估多模态模型在视觉模拟中的空间认知能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间认知` `多模态模型` `视觉模拟` `STARE基准` `几何变换` `空间推理` `人工智能评估`

## 📋 核心要点

1. 现有AI基准主要集中于语言推理，忽视了多步骤视觉模拟的复杂性，导致模型在空间认知任务上的表现不佳。
2. 本文提出STARE基准，专门设计用于评估多模态大型语言模型在空间变换和推理任务中的能力，强调视觉模拟的重要性。
3. 实验结果表明，尽管模型在简单任务上表现良好，但在复杂任务上表现接近随机，显示出模型对中间视觉信息的利用不充分。

## 📝 摘要（中文）

空间认知是人类智能的重要组成部分，使得通过视觉模拟进行问题解决成为可能，而不仅仅依赖于语言推理。然而，现有的AI基准主要评估语言推理，忽视了非语言多步骤视觉模拟的复杂性。本文提出了STARE（空间变换与推理评估）基准，旨在严格评估多模态大型语言模型在通过多步骤视觉模拟更好解决的任务上的表现。STARE包含4000个任务，涵盖基础几何变换（2D和3D）、综合空间推理（立方体展开与拼图）及现实世界空间推理（透视与时间推理），反映了物体组装、机械图解读和日常空间导航等实际认知挑战。评估结果显示，模型在简单的2D变换上表现良好，但在更复杂的任务上表现接近随机，表明模型可能无法有效利用中间视觉信息。

## 🔬 方法详解

**问题定义**：本文旨在解决现有AI模型在空间认知任务中表现不佳的问题，尤其是在多步骤视觉模拟方面的不足。现有方法主要评估语言推理，未能有效处理非语言的复杂任务。

**核心思路**：论文提出STARE基准，通过设计多样化的任务来评估模型在空间变换和推理中的能力，强调视觉模拟在解决复杂问题中的重要性。

**技术框架**：STARE基准包含4000个任务，分为基础几何变换、综合空间推理和现实世界空间推理三个主要模块，涵盖了多种空间认知挑战。

**关键创新**：STARE基准的设计是本文的核心创新，提供了一种新的评估方式，能够全面考察模型在空间认知任务中的表现，与传统语言推理基准形成鲜明对比。

**关键设计**：在任务设计中，考虑了不同的空间变换和推理类型，确保任务的多样性和复杂性，同时评估模型在不同任务上的表现差异。

## 📊 实验亮点

实验结果显示，模型在简单的2D变换任务上表现良好，但在复杂的3D立方体展开和拼图任务上表现接近随机。人类在复杂任务上接近完美准确率，但需要较长时间，使用中间视觉模拟可显著缩短时间（平均减少7.5秒）。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶、增强现实等，需要模型具备良好的空间认知能力。通过提升模型在视觉模拟任务中的表现，可以为实际应用提供更智能的解决方案，推动相关技术的发展。

## 📄 摘要（原文）

> Spatial cognition is essential for human intelligence, enabling problem-solving through visual simulations rather than solely relying on verbal reasoning. However, existing AI benchmarks primarily assess verbal reasoning, neglecting the complexities of non-verbal, multi-step visual simulation. We introduce STARE(Spatial Transformations and Reasoning Evaluation), a benchmark designed to rigorously evaluate multimodal large language models on tasks better solved through multi-step visual simulation. STARE features 4K tasks spanning foundational geometric transformations (2D and 3D), integrated spatial reasoning (cube net folding and tangram puzzles), and real-world spatial reasoning (perspective and temporal reasoning), reflecting practical cognitive challenges like object assembly, mechanical diagram interpretation, and everyday spatial navigation. Our evaluations show that models excel at reasoning over simpler 2D transformations, but perform close to random chance on more complex tasks like 3D cube net folding and tangram puzzles that require multi-step visual simulations. Humans achieve near-perfect accuracy but take considerable time (up to 28.9s) on complex tasks, significantly speeding up (down by 7.5 seconds on average) with intermediate visual simulations. In contrast, models exhibit inconsistent performance gains from visual simulations, improving on most tasks but declining in specific cases like tangram puzzles (GPT-4o, o1) and cube net folding (Claude-3.5, Gemini-2.0 Flash), indicating that models may not know how to effectively leverage intermediate visual information.

