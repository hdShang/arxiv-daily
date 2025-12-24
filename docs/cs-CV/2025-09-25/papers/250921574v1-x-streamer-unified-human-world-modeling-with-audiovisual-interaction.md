---
layout: default
title: "X-Streamer: Unified Human World Modeling with Audiovisual Interaction"
---

# X-Streamer: Unified Human World Modeling with Audiovisual Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21574" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21574v1</a>
  <a href="https://arxiv.org/pdf/2509.21574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21574v1', 'X-Streamer: Unified Human World Modeling with Audiovisual Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: You Xie, Tianpei Gu, Zenan Li, Chenxu Zhang, Guoxian Song, Xiaochen Zhao, Chao Liang, Jianwen Jiang, Hongyi Xu, Linjie Luo

**分类**: cs.CV

**发布日期**: 2025-09-25

**备注**: Project Page at https://byteaigc.github.io/X-Streamer

---

## 💡 一句话要点

**X-Streamer：提出基于视听交互的统一人类世界建模框架，实现数字人实时交互。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态建模` `数字人` `视听交互` `Transformer` `扩散模型`

## 📋 核心要点

1. 现有数字人交互方法难以统一处理文本、语音和视频等多模态输入，且缺乏长时程交互的稳定性。
2. X-Streamer采用Thinker-Actor双Transformer架构，Thinker负责理解多模态输入，Actor生成同步的多模态响应。
3. X-Streamer在两块A100 GPU上实现实时运行，能够从任意人像持续数小时的稳定视频聊天体验。

## 📝 摘要（中文）

本文介绍X-Streamer，一个端到端的多模态人类世界建模框架，旨在构建能够在单一统一架构内，通过文本、语音和视频进行无限交互的数字人智能体。X-Streamer从单张人像照片出发，能够实现由流式多模态输入驱动的实时、开放式视频通话。其核心是一个Thinker-Actor双Transformer架构，统一了多模态理解和生成，将静态人像转化为持久且智能的视听交互。Thinker模块感知并推理流式用户输入，其隐藏状态由Actor转化为实时同步的多模态流。具体而言，Thinker利用预训练的大型语言-语音模型，而Actor采用分块自回归扩散模型，该模型交叉关注Thinker的隐藏状态，以产生时间对齐的多模态响应，包括交错的离散文本和音频token以及连续的视频潜在变量。为了确保长时程稳定性，我们设计了具有时间对齐的多模态位置嵌入的块间和块内注意力机制，以实现细粒度的跨模态对齐和上下文保持，并通过分块扩散强制和全局身份引用进一步加强。X-Streamer在两块A100 GPU上实时运行，能够从任意人像持续数小时的稳定视频聊天体验，为交互式数字人的统一世界建模铺平了道路。

## 🔬 方法详解

**问题定义**：现有数字人建模方法通常难以统一处理多种模态的输入（文本、语音、视频），并且在长时间交互过程中容易出现身份不一致、上下文丢失等问题，导致交互体验不佳。这些方法往往针对特定任务设计，缺乏通用性和可扩展性。

**核心思路**：X-Streamer的核心思路是构建一个统一的多模态理解和生成框架，通过Thinker-Actor双Transformer架构，将多模态输入转化为连贯、自然的视听响应。Thinker模块负责理解用户输入，Actor模块负责生成与Thinker模块输出对齐的多模态内容。这种解耦的设计使得模型能够更好地处理不同模态的信息，并生成高质量的交互内容。

**技术框架**：X-Streamer的整体架构包含两个主要模块：Thinker和Actor。Thinker模块利用预训练的大型语言-语音模型，接收文本、语音等输入，并进行推理，生成隐藏状态。Actor模块采用分块自回归扩散模型，以Thinker模块的隐藏状态为条件，生成时间对齐的多模态响应，包括文本、音频和视频。为了保证长时程的连贯性，模型还引入了块间和块内注意力机制。

**关键创新**：X-Streamer的关键创新在于其统一的多模态建模框架，能够同时处理文本、语音和视频输入，并生成相应的输出。此外，模型采用分块自回归扩散模型，能够生成高质量的视频内容，并保证长时程的连贯性。时间对齐的多模态位置嵌入以及分块扩散强制和全局身份引用进一步提升了模型的性能。

**关键设计**：在Actor模块中，采用了chunk-wise的自回归扩散模型，将视频生成过程分解为多个chunk，每个chunk独立生成，并通过chunk间的attention机制保证连贯性。为了实现细粒度的跨模态对齐，模型使用了time-aligned的多模态位置嵌入。此外，为了保证长时程的身份一致性，模型引入了global identity referencing机制，在生成过程中不断参考初始人像的信息。

## 📊 实验亮点

X-Streamer能够在两块A100 GPU上实时运行，支持从任意人像生成持续数小时的稳定视频聊天体验。通过引入时间对齐的多模态位置嵌入和分块扩散强制等技术，模型能够生成高质量、连贯的多模态内容，并在长时程交互中保持身份一致性。实验结果表明，X-Streamer在多模态交互任务上取得了显著的性能提升。

## 🎯 应用场景

X-Streamer具有广泛的应用前景，例如虚拟助手、在线教育、娱乐互动等。它可以用于创建更逼真、更智能的数字人，提供更自然、更个性化的交互体验。该技术还可以应用于远程协作、虚拟会议等场景，提升沟通效率和参与感。未来，X-Streamer有望成为构建下一代人机交互界面的关键技术。

## 📄 摘要（原文）

> We introduce X-Streamer, an end-to-end multimodal human world modeling framework for building digital human agents capable of infinite interactions across text, speech, and video within a single unified architecture. Starting from a single portrait, X-Streamer enables real-time, open-ended video calls driven by streaming multimodal inputs. At its core is a Thinker-Actor dual-transformer architecture that unifies multimodal understanding and generation, turning a static portrait into persistent and intelligent audiovisual interactions. The Thinker module perceives and reasons over streaming user inputs, while its hidden states are translated by the Actor into synchronized multimodal streams in real time. Concretely, the Thinker leverages a pretrained large language-speech model, while the Actor employs a chunk-wise autoregressive diffusion model that cross-attends to the Thinker's hidden states to produce time-aligned multimodal responses with interleaved discrete text and audio tokens and continuous video latents. To ensure long-horizon stability, we design inter- and intra-chunk attentions with time-aligned multimodal positional embeddings for fine-grained cross-modality alignment and context retention, further reinforced by chunk-wise diffusion forcing and global identity referencing. X-Streamer runs in real time on two A100 GPUs, sustaining hours-long consistent video chat experiences from arbitrary portraits and paving the way toward unified world modeling of interactive digital humans.

