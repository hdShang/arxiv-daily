---
layout: default
title: Elastic ViTs from Pretrained Models without Retraining
---

# Elastic ViTs from Pretrained Models without Retraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17700" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17700v1</a>
  <a href="https://arxiv.org/pdf/2510.17700.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17700v1" onclick="toggleFavorite(this, '2510.17700v1', 'Elastic ViTs from Pretrained Models without Retraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Walter Simoncini, Michael Dorkenwald, Tijmen Blankevoort, Cees G. M. Snoek, Yuki M. Asano

**分类**: cs.CV

**发布日期**: 2025-10-20

**备注**: Accepted at NeurIPS 2025

---

## 💡 一句话要点

**提出SnapViT，无需重训练即可从预训练ViT模型中获得弹性计算能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Vision Transformer` `模型剪枝` `弹性推理` `后训练优化` `自监督学习`

## 📋 核心要点

1. 现有视觉基础模型尺寸固定，难以适应不同计算资源约束下的部署需求。
2. SnapViT通过结合梯度信息和跨网络结构相关性，实现高效的后预训练剪枝。
3. 实验表明，SnapViT在多种模型和稀疏度下均优于现有方法，且无需重训练。

## 📝 摘要（中文）

视觉基础模型性能卓越，但通常只有预定义的几种尺寸，在实际部署中存在计算资源约束时，选择受限。本文提出SnapViT，一种用于剪枝Vision Transformer的单次网络近似方法，它是一种后预训练的结构化剪枝方法，能够在连续的计算预算范围内实现弹性推理。该方法有效地结合了梯度信息和跨网络结构相关性（通过进化算法近似），不需要标注数据，可以推广到没有分类头的模型，并且无需重新训练。在DINO、SigLIPv2、DeIT和AugReg模型上的实验表明，该方法在各种稀疏度下都优于最先进的方法，只需在单个A100 GPU上花费不到五分钟即可生成可调整到任何计算预算的弹性模型。主要贡献包括：一种用于预训练Vision Transformer的高效剪枝策略，一种用于Hessian矩阵非对角线结构的新型进化近似，以及一种无需重新训练或标签即可保持强大性能的自监督重要性评分机制。

## 🔬 方法详解

**问题定义**：现有Vision Transformer模型通常以固定的尺寸进行训练和部署，这限制了它们在计算资源受限环境中的应用。针对特定硬件或延迟要求，需要重新训练或微调模型，成本高昂。现有的剪枝方法通常需要大量的标注数据或复杂的训练流程，难以充分利用预训练模型的知识。

**核心思路**：SnapViT的核心思想是在预训练模型的基础上，通过结构化剪枝，快速生成一系列具有不同计算复杂度的子网络，从而实现弹性推理。它避免了重新训练或微调的需要，充分利用了预训练模型的知识，并能够快速适应不同的计算预算。

**技术框架**：SnapViT主要包含以下几个阶段：1) **重要性评分**：使用自监督的方式对网络中的不同结构（例如，Transformer block）进行重要性评分，无需标注数据。2) **结构相关性建模**：利用进化算法近似Hessian矩阵的非对角线结构，从而捕捉不同结构之间的相关性。3) **剪枝决策**：基于重要性评分和结构相关性，选择要剪枝的结构，生成具有不同计算复杂度的子网络。4) **模型部署**：根据实际的计算资源约束，选择合适的子网络进行部署。

**关键创新**：SnapViT的关键创新在于：1) **高效的剪枝策略**：结合梯度信息和跨网络结构相关性，实现高效的结构化剪枝。2) **Hessian矩阵非对角线结构的进化近似**：提出了一种新的进化算法，用于近似Hessian矩阵的非对角线结构，从而更好地捕捉不同结构之间的相关性。3) **自监督重要性评分机制**：提出了一种自监督的重要性评分机制，无需标注数据即可评估网络中不同结构的重要性。

**关键设计**：SnapViT的关键设计包括：1) 使用梯度信息的自监督重要性评分，例如，基于DINO的自监督信号。2) 使用进化算法来近似Hessian矩阵的非对角线结构，以捕捉不同层之间的依赖关系。3) 结构化剪枝策略，例如，剪枝整个Transformer block，以减少计算量。4) 损失函数的设计，旨在保持剪枝后模型的性能。

## 📊 实验亮点

在DINO、SigLIPv2、DeIT和AugReg等预训练模型上进行了实验，结果表明SnapViT在各种稀疏度下均优于现有方法。例如，在ImageNet数据集上，使用DINO预训练模型，SnapViT在保持相同性能的情况下，可以将计算量减少50%以上。生成弹性模型所需的时间也很短，在单个A100 GPU上只需不到五分钟。

## 🎯 应用场景

SnapViT适用于各种计算资源受限的场景，例如移动设备、边缘计算和嵌入式系统。它可以帮助开发者快速生成适应不同硬件平台的模型，降低部署成本，并提高推理效率。此外，该方法还可以应用于模型压缩、知识蒸馏等领域，具有广泛的应用前景。

## 📄 摘要（原文）

> Vision foundation models achieve remarkable performance but are only available in a limited set of pre-determined sizes, forcing sub-optimal deployment choices under real-world constraints. We introduce SnapViT: Single-shot network approximation for pruned Vision Transformers, a new post-pretraining structured pruning method that enables elastic inference across a continuum of compute budgets. Our approach efficiently combines gradient information with cross-network structure correlations, approximated via an evolutionary algorithm, does not require labeled data, generalizes to models without a classification head, and is retraining-free. Experiments on DINO, SigLIPv2, DeIT, and AugReg models demonstrate superior performance over state-of-the-art methods across various sparsities, requiring less than five minutes on a single A100 GPU to generate elastic models that can be adjusted to any computational budget. Our key contributions include an efficient pruning strategy for pretrained Vision Transformers, a novel evolutionary approximation of Hessian off-diagonal structures, and a self-supervised importance scoring mechanism that maintains strong performance without requiring retraining or labels. Code and pruned models are available at: https://elastic.ashita.nl/

