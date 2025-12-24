---
layout: default
title: Lossless Token Sequence Compression via Meta-Tokens
---

# Lossless Token Sequence Compression via Meta-Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00307" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00307v2</a>
  <a href="https://arxiv.org/pdf/2506.00307.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00307v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00307v2', 'Lossless Token Sequence Compression via Meta-Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: John Harvill, Ziwei Fan, Hao Wang, Luke Huan, Anoop Deoras, Yizhou Sun, Hao Ding

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-30 (更新: 2025-08-20)

**备注**: 16 pages, 8 figures

---

## 💡 一句话要点

**提出无损令牌序列压缩方法以优化大语言模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无损压缩` `大语言模型` `序列处理` `自然语言处理` `计算效率` `语义保留` `LZ77算法`

## 📋 核心要点

1. 现有的提示压缩方法主要采用有损技术，难以在保留语义信息的同时有效减少序列长度。
2. 本文提出了一种无损压缩技术，能够在不损失语义信息的情况下，显著减少输入令牌序列的长度。
3. 实验结果显示，所提方法在两个任务上分别实现了27%和18%的序列长度减少，并且计算效率显著提升。

## 📝 摘要（中文）

现有的大语言模型（LLM）提示压缩研究主要集中在有损方法上，旨在最大限度地保留与下游任务相关的语义信息，同时显著减少序列长度。本文提出了一种类似于LZ77的任务无关无损压缩技术，使得输入令牌序列长度平均减少27%和18%。在使用基于变换器的LLM时，这分别对应于47%和33%的编码计算减少。该令牌序列转换过程易于逆转，确保没有语义信息丢失。我们在两个需要严格保留语义和语法的任务上评估了所提出的方法，结果表明现有的有损压缩方法在此设置下表现不佳。我们的无损压缩技术与未压缩输入相比，性能差距微小，推测更大的模型和扩展的计算预算可能会完全消除这一差距。

## 🔬 方法详解

**问题定义**：本文旨在解决现有有损压缩方法在保留语义信息方面的不足，尤其是在需要严格保留语义和语法的任务中，现有方法表现不佳。

**核心思路**：提出了一种无损压缩技术，类似于LZ77算法，能够在压缩过程中不丢失任何语义信息，从而实现更高效的输入令牌序列处理。

**技术框架**：整体架构包括输入令牌序列的压缩模块和解压模块，压缩模块负责将输入序列转换为压缩格式，解压模块则确保可以轻松恢复原始序列。

**关键创新**：最重要的创新在于提出了一种无损压缩方法，显著区别于现有的有损方法，确保在压缩过程中不损失任何语义信息。

**关键设计**：在设计中，采用了类似LZ77的算法结构，确保压缩和解压过程的高效性，同时在参数设置上优化了编码计算，减少了计算复杂度。

## 📊 实验亮点

实验结果表明，所提出的无损压缩方法在两个评估任务上分别实现了27%和18%的序列长度减少，计算效率提升达到47%和33%。与未压缩输入相比，性能差距微小，显示出该方法在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等场景，能够显著提高大语言模型的计算效率和响应速度。未来，随着模型规模的扩大和计算资源的增加，该方法的应用价值将更加凸显，可能推动更高效的AI系统的开发。

## 📄 摘要（原文）

> Existing work on prompt compression for Large Language Models (LLM) focuses on lossy methods that try to maximize the retention of semantic information that is relevant to downstream tasks while significantly reducing the sequence length. In this paper, we introduce a task-agnostic lossless compression technique similar to LZ77 that makes it possible to reduce the input token sequence length on average by 27\% and 18\% for the two evaluation tasks explored here. Given that we use transformer-based LLMs, this equates to 47\% and 33\% less encoding computation, respectively, due to the quadratic nature of attention. The token sequence transformation is trivial to reverse and highlights that no semantic information is lost in the process. We evaluate our proposed approach on two tasks that require strict preservation of semantics/syntax and demonstrate that existing lossy compression methods perform poorly in this setting. We find that our lossless compression technique produces only a small gap in performance compared to using the uncompressed input and posit that larger models and an expanded computing budget would likely erase the gap entirely.

