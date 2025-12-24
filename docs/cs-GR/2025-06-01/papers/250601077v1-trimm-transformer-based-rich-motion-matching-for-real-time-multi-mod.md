---
layout: default
title: "TRiMM: Transformer-Based Rich Motion Matching for Real-Time multi-modal Interaction in Digital Humans"
---

# TRiMM: Transformer-Based Rich Motion Matching for Real-Time multi-modal Interaction in Digital Humans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01077" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01077v1</a>
  <a href="https://arxiv.org/pdf/2506.01077.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01077v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01077v1', 'TRiMM: Transformer-Based Rich Motion Matching for Real-Time multi-modal Interaction in Digital Humans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yueqian Guo, Tianzhao Li, Xin Lyu, Jiehaolin Chen, Zhaohan Wang, Sirui Xiao, Yurun Chen, Yezi He, Helin Li, Fan Zhang

**分类**: cs.GR, cs.HC

**发布日期**: 2025-06-01

**备注**: 24 pages,12 figures

**🔗 代码/项目**: [GITHUB](https://github.com/teroon/TRiMM-Transformer-Based-Rich-Motion-Matching)

---

## 💡 一句话要点

**提出TRiMM以解决实时多模态交互中的手势生成问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实时手势生成` `多模态交互` `跨模态注意力` `长上下文建模` `数字人类`

## 📋 核心要点

1. 现有的共语手势生成方法在实时合成和长文本理解方面存在显著不足，难以满足实际应用需求。
2. TRiMM通过引入跨模态注意力机制、长上下文自回归模型和大规模手势匹配系统，提供了一种高效的手势生成解决方案。
3. 在ZEGGS和BEAT数据集上的广泛评估表明，TRiMM在手势生成速度和质量上均优于现有的最先进方法。

## 📝 摘要（中文）

基于大型语言模型（LLM）的数字人类引发了一系列关于共语手势生成系统的研究。然而，现有方法在实时合成和长文本理解方面面临挑战。本文提出了一种新颖的多模态框架TRiMM，旨在实现实时3D手势生成。该方法包含三个模块：1）跨模态注意力机制，实现语音与手势之间的精确时间对齐；2）长上下文自回归模型，结合滑动窗口机制进行有效的序列建模；3）大规模手势匹配系统，构建原子动作库并实现实时检索。实验表明，该方法在消费级GPU上以120 fps的速度实现实时推理，每句的延迟为0.15秒，超越了当前最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决实时多模态交互中手势生成的挑战，现有方法在处理长文本和实时合成时表现不佳，导致生成的手势与语音不够协调。

**核心思路**：TRiMM的核心思路是通过跨模态注意力机制实现语音与手势之间的精确时间对齐，同时结合长上下文自回归模型来处理复杂的序列信息，以提高生成的实时性和准确性。

**技术框架**：TRiMM的整体架构包括三个主要模块：跨模态注意力机制、长上下文自回归模型和大规模手势匹配系统。跨模态注意力机制用于对齐语音与手势，长上下文模型则通过滑动窗口处理长文本，而手势匹配系统则提供实时检索功能。

**关键创新**：TRiMM的关键创新在于其跨模态注意力机制和长上下文自回归模型的结合，显著提升了手势生成的实时性和质量。这一设计与传统方法相比，能够更好地处理长文本和复杂的语音输入。

**关键设计**：在模型设计中，采用了滑动窗口机制来增强序列建模能力，并构建了一个原子动作库以支持实时手势检索。模型在消费级GPU上优化，确保了120 fps的实时推理速度和0.15秒的每句延迟。

## 📊 实验亮点

TRiMM在ZEGGS和BEAT数据集上的实验结果显示，其在手势生成速度上达到了120 fps，并且每句的延迟仅为0.15秒，显著优于现有最先进的方法。这一性能提升使得数字人类能够实时响应语音并生成相应的手势，极大地增强了交互体验。

## 🎯 应用场景

TRiMM的研究成果在虚拟现实、游戏开发和人机交互等领域具有广泛的应用潜力。通过实现实时的手势生成，数字人类能够更自然地与用户进行互动，提升用户体验。此外，该技术还可用于教育、培训和娱乐等多个场景，推动相关行业的发展。

## 📄 摘要（原文）

> Large Language Model (LLM)-driven digital humans have sparked a series of recent studies on co-speech gesture generation systems. However, existing approaches struggle with real-time synthesis and long-text comprehension. This paper introduces Transformer-Based Rich Motion Matching (TRiMM), a novel multi-modal framework for real-time 3D gesture generation. Our method incorporates three modules: 1) a cross-modal attention mechanism to achieve precise temporal alignment between speech and gestures; 2) a long-context autoregressive model with a sliding window mechanism for effective sequence modeling; 3) a large-scale gesture matching system that constructs an atomic action library and enables real-time retrieval. Additionally, we develop a lightweight pipeline implemented in the Unreal Engine for experimentation. Our approach achieves real-time inference at 120 fps and maintains a per-sentence latency of 0.15 seconds on consumer-grade GPUs (Geforce RTX3060). Extensive subjective and objective evaluations on the ZEGGS, and BEAT datasets demonstrate that our model outperforms current state-of-the-art methods. TRiMM enhances the speed of co-speech gesture generation while ensuring gesture quality, enabling LLM-driven digital humans to respond to speech in real time and synthesize corresponding gestures. Our code is available at https://github.com/teroon/TRiMM-Transformer-Based-Rich-Motion-Matching

