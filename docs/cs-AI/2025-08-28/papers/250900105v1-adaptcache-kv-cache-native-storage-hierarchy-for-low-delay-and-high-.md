---
layout: default
title: "AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving"
---

# AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00105" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00105v1</a>
  <a href="https://arxiv.org/pdf/2509.00105.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00105v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00105v1', 'AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaoting Feng, Hanchen Li, Kuntai Du, Zhuohan Gu, Yuhan Liu, Jiayi Yao, Siddhant Ray, Samuel Shen, Yihua Cheng, Ganesh Ananthanarayanan, Junchen Jiang

**分类**: cs.OS, cs.AI, cs.LG

**发布日期**: 2025-08-28

---

## 💡 一句话要点

**提出AdaptCache以解决LLM服务中的KV缓存延迟问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `KV缓存` `有损压缩` `延迟优化` `生成质量` `动态策略` `智能服务`

## 📋 核心要点

1. 现有LLM服务系统在处理上下文时存在冗余计算，导致KV缓存的加载延迟较高，影响服务效率。
2. 本文提出AdaptCache，通过有损压缩技术优化KV缓存的存储和加载策略，以提高DRAM命中率。
3. 实验结果表明，AdaptCache在延迟和生成质量上均显著优于现有静态压缩方法，提升幅度可达55%。

## 📝 摘要（中文）

大型语言模型（LLM）应用通常会重用先前处理的上下文，如聊天记录和文档，这导致了显著的冗余计算。现有的LLM服务系统通过存储已处理上下文的KV缓存来解决这一问题。然而，随着LLM应用的扩展，KV缓存的总大小变得过于庞大，需同时使用DRAM和SSD进行存储。以往将KV缓存存储在DRAM和SSD中的方法存在高加载延迟的问题，主要是因为大多数KV缓存命中来自SSD，加载速度较慢。为提高DRAM中的KV缓存命中率，本文提出了一种有损KV缓存压缩的方法，旨在最大化DRAM命中率并最小化加载延迟，同时不显著降低生成质量。与多种静态压缩基线相比，AdaptCache在相同质量下实现了1.43至2.4倍的延迟节省，并在相同延迟下提高了6%至55%的质量。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型服务中KV缓存的高延迟问题。现有方法在DRAM和SSD中存储KV缓存，导致加载延迟较高，影响服务效率。

**核心思路**：提出了一种有损KV缓存压缩系统，动态选择压缩算法、压缩率和设备放置，以最大化DRAM命中率并最小化加载延迟，同时保持生成质量。

**技术框架**：系统主要包括KV缓存管理模块、压缩决策模块和加载优化模块。KV缓存管理模块负责缓存的存储和检索，压缩决策模块根据上下文特征选择合适的压缩策略，加载优化模块则负责高效加载缓存。

**关键创新**：AdaptCache的创新在于其动态压缩策略，能够根据不同KV缓存条目的特性进行优化，与传统静态压缩方法相比，显著提高了缓存命中率和降低了延迟。

**关键设计**：系统设计中考虑了压缩算法的选择、压缩率的调整以及存储设备的合理分配等关键参数，以确保在不显著降低生成质量的前提下，最大化性能提升。

## 📊 实验亮点

实验结果显示，AdaptCache在延迟方面实现了1.43至2.4倍的节省，同时在相同延迟条件下，生成质量提升了6%至55%。与多种静态压缩基线相比，表现出显著的优势，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、在线教育和实时翻译等需要高效处理大量上下文的LLM应用。通过优化KV缓存的存储和加载，AdaptCache能够显著提升系统响应速度和用户体验，具有广泛的实际价值和应用前景。

## 📄 摘要（原文）

> Large language model (LLM) applications often reuse previously processed context, such as chat history and documents, which introduces significant redundant computation. Existing LLM serving systems address such redundant computation by storing the KV caches of processed context and loading the corresponding KV cache when a new request reuses the context. Further, as these LLM applications scale, the total size of KV caches becomes excessively large and requires both DRAM and SSD for full storage.
>   However, prior work that stores KV caches in DRAM and SSD suffers from high loading delays, as most KV cache hits come from SSD, which is slow to load. To increase the KV cache hit rate on DRAM, we identify lossy KV cache compression as a promising approach. We design a lossy compression system that decides the compression algorithm, compression rate and device placement for each KV cache entry to maximise DRAM hits and minimise loading delay without significantly degrading generation quality. Compared to various static compression baselines across three tasks, our system AdaptCache achieves 1.43--2.4 x delay savings at the same quality and 6--55% quality improvements at the same delay.

