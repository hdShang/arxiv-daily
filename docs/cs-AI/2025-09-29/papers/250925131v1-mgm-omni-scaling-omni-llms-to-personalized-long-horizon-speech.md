---
layout: default
title: "MGM-Omni: Scaling Omni LLMs to Personalized Long-Horizon Speech"
---

# MGM-Omni: Scaling Omni LLMs to Personalized Long-Horizon Speech

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25131" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25131v1</a>
  <a href="https://arxiv.org/pdf/2509.25131.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25131v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25131v1', 'MGM-Omni: Scaling Omni LLMs to Personalized Long-Horizon Speech')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengyao Wang, Zhisheng Zhong, Bohao Peng, Senqiao Yang, Yuqi Liu, Haokun Gui, Bin Xia, Jingyao Li, Bei Yu, Jiaya Jia

**分类**: cs.SD, cs.AI, cs.CL, cs.CV, cs.MM

**发布日期**: 2025-09-29

**备注**: Code is available at https://github.com/dvlab-research/MGM-Omni

---

## 💡 一句话要点

**MGM-Omni：面向个性化长时程语音的通用多模态大语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `语音生成` `长时程语音` `零样本语音克隆` `跨模态理解`

## 📋 核心要点

1. 现有语音生成方法通常采用级联流程，缺乏跨模态信息的有效融合和实时性。
2. MGM-Omni采用“脑-口”双轨架构，解耦多模态推理和语音生成，实现高效跨模态交互。
3. 实验表明，MGM-Omni在音色保持、语音自然度和长音频理解方面优于现有开源模型。

## 📝 摘要（中文）

本文提出了MGM-Omni，一个统一的通用多模态大语言模型，用于多模态理解和富有表现力的长时程语音生成。与孤立语音合成的级联流程不同，MGM-Omni采用“脑-口”设计，具有双轨、基于token的架构，将多模态推理与实时语音生成干净地解耦。这种设计实现了高效的跨模态交互和低延迟的流式语音生成。在理解方面，统一的训练策略与双音频编码器设计相结合，实现了跨不同声学条件的长格式音频感知。在生成方面，基于块的并行解码方案缩小了文本-语音token速率差距，加速了推理，并支持具有稳定音色的扩展持续时间的流式零样本语音克隆。与同期的工作相比，MGM-Omni以显著的数据高效训练实现了这些能力。大量的实验表明，MGM-Omni在跨扩展序列保持音色身份、生成自然和上下文感知的语音以及实现卓越的长格式音频和全模态理解方面优于现有的开源模型。MGM-Omni为全模态理解和可控的个性化长时程语音生成建立了一个高效的端到端范例。

## 🔬 方法详解

**问题定义**：现有语音生成系统通常采用级联pipeline，将语音合成与多模态理解分离，导致跨模态信息交互受限，难以实现低延迟的流式语音生成，并且在长时程语音生成中音色容易漂移。此外，现有方法在处理不同声学条件下的长音频时，鲁棒性和理解能力有待提高。

**核心思路**：MGM-Omni的核心在于采用一个统一的Omni LLM框架，通过“脑-口”双轨架构，将多模态理解（“脑”）和语音生成（“口”）解耦，从而实现高效的跨模态交互和低延迟的流式语音生成。这种设计允许模型在理解多模态输入的同时，并行地生成语音，从而显著提升了生成效率和实时性。

**技术框架**：MGM-Omni的整体架构包含两个主要部分：多模态理解模块和语音生成模块。多模态理解模块负责处理包括文本、音频等多种模态的输入，并将其编码成统一的token表示。该模块采用了双音频编码器设计，以增强对不同声学条件的鲁棒性。语音生成模块则基于这些token表示生成语音，采用chunk-based并行解码方案，加速推理过程。整个框架采用端到端的方式进行训练，以优化跨模态信息的流动和语音生成的质量。

**关键创新**：MGM-Omni的关键创新在于其“脑-口”双轨架构和统一的Omni LLM框架。这种架构不仅实现了多模态理解和语音生成的解耦，还通过chunk-based并行解码方案显著提升了语音生成的效率和实时性。此外，该模型采用统一的训练策略，实现了数据高效的训练，并在长时程语音生成中保持了稳定的音色。

**关键设计**：MGM-Omni采用了双音频编码器设计，以增强对不同声学条件的鲁棒性。在语音生成模块，采用了chunk-based并行解码方案，将长序列分割成多个chunk并行解码，从而加速推理过程。此外，模型还采用了特殊的损失函数，以优化音色保持和语音自然度。

## 📊 实验亮点

MGM-Omni在长时程语音生成中表现出色，能够保持稳定的音色身份，并在语音自然度和上下文感知方面优于现有开源模型。实验结果表明，MGM-Omni在长格式音频和全模态理解方面也取得了显著的性能提升，并且以更少的数据实现了这些能力，体现了其数据高效性。

## 🎯 应用场景

MGM-Omni具有广泛的应用前景，包括个性化语音助手、智能客服、游戏角色配音、有声读物生成等。该模型能够理解多模态输入，生成自然、流畅且具有个性化音色的语音，从而提升用户体验。此外，MGM-Omni的低延迟特性使其适用于实时语音交互场景，例如在线会议和远程教育。

## 📄 摘要（原文）

> We present MGM-Omni, a unified Omni LLM for omni-modal understanding and expressive, long-horizon speech generation. Unlike cascaded pipelines that isolate speech synthesis, MGM-Omni adopts a "brain-mouth" design with a dual-track, token-based architecture that cleanly decouples multimodal reasoning from real-time speech generation. This design enables efficient cross-modal interaction and low-latency, streaming speech generation. For understanding, a unified training strategy coupled with a dual audio encoder design enables long-form audio perception across diverse acoustic conditions. For generation, a chunk-based parallel decoding scheme narrows the text speech token-rate gap, accelerating inference and supporting streaming zero-shot voice cloning with stable timbre over extended durations. Compared to concurrent work, MGM-Omni achieves these capabilities with markedly data-efficient training. Extensive experiments demonstrate that MGM-Omni outperforms existing open source models in preserving timbre identity across extended sequences, producing natural and context-aware speech, and achieving superior long-form audio and omnimodal understanding. MGM-Omni establishes an efficient, end-to-end paradigm for omnimodal understanding and controllable, personalised long-horizon speech generation.

