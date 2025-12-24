---
layout: default
title: "GPTailor: Large Language Model Pruning Through Layer Cutting and Stitching"
---

# GPTailor: Large Language Model Pruning Through Layer Cutting and Stitching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20480" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20480v1</a>
  <a href="https://arxiv.org/pdf/2506.20480.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20480v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20480v1', 'GPTailor: Large Language Model Pruning Through Layer Cutting and Stitching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guinan Su, Li Shen, Lu Yin, Shiwei Liu, Yanwu Yang, Jonas Geiping

**分类**: cs.CL

**发布日期**: 2025-06-25

**🔗 代码/项目**: [GITHUB](https://github.com/Guinan-Su/auto-merge-llm)

---

## 💡 一句话要点

**提出GPTailor以解决大语言模型压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `模型剪枝` `层合并` `优化算法` `自然语言处理` `模型压缩` `深度学习`

## 📋 核心要点

1. 现有的模型剪枝方法主要集中于单一模型，难以有效利用多个微调模型的优势。
2. 本文提出了一种通过层的组合和合并来压缩模型的新策略，旨在保留不同微调模型的能力。
3. 实验结果显示，所提方法在压缩模型时能够保持高达97.3%的性能，同时减少约25%的参数量。

## 📝 摘要（中文）

大语言模型（LLMs）在语言理解和生成方面展现了卓越的能力，但其庞大的模型规模在部署和推理时带来了显著挑战。虽然结构化剪枝方法能够有效降低计算成本，但现有方法主要集中于单一模型的剪枝。本文提出了一种新策略，通过从微调后的模型变体中战略性地组合或合并层，来压缩模型，同时保留原始模型的能力。我们将这些LLMs的最优定制视为一个零阶优化问题，采用支持层移除、层选择和层合并的搜索空间。实验表明，该方法在压缩模型方面表现出色，例如，针对Llama2-13B模型系列，我们的压缩模型在移除约25%参数的同时，保持了约97.3%的原始性能，显著优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在部署时面临的计算成本高和模型规模庞大的问题。现有的剪枝方法大多集中于单一模型，未能有效利用多个微调模型的特性。

**核心思路**：本文的核心思路是通过战略性地组合和合并不同微调模型的层，形成一个新的压缩模型，从而保留原始模型的能力。通过这种方式，可以在保持性能的同时，显著减少模型参数。

**技术框架**：整体架构包括三个主要模块：层移除、层选择和层合并。首先，识别需要移除的层；其次，从不同候选模型中选择合适的层；最后，将选定的层进行合并，形成新的模型结构。

**关键创新**：最重要的技术创新在于将模型压缩问题视为一个零阶优化问题，允许在一个统一的搜索空间中进行多种操作。这种方法与传统的单一模型剪枝方法本质上不同，能够更全面地利用多个模型的优势。

**关键设计**：在参数设置上，本文设计了适应不同模型特性的损失函数，并在网络结构上采用了灵活的层组合策略，以确保压缩后的模型能够保持高性能。

## 📊 实验亮点

实验结果显示，针对Llama2-13B模型系列，所提压缩模型在移除约25%参数的情况下，仍能保持约97.3%的原始性能。这一结果显著优于现有的最先进方法，展示了该方法在模型压缩领域的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等，能够有效降低模型的计算资源需求，提升部署效率。未来，该方法可能在大规模语言模型的应用中发挥重要作用，推动更广泛的商业化和实用化进程。

## 📄 摘要（原文）

> Large language models (LLMs) have shown remarkable capabilities in language understanding and generation. However, such impressive capability typically comes with a substantial model size, which presents significant challenges in deployment and inference. While structured pruning of model parameters offers a promising way to reduce computational costs at deployment time, current methods primarily focus on single model pruning. In this work, we develop a novel strategy to compress models by strategically combining or merging layers from finetuned model variants, which preserves the original model's abilities by aggregating capabilities accentuated in different finetunes. We pose the optimal tailoring of these LLMs as a zero-order optimization problem, adopting a search space that supports three different operations: (1) Layer removal, (2) Layer selection from different candidate models, and (3) Layer merging. Our experiments demonstrate that this approach leads to competitive model pruning, for example, for the Llama2-13B model families, our compressed models maintain approximately 97.3\% of the original performance while removing $\sim25\%$ of parameters, significantly outperforming previous state-of-the-art methods. The code is available at https://github.com/Guinan-Su/auto-merge-llm.

