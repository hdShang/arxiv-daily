---
layout: default
title: "Type-Compliant Adaptation Cascades: Adapting Programmatic LM Workflows to Data"
---

# Type-Compliant Adaptation Cascades: Adapting Programmatic LM Workflows to Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18244" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18244v2</a>
  <a href="https://arxiv.org/pdf/2508.18244.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18244v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18244v2', 'Type-Compliant Adaptation Cascades: Adapting Programmatic LM Workflows to Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chu-Cheng Lin, Daiyi Peng, Yifeng Lu, Ming Zhang, Eugene Ie

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-25 (更新: 2025-09-26)

---

## 💡 一句话要点

**提出类型兼容适应级联以解决复杂工作流适应问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `工作流适应` `类型概率程序` `结构化任务` `优化算法`

## 📋 核心要点

1. 现有方法在复杂工作流中组合大型语言模型时，常常面临脆弱性和合规性不足的问题。
2. 本文提出的TACs框架通过学习类型概率程序来实现工作流适应，增强了模型的稳定性和合规性。
3. 实验结果显示，TACs在多个结构化任务上显著提升性能，例如FinQA从12.0%提升至24.7%。

## 📝 摘要（中文）

在复杂的多步骤工作流中，可靠地组合大型语言模型（LLMs）仍然是一个重大挑战。现有的主流方法——在管道中优化离散提示——常常脆弱，难以强制执行结构化任务所需的正式合规性。本文提出了类型兼容适应级联（TACs）框架，将工作流适应重新定义为学习类型概率程序。TACs将整个工作流视为未归一化的联合分布，从而实现了基于梯度的原则性训练，即使在潜在的中间结构下也能有效进行。我们为可处理的优化目标提供了理论依据，证明了随着模型学习类型合规性，优化偏差会消失。实验证明，TACs在结构化任务上显著优于最先进的提示优化基线。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂多步骤工作流中，如何可靠地组合大型语言模型（LLMs）的问题。现有方法在优化离散提示时表现脆弱，难以满足结构化任务的合规性要求。

**核心思路**：TACs框架通过将工作流适应视为学习类型概率程序，重新定义了工作流的适应过程。这种方法允许在潜在中间结构下进行基于梯度的训练，从而提高了模型的稳定性和合规性。

**技术框架**：TACs的整体架构包括参数高效适应的LLMs和确定性逻辑，整个工作流被视为未归一化的联合分布。通过这种方式，模型可以在训练过程中逐步学习类型合规性。

**关键创新**：TACs的主要创新在于其将工作流适应转化为学习类型概率程序的能力，这与现有的提示优化方法本质上不同，后者往往依赖于固定的提示设计。

**关键设计**：在TACs中，采用了特定的损失函数以确保类型合规性，并设计了高效的参数调整机制，以便在训练过程中优化模型性能。

## 📊 实验亮点

实验结果表明，TACs在多个结构化任务上显著优于现有的提示优化基线。例如，FinQA的准确率从12.0%提升至24.7%，MGSM-SymPy从57.1%提升至75.9%，MGSM从1.6%提升至27.3%，MuSR从36.5%提升至62.6%。

## 🎯 应用场景

该研究的潜在应用领域包括自动化问答系统、智能助手和复杂数据处理工作流等。通过提高大型语言模型在结构化任务中的表现，TACs能够为实际应用提供更可靠的解决方案，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Reliably composing Large Language Models (LLMs) for complex, multi-step workflows remains a significant challenge. The dominant paradigm -- optimizing discrete prompts in a pipeline -- is notoriously brittle and struggles to enforce the formal compliance required for structured tasks. We introduce Type-Compliant Adaptation Cascades (TACs), a framework that recasts workflow adaptation as learning typed probabilistic programs. TACs treat the entire workflow, which is composed of parameter-efficiently adapted LLMs and deterministic logic, as an unnormalized joint distribution. This enables principled, gradient-based training even with latent intermediate structures. We provide theoretical justification for our tractable optimization objective, proving that the optimization bias vanishes as the model learns type compliance. Empirically, TACs significantly outperform state-of-the-art prompt-optimization baselines. Gains are particularly pronounced on structured tasks, improving FinQA from $12.0\%$ to $24.7\%$ for a Qwen 3 8B model, MGSM-SymPy from $57.1\%$ to $75.9\%$ for a Gemma 2 27B model, MGSM from $1.6\%$ to $27.3\%$, and MuSR from $36.5\%$ to $62.6\%$ for a Gemma 7B model. TACs offer a robust and theoretically grounded paradigm for developing reliable, task-compliant LLM systems.

