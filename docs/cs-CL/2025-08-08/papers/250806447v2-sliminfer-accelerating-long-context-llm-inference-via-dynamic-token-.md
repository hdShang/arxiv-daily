---
layout: default
title: "SlimInfer: Accelerating Long-Context LLM Inference via Dynamic Token Pruning"
---

# SlimInfer: Accelerating Long-Context LLM Inference via Dynamic Token Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06447" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06447v2</a>
  <a href="https://arxiv.org/pdf/2508.06447.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06447v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06447v2', 'SlimInfer: Accelerating Long-Context LLM Inference via Dynamic Token Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingkun Long, Rubing Yang, Yushi Huang, Desheng Hui, Ao Zhou, Jianlei Yang

**分类**: cs.CL

**发布日期**: 2025-08-08 (更新: 2025-11-24)

**🔗 代码/项目**: [GITHUB](https://github.com/Longxmas/SlimInfer)

---

## 💡 一句话要点

**提出SlimInfer以加速长上下文LLM推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文推理` `动态修剪` `大型语言模型` `信息扩散` `推理加速` `内存优化` `KV缓存管理`

## 📋 核心要点

1. 现有方法在长上下文推理中效率低下，仍需处理完整的隐藏状态，导致计算资源浪费。
2. SlimInfer通过动态修剪不重要的提示token，利用信息扩散现象来提高推理速度和效率。
3. 实验结果显示，SlimInfer在不牺牲性能的前提下，显著提升了推理速度和延迟，具有良好的实用性。

## 📝 摘要（中文）

长上下文推理对于大型语言模型（LLMs）在计算需求上存在很大限制。尽管已有多种方法优化了注意力计算，但它们仍需在每一层处理完整的隐藏状态，限制了整体效率。本文提出了SlimInfer，一个创新框架，旨在通过在前向传播过程中动态修剪不重要的提示token来加速推理。我们的关键见解是信息扩散现象：随着关键信息在层间传播，它会分布在整个序列中。这一扩散过程表明，LLMs在隐藏状态中修剪过多的token（甚至包括这些关键token）时，仍能保持语义完整性。SlimInfer引入了一种动态细粒度修剪机制，准确去除中间层隐藏状态中的冗余token。实验表明，SlimInfer在单个RTX 4090上对LLaMA3.1-8B-Instruct实现了最高2.53倍的首次token响应时间加速和1.88倍的端到端延迟减少，同时在LongBench上保持了性能。

## 🔬 方法详解

**问题定义**：长上下文推理在大型语言模型中面临高计算需求的挑战，现有方法仍需处理完整的隐藏状态，导致效率低下和资源浪费。

**核心思路**：SlimInfer的核心思路是利用信息扩散现象，在前向传播过程中动态修剪不重要的提示token，从而提高推理效率。通过这种方式，模型能够在保持语义完整性的同时，减少计算负担。

**技术框架**：SlimInfer的整体架构包括动态细粒度修剪机制和异步KV缓存管理器。动态修剪机制在中间层准确去除冗余token，而KV缓存管理器则预取所需的token块，减少内存使用和I/O成本。

**关键创新**：SlimInfer的主要创新在于其动态修剪机制，能够在推理过程中实时识别并去除不重要的token。这与现有方法的静态修剪或全量处理方式形成了鲜明对比，显著提升了推理效率。

**关键设计**：在设计中，SlimInfer采用了细粒度的修剪策略，结合信息扩散理论，确保在修剪过程中不影响模型的语义理解。同时，设计了高效的KV缓存管理机制，以优化内存和I/O性能。

## 📊 实验亮点

SlimInfer在实验中实现了最高2.53倍的首次token响应时间加速和1.88倍的端到端延迟减少，表现出色。与LLaMA3.1-8B-Instruct的对比实验显示，该方法在保持性能的同时，显著提升了推理速度，具有良好的实用性和可扩展性。

## 🎯 应用场景

SlimInfer的研究成果在自然语言处理、对话系统和智能助手等领域具有广泛的应用潜力。通过提高长上下文推理的效率，SlimInfer能够支持更复杂的任务和更大规模的模型，推动智能应用的发展。未来，随着模型规模的不断扩大，该方法的实际价值将愈加显著。

## 📄 摘要（原文）

> Long-context inference for Large Language Models (LLMs) is heavily limited by high computational demands. While several existing methods optimize attention computation, they still process the full set of hidden states at each layer, limiting overall efficiency. In this work, we propose SlimInfer, an innovative framework that aims to accelerate inference by directly pruning less critical prompt tokens during the forward pass. Our key insight is an information diffusion phenomenon: As information from critical tokens propagates through layers, it becomes distributed across the entire sequence. This diffusion process suggests that LLMs can maintain their semantic integrity when excessive tokens, even including these critical ones, are pruned in hidden states. Motivated by this, SlimInfer introduces a dynamic fine-grained pruning mechanism that accurately removes redundant tokens of hidden state at intermediate layers. This layer-wise pruning naturally enables an asynchronous KV cache manager that prefetches required token blocks without complex predictors, reducing both memory usage and I/O costs. Extensive experiments show that SlimInfer can achieve up to $\mathbf{2.53\times}$ time-to-first-token (TTFT) speedup and $\mathbf{1.88\times}$ end-to-end latency reduction for LLaMA3.1-8B-Instruct on a single RTX 4090, without sacrificing performance on LongBench. Our code is available at https://github.com/Longxmas/SlimInfer.

