---
layout: default
title: Efficient Shapley Value-based Non-Uniform Pruning of Large Language Models
---

# Efficient Shapley Value-based Non-Uniform Pruning of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01731" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01731v3</a>
  <a href="https://arxiv.org/pdf/2505.01731.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01731v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01731v3', 'Efficient Shapley Value-based Non-Uniform Pruning of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuan Sun, Han Yu, Lizhen Cui, Xiaoxiao Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-03 (更新: 2025-05-21)

---

## 💡 一句话要点

**提出基于Shapley值的非均匀剪枝方法以优化大语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `非均匀剪枝` `Shapley值` `模型优化` `计算效率` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有的均匀剪枝方法未能考虑不同层在模型中的重要性，导致性能损失。
2. 提出的SV-NUP方法通过Shapley值量化每层的贡献，进行非均匀剪枝，优化剪枝预算分配。
3. 实验结果显示，SV-NUP在多个LLM上显著提升了性能，困惑度降低幅度达到18.01%和19.55%。

## 📝 摘要（中文）

剪枝大语言模型（LLMs）是减少模型规模和计算复杂度的有效方法，同时保持性能。传统的层级剪枝方法通常采用均匀稀疏策略，未能考虑各个变换器层的重要性，导致性能不佳。为此，本文提出了基于Shapley值的非均匀剪枝（SV-NUP）方法，通过量化每个变换器层对整体模型性能的贡献，为不同层分配定制的剪枝预算，以保留关键参数。此外，设计了基于滑动窗口的Shapley值近似方法，显著降低了计算开销。实验结果表明，SV-NUP在多个LLM（如LLaMA-v1、LLaMA-v2和OPT）上有效提升了剪枝模型的性能，LLaMA-7B和LLaMA-13B的困惑度分别降低了18.01%和19.55%。

## 🔬 方法详解

**问题定义**：本文旨在解决传统均匀剪枝方法在大语言模型中未能考虑各层重要性的问题，导致模型性能下降。

**核心思路**：SV-NUP方法通过Shapley值来量化每个变换器层对模型性能的贡献，从而为不同层分配适当的剪枝预算，以保留对性能至关重要的参数。

**技术框架**：该方法包括两个主要模块：首先是Shapley值计算模块，用于评估各层的贡献；其次是剪枝决策模块，根据评估结果进行非均匀剪枝。为提高效率，采用滑动窗口技术近似Shapley值计算。

**关键创新**：SV-NUP的核心创新在于引入Shapley值进行非均匀剪枝，这与传统均匀剪枝方法的本质区别在于能够针对每层的实际贡献进行优化。

**关键设计**：在设计中，采用滑动窗口方法来近似Shapley值计算，显著降低了计算复杂度，同时确保了剪枝效果的有效性。

## 📊 实验亮点

实验结果表明，SV-NUP方法在LLaMA-7B和LLaMA-13B模型上分别实现了18.01%和19.55%的困惑度降低，相较于SparseGPT在70%稀疏率下的表现，显著提升了剪枝模型的性能。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和机器翻译等，能够有效提升大语言模型的性能和效率。通过优化模型结构，SV-NUP方法有助于在资源受限的环境中部署更强大的语言模型，推动智能应用的发展。

## 📄 摘要（原文）

> Pruning large language models (LLMs) is a promising solution for reducing model sizes and computational complexity while preserving performance. Traditional layer-wise pruning methods often adopt a uniform sparsity approach across all layers, which leads to suboptimal performance due to the varying significance of individual transformer layers within the model not being accounted for. To this end, we propose the Shapley Value-based Non-Uniform Pruning (SV-NUP) method for LLMs. This approach quantifies the contribution of each transformer layer to the overall model performance, enabling the assignment of tailored pruning budgets to different layers to retain critical parameters. To further improve efficiency, we design the Sliding Window-based Shapley Value approximation method. It substantially reduces computational overhead compared to exact SV calculation methods. Extensive experiments on various LLMs including LLaMA-v1, LLaMA-v2 and OPT demonstrate the effectiveness of the proposed approach. The results reveal that non-uniform pruning significantly enhances the performance of pruned models. Notably, SV-NUP achieves a reduction in perplexity (PPL) of 18.01% and 19.55% on LLaMA-7B and LLaMA-13B, respectively, compared to SparseGPT at 70% sparsity.

