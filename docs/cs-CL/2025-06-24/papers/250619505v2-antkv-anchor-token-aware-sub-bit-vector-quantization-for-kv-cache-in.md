---
layout: default
title: "AnTKV: Anchor Token-Aware Sub-Bit Vector Quantization for KV Cache in Large Language Models"
---

# AnTKV: Anchor Token-Aware Sub-Bit Vector Quantization for KV Cache in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19505" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19505v2</a>
  <a href="https://arxiv.org/pdf/2506.19505.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19505v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19505v2', 'AnTKV: Anchor Token-Aware Sub-Bit Vector Quantization for KV Cache in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyu Li, Chuanfu Xiao, Yang Wang, Xiang Liu, Zhenheng Tang, Baotong Lu, Mao Yang, Xinyu Chen, Xiaowen Chu

**分类**: cs.CL

**发布日期**: 2025-06-24 (更新: 2025-10-18)

---

## 💡 一句话要点

**提出AnTKV以解决大语言模型KV缓存量化精度下降问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `大语言模型` `KV缓存` `锚得分` `向量量化` `模型压缩` `性能优化` `自然语言处理`

## 📋 核心要点

1. 现有的KV缓存量化方法在超低比特量化时，精度下降不均匀，导致整体性能受损。
2. AnTKV通过引入锚得分来识别对量化敏感的token，并保留这些token以减轻精度损失。
3. 实验结果表明，AnTKV在4比特下与现有方法相当，在1比特下显著降低困惑度，表现优异。

## 📝 摘要（中文）

量化已成为减少大语言模型KV缓存内存占用的有效轻量级解决方案。然而，超低比特KV缓存量化导致的精度下降仍然是一个重大挑战。现有的标量量化受限于1比特，而向量量化则利用了向量内的相关性，允许在超低比特范围内进行量化。为进一步减轻量化引起的精度下降，本文引入了锚得分来衡量每个token对量化的敏感性。我们的分析和实验表明，保留1%具有最高锚得分的token可以显著减轻激进量化下的精度损失。我们提出了AnTKV，一个双阶段框架，利用锚token感知向量量化来压缩KV缓存，结合离线token感知中心学习和在线锚token选择，以平衡压缩和精度。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型KV缓存的超低比特量化导致的精度下降问题。现有方法在量化过程中未能有效识别和保留对精度影响较大的token，导致整体性能下降。

**核心思路**：论文提出通过锚得分来评估每个token对量化的敏感性，保留少量高敏感性token，从而减轻量化带来的精度损失。该方法结合了离线学习和在线选择，以实现更好的压缩与精度平衡。

**技术框架**：AnTKV框架分为两个主要阶段：第一阶段为离线token感知中心学习，第二阶段为在线锚token选择。该框架设计了与FlashAttention兼容的在线选择内核，以提高部署效率。

**关键创新**：AnTKV的核心创新在于引入锚得分机制，识别出对量化敏感的token，并通过保留这些token来显著减轻精度损失。这一方法与传统的量化方法相比，能够更有效地利用token间的相关性。

**关键设计**：在设计中，AnTKV采用了高效的在线锚token选择内核，支持在单个80GB A100上扩展到840K tokens，同时在解码吞吐量上比FP16基线提高了3.5倍。

## 📊 实验亮点

实验结果显示，AnTKV在4比特量化下的性能与现有方法相当，而在1比特量化下，困惑度显著降低至6.32，相比之下，CQ为7.25，KVQuant为15.36，展示了其在超低比特量化中的优势。

## 🎯 应用场景

AnTKV的研究成果在大语言模型的实际应用中具有广泛的潜力，尤其是在需要高效内存管理和快速推理的场景中，如自然语言处理、对话系统和实时翻译等。通过有效压缩KV缓存，AnTKV能够在保持高精度的同时，显著提升模型的运行效率，推动大规模语言模型的实际应用落地。

## 📄 摘要（原文）

> Quantization has emerged as an effective and lightweight solution to reduce the memory footprint of the KV cache in Large Language Models. Nevertheless, minimizing the accuracy degradation caused by ultra-low-bit KV cache quantization remains a significant challenge. While scalar quantization is constrained by 1-bit bound, vector quantization exploits intra-vector correlations and enables sub-bit regimes, making it more suitable for ultra-low-bit quantization. To further mitigate quantization-induced degradation, we reveal that the degradation is highly uneven across tokens in attention quality. To investigate this unevenness, we introduce anchor score to measure each token's sensitivity to quantization. Our analysis and experiments show that preserving a small subset (1\%) of tokens with the highest Anchor Score significantly mitigates accuracy loss under aggressive quantization.
>   We propose AnTKV, a dual-stage framework that leverages anchor token-aware vector quantization to compress the KV cache. It combines offline token-aware centroids learning and online anchor token selection to balance compression and accuracy. To enable efficient deployment, we design an online anchor token selection kernel compatible with FlashAttention. It allows LLaMA3-8B to scale to 840K tokens on a single 80GB A100, while delivering up to $3.5\times$ higher decoding throughput over the FP16 baseline. Experiments demonstrate that AnTKV matches or surpasses prior methods at 4-bit, and significantly reduce perplexity under ultra-low-bit quantization, achieving 6.32 at 1-bit on Mistral-7B, compared to 7.25 for CQ and 15.36 for KVQuant.

