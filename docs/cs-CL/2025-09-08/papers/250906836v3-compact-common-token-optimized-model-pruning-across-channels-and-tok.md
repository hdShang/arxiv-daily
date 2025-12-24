---
layout: default
title: "COMPACT: Common-token Optimized Model Pruning Across Channels and Tokens"
---

# COMPACT: Common-token Optimized Model Pruning Across Channels and Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06836" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06836v3</a>
  <a href="https://arxiv.org/pdf/2509.06836.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06836v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06836v3', 'COMPACT: Common-token Optimized Model Pruning Across Channels and Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eugene Kwek, Wenpeng Yin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-08 (更新: 2025-10-10)

---

## 💡 一句话要点

**提出COMPACT，通过联合优化词表和FFN通道剪枝，提升LLM和SLM的效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型剪枝` `语言模型压缩` `Transformer` `词表剪枝` `FFN通道剪枝` `低延迟推理` `边缘部署`

## 📋 核心要点

1. 现有剪枝方法在保持Transformer结构和处理小型语言模型（SLM）方面存在局限性，宽度剪枝破坏标准结构，深度剪枝导致精度骤降。
2. COMPACT联合剪枝稀有词汇和FFN中间通道，利用common-token-weighted activations对齐重要性，保持标准Transformer结构。
3. 实验结果表明，COMPACT在多种模型（Qwen、LLaMA、Gemma）上实现了最先进的下游性能，并显著降低了参数量、内存占用和延迟。

## 📝 摘要（中文）

为了提高大型语言模型（LLM）在内存、延迟和服务成本方面的效率，使其更适用于边缘部署、交互式应用和大规模可持续推理，本文提出了COMPACT方法。该方法联合执行：（i）剪枝稀有词汇以缩小嵌入/LM头层；（ii）使用common-token-weighted activations剪枝FFN中间通道，使重要性与剪枝后的token分布对齐。COMPACT继承了深度和宽度剪枝的优点，如部署友好性（保持标准的Transformer架构）、尺度适应性（权衡词汇表与FFN剪枝）、具有竞争力的剪枝时间和显著的内存节省以及吞吐量提升。在Qwen、LLaMA和Gemma系列（0.5B-70B）上的实验表明，COMPACT实现了最先进的下游性能，并显著减少了参数量、GPU内存和延迟。

## 🔬 方法详解

**问题定义**：现有宽度剪枝方法通常会破坏Transformer的标准结构，导致需要定制化的推理代码。深度剪枝虽然保持了结构，但可能导致显著的精度下降。此外，许多剪枝方法在大型语言模型（LLM）上表现良好，但在小型语言模型（SLM）上难以维持性能。因此，如何设计一种既能保持标准Transformer结构，又能有效应用于不同规模语言模型的剪枝方法是一个关键问题。

**核心思路**：COMPACT的核心思路是联合优化词表剪枝和FFN通道剪枝。通过剪枝低频词汇来减小embedding层和LM head的大小，同时利用common-token-weighted activations来指导FFN中间层的通道剪枝。这种联合优化使得剪枝过程能够更好地适应剪枝后的token分布，从而在保持模型性能的同时，减少参数量和计算量。

**技术框架**：COMPACT方法包含两个主要阶段：词表剪枝和FFN通道剪枝。首先，根据词汇的频率进行剪枝，移除低频词汇，从而减小embedding层和LM head的大小。然后，利用common-token-weighted activations来评估FFN中间层通道的重要性，并剪枝不重要的通道。整个过程保持了标准的Transformer架构，无需定制化的推理代码。

**关键创新**：COMPACT的关键创新在于联合优化词表剪枝和FFN通道剪枝，并利用common-token-weighted activations来指导FFN通道剪枝。与传统的独立剪枝方法相比，COMPACT能够更好地适应剪枝后的token分布，从而在保持模型性能的同时，实现更高的压缩率。此外，COMPACT方法保持了标准的Transformer架构，避免了定制化推理代码的需求。

**关键设计**：在词表剪枝方面，需要确定一个合适的词汇频率阈值，低于该阈值的词汇将被移除。在FFN通道剪枝方面，common-token-weighted activations的计算方式是关键。具体来说，对于每个通道，计算其对常见token的激活值的加权平均，权重可以是token的频率或其他重要性指标。然后，根据这些加权平均值对通道进行排序，并剪枝不重要的通道。损失函数方面，可以使用标准的语言模型损失函数，并在剪枝过程中加入正则化项，以鼓励稀疏性。

## 📊 实验亮点

实验结果表明，COMPACT在Qwen、LLaMA和Gemma等多个模型家族（0.5B-70B）上实现了最先进的下游性能。例如，在保持相似性能的前提下，COMPACT能够显著减少参数量、GPU内存占用和推理延迟。具体的性能提升数据在论文中详细展示，并与现有的剪枝方法进行了对比。

## 🎯 应用场景

COMPACT方法可应用于各种需要高效部署语言模型的场景，例如边缘设备上的自然语言处理、移动应用中的智能助手、以及大规模在线服务的低延迟推理。通过降低模型大小和计算复杂度，COMPACT能够显著降低部署成本，提高用户体验，并促进可持续的AI发展。

## 📄 摘要（原文）

> Making large language models (LLMs) more efficient in memory, latency, and serving cost is crucial for edge deployment, interactive applications, and sustainable inference at scale. Pruning is a promising technique, but existing pruning methods are limited: width pruning often breaks the standard transformer layout, requiring custom inference code, while depth pruning can cause abrupt accuracy drops. Also, while many pruning approaches are effective against LLMs, they struggle to maintain performance on small language models (SLMs). In this work, we propose COMPACT, which jointly (i) prunes rare vocabulary to shrink embedding/LM head layers and (ii) prunes FFN intermediate channels using common-token-weighted activations, aligning importance with the post-pruning token distribution. COMPACT inherits strengths of both depth and width pruning, such as: deployment-friendliness (keeps a standard transformer architecture), scale-adaptivity (trade off vocab. vs. FFN pruning), competitive pruning times, and strong memory savings alongside throughput gains. Experiments across Qwen, LLaMA, and Gemma families (0.5B-70B) show state-of-the-art downstream performance, with substantial reductions in parameters, GPU memory, and latency.

