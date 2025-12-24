---
layout: default
title: "SpecExtend: A Drop-in Enhancement for Speculative Decoding of Long Sequences"
---

# SpecExtend: A Drop-in Enhancement for Speculative Decoding of Long Sequences

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20776" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20776v3</a>
  <a href="https://arxiv.org/pdf/2505.20776.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20776v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20776v3', 'SpecExtend: A Drop-in Enhancement for Speculative Decoding of Long Sequences')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jungyoub Cha, Hyunjong Kim, Sungzoon Cho

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-27 (更新: 2025-09-29)

**🔗 代码/项目**: [GITHUB](https://github.com/jycha98/SpecExtend)

---

## 💡 一句话要点

**提出SpecExtend以解决长序列推理性能下降问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推测解码` `长序列` `语言模型` `注意力机制` `性能提升` `KV缓存` `自然语言处理`

## 📋 核心要点

1. 现有的推测解码技术在处理长序列时性能显著下降，尤其在中等长度输入时降幅明显，导致推理效率降低。
2. 本文提出SpecExtend，通过集成高效的注意力机制和跨模型检索策略，改善长输入的推测解码性能，无需额外训练。
3. 实验结果显示，SpecExtend在长摘要和长推理任务中分别实现了最高2.84倍和3.86倍的加速，同时保持了短输入的性能表现。

## 📝 摘要（中文）

推测解码是一种广泛应用于大型语言模型（LLMs）推理加速的技术，但随着输入长度的增加，其性能会显著下降，尤其在中等长度时降幅明显。为此，本文提出了SpecExtend，这是一种无需额外训练的增强方案，旨在改善长序列的推测解码性能。SpecExtend集成了高效的注意力机制，如FlashAttention和Hybrid Tree Attention，以加速预填充和验证步骤。此外，本文提出了一种新的KV缓存驱逐策略——跨模型检索，利用目标模型的注意力分数动态选择与小型草稿模型相关的上下文。广泛的评估表明，SpecExtend在16K标记的长摘要推理中加速了推测解码，提升幅度可达2.84倍，而在长推理任务中提升幅度可达3.86倍，同时保持了短输入的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推测解码技术在长序列输入时性能下降的问题，尤其是在中等长度输入时的显著降幅，影响推理效率。

**核心思路**：提出SpecExtend作为一种无需额外训练的增强方案，通过集成高效的注意力机制和新的KV缓存驱逐策略，改善长序列的推测解码性能。

**技术框架**：SpecExtend的整体架构包括预填充和验证两个主要阶段，采用FlashAttention和Hybrid Tree Attention等高效注意力机制来加速这些步骤，同时引入跨模型检索策略以动态选择相关上下文。

**关键创新**：最重要的技术创新在于跨模型检索策略，该策略利用目标模型的注意力分数来选择与小型草稿模型相关的上下文，从而有效提升长序列的推测解码性能。

**关键设计**：在设计中，SpecExtend采用了高效的注意力机制，具体参数设置和网络结构细节未在摘要中详细说明，需参考完整论文以获取更多信息。

## 📊 实验亮点

实验结果表明，SpecExtend在16K标记的长摘要任务中实现了最高2.84倍的加速，而在长推理任务中则达到了3.86倍的加速，与现有最先进框架相比，短输入性能得以保持，显示出其在长序列推理中的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的长文本生成、摘要和推理任务，尤其适用于需要快速响应的实时应用场景。通过提高长序列的推理效率，SpecExtend有望在实际应用中显著提升用户体验和系统性能，未来可能影响更多基于语言模型的应用开发。

## 📄 摘要（原文）

> Speculative decoding is a widely used technique for accelerating inference in large language models (LLMs), but its performance degrades as input length grows, with significant drops even at moderate lengths. Yet, this early degradation has remained largely underexplored. We introduce SpecExtend, a drop-in enhancement that improves speculative decoding on long sequences without additional training. SpecExtend integrates efficient attention mechanisms such as FlashAttention and Hybrid Tree Attention to accelerate prefill and verification steps. To improve both draft accuracy and speed on long inputs without retraining, we propose Cross-model Retrieval, a novel KV cache eviction strategy that leverages the target model's attention scores to dynamically select relevant context for the smaller draft model. Extensive evaluations show that SpecExtend accelerates speculative decoding by up to 2.84x on 16K-token long summarization and up to 3.86x on long reasoning, while preserving the short-input performance of state-of-the-art frameworks. Our code is available at https://github.com/jycha98/SpecExtend .

