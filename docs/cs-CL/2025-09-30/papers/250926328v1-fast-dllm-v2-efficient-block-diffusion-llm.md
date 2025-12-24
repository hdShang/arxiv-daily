---
layout: default
title: "Fast-dLLM v2: Efficient Block-Diffusion LLM"
---

# Fast-dLLM v2: Efficient Block-Diffusion LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26328" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26328v1</a>
  <a href="https://arxiv.org/pdf/2509.26328.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26328v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26328v1', 'Fast-dLLM v2: Efficient Block-Diffusion LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengyue Wu, Hao Zhang, Shuchen Xue, Shizhe Diao, Yonggan Fu, Zhijian Liu, Pavlo Molchanov, Ping Luo, Song Han, Enze Xie

**分类**: cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**Fast-dLLM v2：高效块扩散语言模型，加速并行文本生成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `块扩散语言模型` `并行文本生成` `高效推理` `分层缓存` `自回归模型` `互补注意力掩码` `低资源微调`

## 📋 核心要点

1. 自回归LLM推理效率受限于顺序解码，成为实际应用的瓶颈。
2. Fast-dLLM v2通过块扩散机制和互补注意力掩码，将预训练AR模型转化为支持并行生成的dLLM。
3. 实验表明，Fast-dLLM v2在保持或超过AR模型准确率的同时，实现了高达2.5倍的推理加速。

## 📝 摘要（中文）

自回归（AR）大型语言模型（LLM）在各种自然语言任务中取得了显著的性能，但其固有的顺序解码限制了推理效率。本文提出了Fast-dLLM v2，一种精心设计的块扩散语言模型（dLLM），它能有效地将预训练的AR模型适配为dLLM，用于并行文本生成，仅需约10亿token的微调。与Dream等全注意力扩散LLM（5800亿token）相比，这减少了500倍的训练数据，同时保留了原始模型的性能。我们的方法引入了一种新的训练方案，将块扩散机制与互补注意力掩码相结合，从而实现块状双向上下文建模，而不会牺牲AR训练目标。为了进一步加速解码，我们设计了一种分层缓存机制：块级缓存，用于存储跨块的历史上下文表示；子块缓存，用于在部分解码的块内实现高效的并行生成。结合我们的并行解码流水线，Fast-dLLM v2在不影响生成质量的前提下，实现了比标准AR解码高达2.5倍的加速。在各种基准测试中进行的大量实验表明，Fast-dLLM v2在准确性方面与AR基线相匹配或超过，同时在dLLM中提供了最先进的效率——标志着朝着快速准确的LLM的实际部署迈出了重要一步。代码和模型将公开发布。

## 🔬 方法详解

**问题定义**：现有自回归（AR）大型语言模型在推理时需要顺序解码，效率较低，难以满足实际应用的需求。全注意力扩散语言模型虽然支持并行生成，但需要大量的训练数据，成本高昂。因此，如何在降低训练成本的同时，实现LLM的并行高效生成是一个关键问题。

**核心思路**：Fast-dLLM v2的核心思路是将预训练的AR模型转化为块扩散语言模型（dLLM），利用块扩散机制实现并行文本生成。通过结合块扩散机制和互补注意力掩码，模型可以在块级别进行双向上下文建模，同时保留AR模型的训练目标，从而减少了对大量训练数据的需求。

**技术框架**：Fast-dLLM v2的整体框架包括以下几个主要模块：1) 块扩散机制：将文本分成块，并使用扩散过程并行生成这些块。2) 互补注意力掩码：在训练过程中，使用互补注意力掩码来保留AR模型的训练目标，同时允许块级别的双向上下文建模。3) 分层缓存机制：包括块级缓存和子块缓存，用于存储历史上下文表示，加速解码过程。4) 并行解码流水线：利用并行计算资源，加速块的生成和解码。

**关键创新**：Fast-dLLM v2的关键创新在于其高效的训练方法和分层缓存机制。与需要大量训练数据的全注意力扩散LLM相比，Fast-dLLM v2仅需少量微调即可实现并行生成，大大降低了训练成本。分层缓存机制进一步加速了解码过程，提高了推理效率。

**关键设计**：在训练过程中，使用了块扩散损失和AR损失的加权组合，以平衡并行生成和序列建模的能力。互补注意力掩码的设计允许模型在块内进行双向注意力计算，同时限制块间的注意力，以保留AR模型的因果关系。分层缓存机制中的块大小和子块大小是重要的超参数，需要根据具体的任务和模型大小进行调整。

## 📊 实验亮点

Fast-dLLM v2在多个基准测试中表现出色，在准确性方面与AR基线相匹配或超过。更重要的是，它实现了高达2.5倍的推理加速，同时仅需约10亿token的微调，与全注意力扩散LLM相比，训练数据减少了500倍。这些结果表明，Fast-dLLM v2在效率和准确性之间取得了良好的平衡，是dLLM领域的一项重要进展。

## 🎯 应用场景

Fast-dLLM v2具有广泛的应用前景，例如：实时对话系统、机器翻译、文本摘要、代码生成等。其高效的并行生成能力可以显著降低延迟，提高用户体验。此外，由于其训练成本较低，可以更容易地部署在资源受限的设备上，例如移动设备和边缘计算平台。未来，该技术有望推动LLM在更多实际场景中的应用。

## 📄 摘要（原文）

> Autoregressive (AR) large language models (LLMs) have achieved remarkable performance across a wide range of natural language tasks, yet their inherent sequential decoding limits inference efficiency. In this work, we propose Fast-dLLM v2, a carefully designed block diffusion language model (dLLM) that efficiently adapts pretrained AR models into dLLMs for parallel text generation, requiring only approximately 1B tokens of fine-tuning. This represents a 500x reduction in training data compared to full-attention diffusion LLMs such as Dream (580B tokens), while preserving the original model's performance. Our approach introduces a novel training recipe that combines a block diffusion mechanism with a complementary attention mask, enabling blockwise bidirectional context modeling without sacrificing AR training objectives. To further accelerate decoding, we design a hierarchical caching mechanism: a block-level cache that stores historical context representations across blocks, and a sub-block cache that enables efficient parallel generation within partially decoded blocks. Coupled with our parallel decoding pipeline, Fast-dLLM v2 achieves up to 2.5x speedup over standard AR decoding without compromising generation quality. Extensive experiments across diverse benchmarks demonstrate that Fast-dLLM v2 matches or surpasses AR baselines in accuracy, while delivering state-of-the-art efficiency among dLLMs - marking a significant step toward the practical deployment of fast and accurate LLMs. Code and model will be publicly released.

