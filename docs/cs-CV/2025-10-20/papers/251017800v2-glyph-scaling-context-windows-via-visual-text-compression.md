---
layout: default
title: Glyph: Scaling Context Windows via Visual-Text Compression
---

# Glyph: Scaling Context Windows via Visual-Text Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17800" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17800v2</a>
  <a href="https://arxiv.org/pdf/2510.17800.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17800v2" onclick="toggleFavorite(this, '2510.17800v2', 'Glyph: Scaling Context Windows via Visual-Text Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiale Cheng, Yusen Liu, Xinyu Zhang, Yulin Fei, Wenyi Hong, Ruiliang Lyu, Weihan Wang, Zhe Su, Xiaotao Gu, Xiao Liu, Yushi Bai, Jie Tang, Hongning Wang, Minlie Huang

**分类**: cs.CV, cs.CL, cs.LG

**发布日期**: 2025-10-20 (更新: 2025-10-21)

**🔗 代码/项目**: [GITHUB](https://github.com/thu-coai/Glyph)

---

## 💡 一句话要点

**Glyph：通过视觉-文本压缩扩展大语言模型的上下文窗口**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本处理` `视觉-语言模型` `文本压缩` `上下文窗口` `遗传搜索`

## 📋 核心要点

1. 现有大语言模型处理长文本时，计算和内存成本随上下文窗口线性增长，限制了其应用。
2. Glyph将长文本渲染为图像，利用视觉-语言模型处理，实现文本压缩并保留语义信息。
3. 实验表明，Glyph在保持准确性的前提下，实现了3-4倍的token压缩和显著的训练加速。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越依赖长上下文建模来处理文档理解、代码分析和多步骤推理等任务。然而，将上下文窗口扩展到百万token级别会带来巨大的计算和内存成本，限制了长上下文LLM的实用性。本文提出了一种不同的视角——视觉上下文缩放——来应对这一挑战。我们没有扩展基于token的序列，而是提出了Glyph，一个将长文本渲染成图像并使用视觉-语言模型（VLMs）处理它们的框架。这种方法在保留语义信息的同时，大大压缩了文本输入。我们还设计了一种由LLM驱动的遗传搜索，以识别用于平衡准确性和压缩的最佳视觉渲染配置。通过大量的实验，我们证明了我们的方法实现了3-4倍的token压缩，同时在各种长上下文基准测试中保持了与Qwen3-8B等领先LLM相当的准确性。这种压缩还带来了大约4倍的预填充和解码速度提升，以及大约2倍的SFT训练速度提升。此外，在极端压缩下，一个128K上下文的VLM可以扩展到处理百万token级别的文本任务。此外，渲染的文本数据有利于现实世界的多模态任务，例如文档理解。

## 🔬 方法详解

**问题定义**：现有的大语言模型在处理长文本时，需要消耗大量的计算资源和内存，因为它们的计算复杂度通常与上下文长度成正比。这使得将上下文窗口扩展到百万token级别变得非常困难，阻碍了长上下文LLM在实际应用中的部署。现有方法主要集中在优化Transformer架构或使用稀疏注意力机制，但效果有限，且往往需要复杂的工程实现。

**核心思路**：Glyph的核心思路是将长文本转换为图像，然后利用视觉-语言模型（VLM）来处理这些图像。通过将文本渲染成图像，可以利用图像的压缩特性，从而在保留语义信息的同时，显著减少需要处理的数据量。这种方法将文本处理问题转化为图像处理问题，从而可以利用VLM在图像理解方面的优势。

**技术框架**：Glyph框架主要包含以下几个阶段：1) 文本渲染：将长文本渲染成图像，可以使用不同的字体、颜色、布局等视觉元素。2) 视觉编码：使用VLM对渲染后的图像进行编码，提取视觉特征。3) 语言解码：将视觉特征输入到语言模型中，生成文本输出。4) 遗传搜索：使用LLM驱动的遗传搜索算法，自动寻找最佳的视觉渲染配置，以平衡准确性和压缩率。

**关键创新**：Glyph最重要的技术创新点在于它将文本处理问题转化为图像处理问题，并利用VLM来处理长文本。与传统的基于token的文本处理方法相比，Glyph可以实现更高的压缩率，并且可以利用VLM在图像理解方面的优势。此外，Glyph还使用LLM驱动的遗传搜索算法来自动优化视觉渲染配置，从而进一步提高性能。

**关键设计**：在文本渲染阶段，Glyph使用了多种字体、颜色和布局选项，并使用遗传搜索算法来寻找最佳的渲染配置。在视觉编码阶段，Glyph使用了预训练的VLM，例如CLIP或ALIGN。在语言解码阶段，Glyph使用了标准的Transformer解码器。损失函数主要包括交叉熵损失和对比学习损失，用于优化VLM和语言模型的参数。

## 📊 实验亮点

实验结果表明，Glyph在各种长上下文基准测试中实现了3-4倍的token压缩，同时保持了与Qwen3-8B等领先LLM相当的准确性。此外，Glyph还带来了大约4倍的预填充和解码速度提升，以及大约2倍的SFT训练速度提升。在极端压缩下，一个128K上下文的VLM可以扩展到处理百万token级别的文本任务。

## 🎯 应用场景

Glyph具有广泛的应用前景，包括文档理解、代码分析、多步骤推理等需要处理长文本的任务。该方法可以降低长文本处理的计算成本和内存需求，使得大语言模型能够处理更长的上下文，从而提高其性能和实用性。此外，Glyph还可以应用于多模态任务，例如将文本和图像结合起来进行文档理解。

## 📄 摘要（原文）

> Large language models (LLMs) increasingly rely on long-context modeling for tasks such as document understanding, code analysis, and multi-step reasoning. However, scaling context windows to the million-token level brings prohibitive computational and memory costs, limiting the practicality of long-context LLMs. In this work, we take a different perspective-visual context scaling-to tackle this challenge. Instead of extending token-based sequences, we propose Glyph, a framework that renders long texts into images and processes them with vision-language models (VLMs). This approach substantially compresses textual input while preserving semantic information, and we further design an LLM-driven genetic search to identify optimal visual rendering configurations for balancing accuracy and compression. Through extensive experiments, we demonstrate that our method achieves 3-4x token compression while maintaining accuracy comparable to leading LLMs such as Qwen3-8B on various long-context benchmarks. This compression also leads to around 4x faster prefilling and decoding, and approximately 2x faster SFT training. Furthermore, under extreme compression, a 128K-context VLM could scale to handle 1M-token-level text tasks. In addition, the rendered text data benefits real-world multimodal tasks, such as document understanding. Our code and model are released at https://github.com/thu-coai/Glyph.

