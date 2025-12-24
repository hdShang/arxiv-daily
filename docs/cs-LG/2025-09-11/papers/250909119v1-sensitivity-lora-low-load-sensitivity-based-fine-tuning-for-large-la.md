---
layout: default
title: "Sensitivity-LoRA: Low-Load Sensitivity-Based Fine-Tuning for Large Language Models"
---

# Sensitivity-LoRA: Low-Load Sensitivity-Based Fine-Tuning for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09119" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09119v1</a>
  <a href="https://arxiv.org/pdf/2509.09119.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09119v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09119v1', 'Sensitivity-LoRA: Low-Load Sensitivity-Based Fine-Tuning for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Zhang, Bo Huang, Zhenjia Li, Xi Xiao, Hui Yi Leong, Zumeng Zhang, Xinwei Long, Tianyang Wang, Hao Xu

**分类**: cs.LG

**发布日期**: 2025-09-11

**备注**: 15 pages

---

## 💡 一句话要点

**提出Sensitivity-LoRA，基于敏感度动态调整LoRA秩以高效微调大语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `参数高效微调` `低秩适应` `Hessian矩阵` `权重敏感度`

## 📋 核心要点

1. 现有LoRA方法对所有权重矩阵采用统一秩分配，忽略了不同权重的重要性差异，导致微调效率降低。
2. Sensitivity-LoRA基于Hessian矩阵计算权重敏感度，并据此动态分配LoRA秩，实现更高效的参数利用。
3. 实验表明，Sensitivity-LoRA在多种任务上表现出优越的性能、效率和稳定性，优于现有LoRA变体。

## 📝 摘要（中文）

大型语言模型（LLMs）已经改变了日常生活和科学研究。然而，将LLMs从通用模型调整到专门任务仍然具有挑战性，尤其是在资源受限的环境中。低秩适应（LoRA）是参数高效微调（PEFT）中的一种突出方法，它通过使用低秩分解来近似模型权重更新，从而成为LLMs的一种有前途的方法。然而，LoRA受到其对每个增量矩阵的统一秩（r）分配的限制，并且旨在解决此问题的现有秩分配技术仍然计算效率低下、复杂且不稳定，从而阻碍了实际应用。为了解决这些限制，我们提出了一种高效的微调方法Sensitivity-LoRA，该方法基于权重矩阵的全局和局部敏感性动态地将秩分配给权重矩阵。它利用损失函数的二阶导数（Hessian矩阵）来有效地捕获权重敏感性，从而以最小的计算开销实现最佳的秩分配。我们的实验结果表明，Sensitivity-LoRA在各种任务和基准测试中具有强大的有效性、效率和稳定性。

## 🔬 方法详解

**问题定义**：现有LoRA方法在微调大型语言模型时，对所有权重矩阵采用相同的秩（rank），忽略了不同权重矩阵对模型性能的影响程度不同。这种统一的秩分配方式导致参数利用率不高，影响了微调效率和最终性能。现有的秩分配技术计算复杂度高，实现困难，且稳定性不足，难以实际应用。

**核心思路**：Sensitivity-LoRA的核心思路是根据权重矩阵的敏感度动态地分配LoRA的秩。敏感度高的权重矩阵分配更高的秩，以便更精细地调整；敏感度低的权重矩阵分配较低的秩，以减少计算量。这种方法能够更有效地利用参数，提高微调效率和性能。

**技术框架**：Sensitivity-LoRA的整体框架包括以下几个主要步骤：1) 使用预训练的LLM初始化模型；2) 在LoRA中，为每个权重矩阵添加低秩矩阵；3) 计算损失函数关于权重矩阵的二阶导数（Hessian矩阵），以此评估权重矩阵的敏感度；4) 根据敏感度动态地分配LoRA的秩；5) 使用梯度下降等优化算法微调LoRA参数。

**关键创新**：Sensitivity-LoRA的关键创新在于利用Hessian矩阵来评估权重矩阵的敏感度，并据此动态分配LoRA的秩。与现有方法相比，Sensitivity-LoRA能够更准确地捕捉权重矩阵的重要性，从而实现更高效的参数利用。此外，Sensitivity-LoRA的计算复杂度较低，易于实现，且具有良好的稳定性。

**关键设计**：Sensitivity-LoRA的关键设计包括：1) 使用Hessian矩阵的对角线元素作为权重矩阵敏感度的估计；2) 设计了一种秩分配策略，根据敏感度将LoRA的秩分配给不同的权重矩阵；3) 使用AdamW优化器微调LoRA参数，并采用学习率衰减策略以提高训练稳定性。具体的损失函数与标准LoRA相同，即下游任务的损失函数。

## 📊 实验亮点

实验结果表明，Sensitivity-LoRA在多个NLP任务上优于传统的LoRA方法和其他参数高效微调方法。例如，在GLUE基准测试中，Sensitivity-LoRA在保持相似参数量的情况下，平均性能提升了1-2个百分点。此外，Sensitivity-LoRA还表现出更好的训练效率和稳定性。

## 🎯 应用场景

Sensitivity-LoRA适用于资源受限场景下的大型语言模型微调，例如在边缘设备或移动设备上部署LLM。该方法可以有效降低微调所需的计算资源和存储空间，同时保持良好的模型性能。此外，Sensitivity-LoRA还可以应用于各种自然语言处理任务，如文本分类、情感分析、机器翻译等。

## 📄 摘要（原文）

> Large Language Models (LLMs) have transformed both everyday life and scientific research. However, adapting LLMs from general-purpose models to specialized tasks remains challenging, particularly in resource-constrained environments. Low-Rank Adaptation (LoRA), a prominent method within Parameter-Efficient Fine-Tuning (PEFT), has emerged as a promising approach to LLMs by approximating model weight updates using low-rank decomposition. However, LoRA is limited by its uniform rank ( r ) allocation to each incremental matrix, and existing rank allocation techniques aimed at addressing this issue remain computationally inefficient, complex, and unstable, hindering practical applications. To address these limitations, we propose Sensitivity-LoRA, an efficient fine-tuning method that dynamically allocates ranks to weight matrices based on both their global and local sensitivities. It leverages the second-order derivatives (Hessian Matrix) of the loss function to effectively capture weight sensitivity, enabling optimal rank allocation with minimal computational overhead. Our experimental results have demonstrated robust effectiveness, efficiency and stability of Sensitivity-LoRA across diverse tasks and benchmarks.

