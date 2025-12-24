---
layout: default
title: "MOGO: Residual Quantized Hierarchical Causal Transformer for High-Quality and Real-Time 3D Human Motion Generation"
---

# MOGO: Residual Quantized Hierarchical Causal Transformer for High-Quality and Real-Time 3D Human Motion Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05952" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05952v2</a>
  <a href="https://arxiv.org/pdf/2506.05952.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05952v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05952v2', 'MOGO: Residual Quantized Hierarchical Causal Transformer for High-Quality and Real-Time 3D Human Motion Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongjie Fu, Tengjiao Sun, Pengcheng Fang, Xiaohao Cai, Hansung Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-08-07)

**备注**: 9 pages, 4 figures, conference

---

## 💡 一句话要点

**提出MOGO以解决高质量实时3D人类运动生成问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D运动生成` `变换器` `自回归框架` `残差量化` `实时性能` `文本条件对齐` `运动表示`

## 📋 核心要点

1. 现有的文本到运动生成方法在高保真度、实时性和可扩展性方面面临挑战，难以同时满足这些需求。
2. MOGO通过引入MoSA-VQ和RQHC-Transformer模块，提供了一种高效的自回归框架，能够在单次前向传递中生成运动序列。
3. 在多个基准数据集上，MOGO的生成质量与最先进的方法相当或更优，同时在实时性能和流媒体生成方面有显著提升。

## 📝 摘要（中文）

近年来，基于变换器的文本到运动生成技术取得了显著进展，能够合成高质量的人类运动。然而，实现高保真度、流媒体能力、实时响应和可扩展性仍然是一个基本挑战。本文提出了MOGO（Motion Generation with One-pass），一种新颖的自回归框架，旨在高效且实时地生成3D运动。MOGO包含两个关键组件：MoSA-VQ，一个运动尺度自适应残差向量量化模块，能够分层离散运动序列并生成紧凑而富有表现力的表示；RQHC-Transformer，一个残差量化层次因果变换器，能够在单次前向传递中生成多层运动标记，显著降低推理延迟。通过引入文本条件对齐机制，进一步提高了运动解码的语义保真度。大量实验表明，MOGO在多个基准数据集上实现了与现有最先进的变换器方法相比具有竞争力或更优的生成质量，同时在实时性能、流媒体生成和零-shot设置下的泛化能力上有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决高质量实时3D人类运动生成中的高保真度、流媒体能力和实时响应等基本挑战。现有方法在这些方面存在明显不足，难以满足实际应用需求。

**核心思路**：MOGO的核心思路是通过MoSA-VQ和RQHC-Transformer模块，采用自回归框架实现高效的运动生成，特别是在推理延迟方面进行优化。

**技术框架**：MOGO的整体架构包括两个主要模块：MoSA-VQ用于运动序列的层次离散化，RQHC-Transformer用于在单次前向传递中生成多层运动标记。

**关键创新**：MOGO的关键创新在于引入了运动尺度自适应残差向量量化和残差量化层次因果变换器，这使得生成过程更加高效，并显著降低了推理延迟。

**关键设计**：在设计中，MoSA-VQ模块采用可学习的缩放策略，确保生成的运动表示既紧凑又富有表现力。同时，RQHC-Transformer通过残差连接优化了信息流动，提升了生成质量。实验中还引入了文本条件对齐机制，以增强运动解码的语义保真度。

## 📊 实验亮点

在HumanML3D、KIT-ML和CMP等基准数据集上的实验结果显示，MOGO在生成质量上与最先进的变换器方法相当或更优，同时在实时性能上提升了显著的速度，推理延迟大幅降低，展现出良好的流媒体生成能力和零-shot泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和人机交互等场景，能够为这些领域提供高质量的运动生成技术。MOGO的实时性能和高保真度使其在动态环境中具有实际价值，未来可能推动更广泛的应用和研究。

## 📄 摘要（原文）

> Recent advances in transformer-based text-to-motion generation have led to impressive progress in synthesizing high-quality human motion. Nevertheless, jointly achieving high fidelity, streaming capability, real-time responsiveness, and scalability remains a fundamental challenge. In this paper, we propose MOGO (Motion Generation with One-pass), a novel autoregressive framework tailored for efficient and real-time 3D motion generation. MOGO comprises two key components: (1) MoSA-VQ, a motion scale-adaptive residual vector quantization module that hierarchically discretizes motion sequences with learnable scaling to produce compact yet expressive representations; and (2) RQHC-Transformer, a residual quantized hierarchical causal transformer that generates multi-layer motion tokens in a single forward pass, significantly reducing inference latency. To enhance semantic fidelity, we further introduce a text condition alignment mechanism that improves motion decoding under textual control. Extensive experiments on benchmark datasets including HumanML3D, KIT-ML, and CMP demonstrate that MOGO achieves competitive or superior generation quality compared to state-of-the-art transformer-based methods, while offering substantial improvements in real-time performance, streaming generation, and generalization under zero-shot settings.

