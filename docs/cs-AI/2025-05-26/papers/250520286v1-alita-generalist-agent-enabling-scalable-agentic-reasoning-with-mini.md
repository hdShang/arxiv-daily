---
layout: default
title: Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution
---

# Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20286" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20286v1</a>
  <a href="https://arxiv.org/pdf/2505.20286.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20286v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20286v1', 'Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Qiu, Xuan Qi, Tongcheng Zhang, Xinzhe Juan, Jiacheng Guo, Yifu Lu, Yimin Wang, Zixin Yao, Qihan Ren, Xun Jiang, Xing Zhou, Dongrui Liu, Ling Yang, Yue Wu, Kaixuan Huang, Shilong Liu, Hongru Wang, Mengdi Wang

**分类**: cs.AI

**发布日期**: 2025-05-26

**备注**: 9 pages, 3 figures

**🔗 代码/项目**: [GITHUB](https://github.com/CharlesQ9/Alita)

---

## 💡 一句话要点

**提出Alita以解决现有智能体适应性不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `通用智能体` `自我进化` `智能推理` `模型上下文协议` `任务适应性` `复杂任务处理` `人工智能`

## 📋 核心要点

1. 现有智能体框架过度依赖手动预定义的工具，限制了其适应性和可扩展性。
2. Alita通过最小化预定义组件和最大化自我进化能力，简化了智能体的设计，提升了其泛化能力。
3. 在GAIA基准验证数据集上，Alita的表现优于许多复杂的智能体系统，显示出其高效的智能推理能力。

## 📝 摘要（中文）

近年来，大型语言模型的进步使得智能体能够自主执行复杂的开放式任务。然而，许多现有框架过于依赖手动预定义的工具和工作流程，限制了其适应性、可扩展性和跨领域的泛化能力。本文提出了Alita——一个遵循“简单即是终极复杂”的原则的通用智能体，通过最小预定义和最大自我进化实现可扩展的智能推理。Alita仅配备一个直接解决问题的组件，简化了设计，增强了其对复杂问题的泛化能力。同时，Alita通过生成与任务相关的模型上下文协议（MCPs），自主构建、优化和重用外部能力，进一步推动了可扩展的智能推理。Alita在GAIA基准验证数据集上实现了75.15%的pass@1和87.27%的pass@3准确率，表现优于许多复杂的智能体系统。

## 🔬 方法详解

**问题定义**：本文旨在解决现有智能体在执行复杂任务时对手动预定义工具的过度依赖问题。这种依赖限制了智能体的适应性和跨领域的泛化能力。

**核心思路**：Alita的核心思想是通过最小化预定义组件和最大化自我进化能力来简化智能体的设计。这样可以使智能体在面对复杂问题时不受限于特定工具，从而提升其灵活性和创造力。

**技术框架**：Alita的整体架构包括一个直接问题解决的核心组件，以及一套通用组件，用于自主生成任务相关的模型上下文协议（MCPs）。这些组件协同工作，使得智能体能够构建、优化和重用外部能力。

**关键创新**：Alita的主要创新在于其简化的设计和自我进化能力。与现有方法相比，Alita不再依赖复杂的手工工具，而是通过生成MCPs来实现智能推理的可扩展性。

**关键设计**：在设计上，Alita仅使用一个核心组件进行问题解决，避免了复杂的工具链。同时，MCPs的生成机制允许智能体根据任务需求动态调整其能力，增强了其适应性和灵活性。

## 📊 实验亮点

Alita在GAIA基准验证数据集上达到了75.15%的pass@1和87.27%的pass@3的准确率，表现优于许多复杂的智能体系统。此外，在Mathvista和PathVQA数据集上，Alita分别实现了74.00%和52.00%的pass@1，显示出其在多种任务中的优越性能。

## 🎯 应用场景

Alita的研究成果在多个领域具有潜在应用价值，包括自动化客服、智能助手、教育辅导等。其简化的设计和自我进化能力使得智能体能够更好地适应不同的任务需求，提升用户体验。未来，Alita有望在更广泛的智能系统中得到应用，推动智能体技术的发展。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled agents to autonomously perform complex, open-ended tasks. However, many existing frameworks depend heavily on manually predefined tools and workflows, which hinder their adaptability, scalability, and generalization across domains. In this work, we introduce Alita--a generalist agent designed with the principle of "Simplicity is the ultimate sophistication," enabling scalable agentic reasoning through minimal predefinition and maximal self-evolution. For minimal predefinition, Alita is equipped with only one component for direct problem-solving, making it much simpler and neater than previous approaches that relied heavily on hand-crafted, elaborate tools and workflows. This clean design enhances its potential to generalize to challenging questions, without being limited by tools. For Maximal self-evolution, we enable the creativity of Alita by providing a suite of general-purpose components to autonomously construct, refine, and reuse external capabilities by generating task-related model context protocols (MCPs) from open source, which contributes to scalable agentic reasoning. Notably, Alita achieves 75.15% pass@1 and 87.27% pass@3 accuracy, which is top-ranking among general-purpose agents, on the GAIA benchmark validation dataset, 74.00% and 52.00% pass@1, respectively, on Mathvista and PathVQA, outperforming many agent systems with far greater complexity. More details will be updated at $\href{https://github.com/CharlesQ9/Alita}{https://github.com/CharlesQ9/Alita}$.

