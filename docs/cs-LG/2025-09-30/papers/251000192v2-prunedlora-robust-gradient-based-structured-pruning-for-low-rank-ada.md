---
layout: default
title: "PrunedLoRA: Robust Gradient-Based structured pruning for Low-rank Adaptation in Fine-tuning"
---

# PrunedLoRA: Robust Gradient-Based structured pruning for Low-rank Adaptation in Fine-tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00192" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00192v2</a>
  <a href="https://arxiv.org/pdf/2510.00192.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00192v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00192v2', 'PrunedLoRA: Robust Gradient-Based structured pruning for Low-rank Adaptation in Fine-tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Yu, Cong Xie, Ziyu Zhao, Tiantian Fan, Lingzhou Xue, Zhi Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30 (更新: 2025-11-01)

---

## 💡 一句话要点

**PrunedLoRA：基于梯度鲁棒结构化剪枝的低秩自适应微调方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩自适应` `参数高效微调` `结构化剪枝` `梯度剪枝` `大型语言模型`

## 📋 核心要点

1. LoRA微调方法存在表征能力不足的问题，如何从过参数化的LoRA空间中获得更具表达能力的适配器是关键挑战。
2. PrunedLoRA通过结构化剪枝动态地剪除不重要的LoRA组件，并阻止其重新激活，从而实现灵活的秩分配和更优的性能。
3. 实验表明，PrunedLoRA在数学推理、代码生成和自然语言理解等任务上，均优于LoRA及其变体以及现有的结构化剪枝方法。

## 📝 摘要（中文）

低秩自适应(LoRA)已成为大型语言模型参数高效微调的常用范例，但其表征能力通常落后于全量微调。在LoRA的背景下，一个关键的开放问题是如何从过度参数化的空间中获得富有表现力的低秩适配器。我们提出了PrunedLoRA，一个新的框架，它利用结构化剪枝从过度参数化的初始化中获得高度代表性的低秩适配器。与施加固定低秩预算的先前方法不同，PrunedLoRA在微调期间动态地剪枝不太重要的组件并防止它们的重新激活，从而实现灵活和自适应的秩分配。对于结构化剪枝，通过最小化整体损失的剪枝误差，我们提供了一种基于梯度的剪枝策略中的细粒度剪枝和恢复更新，并具有可靠的解释。我们提供了结构化剪枝鲁棒性的第一个理论分析，并证明在权重扰动的影响下，基于梯度的剪枝比基于激活的剪枝在整体损失方面更鲁棒。在经验上，PrunedLoRA在数学推理、代码生成和自然语言理解的监督微调任务中始终优于LoRA及其变体，并且还在不同的稀疏度水平上展示了优于现有结构化剪枝方法的优势。

## 🔬 方法详解

**问题定义**：LoRA虽然参数高效，但其表征能力有限，难以达到全量微调的效果。现有方法通常采用固定的低秩预算，无法根据任务自适应地调整秩的大小。因此，如何从过参数化的LoRA空间中找到更具表达能力的低秩适配器，同时保持参数效率，是一个亟待解决的问题。

**核心思路**：PrunedLoRA的核心思想是通过结构化剪枝，动态地去除LoRA中不重要的组件，从而在微调过程中自适应地调整秩的大小。通过这种方式，PrunedLoRA能够从过参数化的初始化中提取出更具代表性的低秩适配器，提高模型的表征能力。

**技术框架**：PrunedLoRA框架主要包含以下几个阶段：1) 初始化一个过参数化的LoRA模型；2) 在微调过程中，使用基于梯度的结构化剪枝策略，动态地剪除不重要的LoRA组件；3) 为了防止被剪枝的组件重新激活，框架会阻止这些组件的权重更新。整个过程旨在优化LoRA的秩分配，使其更适应特定任务。

**关键创新**：PrunedLoRA的关键创新在于其动态结构化剪枝策略。与传统的固定秩LoRA方法不同，PrunedLoRA能够根据梯度信息，自适应地调整LoRA的秩，从而更好地平衡参数效率和模型性能。此外，论文还提供了结构化剪枝鲁棒性的理论分析，证明了基于梯度的剪枝方法在权重扰动下比基于激活的剪枝方法更鲁棒。

**关键设计**：PrunedLoRA的关键设计包括：1) 基于梯度的剪枝策略，通过最小化剪枝误差来确定需要剪枝的组件；2) 阻止被剪枝组件重新激活的机制，确保剪枝的有效性；3) 细粒度的剪枝和恢复更新，允许模型在微调过程中动态地调整结构。具体的损失函数设计和参数设置在论文中有详细描述，旨在平衡剪枝的强度和模型的性能。

## 📊 实验亮点

PrunedLoRA在多个任务上取得了显著的性能提升。在数学推理、代码生成和自然语言理解等任务中，PrunedLoRA均优于LoRA及其变体。此外，实验结果还表明，PrunedLoRA在不同的稀疏度水平下，都优于现有的结构化剪枝方法。这些结果充分证明了PrunedLoRA的有效性和优越性。

## 🎯 应用场景

PrunedLoRA具有广泛的应用前景，可用于各种需要高效微调大型语言模型的场景，例如自然语言处理、代码生成、数学推理等。该方法能够提升LoRA的表征能力，使其在资源受限的环境下也能达到接近全量微调的性能。此外，PrunedLoRA的动态秩分配机制，使其能够更好地适应不同的任务和数据集，具有很强的通用性。

## 📄 摘要（原文）

> Low-rank adaptation (LoRA) has become a widely used paradigm for parameter-efficient fine-tuning of large language models, yet its representational capacity often lags behind full fine-tuning. Within the context of LoRA, a key open question is how to obtain expressive low-rank adapters from over-parameterized spaces. We propose \textit{PrunedLoRA}, a new framework that leverages structured pruning to obtain highly representative low-rank adapters from an over-parameterized initialization. Unlike prior approaches that impose a fixed low-rank budget, PrunedLoRA dynamically prunes less important components during fine-tuning and prevents their reactivation, enabling flexible and adaptive rank allocation. For structured pruning, by minimizing the pruning error for overall loss, we provide fine-grained pruning and recovery updates in a gradient-based pruning strategy with grounded interpretation. We provide the first theoretical analysis of the robustness of structured pruning and provably show that under the impact of weight perturbation, gradient-based pruning is more robust than activation-based pruning with respect to overall loss. Empirically, PrunedLoRA consistently outperforms LoRA and its variants across supervised fine-tuning tasks in mathematical reasoning, code generation, and natural language understanding, and it also demonstrates advantages over existing structured pruning methods across diverse sparsity levels.

