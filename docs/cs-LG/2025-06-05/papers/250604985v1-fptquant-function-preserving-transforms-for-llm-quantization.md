---
layout: default
title: "FPTQuant: Function-Preserving Transforms for LLM Quantization"
---

# FPTQuant: Function-Preserving Transforms for LLM Quantization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04985" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04985v1</a>
  <a href="https://arxiv.org/pdf/2506.04985.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04985v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04985v1', 'FPTQuant: Function-Preserving Transforms for LLM Quantization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boris van Breugel, Yelysei Bondarenko, Paul Whatmough, Markus Nagel

**分类**: cs.LG

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出FPTQuant以解决大语言模型量化效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `量化` `函数保持变换` `推理效率` `自然语言处理` `模型优化` `深度学习`

## 📋 核心要点

1. 现有的量化方法在处理大语言模型时，容易因大幅度异常值导致性能显著下降。
2. FPTQuant通过引入四种函数保持变换，旨在优化变换器的量化过程，同时保持模型的功能。
3. 实验结果表明，FPTQuant在准确性与速度上表现优异，达到最高3.9倍的加速效果。

## 📝 摘要（中文）

大语言模型（LLMs）在推理时需要大量计算和能量。虽然量化权重和激活值可以提高效率，但简单的量化方法可能会因大幅度异常值而显著降低性能。本文提出FPTQuant，介绍了四种新颖、轻量且表达能力强的函数保持变换（FPTs），以促进变换器的量化。这些变换旨在在保持模型功能的同时，使中间激活分布更适合量化。FPTQuant无需自定义内核，几乎不增加推理开销，支持静态INT4量化，并在性能上实现了高达3.9倍的加速，且在准确性与速度的权衡上表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在量化过程中因大幅度异常值导致的性能下降问题。现有的简单量化方法未能有效处理这些异常值，影响了模型的推理效率和准确性。

**核心思路**：FPTQuant的核心思路是设计四种函数保持变换（FPTs），通过调整中间激活分布，使其更适合量化，同时保持模型的功能。这样的设计利用了变换器操作中的等变性和独立性。

**技术框架**：FPTQuant的整体架构包括四个主要模块：1) 针对查询和键的可合并预RoPE变换；2) 针对值的可合并变换；3) MLP块内的可合并缩放变换；4) 便宜的动态缩放变换。这些模块共同作用以优化量化过程。

**关键创新**：FPTQuant的主要创新在于其轻量级的函数保持变换设计，能够在不增加推理开销的情况下，显著提高量化模型的性能。这与现有方法的本质区别在于其对中间激活分布的优化。

**关键设计**：FPTQuant在训练过程中采用局部和端到端的方式，以减少异常值，并确保量化模型与全精度模型的输出匹配。该方法无需自定义内核，且在推理时几乎不增加额外开销。

## 📊 实验亮点

FPTQuant在实验中实现了最高3.9倍的速度提升，相较于全精度模型在准确性上表现优异，仅略低于一种速度慢达29%的方法。这表明FPTQuant在准确性与速度之间达成了良好的平衡。

## 🎯 应用场景

FPTQuant的研究成果在大语言模型的推理效率优化方面具有重要应用价值，能够广泛应用于自然语言处理、对话系统和智能助手等领域。其高效的量化方法将推动大规模模型在资源受限环境中的应用，提升实际部署的可行性。

## 📄 摘要（原文）

> Large language models (LLMs) require substantial compute, and thus energy, at inference time. While quantizing weights and activations is effective at improving efficiency, naive quantization of LLMs can significantly degrade performance due to large magnitude outliers. This paper describes FPTQuant, which introduces four novel, lightweight, and expressive function-preserving transforms (FPTs) to facilitate quantization of transformers: (1) a mergeable pre-RoPE transform for queries and keys, (2) a mergeable transform for values, (3) a mergeable scaling transform within the MLP block, and (4) a cheap, dynamic scaling transform. By leveraging the equivariances and independencies inherent to canonical transformer operation, we designed these FPTs to maintain the model's function while shaping the intermediate activation distributions to be more quantization friendly. FPTQuant requires no custom kernels and adds virtually no overhead during inference. The FPTs are trained both locally to reduce outliers, and end-to-end such that the outputs of the quantized and full-precision models match. FPTQuant enables static INT4 quantization with minimal overhead and shows SOTA speed-up of up to 3.9 times over FP. Empirically, FPTQuant has an excellent accuracy-speed trade-off -- it is performing on par or exceeding most prior work and only shows slightly lower accuracy compared to a method that is up to 29% slower.

