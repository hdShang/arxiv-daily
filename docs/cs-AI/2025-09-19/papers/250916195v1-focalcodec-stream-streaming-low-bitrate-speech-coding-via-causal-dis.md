---
layout: default
title: "FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation"
---

# FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16195" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16195v1</a>
  <a href="https://arxiv.org/pdf/2509.16195.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16195v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16195v1', 'FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luca Della Libera, Cem Subakan, Mirco Ravanelli

**分类**: cs.SD, cs.AI, cs.LG, eess.AS

**发布日期**: 2025-09-19

**备注**: 5 pages, 1 figure

**🔗 代码/项目**: [GITHUB](https://github.com/lucadellalib/focalcodec)

---

## 💡 一句话要点

**提出FocalCodec-Stream，通过因果蒸馏实现低码率流式语音编码**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `流式语音编码` `神经音频编解码器` `因果蒸馏` `焦点调制` `低码率` `实时语音通信` `WavLM`

## 📋 核心要点

1. 现有神经音频编解码器大多为非流式，难以应用于实时语音通信等场景。
2. FocalCodec-Stream通过WavLM的因果蒸馏，结合焦点调制和轻量级细化模块，实现低延迟高质量的流式编码。
3. 实验表明，该方法在低码率下优于现有流式编解码器，并在重建质量和下游任务性能之间取得平衡。

## 📝 摘要（中文）

神经音频编解码器是现代生成音频管道中的关键组成部分。虽然最近的编解码器在低码率重建方面表现出色，并为下游任务提供了强大的表征，但大多数是非流式的，限制了它们在实时应用中的使用。本文提出了FocalCodec-Stream，一种基于焦点调制的混合编解码器，它以0.55 - 0.80 kbps的码率将语音压缩成单个二进制码本，理论延迟为80 ms。该方法结合了WavLM的多阶段因果蒸馏和有针对性的架构改进，包括一个轻量级的细化模块，可在延迟约束下提高质量。实验表明，FocalCodec-Stream在可比的比特率下优于现有的流式编解码器，同时保留了语义和声学信息。最终实现了重建质量、下游任务性能、延迟和效率之间的良好权衡。代码和检查点将在https://github.com/lucadellalib/focalcodec上发布。

## 🔬 方法详解

**问题定义**：现有的神经音频编解码器虽然在低码率重建和下游任务表征方面表现出色，但大多为非流式，无法满足实时语音通信等对延迟敏感的应用需求。因此，需要一种能够在低码率下实现高质量、低延迟的流式语音编码方法。

**核心思路**：论文的核心思路是利用WavLM的强大表征能力，通过因果蒸馏的方式将其知识转移到流式编解码器中。同时，采用焦点调制机制和轻量级细化模块，在保证低延迟的前提下，进一步提升重建质量。这种混合方法旨在实现重建质量、下游任务性能、延迟和效率之间的良好权衡。

**技术框架**：FocalCodec-Stream的整体架构包含以下几个主要模块：1) WavLM编码器：利用预训练的WavLM模型提取语音特征。2) 因果蒸馏：将WavLM的知识蒸馏到流式编解码器中，保证编码器的因果性。3) 焦点调制：采用焦点调制机制进行特征压缩和编码。4) 轻量级细化模块：在解码端，使用轻量级的细化模块进一步提升重建质量。整个流程是端到端可训练的。

**关键创新**：该论文的关键创新在于将因果蒸馏、焦点调制和轻量级细化模块相结合，构建了一个高性能的流式语音编解码器。与现有方法相比，FocalCodec-Stream在保证低延迟的同时，实现了更高的重建质量和更好的下游任务性能。此外，该方法采用单二进制码本，进一步降低了码率。

**关键设计**：在因果蒸馏过程中，采用了多阶段蒸馏策略，逐步将WavLM的知识转移到流式编解码器中。焦点调制机制的具体实现方式未知。轻量级细化模块的网络结构也未知。码率为0.55-0.80kbps，理论延迟为80ms。

## 📊 实验亮点

实验结果表明，FocalCodec-Stream在0.55-0.80 kbps的码率下，优于现有的流式编解码器。该方法在保证低延迟（80ms）的同时，实现了更高的重建质量和更好的下游任务性能。具体的性能指标和对比基线未知，但论文强调了在重建质量、下游任务性能、延迟和效率之间取得了良好的权衡。

## 🎯 应用场景

FocalCodec-Stream具有广泛的应用前景，包括实时语音通信、低带宽语音传输、语音助手、在线游戏等。该方法可以在保证语音质量的前提下，显著降低带宽需求和延迟，为用户提供更好的实时交互体验。此外，该方法还可以应用于语音内容分析、语音识别等下游任务，为这些任务提供更高效的语音表征。

## 📄 摘要（原文）

> Neural audio codecs are a fundamental component of modern generative audio pipelines. Although recent codecs achieve strong low-bitrate reconstruction and provide powerful representations for downstream tasks, most are non-streamable, limiting their use in real-time applications. We present FocalCodec-Stream, a hybrid codec based on focal modulation that compresses speech into a single binary codebook at 0.55 - 0.80 kbps with a theoretical latency of 80 ms. Our approach combines multi-stage causal distillation of WavLM with targeted architectural improvements, including a lightweight refiner module that enhances quality under latency constraints. Experiments show that FocalCodec-Stream outperforms existing streamable codecs at comparable bitrates, while preserving both semantic and acoustic information. The result is a favorable trade-off between reconstruction quality, downstream task performance, latency, and efficiency. Code and checkpoints will be released at https://github.com/lucadellalib/focalcodec.

