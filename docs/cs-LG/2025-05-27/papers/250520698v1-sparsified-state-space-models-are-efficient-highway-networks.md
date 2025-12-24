---
layout: default
title: Sparsified State-Space Models are Efficient Highway Networks
---

# Sparsified State-Space Models are Efficient Highway Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20698" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20698v1</a>
  <a href="https://arxiv.org/pdf/2505.20698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20698v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20698v1', 'Sparsified State-Space Models are Efficient Highway Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Woomin Song, Jihoon Tack, Sangwoo Mo, Seunghyuk Oh, Jinwoo Shin

**分类**: cs.LG

**发布日期**: 2025-05-27

**备注**: Accepted to TMLR 2025.03

**🔗 代码/项目**: [GITHUB](https://github.com/woominsong/Simba)

---

## 💡 一句话要点

**提出Simba方法以提高状态空间模型的效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `状态空间模型` `序列建模` `稀疏化` `自然语言处理` `信息流动` `token修剪` `计算效率`

## 📋 核心要点

1. 现有的状态空间模型在处理长序列时，因冗余的递归更新导致信息传递效率低下。
2. 本文提出Simba方法，通过分层稀疏化策略，优先稀疏化上层token以提高信息流动效率。
3. 实验结果显示，Simba在多个自然语言处理任务中超越了基线模型Mamba，提升了模型性能。

## 📝 摘要（中文）

状态空间模型（SSMs）为序列建模提供了有前景的架构，通过用线性递归替代昂贵的自注意力机制，成为Transformer的替代方案。本文提出了一种简单而有效的技巧，通过稀疏化SSMs来增强其在给定计算预算内的表现。我们认为，SSMs中的token由于逐步递归更新而高度冗余，密集的递归操作阻碍了过去信息的传递。特别地，我们观察到SSMs的上层往往更冗余，因为它们编码全局信息，而下层则编码局部信息。基于此，我们引入了Simba，一种基于token修剪的分层稀疏化方法，鼓励上层像高速公路一样运作。实验表明，Simba在各种自然语言任务中超过了基线模型Mamba，且在相同的FLOPS下表现更佳。

## 🔬 方法详解

**问题定义**：本文旨在解决状态空间模型在长序列建模中信息传递效率低下的问题。现有方法由于密集的递归操作，导致token冗余，影响模型性能。

**核心思路**：论文提出的Simba方法通过分层稀疏化策略，优先稀疏化上层token，减少冗余信息的传递，从而提高模型的效率和信息流动。

**技术框架**：Simba的整体架构包括token修剪模块和分层稀疏化策略。首先，通过评估token对最终输出的全局影响，决定哪些token可以被稀疏化。然后，实施分层稀疏化，确保上层token的稀疏化程度高于下层。

**关键创新**：Simba的主要创新在于提出了一种新的token修剪标准，基于局部递归累积全局影响，显著提高了信息流动效率，与传统的密集递归方法形成鲜明对比。

**关键设计**：在Simba中，关键参数包括稀疏化比例和token修剪标准，损失函数设计上考虑了全局信息的影响，确保模型在稀疏化后仍能保持良好的性能。网络结构上，采用了分层设计，使得上层和下层的稀疏化策略有所不同。

## 📊 实验亮点

实验结果表明，Simba在多个自然语言处理任务中表现优异，相比基线模型Mamba，在相同FLOPS下，性能提升显著，证明了其在信息流动和计算效率上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、时间序列分析和其他需要高效序列建模的任务。通过提高状态空间模型的效率，Simba能够在资源有限的情况下处理更长的序列，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> State-space models (SSMs) offer a promising architecture for sequence modeling, providing an alternative to Transformers by replacing expensive self-attention with linear recurrences. In this paper, we propose a simple yet effective trick to enhance SSMs within given computational budgets by sparsifying them. Our intuition is that tokens in SSMs are highly redundant due to gradual recurrent updates, and dense recurrence operations block the delivery of past information. In particular, we observe that upper layers of SSMs tend to be more redundant as they encode global information, while lower layers encode local information. Motivated by this, we introduce Simba, a hierarchical sparsification method for SSMs based on token pruning. Simba sparsifies upper layers more than lower layers, encouraging the upper layers to behave like highways. To achieve this, we propose a novel token pruning criterion for SSMs, measuring the global impact of tokens on the final output by accumulating local recurrences. We demonstrate that Simba outperforms the baseline model, Mamba, with the same FLOPS in various natural language tasks. Moreover, we illustrate the effect of highways, showing that Simba not only enhances efficiency but also improves the information flow across long sequences. Code is available at https://github.com/woominsong/Simba.

