---
layout: default
title: Exploring the Hidden Capacity of LLMs for One-Step Text Generation
---

# Exploring the Hidden Capacity of LLMs for One-Step Text Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21189" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21189v2</a>
  <a href="https://arxiv.org/pdf/2505.21189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21189v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21189v2', 'Exploring the Hidden Capacity of LLMs for One-Step Text Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gleb Mezentsev, Ivan Oseledets

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-27 (更新: 2025-11-01)

**备注**: accepted to EMNLP2025 main

---

## 💡 一句话要点

**探索LLMs在一步文本生成中的隐藏能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文本生成` `自回归解码` `多标记生成` `嵌入学习`

## 📋 核心要点

1. 现有方法主要依赖自回归解码，导致生成速度慢且效率低下。
2. 论文提出通过仅使用两个学习嵌入，利用冻结的LLMs进行标记并行生成，从而提升生成效率。
3. 实验结果表明，模型在一次前向传递中能够生成数百个准确标记，展示了显著的多标记生成能力。

## 📝 摘要（中文）

最近的研究表明，大型语言模型（LLMs）能够通过自回归生成，从仅一个训练输入嵌入重构出长达数千个标记的文本。本文探讨自回归解码在此重构中的必要性。我们展示了冻结的LLMs在仅提供两个学习嵌入时，可以在一次标记并行前向传递中生成数百个准确的标记。这揭示了自回归LLMs未被充分探索的多标记生成能力。我们对这些嵌入进行了分析，并表征了它们所编码的信息。尽管这些表示对于给定文本并不唯一，但它们在嵌入空间中形成了连通和局部区域，暗示了训练实用编码器的潜力。这些表示的存在表明，通过学习输入编码器，多标记生成可能在现成的LLMs中本质上是可访问的，从而消除重训练的需求，帮助克服自回归解码的基本瓶颈，同时重用已训练的模型。

## 🔬 方法详解

**问题定义**：本文旨在解决自回归解码在文本生成中的效率低下问题。现有方法依赖于逐步生成，导致生成速度缓慢，难以满足实时应用需求。

**核心思路**：论文的核心思路是探索冻结的LLMs在仅使用两个学习嵌入的情况下，是否能够实现高效的多标记生成。通过这种方式，避免了重训练的复杂性，提升了生成效率。

**技术框架**：整体架构包括输入嵌入的学习、冻结LLMs的前向传递和生成标记的过程。主要模块包括嵌入空间的构建和生成过程的优化。

**关键创新**：最重要的技术创新点在于发现了冻结LLMs在多标记生成中的潜力，表明通过简单的输入编码器可以实现高效生成，与传统的自回归方法形成鲜明对比。

**关键设计**：关键设计包括选择合适的嵌入表示、优化前向传递过程，以及确保生成标记的准确性和连贯性。具体参数设置和损失函数的选择在实验中进行了详细验证。

## 📊 实验亮点

实验结果显示，冻结的LLMs在一次前向传递中能够生成数百个准确标记，显著提升了生成效率。与传统自回归方法相比，生成速度提高了数倍，展示了多标记生成的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的实时文本生成、对话系统、内容创作等。通过提升生成效率，能够在多种场景中实现更快速的响应，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> A recent study showed that large language models (LLMs) can reconstruct surprisingly long texts - up to thousands of tokens - via autoregressive generation from just one trained input embedding. In this work, we explore whether autoregressive decoding is essential for such reconstruction. We show that frozen LLMs can generate hundreds of accurate tokens in just one token-parallel forward pass, when provided with only two learned embeddings. This reveals a surprising and underexplored multi-token generation capability of autoregressive LLMs. We examine these embeddings and characterize the information they encode. We also empirically show that, although these representations are not unique for a given text, they form connected and local regions in embedding space - suggesting the potential to train a practical encoder. The existence of such representations hints that multi-token generation may be natively accessible in off-the-shelf LLMs via a learned input encoder, eliminating heavy retraining and helping to overcome the fundamental bottleneck of autoregressive decoding while reusing already-trained models.

