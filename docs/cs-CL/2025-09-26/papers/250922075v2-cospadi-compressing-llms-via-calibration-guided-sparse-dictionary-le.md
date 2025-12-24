---
layout: default
title: "COSPADI: Compressing LLMs via Calibration-Guided Sparse Dictionary Learning"
---

# COSPADI: Compressing LLMs via Calibration-Guided Sparse Dictionary Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22075" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22075v2</a>
  <a href="https://arxiv.org/pdf/2509.22075.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22075v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22075v2', 'COSPADI: Compressing LLMs via Calibration-Guided Sparse Dictionary Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dmitriy Shopkhoev, Denis Makhov, Magauiya Zhussip, Ammar Ali, Stamatios Lefkimmiatis

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26 (更新: 2025-10-06)

---

## 💡 一句话要点

**提出COSPADI，通过校准引导的稀疏字典学习压缩LLM，提升压缩性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型压缩` `稀疏字典学习` `模型量化` `后训练压缩` `结构化稀疏性`

## 📋 核心要点

1. 现有LLM压缩方法依赖低秩近似，但其结构约束过于严格，导致模型精度显著下降。
2. CoSpaDi采用稀疏字典学习，用稠密字典和稀疏系数矩阵表示权重，实现更灵活的子空间联合表示。
3. 实验表明，CoSpaDi在Llama和Qwen模型上优于现有低秩方法，提升了压缩性能和模型精度。

## 📝 摘要（中文）

本文提出了一种名为CoSpaDi（通过稀疏字典学习进行压缩）的免训练压缩框架，用于压缩大型语言模型（LLMs）。CoSpaDi使用稠密字典和列稀疏系数矩阵来表示权重矩阵，取代了传统的低秩分解。这种方法实现了子空间联合表示，允许原始权重矩阵的不同列在自适应选择的字典原子所跨越的不同子空间中进行近似，提供了比单一不变基更大的表达能力。CoSpaDi利用小型校准数据集优化分解，使压缩投影层的输出激活与原始激活紧密匹配，从而最小化功能重建误差。这种数据感知策略在合理的压缩率下保持了更好的模型保真度，无需任何微调。此外，由此产生的结构化稀疏性允许高效的稀疏-稠密矩阵乘法，并与后训练量化兼容，以进一步提高内存和延迟性能。在多个Llama和Qwen模型上，以20-50%的压缩率进行评估，结果表明CoSpaDi在准确性和困惑度方面均优于最先进的数据感知低秩方法。研究结果表明，结构化稀疏字典学习是高效LLM部署中传统低秩方法的强大替代方案。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）压缩方法，特别是基于低秩分解的方法，虽然计算效率高，但由于其固定的结构约束，在压缩过程中容易导致模型精度显著下降。这些方法通常将权重矩阵的每一列投影到同一个低维子空间，限制了模型的表达能力，无法充分捕捉原始权重矩阵的复杂结构。

**核心思路**：CoSpaDi的核心思路是用一个更灵活的结构化稀疏分解来替代传统的低秩分解。具体来说，它使用一个稠密字典和一个列稀疏的系数矩阵来表示每个权重矩阵。这种方法允许原始权重矩阵的不同列在由自适应选择的字典原子所张成的不同子空间中进行近似，从而实现了一种子空间联合表示。这种表示方法比单一不变基具有更大的表达能力，能够更好地保留原始权重矩阵的信息。

**技术框架**：CoSpaDi的整体框架包括以下几个主要步骤：1) **字典学习**：使用一个稠密字典来表示权重矩阵。2) **稀疏编码**：为每个权重矩阵找到一个列稀疏的系数矩阵，使得字典和系数矩阵的乘积能够近似原始的权重矩阵。3) **校准优化**：使用一个小的校准数据集来优化字典和系数矩阵，使得压缩后的投影层的输出激活与原始模型的输出激活尽可能接近。这个过程旨在最小化功能重建误差，而不是仅仅近似权重。

**关键创新**：CoSpaDi最重要的技术创新点在于它使用结构化稀疏字典学习来表示权重矩阵，而不是传统的低秩分解。这种方法允许模型在不同的子空间中近似不同的权重列，从而提供了更大的灵活性和表达能力。此外，CoSpaDi还引入了一种数据感知的校准优化策略，通过最小化压缩模型的输出激活与原始模型的输出激活之间的差异来提高压缩性能。

**关键设计**：CoSpaDi的关键设计包括：1) **稀疏性约束**：通过对系数矩阵施加稀疏性约束，可以减少模型的存储空间和计算复杂度。2) **校准数据集**：使用一个小的校准数据集来优化字典和系数矩阵，使得压缩模型的输出激活与原始模型的输出激活尽可能接近。3) **损失函数**：使用均方误差（MSE）作为损失函数，来衡量压缩模型的输出激活与原始模型的输出激活之间的差异。4) **压缩比例**：通过调整稀疏性约束的强度来控制压缩比例。

## 📊 实验亮点

CoSpaDi在Llama和Qwen模型上进行了广泛的实验，结果表明，在20-50%的压缩率下，CoSpaDi在准确性和困惑度方面均优于最先进的数据感知低秩方法。例如，在某些模型上，CoSpaDi在保持相同准确率的情况下，实现了比现有方法更高的压缩率，或者在相同压缩率下，实现了更高的准确率。

## 🎯 应用场景

CoSpaDi在大型语言模型的部署和应用中具有广泛的潜力。它可以用于在资源受限的设备上部署LLM，例如移动设备和边缘计算设备。此外，CoSpaDi还可以用于加速LLM的推理速度，从而提高用户体验。该方法在自然语言处理、智能对话系统、文本生成等领域具有重要的应用价值。

## 📄 摘要（原文）

> Post-training compression of large language models (LLMs) largely relies on low-rank weight approximation, which represents each column of a weight matrix in a shared low-dimensional subspace. While this is a computationally efficient strategy, the imposed structural constraint is rigid and can lead to a noticeable model accuracy drop. In this work, we propose CoSpaDi (Compression via Sparse Dictionary Learning), a novel training-free compression framework that replaces low-rank decomposition with a more flexible structured sparse factorization in which each weight matrix is represented with a dense dictionary and a column-sparse coefficient matrix. This formulation enables a union-of-subspaces representation: different columns of the original weight matrix are approximated in distinct subspaces spanned by adaptively selected dictionary atoms, offering greater expressiveness than a single invariant basis. Crucially, CoSpaDi leverages a small calibration dataset to optimize the factorization such that the output activations of compressed projection layers closely match those of the original ones, thereby minimizing functional reconstruction error rather than mere weight approximation. This data-aware strategy preserves better model fidelity without any fine-tuning under reasonable compression ratios. Moreover, the resulting structured sparsity allows efficient sparse-dense matrix multiplication and is compatible with post-training quantization for further memory and latency gains. We evaluate CoSpaDi across multiple Llama and Qwen models under per-layer and per-group settings at 20-50\% compression ratios, demonstrating consistent superiority over state-of-the-art data-aware low-rank methods both in accuracy and perplexity. Our results establish structured sparse dictionary learning as a powerful alternative to conventional low-rank approaches for efficient LLM deployment.

