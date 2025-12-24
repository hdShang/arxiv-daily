---
layout: default
title: "OverFill: Two-Stage Models for Efficient Language Model Decoding"
---

# OverFill: Two-Stage Models for Efficient Language Model Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08446" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08446v1</a>
  <a href="https://arxiv.org/pdf/2508.08446.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08446v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08446v1', 'OverFill: Two-Stage Models for Efficient Language Model Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Woojeong Kim, Junxiong Wang, Jing Nathan Yan, Mohamed Abdelfattah, Alexander M. Rush

**分类**: cs.AI

**发布日期**: 2025-08-11

**备注**: Accepted to COLM 2025

**🔗 代码/项目**: [GITHUB](https://github.com/friendshipkim/overfill)

---

## 💡 一句话要点

**提出OverFill以解决大语言模型解码效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `推理效率` `解码优化` `稠密剪枝` `自然语言处理` `模型训练` `生成质量`

## 📋 核心要点

1. 现有的解码器模型未能有效区分预填充和解码阶段的计算特性，导致推理效率低下。
2. OverFill通过解耦预填充和解码阶段，使用完整模型进行预填充，随后切换到稠密剪枝模型以提高生成质量。
3. 实验结果表明，OverFill在多个标准基准测试中显著超越了同规模的剪枝模型，且使用的训练数据显著减少。

## 📝 摘要（中文）

大型语言模型（LLMs）在多种任务中表现出色，但由于高推理成本面临显著的部署挑战。LLM推理包括预填充（计算密集型）和解码（内存密集型）两个阶段，其中解码阶段在长序列中占主导地位。当前的解码器模型对这两个阶段的处理方式相同，未能考虑其不同的计算特性。本文提出的OverFill通过解耦这两个阶段来优化准确性与效率的权衡。OverFill首先使用完整模型进行预填充，并并行处理系统和用户输入，然后在生成令牌时切换到稠密剪枝模型。通过在预填充阶段利用更多计算资源，OverFill在保持最低延迟开销的同时提高了生成质量。我们的3B-to-1B配置在标准基准测试中比1B剪枝模型提升了83.2%，而8B-to-3B配置则在3B剪枝模型上平均提升了79.2%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理过程中由于解码阶段的内存密集型特性导致的效率低下问题。现有方法未能有效区分预填充和解码阶段的计算需求，造成延迟和资源浪费。

**核心思路**：OverFill的核心思路是将推理过程中的预填充和解码阶段解耦，利用完整模型进行预填充以提高生成质量，然后在解码阶段切换到稠密剪枝模型，从而优化准确性与效率的平衡。

**技术框架**：OverFill的整体架构分为两个主要阶段：首先是预填充阶段，使用完整模型并行处理输入；其次是解码阶段，采用稠密剪枝模型按顺序生成令牌。

**关键创新**：OverFill的创新在于其解耦的推理过程，充分利用计算资源进行预填充，从而在保持低延迟的同时显著提高生成质量。这与现有的统一处理方法形成鲜明对比。

**关键设计**：在设计上，OverFill采用了3B-to-1B和8B-to-3B两种配置，分别在不同的基准测试中表现出色，且在训练数据使用上显著减少，优化了模型的训练效率。

## 📊 实验亮点

在实验中，OverFill的3B-to-1B配置在标准基准测试中比1B剪枝模型提升了83.2%，而8B-to-3B配置则在3B剪枝模型上平均提升了79.2%。这些结果表明，OverFill不仅在性能上超越了同规模的模型，还显著减少了训练数据的需求。

## 🎯 应用场景

OverFill的研究成果在自然语言处理领域具有广泛的应用潜力，尤其是在需要高效推理的场景中，如对话系统、文本生成和机器翻译等。其优化的推理效率和生成质量将推动更大规模语言模型的实际应用，降低部署成本，提升用户体验。

## 📄 摘要（原文）

> Large language models (LLMs) excel across diverse tasks but face significant deployment challenges due to high inference costs. LLM inference comprises prefill (compute-bound) and decode (memory-bound) stages, with decode dominating latency particularly for long sequences. Current decoder-only models handle both stages uniformly, despite their distinct computational profiles. We propose OverFill, which decouples these stages to optimize accuracy-efficiency tradeoffs. OverFill begins with a full model for prefill, processing system and user inputs in parallel. It then switches to a dense pruned model, while generating tokens sequentially. Leveraging more compute during prefill, OverFill improves generation quality with minimal latency overhead. Our 3B-to-1B OverFill configuration outperforms 1B pruned models by 83.2%, while the 8B-to-3B configuration improves over 3B pruned models by 79.2% on average across standard benchmarks. OverFill matches the performance of same-sized models trained from scratch, while using significantly less training data. Our code is available at https://github.com/friendshipkim/overfill.

