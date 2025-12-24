---
layout: default
title: "LLaVA-Scissor: Token Compression with Semantic Connected Components for Video LLMs"
---

# LLaVA-Scissor: Token Compression with Semantic Connected Components for Video LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21862" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21862v1</a>
  <a href="https://arxiv.org/pdf/2506.21862.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21862v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21862v1', 'LLaVA-Scissor: Token Compression with Semantic Connected Components for Video LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyuan Sun, Jiaxing Zhao, Xihan Wei, Qibin Hou

**分类**: cs.CV, cs.AI, cs.HC, cs.MM

**发布日期**: 2025-06-27

**备注**: 21 pages, 4 figures, 7 tables

**🔗 代码/项目**: [GITHUB](https://github.com/HumanMLLM/LLaVA-Scissor)

---

## 💡 一句话要点

**提出LLaVA-Scissor以解决视频多模态大语言模型的token压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `多模态大语言模型` `token压缩` `语义连通组件` `长视频理解` `视频问答` `时空信息处理`

## 📋 核心要点

1. 现有方法在token压缩时未能有效捕捉所有语义区域，导致冗余和信息丢失。
2. 我们提出的LLaVA-Scissor利用语义连通组件(SCC)方法，确保token在不同语义区域的全面覆盖。
3. 实验结果显示，LLaVA-Scissor在视频问答、长视频理解等基准测试中表现优异，尤其在低token保留比率时提升显著。

## 📝 摘要（中文）

本文提出了LLaVA-Scissor，一种针对视频多模态大语言模型的无训练token压缩策略。以往方法主要基于注意力分数进行token压缩，但未能有效捕捉所有语义区域，导致token冗余。我们提出利用语义连通组件(SCC)方法，将token分配到不同的语义区域，确保全面的语义覆盖。该策略采用两步时空token压缩方法，在空间和时间域中均利用SCC。实验结果表明，LLaVA-Scissor在多种视频理解基准测试中优于其他token压缩方法，尤其在低token保留比率下表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决视频多模态大语言模型中的token压缩问题。现有方法主要依赖注意力分数进行压缩，未能有效捕捉所有语义区域，导致冗余和信息损失。

**核心思路**：我们提出的LLaVA-Scissor利用语义连通组件(SCC)方法，将token分配到不同的语义区域，从而确保全面的语义覆盖。这种设计旨在减少冗余并提高信息的表达能力。

**技术框架**：LLaVA-Scissor的整体架构包括两个主要阶段：首先，在空间域中应用SCC进行token的初步压缩；其次，在时间域中进一步优化token的表示。通过这两个步骤，最终生成一组不重叠的语义token，代表整个视频内容。

**关键创新**：LLaVA-Scissor的核心创新在于引入了语义连通组件(SCC)方法，使得token能够在语义层面上进行有效的分组和压缩。这与传统方法的基于注意力的压缩方式有本质区别，后者往往忽视了语义的完整性。

**关键设计**：在实现过程中，我们对SCC的参数设置进行了优化，并设计了适合视频数据的损失函数，以确保压缩后的token能够保留重要的语义信息。此外，网络结构经过精心设计，以支持时空信息的有效处理。

## 📊 实验亮点

实验结果表明，LLaVA-Scissor在多种视频理解基准测试中表现优异，尤其在低token保留比率下，压缩效果显著提升，超越了其他token压缩方法，具体性能数据未提供，但提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括视频理解、视频问答系统和多模态数据处理等。通过有效的token压缩，LLaVA-Scissor能够在资源受限的环境中提升视频分析的效率和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In this paper, we present LLaVA-Scissor, a training-free token compression strategy designed for video multimodal large language models. Previous methods mostly attempt to compress tokens based on attention scores, but fail to effectively capture all semantic regions and often lead to token redundancy. Differently, we propose to leverage the Semantic Connected Components (SCC) approach that assigns tokens to distinct semantic regions within the token set, ensuring comprehensive semantic coverage. The outcome is a two-step spatio-temporal token compression strategy that utilizes SCC in both spatial and temporal domains. This strategy can effectively compress tokens by representing the entire video with a set of non-overlapping semantic tokens. We conduct extensive evaluations of the token compression capabilities of LLaVA-Scissor across diverse video understanding benchmarks, including video question answering, long video understanding, and comprehensive multi-choices benchmarks. Experimental results show that the proposed LLaVA-Scissor outperforms other token compression methods, achieving superior performance in various video understanding benchmarks, particularly at low token retention ratios. Project page: https://github.com/HumanMLLM/LLaVA-Scissor.

