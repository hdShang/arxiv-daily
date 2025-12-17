---
layout: default
title: FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference
---

# FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13109" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13109</a>
  <a href="https://arxiv.org/pdf/2505.13109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13109" onclick="toggleFavorite(this, '2505.13109', 'FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangda Liu, Chengwei Li, Zhenyu Ning, Jing Lin, Yiwu Yao, Danning Ke, Minyi Guo, Jieru Zhao

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**FreeKV：通过增强KV缓存检索实现高效LLM推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `KV缓存` `LLM推理` `长上下文` `推测检索` `系统优化`

## 📋 核心要点

1. 长上下文LLM推理面临KV缓存过大的挑战，现有压缩方法损失精度，检索方法效率低。
2. FreeKV提出推测检索，将KV选择移出关键路径，并进行细粒度校正以保证准确性。
3. FreeKV通过混合KV布局和双缓冲流式召回，在算法和系统层面协同优化，提升效率。

## 📝 摘要（中文）

大型语言模型（LLMs）已被广泛部署，其上下文窗口迅速扩展，以支持日益增长的应用需求。然而，长上下文带来了显著的部署挑战，主要是由于KV缓存的大小与上下文长度成正比增长。虽然已经提出了KV缓存压缩方法来解决这个问题，但KV丢弃方法会导致相当大的精度损失，而KV检索方法则存在显著的效率瓶颈。我们提出了FreeKV，一个算法-系统协同优化框架，以提高KV检索效率，同时保持精度。在算法方面，FreeKV引入了推测检索，将KV选择和召回过程移出关键路径，并结合细粒度校正以确保精度。在系统方面，FreeKV采用跨CPU和GPU内存的混合KV布局，以消除碎片化的数据传输，并利用双缓冲流式召回进一步提高效率。实验表明，FreeKV在各种场景和模型中实现了接近无损的精度，与SOTA KV检索方法相比，速度提高了高达13倍。

## 🔬 方法详解

**问题定义**：论文旨在解决长上下文LLM推理中，KV缓存检索效率低下的问题。现有KV缓存压缩方法（如KV丢弃）会造成精度损失，而KV缓存检索方法则面临严重的效率瓶颈，限制了长上下文LLM的实际应用。

**核心思路**：FreeKV的核心思路是通过推测检索，将KV选择和召回过程从推理的关键路径中移除，从而减少延迟。同时，为了保证精度，引入了细粒度的校正机制，对推测检索的结果进行修正。此外，通过算法和系统层面的协同优化，进一步提升检索效率。

**技术框架**：FreeKV的整体框架包含以下几个主要模块：1) 推测检索模块：基于一定的策略（例如，历史访问频率）推测需要检索的KV对。2) 细粒度校正模块：对推测检索的结果进行校正，以减少误差。3) 混合KV布局模块：将KV缓存分布在CPU和GPU内存中，以减少数据传输的开销。4) 双缓冲流式召回模块：利用双缓冲技术，实现KV数据的流式召回，进一步提高效率。

**关键创新**：FreeKV的关键创新在于推测检索和细粒度校正的结合。传统的KV检索方法需要在推理的关键路径上进行KV选择和召回，而FreeKV通过推测检索将这些操作移出关键路径，从而显著减少延迟。同时，细粒度校正保证了精度，避免了因推测带来的误差。

**关键设计**：在推测检索方面，可以采用多种策略，例如基于历史访问频率、基于语义相似度等。细粒度校正可以采用多种方法，例如基于注意力机制的校正、基于残差连接的校正等。混合KV布局需要根据CPU和GPU的内存大小、带宽等因素进行优化。双缓冲流式召回需要合理设置缓冲区的大小，以平衡延迟和内存占用。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.13109/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.13109/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.13109/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，FreeKV在各种场景和模型中实现了接近无损的精度。与SOTA KV检索方法相比，FreeKV的速度提高了高达13倍。这些结果表明，FreeKV在提高KV缓存检索效率方面具有显著优势，能够有效解决长上下文LLM推理的瓶颈问题。

## 🎯 应用场景

FreeKV可应用于各种需要处理长上下文的LLM应用场景，例如长文本摘要、机器翻译、对话系统、代码生成等。通过提高KV缓存检索效率，FreeKV能够显著提升LLM的推理速度，降低部署成本，并支持更大规模的上下文窗口，从而拓展LLM的应用范围。未来，FreeKV有望成为长上下文LLM推理的重要加速技术。

## 📄 摘要（原文）

> Large language models (LLMs) have been widely deployed with rapidly expanding context windows to support increasingly demanding applications. However, long contexts pose significant deployment challenges, primarily due to the KV cache whose size grows proportionally with context length. While KV cache compression methods are proposed to address this issue, KV dropping methods incur considerable accuracy loss, and KV retrieval methods suffer from significant efficiency bottlenecks. We propose FreeKV, an algorithm-system co-optimization framework to enhance KV retrieval efficiency while preserving accuracy. On the algorithm side, FreeKV introduces speculative retrieval to shift the KV selection and recall processes out of the critical path, combined with fine-grained correction to ensure accuracy. On the system side, FreeKV employs hybrid KV layouts across CPU and GPU memory to eliminate fragmented data transfers, and leverages double-buffered streamed recall to further improve efficiency. Experiments demonstrate that FreeKV achieves near-lossless accuracy across various scenarios and models, delivering up to 13$\times$ speedup compared to SOTA KV retrieval methods.

