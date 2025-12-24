---
layout: default
title: HAMburger: Accelerating LLM Inference via Token Smashing
---

# HAMburger: Accelerating LLM Inference via Token Smashing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20438" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20438v1</a>
  <a href="https://arxiv.org/pdf/2505.20438.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20438v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20438v1', 'HAMburger: Accelerating LLM Inference via Token Smashing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyu Liu, Ce Zhang

**分类**: cs.CL

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出HAMburger以加速大语言模型推理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理效率` `资源优化` `自回归模型` `KV缓存` `动态调整` `文本生成`

## 📋 核心要点

1. 现有大语言模型推理方法在每个token上均匀分配计算和存储，导致效率低下。
2. HAMburger通过分层自回归模型，重新定义了LLM的资源分配，允许多个token共享KV缓存。
3. 实验表明，HAMburger在短文本和长文本任务中均保持质量，同时KV缓存计算和TPS均提升了2倍。

## 📝 摘要（中文）

随着对高效大语言模型（LLM）推理的需求不断增长，算法、系统和硬件的整体优化显得尤为重要。然而，现有方法在生成模式上缺乏根本性变化：每个token都需要一次前向传播和一个KV缓存。基于LLM能够自我识别信息存储量的洞察，本文提出了HAMburger，一个分层自回归模型，通过在推理过程中重新定义资源分配，打破了每个token均匀计算和存储的限制。HAMburger通过将多个token压缩为一个KV并在每一步生成多个token，显著提高了推理速度和内存效率。实验结果表明，HAMburger在保持任务质量的同时，KV缓存计算减少了最多2倍，TPS提升了最多2倍。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大语言模型推理效率低下的问题，现有方法在每个token上均匀分配计算和存储，导致资源浪费和性能瓶颈。

**核心思路**：HAMburger通过将多个token压缩为一个KV缓存，并在每一步生成多个token，突破了传统的推理模式，从而提高了计算和内存的效率。

**技术框架**：HAMburger的整体架构包括一个组合嵌入器和一个微步解码器，位于基础LLM之间，形成一个分层自回归模型。该框架允许在推理过程中动态调整计算资源。

**关键创新**：HAMburger的主要创新在于其能够在推理过程中将多个token合并到一个KV缓存中，显著降低了KV缓存和前向计算的线性增长，使得推理速度与输出长度呈亚线性关系。

**关键设计**：HAMburger的设计包括自草拟token的盲信任机制，允许模型在缺乏全局上下文的情况下生成token，同时根据查询的困惑度和输出结构动态调整推理速度。该方法在硬件上具有无关性，适用于多种计算平台。

## 📊 实验亮点

HAMburger在实验中表现出色，KV缓存计算减少了最多2倍，TPS提升了最多2倍，同时在短文本和长文本任务中保持了高质量的生成效果，展示了其在推理效率和内存利用上的显著优势。

## 🎯 应用场景

HAMburger的研究成果在自然语言处理、对话系统和文本生成等领域具有广泛的应用潜力。通过提高推理效率，该模型能够支持更复杂的应用场景，如实时对话生成和大规模文本分析，推动智能助手和自动化内容生成的发展。

## 📄 摘要（原文）

> The growing demand for efficient Large Language Model (LLM) inference requires a holistic optimization on algorithms, systems, and hardware. However, very few works have fundamentally changed the generation pattern: each token needs one forward pass and one KV cache. This can be sub-optimal because we found that LLMs are extremely capable of self-identifying the exact dose of information that a single KV cache can store, and many tokens can be generated confidently without global context. Based on this insight, we introduce HAMburger, a Hierarchically Auto-regressive Model that redefines resource allocation in LLMs by moving beyond uniform computation and storage per token during inference. Stacking a compositional embedder and a micro-step decoder in between a base LLM, HAMburger smashes multiple tokens into a single KV and generates several tokens per step. Additionally, HAMburger functions as a speculative decoding framework where it can blindly trust self-drafted tokens. As a result, HAMburger shifts the growth of KV cache and forward FLOPs from linear to sub-linear with respect to output length, and adjusts its inference speed based on query perplexity and output structure. Extensive evaluations show that HAMburger reduces the KV cache computation by up to 2$\times$ and achieves up to 2$\times$ TPS, while maintaining quality in both short- and long-context tasks. Our method explores an extremely challenging inference regime that requires both computation- and memory-efficiency with a hardware-agnostic design.

