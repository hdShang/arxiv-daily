---
layout: default
title: Semantic Retention and Extreme Compression in LLMs: Can We Have Both?
---

# Semantic Retention and Extreme Compression in LLMs: Can We Have Both?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07289" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07289v1</a>
  <a href="https://arxiv.org/pdf/2505.07289.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07289v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07289v1', 'Semantic Retention and Extreme Compression in LLMs: Can We Have Both?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stanislas Laborde, Martin Cousseau, Antoun Yaacoub, Lionel Prevost

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-12

**备注**: Accepted for publication in the Proceedings of the 2025 International Joint Conference on Neural Networks (IJCNN); this arXiv version includes an appendix with 6 result tables; 10 pages, 15 figures, 7 tables

---

## 💡 一句话要点

**提出联合剪枝与量化以提升大语言模型压缩性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `模型压缩` `剪枝` `量化` `语义保留`

## 📋 核心要点

1. 现有的剪枝和量化方法在模型压缩中各有优势，但联合应用的潜力尚未被充分挖掘。
2. 本文提出了一种新的评估指标SrCr，旨在量化模型压缩与语义保留之间的权衡，优化剪枝与量化的组合。
3. 实验结果显示，推荐的剪枝与量化组合在性能上比单独量化模型平均提升20%。

## 📝 摘要（中文）

随着大语言模型（LLM）应用的快速增长，模型压缩技术的需求日益迫切，以降低计算和内存成本。虽然剪枝和量化方法已显示出潜力，但它们的联合应用尚未得到充分探索。本文研究了联合压缩，提出通过战略性地结合剪枝和量化来实现比单一方法更优的性能与压缩比。为了解决评估LLM性能的挑战，本文引入了语义保留压缩率（SrCr）这一新指标，量化模型压缩与语义保留之间的权衡，促进剪枝-量化配置的优化。实验结果表明，推荐的组合在相同理论压缩率下，平均性能提升20%。

## 🔬 方法详解

**问题定义**：本文要解决的是如何在大语言模型中有效地进行模型压缩，同时保持语义信息的完整性。现有方法如剪枝和量化各自存在局限性，未能充分发挥联合应用的潜力。

**核心思路**：论文的核心思路是通过结合剪枝和量化技术，利用两者的互补优势来提升模型的压缩性能和语义保留能力。这种设计旨在实现更优的性能与压缩比。

**技术框架**：整体架构包括两个主要模块：剪枝模块和量化模块。首先，通过剪枝减少模型的参数量，然后在此基础上进行量化，以进一步降低模型的存储需求和计算复杂度。

**关键创新**：最重要的技术创新点是引入了语义保留压缩率（SrCr）这一新指标，能够量化模型压缩与语义保留之间的权衡，从而优化剪枝与量化的配置。这一指标为评估和比较不同压缩策略提供了新的视角。

**关键设计**：在参数设置上，剪枝比例和量化位数是关键设计因素。损失函数的选择也至关重要，需确保在压缩过程中尽量保留模型的语义信息。

## 📊 实验亮点

实验结果表明，推荐的剪枝与量化组合在相同理论压缩率下，平均性能提升20%，显著优于仅使用量化的模型。这一结果验证了联合压缩策略的有效性，为大语言模型的应用提供了新的思路。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等。通过提高大语言模型的压缩效率，能够在资源受限的环境中更好地部署这些模型，降低计算成本，同时保持较高的性能。这将推动智能助手、自动翻译等应用的普及与发展。

## 📄 摘要（原文）

> The exponential growth in Large Language Model (LLM) deployment has intensified the need for efficient model compression techniques to reduce computational and memory costs. While pruning and quantization have shown promise, their combined potential remains largely unexplored. In this paper, we examine joint compression and how strategically combining pruning and quantization could yield superior performance-to-compression ratios compared to single-method approaches. Recognizing the challenges in accurately assessing LLM performance, we address key limitations of previous evaluation frameworks and introduce the Semantic Retention Compression Rate (SrCr), a novel metric that quantifies the trade-off between model compression and semantic preservation, facilitating the optimization of pruning-quantization configurations. Experiments demonstrate that our recommended combination achieves, on average, a 20% performance increase compared to an equivalent quantization-only model at the same theoretical compression rate.

