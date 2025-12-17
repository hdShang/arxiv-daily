---
layout: default
title: Metis-HOME: Hybrid Optimized Mixture-of-Experts for Multimodal Reasoning
---

# Metis-HOME: Hybrid Optimized Mixture-of-Experts for Multimodal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20519" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20519v2</a>
  <a href="https://arxiv.org/pdf/2510.20519.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20519v2" onclick="toggleFavorite(this, '2510.20519v2', 'Metis-HOME: Hybrid Optimized Mixture-of-Experts for Multimodal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaohan Lan, Fanfan Liu, Haibo Qiu, Siqi Yang, Delian Ruan, Peng Shi, Lin Ma

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-23 (更新: 2025-11-25)

**🔗 代码/项目**: [GITHUB](https://github.com/MM-Thinking/Metis-HOME)

---

## 💡 一句话要点

**提出Metis-HOME，通过混合专家模型解决多模态推理中的效率与泛化难题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `混合专家模型` `模型效率` `模型泛化` `视觉问答` `OCR` `Qwen2.5-VL-7B`

## 📋 核心要点

1. 现有大型多模态模型在推理时，即使面对简单问题也采用复杂计算，导致效率低下，且牺牲了通用能力。
2. Metis-HOME构建混合专家模型，区分“思考”和“非思考”分支，并用轻量级路由器动态分配查询，实现高效推理。
3. 实验表明，Metis-HOME不仅提升了复杂推理能力，还改善了模型的通用能力，克服了推理专用模型常见的泛化能力下降问题。

## 📝 摘要（中文）

受大型语言模型推理能力进展的启发，多模态推理领域取得了显著进步，在复杂的数学问题求解等任务上获得了显著的性能提升。然而，当前的多模态大型推理模型存在两个主要局限性：即使对于简单的查询，它们也倾向于采用计算成本高昂的推理，导致效率低下；此外，对专门推理的关注往往会损害其更广泛、更通用的理解能力。本文提出了Metis-HOME：一种混合优化的混合专家框架，旨在解决这种权衡。Metis-HOME通过将原始密集模型构建成两个不同的专家分支来实现“混合思维”范式：一个思考分支，专门用于复杂的多步骤推理；一个非思考分支，针对诸如通用VQA和OCR等任务进行优化，以实现快速、直接的推理。一个轻量级的、可训练的路由器动态地将查询分配给最合适的专家。我们通过将Qwen2.5-VL-7B适配成MoE架构来实例化Metis-HOME。全面的评估表明，我们的方法不仅显著增强了复杂推理能力，还提高了模型的通用能力，扭转了其他推理专用模型中观察到的性能下降趋势。我们的工作为构建强大而通用的MLLM建立了一种新的范式，有效地解决了普遍存在的推理与泛化困境。代码和权重可在https://github.com/MM-Thinking/Metis-HOME获取。

## 🔬 方法详解

**问题定义**：当前多模态大型模型在推理任务中面临效率和泛化能力的挑战。具体来说，即使是简单的视觉问答或OCR任务，模型也倾向于使用复杂的推理过程，导致计算资源浪费。同时，为了提升特定推理任务的性能，模型往往牺牲了在其他通用任务上的表现，造成了推理能力和通用能力之间的trade-off。

**核心思路**：Metis-HOME的核心思路是引入混合专家模型（Mixture-of-Experts, MoE），将原始的密集模型分解为两个专门化的分支：一个“思考”分支和一个“非思考”分支。“思考”分支专注于复杂的多步骤推理任务，而“非思考”分支则针对简单的、直接的推理任务进行优化。通过这种方式，模型可以根据输入的不同，动态地选择最合适的专家分支进行处理，从而提高效率和泛化能力。

**技术框架**：Metis-HOME的整体架构包含以下几个主要模块：1) 原始的密集模型（例如Qwen2.5-VL-7B）；2) “思考”专家分支，用于处理复杂的推理任务；3) “非思考”专家分支，用于处理简单的直接推理任务；4) 一个轻量级的可训练路由器，用于根据输入特征动态地将查询分配给合适的专家分支。训练过程中，路由器学习如何根据输入特征的复杂程度，将查询分配给最合适的专家分支。

**关键创新**：Metis-HOME的关键创新在于其“混合思维”的范式，即通过构建专门化的专家分支，并使用路由器动态地选择合适的专家进行处理，从而在效率和泛化能力之间取得平衡。与传统的单一模型相比，Metis-HOME能够根据任务的复杂程度自适应地选择不同的处理方式，从而避免了不必要的计算开销，并提高了模型的通用性。

**关键设计**：Metis-HOME的关键设计包括：1) 专家分支的结构设计，需要根据具体的任务特点进行优化；2) 路由器的设计，需要保证其轻量级和高效性，同时能够准确地将查询分配给合适的专家分支；3) 训练策略的设计，需要保证专家分支和路由器能够协同工作，从而实现最佳的性能。

## 📊 实验亮点

Metis-HOME在复杂推理任务上取得了显著提升，同时避免了通用能力下降的问题。实验结果表明，该方法在提升复杂推理能力的同时，还提高了模型在通用VQA和OCR等任务上的性能，有效解决了推理与泛化之间的trade-off。

## 🎯 应用场景

Metis-HOME适用于各种需要多模态推理的场景，例如智能客服、自动驾驶、医疗诊断等。它可以提高这些应用在处理复杂问题时的效率和准确性，并提升用户体验。未来，该研究可以扩展到更多的模态和任务，构建更加通用和强大的多模态智能系统。

## 📄 摘要（原文）

> Inspired by recent advancements in LLM reasoning, the field of multimodal reasoning has seen remarkable progress, achieving significant performance gains on intricate tasks such as mathematical problem-solving. Despite this progress, current multimodal large reasoning models exhibit two key limitations. They tend to employ computationally expensive reasoning even for simple queries, leading to inefficiency. Furthermore, this focus on specialized reasoning often impairs their broader, more general understanding capabilities. In this paper, we propose Metis-HOME: a Hybrid Optimized Mixture-of-Experts framework designed to address this trade-off. Metis-HOME enables a ''Hybrid Thinking'' paradigm by structuring the original dense model into two distinct expert branches: a thinking branch tailored for complex, multi-step reasoning, and a non-thinking branch optimized for rapid, direct inference on tasks like general VQA and OCR. A lightweight, trainable router dynamically allocates queries to the most suitable expert. We instantiate Metis-HOME by adapting the Qwen2.5-VL-7B into an MoE architecture. Comprehensive evaluations reveal that our approach not only substantially enhances complex reasoning abilities but also improves the model's general capabilities, reversing the degradation trend observed in other reasoning-specialized models. Our work establishes a new paradigm for building powerful and versatile MLLMs, effectively resolving the prevalent reasoning-vs-generalization dilemma. Code and weights are available at https://github.com/MM-Thinking/Metis-HOME.

