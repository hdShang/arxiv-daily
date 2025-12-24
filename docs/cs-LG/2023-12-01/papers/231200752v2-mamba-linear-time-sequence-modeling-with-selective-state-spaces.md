---
layout: default
title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
---

# Mamba: Linear-Time Sequence Modeling with Selective State Spaces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00752" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00752v2</a>
  <a href="https://arxiv.org/pdf/2312.00752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00752v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00752v2', 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Albert Gu, Tri Dao

**分类**: cs.LG, cs.AI

**发布日期**: 2023-12-01 (更新: 2024-05-31)

---

## 💡 一句话要点

**提出Mamba以解决Transformer在长序列建模中的效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长序列建模` `选择性状态空间模型` `Transformer优化` `高效推理` `自然语言处理` `音频处理` `基因组分析`

## 📋 核心要点

1. 现有的Transformer架构在处理长序列时存在计算效率低下的问题，尤其是在语言等重要模态上表现不佳。
2. 论文提出了一种新的选择性状态空间模型（SSM），通过让模型参数依赖于输入，增强了模型在序列长度维度上的信息选择能力。
3. Mamba模型在推理速度上比Transformer高出5倍，并且在处理百万长度序列时性能显著提升，超越了同规模的Transformer模型。

## 📝 摘要（中文）

基础模型如今推动了深度学习中大多数令人兴奋的应用，几乎普遍基于Transformer架构及其核心注意力模块。为了解决Transformer在长序列上的计算低效，许多亚二次时间架构如线性注意力、门控卷积和结构状态空间模型（SSMs）被提出，但在语言等重要模态上表现不佳。我们发现这些模型的一个关键弱点是无法进行基于内容的推理，并提出了几项改进。首先，让SSM参数成为输入的函数，允许模型根据当前token选择性地传播或遗忘信息。其次，尽管这一变化阻止了高效卷积的使用，我们设计了一种硬件感知的并行算法。我们将这些选择性SSMs集成到一个简化的端到端神经网络架构中（Mamba），实现了快速推理和线性扩展，且在真实数据上表现优异。Mamba在语言、音频和基因组等多个模态上达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决Transformer在长序列建模中的计算低效问题，现有的亚二次时间模型在语言等模态上表现不佳，无法进行有效的内容推理。

**核心思路**：通过将选择性状态空间模型（SSM）参数设计为输入的函数，使模型能够根据当前token选择性地传播或遗忘信息，从而增强内容推理能力。

**技术框架**：Mamba模型为一个简化的端到端神经网络架构，去除了传统的注意力机制和多层感知机（MLP）模块，采用选择性SSM进行序列建模。

**关键创新**：最重要的创新在于将SSM参数与输入内容关联，使得模型能够在序列长度维度上灵活处理信息，这一设计显著提升了模型在长序列上的表现。

**关键设计**：模型采用硬件感知的并行算法，尽管牺牲了高效卷积的使用，但在推理速度和扩展性上实现了显著提升，具体参数设置和损失函数设计在论文中详细描述。

## 📊 实验亮点

Mamba模型在语言建模任务中表现出色，其3B参数版本在同规模的Transformer模型上超越了性能，并且在预训练和下游评估中均表现优异，展示了5倍的推理速度提升和线性扩展能力。

## 🎯 应用场景

Mamba模型在多个领域具有广泛的应用潜力，包括自然语言处理、音频信号处理和基因组数据分析等。其高效的序列建模能力使得在长序列数据处理时能够显著提高计算效率和准确性，未来可能推动相关领域的进一步研究和应用。

## 📄 摘要（原文）

> Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba). Mamba enjoys fast inference (5$\times$ higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences. As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation.

