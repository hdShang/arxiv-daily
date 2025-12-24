---
layout: default
title: "DPad: Efficient Diffusion Language Models with Suffix Dropout"
---

# DPad: Efficient Diffusion Language Models with Suffix Dropout

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14148" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14148v2</a>
  <a href="https://arxiv.org/pdf/2508.14148.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14148v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14148v2', 'DPad: Efficient Diffusion Language Models with Suffix Dropout')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinhua Chen, Sitao Huang, Cong Guo, Chiyue Wei, Yintao He, Jianyi Zhang, Hai "Helen" Li, Yiran Chen

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-19 (更新: 2025-08-23)

**🔗 代码/项目**: [GITHUB](https://github.com/Crys-Chen/DPad)

---

## 💡 一句话要点

**提出DPad以解决扩散语言模型的计算效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散语言模型` `文本生成` `计算效率` `注意力机制` `机器学习`

## 📋 核心要点

1. 现有的扩散语言模型在每一步都需预测所有后缀标记，导致计算开销高，效率低下。
2. DPad通过限制注意力范围到附近后缀标记，结合滑动窗口和距离衰减丢弃策略，优化了计算过程。
3. 实验结果表明，DPad在多个基准测试中实现了高达61.4倍的速度提升，同时保持了与传统方法相当的准确性。

## 📝 摘要（中文）

扩散基础的大型语言模型（dLLMs）通过将解码过程视为去噪过程来实现文本生成的并行化，但由于在每一步都预测所有未来后缀标记而导致高计算开销。本文提出了Diffusion Scratchpad（DPad），一种无训练的方法，限制注意力集中在一小部分附近的后缀标记上，既保持了准确性又消除了冗余。DPad结合了两种策略：滑动窗口和距离衰减丢弃，前者维护固定长度的后缀窗口，后者在注意力计算之前确定性地移除远离的后缀标记。全面评估显示，DPad在多个基准测试中相较于传统dLLMs实现了高达61.4倍的速度提升，同时保持了相当的准确性，突显了其在高效和可扩展长序列推理中的潜力。

## 🔬 方法详解

**问题定义**：现有的扩散语言模型在生成文本时需要在每一步预测所有未来的后缀标记，这导致了高昂的计算成本和低效的推理过程。

**核心思路**：DPad通过限制注意力机制仅集中在一小部分附近的后缀标记上，减少了计算冗余，同时保持了生成文本的准确性。该方法不需要额外的训练过程，易于实现。

**技术框架**：DPad的整体架构包括两个主要模块：滑动窗口和距离衰减丢弃。滑动窗口维护固定长度的后缀窗口，而距离衰减丢弃则在注意力计算前去除远离的后缀标记。

**关键创新**：DPad的主要创新在于其简单而有效的设计，能够在不牺牲准确性的情况下显著提升计算效率。这一方法与传统的dLLMs相比，减少了不必要的计算步骤。

**关键设计**：DPad的设计包括固定长度的滑动窗口和确定性的距离衰减丢弃策略，这些设计使得模型能够高效地处理长序列，同时与现有的优化技术（如前缀缓存）兼容。

## 📊 实验亮点

DPad在多个基准测试中表现出色，相较于传统的扩散语言模型，达到了高达61.4倍的速度提升，同时保持了相似的准确性。这一结果突显了DPad在长序列推理中的高效性和实用性。

## 🎯 应用场景

DPad的研究成果在自然语言处理领域具有广泛的应用潜力，特别是在需要高效处理长文本序列的场景中，如对话系统、文本生成和机器翻译等。其高效的推理能力将有助于提升这些应用的响应速度和用户体验。

## 📄 摘要（原文）

> Diffusion-based Large Language Models (dLLMs) parallelize text generation by framing decoding as a denoising process, but suffer from high computational overhead since they predict all future suffix tokens at each step while retaining only a small fraction. We propose Diffusion Scratchpad (DPad), a training-free method that restricts attention to a small set of nearby suffix tokens, preserving fidelity while eliminating redundancy. DPad integrates two strategies: (i) a sliding window, which maintains a fixed-length suffix window, and (ii) distance-decay dropout, which deterministically removes distant suffix tokens before attention computation. This simple design is compatible with existing optimizations such as prefix caching and can be implemented with only a few lines of code. Comprehensive evaluations across multiple benchmarks on LLaDA-1.5 and Dream models demonstrate that DPad delivers up to $\mathbf{61.4\times}$ speedup over vanilla dLLMs while maintaining comparable accuracy, highlighting its potential for efficient and scalable long-sequence inference. Our code is available at https://github.com/Crys-Chen/DPad.

