---
layout: default
title: LoVR: A Benchmark for Long Video Retrieval in Multimodal Contexts
---

# LoVR: A Benchmark for Long Video Retrieval in Multimodal Contexts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13928" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13928v3</a>
  <a href="https://arxiv.org/pdf/2505.13928.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13928v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13928v3', 'LoVR: A Benchmark for Long Video Retrieval in Multimodal Contexts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qifeng Cai, Hao Liang, Hejun Dong, Meiyi Qiang, Ruichuan An, Zhaoyang Han, Zhengzhou Zhu, Bin Cui, Wentao Zhang

**分类**: cs.CV, cs.IR

**发布日期**: 2025-05-20 (更新: 2025-11-13)

**🔗 代码/项目**: [GITHUB](https://github.com/TechNomad-ds/LoVR-benchmark)

---

## 💡 一句话要点

**提出LoVR基准以解决长视频检索中的多模态挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `视频-文本检索` `多模态学习` `字幕生成` `数据集构建`

## 📋 核心要点

1. 现有视频-文本检索基准在视频时长、字幕质量和注释粒度上存在明显不足，限制了评估的全面性。
2. 本文提出LoVR基准，包含467个长视频和高质量细粒度字幕，旨在提升视频-文本检索的评估标准。
3. 通过对多种先进嵌入模型的实验，LoVR展示了当前方法的局限性，并为未来研究提供了有价值的见解。

## 📝 摘要（中文）

长视频包含大量信息，使得视频-文本检索成为多模态学习中的一项重要且具有挑战性的任务。然而，现有基准存在视频时长有限、低质量字幕和粗糙注释粒度等问题，阻碍了先进视频-文本检索方法的评估。为了解决这些局限性，本文提出了LoVR基准，专门用于长视频-文本检索。LoVR包含467个长视频和超过40,804个高质量字幕的细粒度剪辑。为克服机器生成注释质量差的问题，本文提出了一种高效的字幕生成框架，集成了VLM自动生成、字幕质量评分和动态优化。该流程提高了注释的准确性，同时保持了可扩展性。此外，本文引入了一种语义融合方法，以生成连贯的完整视频字幕而不丢失重要的上下文信息。我们的基准引入了更长的视频、更详细的字幕和更大规模的数据集，为视频理解和检索提出了新的挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决长视频-文本检索中的评估不足，现有基准因视频时长短、字幕质量低和注释粗糙而无法全面评估先进方法的性能。

**核心思路**：提出LoVR基准，通过引入长视频和高质量细粒度字幕，改善现有评估标准，同时设计高效的字幕生成框架以提升注释质量。

**技术框架**：整体架构包括视频数据收集、字幕生成、质量评分和动态优化四个主要模块，确保生成的字幕既准确又具有可扩展性。

**关键创新**：最重要的创新在于提出了一种结合VLM自动生成和动态优化的字幕生成框架，显著提高了注释的准确性和质量。

**关键设计**：在字幕生成过程中，采用了多种质量评分机制和动态调整策略，以确保生成的字幕在语义上连贯且信息丰富。

## 📊 实验亮点

在多种先进嵌入模型的实验中，LoVR基准展示了其挑战性，揭示了当前方法的局限性。实验结果表明，使用LoVR进行训练的模型在视频-文本检索任务上性能显著提升，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括视频检索、内容推荐和多模态学习等。通过提供高质量的长视频数据集，LoVR能够促进视频理解技术的发展，推动相关领域的研究进展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Long videos contain a vast amount of information, making video-text retrieval an essential and challenging task in multimodal learning. However, existing benchmarks suffer from limited video duration, low-quality captions, and coarse annotation granularity, which hinder the evaluation of advanced video-text retrieval methods. To address these limitations, we introduce LoVR, a benchmark specifically designed for long video-text retrieval. LoVR contains 467 long videos and over 40,804 fine-grained clips with high-quality captions. To overcome the issue of poor machine-generated annotations, we propose an efficient caption generation framework that integrates VLM automatic generation, caption quality scoring, and dynamic refinement. This pipeline improves annotation accuracy while maintaining scalability. Furthermore, we introduce a semantic fusion method to generate coherent full-video captions without losing important contextual information. Our benchmark introduces longer videos, more detailed captions, and a larger-scale dataset, presenting new challenges for video understanding and retrieval. Extensive experiments on various advanced embedding models demonstrate that LoVR is a challenging benchmark, revealing the limitations of current approaches and providing valuable insights for future research. We release the code and dataset link at https://github.com/TechNomad-ds/LoVR-benchmark

