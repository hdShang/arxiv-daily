---
layout: default
title: "SecoustiCodec: Cross-Modal Aligned Streaming Single-Codecbook Speech Codec"
---

# SecoustiCodec: Cross-Modal Aligned Streaming Single-Codecbook Speech Codec

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02849" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02849v1</a>
  <a href="https://arxiv.org/pdf/2508.02849.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02849v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02849v1', 'SecoustiCodec: Cross-Modal Aligned Streaming Single-Codecbook Speech Codec')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chunyu Qiang, Haoyu Wang, Cheng Gong, Tianrui Wang, Ruibo Fu, Tao Wang, Ruilong Chen, Jiangyan Yi, Zhengqi Wen, Chen Zhang, Longbiao Wang, Jianwu Dang, Jianhua Tao

**分类**: eess.AS, cs.AI, cs.CL, cs.SD

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出SecoustiCodec以解决语音编码中的语义与副语言信息分离问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音编解码` `跨模态对齐` `低比特率` `语义解耦` `对比学习` `多阶段优化` `流媒体技术`

## 📋 核心要点

1. 现有语音编解码方法在语义编码中面临副语言信息残留、语义完整性不足等多重挑战。
2. 本文提出SecoustiCodec，通过解耦语义与副语言信息，采用对比学习和多阶段优化策略提升编码质量。
3. 实验结果表明，SecoustiCodec在0.27/1 kbps下实现了1.77/2.58的重构质量，达到当前最优水平。

## 📝 摘要（中文）

语音编解码器在统一语音和文本语言模型中起着关键作用。现有编解码方法面临诸多挑战，如残余的副语言信息（如音色、情感）、语义完整性不足、重构能力有限以及缺乏流媒体支持。为了解决这些问题，本文提出了SecoustiCodec，这是一种跨模态对齐的低比特率流媒体语音编解码器，能够在单一代码本空间中解耦语义和副语言信息。通过引入副语言编码，弥补语义与声学编码之间的信息差距，确保语义完整性和重构保真度。本文还提出了一种基于变分自编码器（VAE）和有限标量量化（FSQ）的高效语义量化方法，缓解了令牌的长尾分布问题，同时保持高代码本利用率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语音编解码器在语义与副语言信息编码中的不足，尤其是如何有效分离和重构这些信息，以提高语音质量和语义完整性。现有方法往往无法有效处理副语言信息，导致重构效果不佳。

**核心思路**：SecoustiCodec通过引入副语言编码来弥补语义与声学编码之间的信息差距，确保语义的完整性和重构的保真度。采用对比学习方法实现语义的解耦，确保文本与语音在多模态框架下的对齐。

**技术框架**：SecoustiCodec的整体架构包括多个模块：首先是语义编码模块，采用VAE和FSQ进行高效量化；其次是副语言编码模块，负责提取和编码副语言信息；最后是多阶段优化策略，确保模型的稳定收敛。

**关键创新**：本文的主要创新在于提出了一种新的语义解耦方法，利用对比学习有效去除副语言信息，并在单一代码本空间中实现语义与副语言的分离，这在现有方法中尚属首次。

**关键设计**：在设计中，采用了变分自编码器（VAE）和有限标量量化（FSQ）相结合的量化方法，解决了长尾分布问题，同时保持高代码本利用率。损失函数的设计也考虑了语义完整性与重构保真度的平衡。

## 📊 实验亮点

SecoustiCodec在0.27/1 kbps下分别实现了1.77/2.58的重构质量，显著优于现有方法，展示了其在低比特率条件下的卓越性能。该研究不仅提升了语音编码的质量，还为未来的流媒体应用提供了新的解决方案。

## 🎯 应用场景

SecoustiCodec的研究成果在语音通信、语音识别和语音合成等领域具有广泛的应用潜力。通过提高语音编码的质量和效率，该技术能够改善语音交互的用户体验，并推动智能助手和自动语音识别系统的发展。未来，随着技术的进一步成熟，SecoustiCodec可能会在实时语音流媒体传输中发挥重要作用。

## 📄 摘要（原文）

> Speech codecs serve as a crucial bridge in unifying speech and text language models. Existing codec methods face several challenges in semantic encoding, such as residual paralinguistic information (e.g., timbre, emotion), insufficient semantic completeness, limited reconstruction capability, and lack of support for streaming. To address these challenges, we propose SecoustiCodec, a cross-modal aligned low-bitrate streaming speech codec that disentangles semantic and paralinguistic information in a single-codebook space. To ensure semantic completeness and reconstruction fidelity, paralinguistic encoding is introduced to bridge the information gap between semantic and acoustic encoding. A semantic-only efficient quantization method based on VAE (Variational Autoencoder) and FSQ (Finite Scalar Quantization) is proposed. This approach alleviates the long-tail distribution problem of tokens while maintaining high codebook utilization. A semantic disentanglement method based on contrastive learning is proposed, which aligns text and speech in a joint multimodal frame-level space, effectively removing paralinguistic information from semantic encoding. An acoustic-constrained multi-stage optimization strategy is proposed to ensure robust and stable convergence. Figure~\ref{fig:pesq_kbps_below_2kbps} shows SecoustiCodec achieves SOTA (state-of-the-art) reconstruction quality (PESQ) of 1.77/2.58 at 0.27/1 kbps. The code and model weights for SecoustiCodec will be open-sourced upon the completion of the peer-review process. We've open-sourced SecoustiCodec's demo, code, and model weights.

