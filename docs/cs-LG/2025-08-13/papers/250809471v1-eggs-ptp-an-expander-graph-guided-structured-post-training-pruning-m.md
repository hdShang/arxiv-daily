---
layout: default
title: "EGGS-PTP: An Expander-Graph Guided Structured Post-training Pruning Method for Large Language Models"
---

# EGGS-PTP: An Expander-Graph Guided Structured Post-training Pruning Method for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09471" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09471v1</a>
  <a href="https://arxiv.org/pdf/2508.09471.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09471v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09471v1', 'EGGS-PTP: An Expander-Graph Guided Structured Post-training Pruning Method for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Omar Bazarbachi, Zijun Sun, Yanning Shen

**分类**: cs.LG

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出EGGS-PTP以解决大语言模型的计算与内存挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `结构化剪枝` `扩展图` `后训练优化` `模型压缩` `计算效率` `内存优化`

## 📋 核心要点

1. 现有的大语言模型在计算和内存方面面临严峻挑战，导致部署困难。
2. EGGS-PTP通过扩展图理论指导N:M结构化剪枝，优化模型的大小和计算效率。
3. 实验结果显示，EGGS-PTP在加速和内存节省方面表现优异，并在准确性上超越了传统剪枝方法。

## 📝 摘要（中文）

随着大语言模型（LLMs）的广泛应用及规模不断扩大，部署这些庞大基础模型所面临的计算和内存挑战日益严重。这凸显了开发更高效模型变体的迫切需求。为应对这一挑战，本文提出了EGGS-PTP：一种基于扩展图的结构化后训练剪枝方法。该方法利用图论指导N:M结构化剪枝的设计，有效减少模型大小和计算需求。通过引入扩展图的概念，EGGS-PTP确保了剪枝网络内的信息流动，保留了模型的基本功能。大量数值实验表明，EGGS-PTP不仅因结构稀疏性实现了显著的加速和内存节省，还在多个LLM的准确性上超越了现有的结构化剪枝技术。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在计算和内存使用上的高成本问题。现有方法在剪枝过程中往往无法有效保持模型性能，导致信息流失和功能下降。

**核心思路**：EGGS-PTP通过引入扩展图的概念，设计了一种结构化的后训练剪枝方法，确保在剪枝过程中信息流的有效性，从而保留模型的核心功能。

**技术框架**：EGGS-PTP的整体架构包括数据预处理、扩展图构建、N:M结构化剪枝和模型评估四个主要模块。首先，通过图论构建扩展图，然后在此基础上进行结构化剪枝，最后评估剪枝后的模型性能。

**关键创新**：EGGS-PTP的创新在于将扩展图理论应用于模型剪枝，确保了剪枝后模型的信息流动性，与传统剪枝方法相比，能够更好地保留模型的功能和准确性。

**关键设计**：在EGGS-PTP中，关键参数包括剪枝比例、结构化方式（N:M），以及损失函数的设计，确保在剪枝过程中尽量减少性能损失。

## 📊 实验亮点

实验结果表明，EGGS-PTP在多个大语言模型上实现了显著的性能提升，具体表现为在加速和内存节省方面的提升幅度超过了现有结构化剪枝技术，且在准确性上保持了较高水平，展示了其优越性。

## 🎯 应用场景

EGGS-PTP方法具有广泛的应用潜力，特别是在需要高效部署大语言模型的场景中，如智能助手、自动翻译和内容生成等领域。通过降低计算和内存需求，该方法能够使得大语言模型在资源有限的环境中更为可行，推动相关技术的普及与应用。

## 📄 摘要（原文）

> As Large Language Models (LLMs) become more widely adopted and scale up in size, the computational and memory challenges involved in deploying these massive foundation models have grown increasingly severe. This underscores the urgent need to develop more efficient model variants. Faced with this challenge, the present work introduces EGGS-PTP: an Expander-Graph Guided Structured Post-training Pruning method. The proposed approach leverages graph theory to guide the design of N:M structured pruning, effectively reducing model size and computational demands. By incorporating concepts from expander graphs, EGGS-PTP ensures information flow within the pruned network, preserving essential model functionality. Extensive numerical experiments demonstrate that EGGS-PTP not only achieves significant acceleration and memory savings due to structured sparsity but also outperforms existing structured pruning techniques in terms of accuracy across various LLMs.

