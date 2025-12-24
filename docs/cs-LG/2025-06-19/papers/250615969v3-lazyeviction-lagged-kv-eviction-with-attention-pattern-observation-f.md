---
layout: default
title: "LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning"
---

# LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15969" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15969v3</a>
  <a href="https://arxiv.org/pdf/2506.15969.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15969v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15969v3', 'LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyue Zhang, Hualei Zhang, Xiaosong Ma, Jie Zhang, Song Guo

**分类**: cs.LG, cs.CL

**发布日期**: 2025-06-19 (更新: 2025-10-15)

**🔗 代码/项目**: [GITHUB](https://github.com/Halo-949/LazyEviction)

---

## 💡 一句话要点

**提出LazyEviction以解决长推理任务中的KV缓存效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长推理` `KV缓存` `注意力机制` `内存优化` `语言模型`

## 📋 核心要点

1. 现有的KV缓存压缩方法在长推理任务中无法有效应对内存开销，导致性能下降。
2. LazyEviction通过观察令牌的重复模式，优先保留重要令牌，从而优化KV缓存的使用效率。
3. 实验结果显示LazyEviction在KV缓存减少50%至70%的同时，保持了与现有方法相当的准确性，表现优越。

## 📝 摘要（中文）

大型语言模型（LLMs）通过链式思维推理展现出增强的能力。然而，扩展的推理序列导致显著的GPU内存开销，主要由于增加的键值（KV）缓存。现有的KV缓存压缩方法虽然能够缓解内存瓶颈，但在长推理任务中表现不佳。本文分析了推理任务中的注意力模式，揭示了一个令牌重要性重复现象：大量令牌在多个解码步骤后重新获得高注意力，这一现象未被现有研究捕捉，可能导致周期性关键令牌的不可预测驱逐。为此，本文提出LazyEviction，一种基于观察窗口的延迟驱逐框架，通过基于令牌的重复模式优先驱逐来保留潜在的重复令牌。大量实验表明，LazyEviction将KV缓存减少了50%至70%，同时保持了相当的准确性，超越了现有的KV缓存压缩基线。

## 🔬 方法详解

**问题定义**：本文旨在解决长推理任务中KV缓存的效率问题，现有方法在处理周期性重要令牌时存在不可预测的驱逐现象，导致性能下降。

**核心思路**：LazyEviction的核心思想是通过观察令牌的注意力模式，识别并保留那些在多个解码步骤中重复获得高注意力的令牌，从而优化KV缓存的使用。

**技术框架**：LazyEviction的整体架构包括观察窗口、令牌重要性评估和优先驱逐机制。首先，通过观察窗口分析令牌的注意力模式，然后根据重要性评估决定哪些令牌应被保留或驱逐。

**关键创新**：LazyEviction的主要创新在于引入了令牌重要性重复现象的概念，并基于此设计了优先驱逐策略，与现有方法相比，能够更有效地管理KV缓存。

**关键设计**：在实现中，LazyEviction采用了动态观察窗口大小和自适应的驱逐策略，确保在不同推理任务中均能保持高效的KV缓存管理。

## 📊 实验亮点

实验结果表明，LazyEviction在KV缓存使用上减少了50%至70%，同时保持了与现有KV缓存压缩方法相当的准确性，显示出显著的性能提升，验证了其在长推理任务中的有效性。

## 🎯 应用场景

LazyEviction的研究成果在自然语言处理、对话系统和其他需要长推理的AI应用中具有广泛的潜在应用价值。通过优化内存使用，该方法能够提升模型的推理效率，降低硬件成本，推动更复杂任务的实现。

## 📄 摘要（原文）

> Large Language Models (LLMs) exhibit enhanced capabilities by Chain-of-Thought reasoning. However, the extended reasoning sequences introduce significant GPU memory overhead due to increased key-value (KV) cache. Existing KV cache compression methods mitigate memory bottlenecks but struggle in long reasoning tasks. In this paper, we analyze attention patterns in reasoning tasks and reveal a Token Importance Recurrence phenomenon: a large proportion of tokens regain high attention after multiple decoding steps, which is failed to capture by existing works and may lead to unpredictable eviction on such periodically critical tokens. To address this, we propose LazyEviction, an observation window-based lagged eviction framework retaining latent recurring tokens by prioritized eviction based on tokens' recurrence patterns. Extensive experiments demonstrate that LazyEviction reduces KV cache by 50%~70% while maintaining comparable accuracy, outperforming existing KV cache compression baselines. Our implementation code can be found at https://github.com/Halo-949/LazyEviction.

