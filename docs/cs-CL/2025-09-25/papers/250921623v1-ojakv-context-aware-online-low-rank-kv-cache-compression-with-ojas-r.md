---
layout: default
title: "OjaKV: Context-Aware Online Low-Rank KV Cache Compression with Oja's Rule"
---

# OjaKV: Context-Aware Online Low-Rank KV Cache Compression with Oja's Rule

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21623" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21623v1</a>
  <a href="https://arxiv.org/pdf/2509.21623.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21623v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21623v1', 'OjaKV: Context-Aware Online Low-Rank KV Cache Compression with Oja\'s Rule')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Zhu, David H. Yang, Mohammad Mohammadi Amiri, Keerthiram Murugesan, Tejaswini Pedapati, Pin-Yu Chen

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**OjaKV：利用Oja规则进行上下文感知在线低秩KV缓存压缩，提升长文本处理效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `KV缓存压缩` `低秩近似` `在线学习` `长文本处理` `Oja规则` `上下文感知` `大型语言模型`

## 📋 核心要点

1. 现有KV缓存压缩方法依赖静态离线学习的子空间，无法适应长文本中动态变化的上下文信息，导致性能下降。
2. OjaKV采用混合存储策略和在线子空间自适应，对重要token全秩保留，中间token进行低秩压缩，并使用Oja算法动态调整投影基。
3. 实验表明，OjaKV在高压缩比下保持甚至提高了zero-shot准确率，尤其在长文本推理任务中表现出色，无需模型微调。

## 📝 摘要（中文）

大型语言模型不断扩展的长上下文处理能力受到显著的内存瓶颈限制：自回归生成所需的键值(KV)缓存。这种瓶颈非常严重；例如，一个Llama-3.1-8B模型处理一个32K token的prompt，batch size为4时，其KV缓存需要大约16GB，超过了模型本身的权重。虽然通过低秩投影进行KV缓存压缩是一个有希望的方向，但现有方法依赖于静态的、离线学习的子空间，在数据分布发生变化时表现不佳。为了克服这些限制，我们引入了OjaKV，这是一个新颖的框架，它将战略性的混合存储策略与在线子空间自适应相结合。首先，OjaKV认识到并非所有token对于压缩都同等重要；它以全秩保留关键的第一个和最近的token，为注意力机制维护高保真度的锚点。其次，对于绝大多数中间token，它通过使用Oja算法进行在线主成分分析来增量地调整投影基，从而应用低秩压缩。这种自适应包括在prompt预填充期间的全面更新和在解码期间的轻量级周期性更新，确保子空间与不断变化的上下文保持一致。至关重要的是，我们的框架与现代注意力模块（如FlashAttention）完全兼容。实验表明，OjaKV在高压缩比下保持甚至提高了zero-shot准确率。特别是，OjaKV在需要复杂推理的超长上下文基准测试中获得了最显著的收益，突出了在线子空间自适应在动态跟踪上下文变化中的重要性。这些结果表明，我们的混合框架是一种实用的、即插即用的解决方案，用于内存高效的长上下文推理，而无需模型微调。

## 🔬 方法详解

**问题定义**：大型语言模型处理长文本时，KV缓存占用大量内存，成为性能瓶颈。现有的低秩压缩方法依赖静态子空间，无法适应长文本中上下文的动态变化，导致压缩性能下降，影响模型准确率。

**核心思路**：OjaKV的核心思路是结合混合存储策略和在线子空间自适应。它认为并非所有token都同等重要，因此对关键token（如首个和最近的token）进行全秩保留，保证重要信息的完整性。对于中间token，则采用低秩压缩，并利用Oja算法进行在线更新，使压缩子空间能够动态适应上下文的变化。

**技术框架**：OjaKV框架包含以下主要模块：1) 混合存储策略：区分重要token和中间token，分别采用全秩存储和低秩压缩。2) 在线子空间自适应：使用Oja算法对低秩压缩的投影基进行在线更新，包括prompt预填充期间的全面更新和解码期间的轻量级周期性更新。3) 兼容性设计：与现代注意力模块（如FlashAttention）完全兼容，易于集成到现有系统中。

**关键创新**：OjaKV的关键创新在于其在线子空间自适应能力。与现有静态子空间方法不同，OjaKV能够根据上下文的动态变化，实时调整压缩子空间，从而更好地捕捉长文本中的信息。这种在线自适应能力是OjaKV在长文本推理任务中取得优异性能的关键。

**关键设计**：OjaKV的关键设计包括：1) 使用Oja算法进行在线主成分分析，以增量方式更新投影基。2) 采用混合存储策略，平衡压缩率和信息损失。3) 设计轻量级的周期性更新机制，降低计算开销，保证实时性。4) 框架设计保证与FlashAttention等现有加速技术的兼容性。

## 📊 实验亮点

OjaKV在长文本基准测试中表现出色，尤其在需要复杂推理的任务中获得了显著提升。实验表明，OjaKV在高压缩比下保持甚至提高了zero-shot准确率，证明了在线子空间自适应在动态跟踪上下文变化中的重要性。该方法无需模型微调，即可作为即插即用的解决方案，实现内存高效的长上下文推理。

## 🎯 应用场景

OjaKV可应用于各种需要处理长文本的场景，如长文档摘要、长篇小说生成、复杂问答系统等。通过降低KV缓存的内存占用，OjaKV能够提升大型语言模型在资源受限设备上的部署能力，并加速长文本推理过程，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> The expanding long-context capabilities of large language models are constrained by a significant memory bottleneck: the key-value (KV) cache required for autoregressive generation. This bottleneck is substantial; for instance, a Llama-3.1-8B model processing a 32K-token prompt at a batch size of 4 requires approximately 16GB for its KV cache, a size exceeding the model's weights. While KV-cache compression via low-rank projection is a promising direction, existing methods rely on a static, offline-learned subspace that performs poorly under data distribution shifts. To overcome these limitations, we introduce OjaKV, a novel framework that integrates a strategic hybrid storage policy with online subspace adaptation. First, OjaKV recognizes that not all tokens are equally important for compression; it preserves the crucial first and most recent tokens in full-rank, maintaining high-fidelity anchors for attention. Second, for the vast majority of intermediate tokens, it applies low-rank compression by incrementally adapting the projection basis using Oja's algorithm for online principal component analysis. This adaptation involves a comprehensive update during prompt prefilling and lightweight periodic updates during decoding, ensuring the subspace remains aligned with the evolving context. Crucially, our framework is fully compatible with modern attention modules like FlashAttention. Experiments demonstrate that OjaKV maintains or even improves zero-shot accuracy at high compression ratios. In particular, OjaKV achieves its strongest gains on very long-context benchmarks that require complex reasoning, highlighting the importance of online subspace adaptation in dynamically tracking context shifts. These results establish our hybrid framework as a practical, plug-and-play solution for memory-efficient long-context inference without requiring model fine-tuning.

