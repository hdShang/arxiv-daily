---
layout: default
title: EFIM: Efficient Serving of LLMs for Infilling Tasks with Improved KV Cache Reuse
---

# EFIM: Efficient Serving of LLMs for Infilling Tasks with Improved KV Cache Reuse

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21889" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21889v2</a>
  <a href="https://arxiv.org/pdf/2505.21889.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21889v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21889v2', 'EFIM: Efficient Serving of LLMs for Infilling Tasks with Improved KV Cache Reuse')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyu Guo, Hande Dong, Yichong Leng, Feng Liu, Cheater Lin, Nong Xiao, Xianwei Zhang

**分类**: cs.CL

**发布日期**: 2025-05-28 (更新: 2025-05-29)

**备注**: 31st International European Conference on Parallel and Distributed Computing (Euro-Par 2025 Oral)

**🔗 代码/项目**: [GITHUB](https://github.com/gty111/EFIM)

---

## 💡 一句话要点

**提出EFIM以解决LLMs在填充任务中的KV缓存重用问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `KV缓存重用` `填充任务` `片段标记化` `自然语言处理` `实时交互服务`

## 📋 核心要点

1. 现有的KV缓存重用方法在填充任务中受到提示格式结构的限制，导致效率低下。
2. 本文提出EFIM，通过转化提示格式来优化KV缓存重用，同时引入片段标记化训练方法解决生成部分单词的问题。
3. 实验结果显示，EFIM显著降低了52%的延迟，并提高了98%的吞吐量，保持了填充能力。

## 📝 摘要（中文）

大型语言模型（LLMs）常用于填充任务，即预测或生成给定文本中的缺失信息。这些任务通常需要多次与相似上下文的交互。为了减少重复历史标记的计算，跨请求的键值（KV）缓存重用成为多轮交互服务中的关键方法。然而，在填充任务中，KV缓存重用常因提示格式的结构而受阻。为了解决这一问题，本文提出了EFIM，一种转化的提示格式，旨在释放KV缓存重用的性能潜力。尽管转化的提示可以解决效率问题，但也暴露了当前LLMs在生成部分单词时的困难。因此，本文引入了一种片段标记化训练方法，在数据处理过程中将文本分割为多个片段。实验表明，使用EFIM的LLM服务可以将延迟降低52%，并提高吞吐量98%，同时保持原有的填充能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在填充任务中KV缓存重用效率低下的问题。现有方法在提示格式的结构上存在局限，导致缓存无效化，影响性能。

**核心思路**：提出EFIM，通过转化提示格式来优化KV缓存的重用，进而提高多轮交互服务的效率。同时，针对当前LLMs在生成部分单词时的困难，引入片段标记化训练方法。

**技术框架**：整体架构包括两个主要模块：转化提示格式和片段标记化训练。转化提示格式旨在优化KV缓存的使用，而片段标记化训练则在数据处理阶段将文本分割为多个片段，以提高生成的准确性。

**关键创新**：最重要的技术创新在于EFIM的提示格式转化，能够有效释放KV缓存重用的潜力，同时解决了当前LLMs在生成部分单词时的不足。这一创新与现有方法的本质区别在于其结构优化和训练方法的结合。

**关键设计**：在片段标记化训练中，文本被分割为多个片段进行处理，确保生成的准确性。此外，模型的参数设置和损失函数设计也经过优化，以适应新的提示格式和训练方法。

## 📊 实验亮点

实验结果表明，使用EFIM的LLM服务在延迟方面降低了52%，吞吐量提高了98%。这些显著的性能提升展示了EFIM在填充任务中的有效性，保持了原有的填充能力，具有较强的竞争优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的文本生成、对话系统以及智能助手等场景。通过提高LLMs在填充任务中的效率，EFIM能够为实时交互服务提供更好的支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) are often used for infilling tasks, which involve predicting or generating missing information in a given text. These tasks typically require multiple interactions with similar context. To reduce the computation of repeated historical tokens, cross-request key-value (KV) cache reuse, a technique that stores and reuses intermediate computations, has become a crucial method in multi-round interactive services. However, in infilling tasks, the KV cache reuse is often hindered by the structure of the prompt format, which typically consists of a prefix and suffix relative to the insertion point. Specifically, the KV cache of the prefix or suffix part is frequently invalidated as the other part (suffix or prefix) is incrementally generated. To address the issue, we propose EFIM, a transformed prompt format of FIM to unleash the performance potential of KV cache reuse. Although the transformed prompt can solve the inefficiency, it exposes subtoken generation problems in current LLMs, where they have difficulty generating partial words accurately. Therefore, we introduce a fragment tokenization training method which splits text into multiple fragments before tokenization during data processing. Experiments on two representative LLMs show that LLM serving with EFIM can lower the latency by 52% and improve the throughput by 98% while maintaining the original infilling capability. EFIM's source code is publicly available at https://github.com/gty111/EFIM.

