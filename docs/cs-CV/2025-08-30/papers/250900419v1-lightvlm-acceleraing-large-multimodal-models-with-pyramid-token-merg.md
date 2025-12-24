---
layout: default
title: "LightVLM: Acceleraing Large Multimodal Models with Pyramid Token Merging and KV Cache Compression"
---

# LightVLM: Acceleraing Large Multimodal Models with Pyramid Token Merging and KV Cache Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00419" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00419v1</a>
  <a href="https://arxiv.org/pdf/2509.00419.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00419v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00419v1', 'LightVLM: Acceleraing Large Multimodal Models with Pyramid Token Merging and KV Cache Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lianyu Hu, Fanhua Shang, Wei Feng, Liang Wan

**分类**: cs.CV

**发布日期**: 2025-08-30

**备注**: EMNLP2025 Findings

---

## 💡 一句话要点

**提出LightVLM以加速多模态模型推理过程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `推理加速` `金字塔令牌合并` `KV缓存压缩` `视觉语言模型` `模型效率` `长文本生成`

## 📋 核心要点

1. 现有的视觉语言模型在推理过程中存在效率低下的问题，尤其是在处理长序列时延迟较高。
2. LightVLM通过金字塔令牌合并和KV缓存压缩，分别在编码和解码阶段同时加速推理过程，显著提升模型效率。
3. 实验表明，LightVLM在保留极少图像令牌的情况下，仍能保持高性能，并在长文本生成中显著减少推理时间。

## 📝 摘要（中文）

本文介绍了LightVLM，一种简单而有效的方法，可以无缝部署在现有的视觉语言模型（VLMs）上，以显著加速推理过程，且无需训练。我们将VLM的推理过程分为编码和解码两个阶段，并提出同时加速这两个阶段以提高模型效率。在编码阶段，我们提出了金字塔令牌合并，通过分层方式减少不同LLM层的令牌，最终仅保留少量主导令牌以实现高效。在解码阶段，为了降低输出长序列的高延迟，我们提出了KV缓存压缩，去除不必要的缓存以提高网络吞吐量。实验结果表明，LightVLM在仅保留35%图像令牌时成功保持100%的性能，而在仅保留3%图像令牌时保持约98%的性能。LightVLM能够将网络吞吐量提高2.02倍，并将预填充时间减少3.65倍。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言模型推理效率低下的问题，尤其是在处理长序列时的高延迟和资源消耗。现有方法在推理过程中未能有效利用令牌信息，导致性能瓶颈。

**核心思路**：LightVLM的核心思路是通过金字塔令牌合并和KV缓存压缩，分别在编码和解码阶段优化推理过程，以提高整体模型的效率和响应速度。

**技术框架**：LightVLM的整体架构分为两个主要阶段：编码阶段和解码阶段。在编码阶段，通过金字塔结构逐层合并令牌；在解码阶段，通过压缩KV缓存来减少不必要的计算和存储。

**关键创新**：LightVLM的主要创新在于金字塔令牌合并技术和KV缓存压缩策略，这两者结合使得模型在保持性能的同时显著提高了推理速度，与现有方法相比具有本质的效率提升。

**关键设计**：在金字塔令牌合并中，设计了分层合并策略，以保留最具代表性的令牌；在KV缓存压缩中，优化了缓存管理策略，去除了冗余数据，提升了网络的吞吐量。

## 📊 实验亮点

实验结果显示，LightVLM在仅保留35%图像令牌时保持100%性能，保留3%图像令牌时仍保持约98%性能。同时，LightVLM将网络吞吐量提高了2.02倍，预填充时间减少了3.65倍，长文本生成的推理时间减少了3.21倍，显著优于现有方法。

## 🎯 应用场景

LightVLM的研究成果具有广泛的应用潜力，尤其是在需要实时处理视觉和语言信息的场景，如智能助手、自动驾驶、视频分析等领域。其高效的推理能力能够支持更复杂的多模态任务，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> In this paper, we introduce LightVLM, a simple but effective method that can be seamlessly deployed upon existing Vision-Language Models (VLMs) to greatly accelerate the inference process in a training-free manner. We divide the inference procedure of VLMs into two stages, i.e., encoding and decoding, and propose to simultaneously accelerate VLMs in both stages to largely improve model efficiency. During encoding, we propose pyramid token merging to reduce tokens of different LLM layers in a hierarchical manner by finally only keeping a few dominant tokens to achieve high efficiency. During decoding, aimed at reducing the high latency of outputting long sequences, we propose KV Cache compression to remove unnecessary caches to increase the network throughput. Experimental results show that LightVLM successfully retains 100% performance when only preserving 35% image tokens, and maintains around 98% performance when keeping only 3% image tokens. LightVLM could 2.02$\times$ the network throughput and reduce the prefilling time by 3.65$\times$. LightVLM also makes large VLMs faster again by enabling a heavy model (e.g., InternVL2.5 26B) to infer faster than significantly smaller models (e.g., InternVL2.5 8B), hopefully facilitating the real-world deployment. When generating long text sequences (e.g., 4096 tokens), LightVLM could reduce the inference time by 3.21$\times$, largely outperforming existing methods.

