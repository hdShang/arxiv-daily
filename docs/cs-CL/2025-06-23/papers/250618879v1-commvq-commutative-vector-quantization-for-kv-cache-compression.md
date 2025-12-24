---
layout: default
title: "CommVQ: Commutative Vector Quantization for KV Cache Compression"
---

# CommVQ: Commutative Vector Quantization for KV Cache Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18879" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18879v1</a>
  <a href="https://arxiv.org/pdf/2506.18879.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18879v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18879v1', 'CommVQ: Commutative Vector Quantization for KV Cache Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junyan Li, Yang Zhang, Muhammad Yusuf Hassan, Talha Chafekar, Tianle Cai, Zhile Ren, Pengsheng Guo, Foroozan Karimzadeh, Colorado Reed, Chong Wang, Chuang Gan

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-23

**备注**: ICML 2025 poster

**🔗 代码/项目**: [GITHUB](https://github.com/UMass-Embodied-AGI/CommVQ)

---

## 💡 一句话要点

**提出CommVQ以解决长上下文LLM推理中的KV缓存瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文推理` `向量量化` `内存优化` `自注意力机制` `自然语言处理`

## 📋 核心要点

1. 随着上下文长度的增加，现有的KV缓存方法在GPU上面临内存瓶颈，限制了大型语言模型的应用。
2. 本文提出了可交换向量量化（CommVQ），通过加法量化和轻量级编码器压缩KV缓存，优化解码过程。
3. 实验结果显示，CommVQ在2位量化下将FP16 KV缓存大小减少87.5%，并实现了1位量化的低精度损失，支持更长上下文的推理。

## 📝 摘要（中文）

大型语言模型（LLMs）在需要长上下文长度的应用中日益普及，但随着上下文的增长，键值（KV）缓存常常成为GPU上的内存瓶颈。为了解决这一问题，本文提出了可交换向量量化（CommVQ），显著减少长上下文LLM推理的内存使用。我们首先引入了一种轻量级编码器和代码本的加法量化方法来压缩KV缓存，解码过程通过简单的矩阵乘法实现。为了进一步降低解码过程中的计算成本，我们设计了与旋转位置嵌入（RoPE）可交换的代码本，并使用期望最大化（EM）算法进行训练。这使得解码能够高效地集成到自注意力机制中。实验表明，我们的方法在2位量化下将FP16 KV缓存大小减少了87.5%，并在长上下文基准和GSM8K上超越了现有的KV缓存量化方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长上下文推理中KV缓存的内存瓶颈问题。现有方法在上下文增长时无法有效管理内存，导致性能下降。

**核心思路**：提出可交换向量量化（CommVQ），通过加法量化和轻量级编码器压缩KV缓存，并设计与RoPE可交换的代码本，优化解码过程。

**技术框架**：整体架构包括加法量化模块、轻量级编码器、RoPE可交换代码本和自注意力机制的集成。解码过程通过简单的矩阵乘法实现，降低计算复杂度。

**关键创新**：CommVQ的核心创新在于引入了与RoPE可交换的代码本设计，使得解码过程能够高效集成到自注意力机制中，显著提升了内存使用效率。

**关键设计**：在设计中，采用了轻量级编码器和EM算法训练代码本，确保了高准确率和低计算开销。量化过程中的参数设置和损失函数设计也经过精心调整，以实现最佳性能。

## 📊 实验亮点

实验结果显示，CommVQ在2位量化下将FP16 KV缓存大小减少了87.5%，并且在1位量化的情况下，准确率损失极小，支持LLaMA-3.1 8B模型在单个RTX 4090 GPU上运行128K上下文长度，展现出显著的性能提升。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在需要处理长上下文的自然语言处理任务中，如对话系统、文本生成和信息检索等。通过有效压缩KV缓存，CommVQ能够在资源受限的环境中运行大型语言模型，推动智能应用的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly used in applications requiring long context lengths, but the key-value (KV) cache often becomes a memory bottleneck on GPUs as context grows. To address this, we propose Commutative Vector Quantization (CommVQ) to significantly reduce memory usage for long-context LLM inference. We first introduce additive quantization with a lightweight encoder and codebook to compress the KV cache, which can be decoded via simple matrix multiplication. To further reduce computational costs during decoding, we design the codebook to be commutative with Rotary Position Embedding (RoPE) and train it using an Expectation-Maximization (EM) algorithm. This enables efficient integration of decoding into the self-attention mechanism. Our approach achieves high accuracy with additive quantization and low overhead via the RoPE-commutative codebook. Experiments on long-context benchmarks and GSM8K show that our method reduces FP16 KV cache size by 87.5% with 2-bit quantization, while outperforming state-of-the-art KV cache quantization methods. Notably, it enables 1-bit KV cache quantization with minimal accuracy loss, allowing a LLaMA-3.1 8B model to run with a 128K context length on a single RTX 4090 GPU. The source code is available at: https://github.com/UMass-Embodied-AGI/CommVQ.

