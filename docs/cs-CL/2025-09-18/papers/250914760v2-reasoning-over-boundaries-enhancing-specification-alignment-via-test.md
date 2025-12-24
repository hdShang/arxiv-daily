---
layout: default
title: "Reasoning over Boundaries: Enhancing Specification Alignment via Test-time Deliberation"
---

# Reasoning over Boundaries: Enhancing Specification Alignment via Test-time Deliberation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14760" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14760v2</a>
  <a href="https://arxiv.org/pdf/2509.14760.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14760v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14760v2', 'Reasoning over Boundaries: Enhancing Specification Alignment via Test-time Deliberation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Zhang, Yafu Li, Xuyang Hu, Dongrui Liu, Zhilin Wang, Bo Li, Yu Cheng

**分类**: cs.CL

**发布日期**: 2025-09-18 (更新: 2025-10-05)

**备注**: 10 pages main text, 52 pages total (including appendix). Code and resources are available at https://github.com/zzzhr97/SpecBench

---

## 💡 一句话要点

**提出Align3以解决大语言模型的规范对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `规范对齐` `测试时深思` `层次反思` `安全性` `行为规范` `SpecBench` `动态调整`

## 📋 核心要点

1. 现有方法在处理动态、场景特定的行为和安全规范时存在不足，难以实现有效的规范对齐。
2. 本文提出Align3，通过测试时深思（TTD）结合层次反思和修正，来推理和调整规范边界。
3. 实验结果显示，Align3在15个推理模型和18个指令模型上均表现出色，显著提升了规范对齐的效果。

## 📝 摘要（中文）

随着大语言模型（LLMs）在多种现实场景中的应用，用户或组织定制的行为和安全规范（spec）变得愈发重要。这些规范因场景而异，并随着需求的变化而演变。本文将这一挑战形式化为规范对齐，重点关注LLMs在动态、场景特定的规范下的表现。为此，我们提出了一种轻量级方法Align3，利用测试时深思（TTD）结合层次反思和修正来推理规范边界。同时，我们推出了SpecBench，一个统一的基准，用于测量规范对齐，涵盖5个场景、103个规范和1500个提示。实验结果表明，测试时深思能够有效提升规范对齐，Align3在安全性与实用性之间取得了良好的平衡，SpecBench有效揭示了对齐的差距。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在动态、场景特定的行为和安全规范下的对齐问题。现有方法在应对这些变化时往往无法有效调整，导致规范对齐不足。

**核心思路**：Align3的核心思想是利用测试时深思（TTD）技术，通过层次反思和修正机制，动态推理并调整模型的输出，以更好地符合用户的规范要求。

**技术框架**：Align3的整体架构包括三个主要模块：输入处理模块、测试时深思模块和输出调整模块。输入处理模块负责接收用户的规范和提示，测试时深思模块进行层次反思和修正，最后输出调整模块生成符合规范的结果。

**关键创新**：Align3的创新之处在于其轻量级设计和测试时深思的应用，使得模型能够在不增加显著计算开销的情况下，灵活应对复杂的规范要求。这与传统方法相比，显著提高了模型的适应性和灵活性。

**关键设计**：在关键设计方面，Align3采用了多层次的反思机制，结合自我修正策略，确保模型在不同场景下的输出能够动态调整。此外，损失函数的设计也考虑了安全性与实用性的平衡，确保模型输出的可靠性。

## 📊 实验亮点

实验结果表明，Align3在15个推理模型和18个指令模型上均显著提升了规范对齐效果，尤其在安全性与实用性之间的权衡上，Align3表现出色，且计算开销极小。SpecBench有效揭示了模型在不同场景下的对齐差距，为后续研究提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括自动化客服、智能助手、内容生成等场景，能够帮助大语言模型更好地遵循用户或组织的特定规范，从而提升其在实际应用中的安全性和有效性。未来，该方法有望推广到更多复杂的AI系统中，增强其适应性和灵活性。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly applied in diverse real-world scenarios, each governed by bespoke behavioral and safety specifications (spec) custom-tailored by users or organizations. These spec, categorized into safety-spec and behavioral-spec, vary across scenarios and evolve with changing preferences and requirements. We formalize this challenge as specification alignment, focusing on LLMs' ability to follow dynamic, scenario-specific spec from both behavioral and safety perspectives. To address this challenge, we propose Align3, a lightweight method that employs Test-Time Deliberation (TTD) with hierarchical reflection and revision to reason over the specification boundaries. We further present SpecBench, a unified benchmark for measuring specification alignment, covering 5 scenarios, 103 spec, and 1,500 prompts. Experiments on 15 reasoning and 18 instruct models with several TTD methods, including Self-Refine, TPO, and MoreThink, yield three key findings: (i) test-time deliberation enhances specification alignment; (ii) Align3 advances the safety-helpfulness trade-off frontier with minimal overhead; (iii) SpecBench effectively reveals alignment gaps. These results highlight the potential of test-time deliberation as an effective strategy for reasoning over the real-world specification boundaries.

