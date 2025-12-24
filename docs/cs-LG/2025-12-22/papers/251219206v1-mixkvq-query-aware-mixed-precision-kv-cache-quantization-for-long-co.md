---
layout: default
title: "MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning"
---

# MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19206" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19206v1</a>
  <a href="https://arxiv.org/pdf/2512.19206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19206v1', 'MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Zhang, Ziqian Zeng, Hao Peng, Huiping Zhuang, Cen Chen

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**MixKVQ：面向长文本推理的查询感知混合精度KV缓存量化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `KV缓存量化` `混合精度量化` `长文本推理` `大型语言模型` `查询感知` `低比特量化` `模型压缩`

## 📋 核心要点

1. 长文本推理对KV缓存造成巨大内存和延迟开销，现有低比特量化方法在复杂推理任务中性能下降明显。
2. MixKVQ提出一种查询感知的混合精度量化方法，根据键通道的量化难度和与查询的相关性自适应分配精度。
3. 实验表明，MixKVQ在复杂推理数据集上显著优于现有低比特方法，内存占用降低的同时性能接近全精度。

## 📝 摘要（中文）

长链思维（CoT）推理显著提升了大型语言模型（LLM）的能力，但同时也带来了巨大的内存和延迟开销，这主要源于庞大的键值（KV）缓存。KV缓存量化是一种有前景的压缩技术，但现有的低比特量化方法在复杂的推理任务上通常表现出严重的性能下降。固定精度量化难以处理键缓存中的异常通道，而当前的混合精度策略无法准确识别需要高精度表示的组件。我们发现，有效的低比特KV缓存量化策略必须考虑两个因素：键通道的内在量化难度及其与查询的相关性。基于此，我们提出了一种新颖的即插即用方法MixKVQ，它引入了一种轻量级的、查询感知的算法来识别和保留需要更高精度的关键键通道，同时对值缓存应用逐token量化。在复杂推理数据集上的实验表明，我们的方法显著优于现有的低比特方法，在显著降低内存占用的同时，实现了与全精度基线相当的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决长文本推理中，大型语言模型（LLM）因KV缓存过大而导致的内存和延迟问题。现有的低比特量化方法在复杂推理任务中性能下降严重，固定精度量化无法有效处理异常值，混合精度量化无法准确识别需要高精度的关键组件。

**核心思路**：论文的核心思路是提出一种查询感知的混合精度KV缓存量化方法，即MixKVQ。该方法认为，有效的低比特KV缓存量化需要同时考虑键通道的内在量化难度以及其与当前查询的相关性。通过查询感知的方式，可以更有针对性地对关键键通道分配更高的精度，从而在保证性能的同时降低内存占用。

**技术框架**：MixKVQ是一种即插即用的方法，可以方便地集成到现有的LLM框架中。其主要流程包括：1) 使用轻量级的查询感知算法来评估每个键通道的重要性；2) 根据重要性评估结果，对不同的键通道分配不同的量化精度；3) 对值缓存应用逐token量化。

**关键创新**：MixKVQ的关键创新在于引入了查询感知机制，能够动态地识别并保留对当前查询至关重要的键通道，并对这些通道使用更高的精度进行量化。这与传统的固定精度或静态混合精度量化方法有本质区别，后者无法根据查询动态调整量化策略。

**关键设计**：MixKVQ的关键设计包括：1) 轻量级的查询感知算法，用于评估键通道的重要性，具体实现细节未知；2) 混合精度量化策略，根据键通道的重要性自适应地分配量化比特数；3) 逐token的值缓存量化，进一步降低内存占用，具体量化方法未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19206v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19206v1/fig/Layer_0_Head_2_KV_Error_Heatmap.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19206v1/fig/quant_analysis_layer_0_combined_v3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MixKVQ在复杂推理数据集上显著优于现有的低比特量化方法，在大幅降低内存占用的同时，实现了与全精度基线相当的性能。具体的性能提升数据和对比基线未知，但摘要强调了其优越性。

## 🎯 应用场景

MixKVQ可应用于各种需要长文本推理的大型语言模型，例如智能问答、文本摘要、机器翻译等。通过降低KV缓存的内存占用和延迟，MixKVQ能够提升LLM在资源受限设备上的部署能力，并加速推理过程，具有重要的实际应用价值和广泛的应用前景。

## 📄 摘要（原文）

> Long Chain-of-Thought (CoT) reasoning has significantly advanced the capabilities of Large Language Models (LLMs), but this progress is accompanied by substantial memory and latency overhead from the extensive Key-Value (KV) cache. Although KV cache quantization is a promising compression technique, existing low-bit quantization methods often exhibit severe performance degradation on complex reasoning tasks. Fixed-precision quantization struggles to handle outlier channels in the key cache, while current mixed-precision strategies fail to accurately identify components requiring high-precision representation. We find that an effective low-bit KV cache quantization strategy must consider two factors: a key channel's intrinsic quantization difficulty and its relevance to the query. Based on this insight, we propose MixKVQ, a novel plug-and-play method that introduces a lightweight, query-aware algorithm to identify and preserve critical key channels that need higher precision, while applying per-token quantization for value cache. Experiments on complex reasoning datasets demonstrate that our approach significantly outperforms existing low-bit methods, achieving performance comparable to a full-precision baseline at a substantially reduced memory footprint.

