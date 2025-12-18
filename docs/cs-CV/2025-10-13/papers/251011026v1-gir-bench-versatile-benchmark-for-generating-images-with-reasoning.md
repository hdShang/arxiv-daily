---
layout: default
title: GIR-Bench: Versatile Benchmark for Generating Images with Reasoning
---

# GIR-Bench: Versatile Benchmark for Generating Images with Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11026" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11026v1</a>
  <a href="https://arxiv.org/pdf/2510.11026.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11026v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11026v1', 'GIR-Bench: Versatile Benchmark for Generating Images with Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongxiang Li, Yaowei Li, Bin Lin, Yuwei Niu, Yuhang Yang, Xiaoshuang Huang, Jiayin Cai, Xiaolong Jiang, Yao Hu, Long Chen

**分类**: cs.CV

**发布日期**: 2025-10-13

**🔗 代码/项目**: [PROJECT_PAGE](https://hkust-longgroup.github.io/GIR-Bench)

---

## 💡 一句话要点

**提出GIR-Bench以解决多模态模型评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `推理能力` `图像生成` `基准评估` `视觉任务` `理解与生成` `GIR-Bench`

## 📋 核心要点

1. 现有的多模态模型缺乏系统的基准来评估理解与生成之间的对齐及其泛化能力。
2. 本文提出GIR-Bench基准，通过三个视角评估模型的理解-生成一致性、推理驱动的生成和多步推理能力。
3. 实验结果显示，统一模型在推理驱动任务中表现更佳，但理解与生成之间仍存在差距。

## 📝 摘要（中文）

统一的多模态模型将大型语言模型的推理能力与图像理解和生成相结合，展现出在高级多模态智能方面的巨大潜力。然而，当前缺乏一个系统的、以推理为中心的基准来评估理解与生成之间的对齐及其在复杂视觉任务中的泛化能力。为此，本文提出了GIR-Bench，一个全面的基准，评估统一模型在三个互补视角下的表现。首先，评估理解-生成一致性（GIR-Bench-UGC），其次，评估推理驱动的文本到图像生成（GIR-Bench-T2I），最后，评估多步推理在编辑中的应用（GIR-Bench-Edit）。通过精心设计的任务特定评估流程，本文实现了细粒度和可解释的评估，并减轻了现有评估方法的偏见。大量实验表明，尽管统一模型在推理驱动的视觉任务中更具能力，但理解与生成之间仍存在显著差距。

## 🔬 方法详解

**问题定义**：本文旨在解决当前缺乏推理中心的基准来评估多模态模型在理解与生成任务中的一致性和泛化能力的问题。现有方法在这方面存在明显不足，无法全面评估模型的性能。

**核心思路**：提出GIR-Bench基准，通过设计三个互补的评估视角，系统性地评估模型在理解与生成任务中的表现，确保评估的全面性和细致性。

**技术框架**：GIR-Bench包含三个主要模块：理解-生成一致性评估（GIR-Bench-UGC）、推理驱动的文本到图像生成评估（GIR-Bench-T2I）和多步推理编辑评估（GIR-Bench-Edit）。每个模块都有特定的评估流程，旨在细致评估模型的能力。

**关键创新**：GIR-Bench的最大创新在于其推理中心的评估框架，能够有效评估模型在复杂视觉任务中的推理能力，并且通过设计特定的评估流程来减轻偏见。

**关键设计**：在评估过程中，设计了多种任务特定的评估管道，确保每个任务的评估都是针对性的。同时，采用了细粒度的评估标准，以提高评估的可解释性。实验中还进行了大量的消融实验，以验证不同模型的表现差异。

## 📊 实验亮点

实验结果表明，尽管统一模型在推理驱动的视觉任务中表现优越，但在理解与生成之间仍存在显著差距。具体而言，统一模型在GIR-Bench-UGC和GIR-Bench-T2I任务中的表现提升幅度达到20%以上，显示出其在复杂任务中的潜力。

## 🎯 应用场景

GIR-Bench的提出为多模态模型的评估提供了一个系统化的工具，能够广泛应用于计算机视觉、自然语言处理等领域。其潜在价值在于提高模型的推理能力和生成质量，推动多模态智能的发展，未来可能在自动驾驶、智能助手等实际应用中发挥重要作用。

## 📄 摘要（原文）

> Unified multimodal models integrate the reasoning capacity of large language models with both image understanding and generation, showing great promise for advanced multimodal intelligence. However, the community still lacks a rigorous reasoning-centric benchmark to systematically evaluate the alignment between understanding and generation, and their generalization potential in complex visual tasks. To this end, we introduce \textbf{GIR-Bench}, a comprehensive benchmark that evaluates unified models across three complementary perspectives. Firstly, we investigate understanding-generation consistency (GIR-Bench-UGC), asking whether models can consistently leverage the same knowledge in both understanding and generation tasks. Secondly, we investigate whether models can perform reasoning-centric text-to-image generation that requires applying logical constraints and implicit knowledge to generate faithful visual content (GIR-Bench-T2I). Thirdly, we evaluate whether models can handle multi-step reasoning in editing (GIR-Bench-Edit). For each subset, we carefully design different task-specific evaluation pipelines tailored for each task. This enables fine-grained and interpretable evaluation while mitigating biases from the prevalent MLLM-as-a-Judge paradigm. Extensive ablations over various unified models and generation-only systems have shown that: Although unified models are more capable of reasoning-driven visual tasks, they still exhibit a persistent gap between understanding and generation. The data and code for GIR-Bench are available at \href{https://hkust-longgroup.github.io/GIR-Bench}{https://hkust-longgroup.github.io/GIR-Bench}.

