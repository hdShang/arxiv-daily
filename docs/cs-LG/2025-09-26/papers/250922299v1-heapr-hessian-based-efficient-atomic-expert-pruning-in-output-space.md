---
layout: default
title: "HEAPr: Hessian-based Efficient Atomic Expert Pruning in Output Space"
---

# HEAPr: Hessian-based Efficient Atomic Expert Pruning in Output Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22299" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22299v1</a>
  <a href="https://arxiv.org/pdf/2509.22299.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22299v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22299v1', 'HEAPr: Hessian-based Efficient Atomic Expert Pruning in Output Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ke Li, Zheng Yang, Zhongbin Zhou, Feng Xue, Zhonglin Jiang, Wenxiao Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-26

**🔗 代码/项目**: [GITHUB](https://github.com/LLIKKE/HEAPr)

---

## 💡 一句话要点

**HEAPr：基于Hessian的输出空间高效原子专家剪枝方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `模型剪枝` `原子专家` `二阶信息` `Hessian矩阵` `模型压缩` `大型语言模型`

## 📋 核心要点

1. MoE模型参数量巨大，部署困难，现有专家级别剪枝粒度粗，精度损失大。
2. HEAPr将专家分解为原子专家，利用Hessian二阶信息评估原子专家的重要性，实现更精细的剪枝。
3. 实验表明，HEAPr在DeepSeek MoE和Qwen MoE模型上，能以20%-25%压缩率实现近乎无损的压缩，并降低约20%的FLOPs。

## 📝 摘要（中文）

本文提出了一种名为HEAPr的新型剪枝算法，用于压缩大型语言模型中的混合专家（MoE）架构。与现有主要关注专家级别剪枝的方法不同，HEAPr将专家分解为更小的、不可分割的原子专家，从而实现更精确和灵活的剪枝。该方法利用基于最优脑外科医生（OBS）理论的二阶信息来衡量每个原子专家的重要性。为了解决二阶信息带来的计算和存储挑战，HEAPr利用原子专家的固有属性，将二阶信息从专家参数转换为原子专家参数，并进一步简化为原子专家输出的二阶信息，从而将空间复杂度从O(d^4)降低到O(d^2)，其中d是模型维度。HEAPr仅需在小型校准集上进行两次前向传递和一次反向传递即可计算原子专家的重要性。在DeepSeek MoE和Qwen MoE系列等MoE模型上的大量实验表明，HEAPr在各种压缩率和基准测试中均优于现有的专家级别剪枝方法。具体而言，HEAPr在大多数模型中以20%~25%的压缩率实现了近乎无损的压缩，同时还将FLOPs降低了近20%。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型中MoE架构因参数量巨大而难以部署的问题。现有的专家级别剪枝方法粒度较粗，容易导致显著的精度下降，无法在压缩模型的同时保持性能。

**核心思路**：论文的核心思路是将MoE模型中的专家进一步分解为更小的“原子专家”，然后对这些原子专家进行选择性剪枝。通过更细粒度的剪枝，可以更精确地去除冗余参数，从而在保持模型性能的同时实现更高的压缩率。利用Hessian矩阵的二阶信息来评估每个原子专家的重要性，类似于Optimal Brain Surgeon (OBS) 理论。

**技术框架**：HEAPr算法主要包含以下几个阶段：1) **原子专家分解**：将MoE模型中的专家分解为更小的原子专家。具体如何分解论文中未明确说明，未知。2) **二阶信息计算**：利用Hessian矩阵计算每个原子专家的重要性。为了降低计算复杂度，将二阶信息从专家参数转换为原子专家输出的二阶信息。3) **原子专家剪枝**：根据计算出的重要性，对原子专家进行剪枝。4) **模型微调**（可选）：对剪枝后的模型进行微调，以恢复性能。

**关键创新**：HEAPr的关键创新在于：1) **原子专家剪枝**：提出了一种更细粒度的剪枝方法，可以更精确地去除冗余参数。2) **二阶信息简化**：通过将二阶信息从专家参数转换为原子专家输出的二阶信息，显著降低了计算复杂度。

**关键设计**：论文的关键设计包括：1) **原子专家的定义**：论文中没有明确给出原子专家的定义，需要进一步研究代码才能确定。2) **二阶信息的计算方法**：论文采用了类似于OBS理论的方法来计算二阶信息，并进行了简化以降低计算复杂度。具体简化方法需要参考论文细节。3) **剪枝策略**：论文根据原子专家的重要性进行剪枝，具体的剪枝策略（例如，剪枝比例、剪枝阈值等）需要参考论文细节。

## 📊 实验亮点

HEAPr在DeepSeek MoE和Qwen MoE系列模型上进行了广泛的实验，结果表明，该算法在各种压缩率和基准测试中均优于现有的专家级别剪枝方法。具体而言，HEAPr在大多数模型中以20%~25%的压缩率实现了近乎无损的压缩，同时还将FLOPs降低了近20%。这些结果表明，HEAPr是一种高效且有效的MoE模型压缩算法。

## 🎯 应用场景

HEAPr算法可应用于各种基于MoE架构的大型语言模型，例如DeepSeek MoE、Qwen MoE等。通过该算法，可以在保持模型性能的同时显著降低模型的大小和计算复杂度，从而使得这些模型能够更容易地部署在资源受限的设备上，例如移动设备、边缘设备等。此外，该算法还可以用于加速模型的推理速度，提高模型的效率。

## 📄 摘要（原文）

> Mixture-of-Experts (MoE) architectures in large language models (LLMs) deliver exceptional performance and reduced inference costs compared to dense LLMs. However, their large parameter counts result in prohibitive memory requirements, limiting practical deployment. While existing pruning methods primarily focus on expert-level pruning, this coarse granularity often leads to substantial accuracy degradation. In this work, we introduce HEAPr, a novel pruning algorithm that decomposes experts into smaller, indivisible atomic experts, enabling more precise and flexible atomic expert pruning. To measure the importance of each atomic expert, we leverage second-order information based on principles similar to Optimal Brain Surgeon (OBS) theory. To address the computational and storage challenges posed by second-order information, HEAPr exploits the inherent properties of atomic experts to transform the second-order information from expert parameters into that of atomic expert parameters, and further simplifies it to the second-order information of atomic expert outputs. This approach reduces the space complexity from $O(d^4)$, where d is the model's dimensionality, to $O(d^2)$. HEAPr requires only two forward passes and one backward pass on a small calibration set to compute the importance of atomic experts. Extensive experiments on MoE models, including DeepSeek MoE and Qwen MoE family, demonstrate that HEAPr outperforms existing expert-level pruning methods across a wide range of compression ratios and benchmarks. Specifically, HEAPr achieves nearly lossless compression at compression ratios of 20% ~ 25% in most models, while also reducing FLOPs nearly by 20%. The code can be found at \href{https://github.com/LLIKKE/HEAPr}{https://github.com/LLIKKE/HEAPr}.

