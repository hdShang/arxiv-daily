---
layout: default
title: "Spotlight Attention: Towards Efficient LLM Generation via Non-linear Hashing-based KV Cache Retrieval"
---

# Spotlight Attention: Towards Efficient LLM Generation via Non-linear Hashing-based KV Cache Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19740" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19740v4</a>
  <a href="https://arxiv.org/pdf/2508.19740.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19740v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19740v4', 'Spotlight Attention: Towards Efficient LLM Generation via Non-linear Hashing-based KV Cache Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhao Li, Yuxin Zhang, Gen Luo, Haiyuan Wan, Ziyang Gong, Fei Chao, Rongrong Ji

**分类**: cs.CL

**发布日期**: 2025-08-27 (更新: 2025-10-09)

---

## 💡 一句话要点

**提出Spotlight Attention以解决LLM生成中的KV缓存效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `键值缓存` `非线性哈希` `推理效率` `CUDA优化` `Bradley-Terry损失` `检索精度` `深度学习`

## 📋 核心要点

1. 现有方法在动态选择KV缓存时效率低下，无法有效应对LLMs中的查询和键的正交分布问题。
2. 论文提出Spotlight Attention，通过非线性哈希函数优化查询和键的嵌入分布，从而提高编码效率和鲁棒性。
3. 实验结果显示，Spotlight Attention在检索精度上有显著提升，哈希码长度缩短至少5倍，且在A100 GPU上实现了高效的检索速度。

## 📝 摘要（中文）

减少大型语言模型（LLMs）中的键值（KV）缓存负担显著加速推理过程。动态选择解码过程中关键的KV缓存有助于保持性能。现有方法使用随机线性哈希来识别重要的token，但由于LLMs中查询和键在两个狭窄锥体内的正交分布，这种方法效率低下。我们提出了Spotlight Attention，这是一种新颖的方法，采用非线性哈希函数优化查询和键的嵌入分布，从而增强编码效率和鲁棒性。实验结果表明，Spotlight Attention在提高检索精度的同时，将哈希码长度缩短至少5倍，相较于传统线性哈希，具有显著优势。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型中KV缓存的效率问题。现有的随机线性哈希方法在处理查询和键的正交分布时表现不佳，导致性能下降。

**核心思路**：我们提出Spotlight Attention，通过非线性哈希函数优化查询和键的嵌入分布，旨在提高KV缓存的检索效率和鲁棒性。此设计能够更好地适应LLMs的特性，克服传统方法的局限。

**技术框架**：整体架构包括非线性哈希模块和基于Bradley-Terry排名的损失函数。该框架支持在16GB内存的GPU上进行高效训练，训练时间约为8小时。

**关键创新**：最重要的技术创新在于采用非线性哈希函数，显著提升了检索精度，并将哈希码长度缩短至少5倍，相较于传统的线性哈希方法具有本质区别。

**关键设计**：损失函数采用Bradley-Terry排名机制，优化了非线性哈希模块的训练过程。此外，使用专门的CUDA内核实现了512K tokens的快速检索，检索时间低于100微秒，整体吞吐量比传统解码高出3倍。

## 📊 实验亮点

实验结果表明，Spotlight Attention在检索精度上有显著提升，哈希码长度缩短至少5倍。使用专门的CUDA内核，512K tokens的检索时间低于100微秒，整体吞吐量比传统解码提高了3倍，展现出优越的性能。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过提高LLMs的推理效率，Spotlight Attention能够在实时应用中提供更快的响应时间，提升用户体验。未来，该方法可能推动更大规模模型的应用，降低计算资源消耗。

## 📄 摘要（原文）

> Reducing the key-value (KV) cache burden in Large Language Models (LLMs) significantly accelerates inference. Dynamically selecting critical KV caches during decoding helps maintain performance. Existing methods use random linear hashing to identify important tokens, but this approach is inefficient due to the orthogonal distribution of queries and keys within two narrow cones in LLMs. We introduce Spotlight Attention, a novel method that employs non-linear hashing functions to optimize the embedding distribution of queries and keys, enhancing coding efficiency and robustness. We also developed a lightweight, stable training framework using a Bradley-Terry ranking-based loss, enabling optimization of the non-linear hashing module on GPUs with 16GB memory in 8 hours. Experimental results show that Spotlight Attention drastically improves retrieval precision while shortening the length of the hash code at least 5$\times$ compared to traditional linear hashing. Finally, we exploit the computational advantages of bitwise operations by implementing specialized CUDA kernels, achieving hashing retrieval for 512K tokens in under 100$μ$s on a single A100 GPU, with end-to-end throughput up to 3$\times$ higher than vanilla decoding.

