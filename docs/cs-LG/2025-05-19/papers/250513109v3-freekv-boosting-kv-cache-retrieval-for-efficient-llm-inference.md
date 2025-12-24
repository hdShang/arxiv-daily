---
layout: default
title: FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference
---

# FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13109" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13109v3</a>
  <a href="https://arxiv.org/pdf/2505.13109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13109v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13109v3', 'FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangda Liu, Chengwei Li, Zhenyu Ning, Jing Lin, Yiwu Yao, Danning Ke, Minyi Guo, Jieru Zhao

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-19 (更新: 2025-12-16)

---

## 💡 一句话要点

**提出FreeKV以解决长上下文KV缓存检索效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `KV缓存` `检索效率` `推测性检索` `算法优化` `系统设计` `双缓冲技术`

## 📋 核心要点

1. 长上下文的KV缓存增长导致大型语言模型的部署面临显著挑战，现有方法在效率和准确性之间难以平衡。
2. FreeKV通过推测性检索和细粒度校正，优化KV选择和回忆过程，提升检索效率并保持准确性。
3. 实验结果显示，FreeKV在多种场景下实现了近乎无损的准确性，并与现有方法相比，速度提升可达13倍。

## 📝 摘要（中文）

大型语言模型（LLMs）在支持日益复杂的应用时，面临着长上下文带来的显著挑战，尤其是KV缓存的大小随上下文长度成比例增长。尽管已有KV缓存压缩方法，但KV丢弃方法会导致显著的准确性损失，而KV检索方法则存在效率瓶颈。为此，本文提出了FreeKV，一个算法-系统协同优化框架，旨在提高KV检索效率并保持准确性。FreeKV在算法层面引入了推测性检索，将KV选择和回忆过程移出关键路径，并结合细粒度校正以确保准确性。在系统层面，FreeKV采用跨CPU和GPU内存的混合KV布局，消除数据传输碎片，并利用双缓冲流式回忆进一步提升效率。实验表明，FreeKV在各种场景和模型中实现了近乎无损的准确性，相较于现有最先进的KV检索方法，速度提升可达13倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长上下文下KV缓存检索效率低下的问题。现有的KV丢弃方法会导致准确性显著下降，而KV检索方法则面临效率瓶颈，难以满足实际应用需求。

**核心思路**：FreeKV的核心思路是通过推测性检索将KV选择和回忆过程移出关键路径，从而提高检索效率，同时结合细粒度校正以确保模型的准确性。这样的设计旨在减少检索过程中的延迟，提升整体性能。

**技术框架**：FreeKV的整体架构包括算法层和系统层。在算法层，采用推测性检索和细粒度校正；在系统层，使用混合KV布局和双缓冲流式回忆，以优化内存使用和数据传输效率。

**关键创新**：FreeKV的主要创新在于其算法-系统协同优化的框架，通过将KV检索过程的关键路径外移，显著提升了检索效率，并保持了高准确性。这与传统方法在效率和准确性之间的权衡形成鲜明对比。

**关键设计**：在设计中，FreeKV采用了混合KV布局以优化CPU和GPU内存的使用，减少数据传输的碎片化。同时，双缓冲流式回忆技术的引入进一步提升了检索效率，确保了在高负载情况下的稳定性能。

## 📊 实验亮点

实验结果表明，FreeKV在多种场景下实现了近乎无损的准确性，相较于现有最先进的KV检索方法，速度提升可达13倍。这一显著的性能提升展示了FreeKV在实际应用中的巨大潜力。

## 🎯 应用场景

FreeKV的研究成果具有广泛的应用潜力，尤其是在需要处理长上下文的自然语言处理任务中，如对话系统、文本生成和信息检索等领域。其高效的KV检索方法能够显著提升大型语言模型的响应速度和准确性，推动智能助手和自动化系统的进一步发展。

## 📄 摘要（原文）

> Large language models (LLMs) have been widely deployed with rapidly expanding context windows to support increasingly demanding applications. However, long contexts pose significant deployment challenges, primarily due to the KV cache whose size grows proportionally with context length. While KV cache compression methods are proposed to address this issue, KV dropping methods incur considerable accuracy loss, and KV retrieval methods suffer from significant efficiency bottlenecks. We propose FreeKV, an algorithm-system co-optimization framework to enhance KV retrieval efficiency while preserving accuracy. On the algorithm side, FreeKV introduces speculative retrieval to shift the KV selection and recall processes out of the critical path, combined with fine-grained correction to ensure accuracy. On the system side, FreeKV employs hybrid KV layouts across CPU and GPU memory to eliminate fragmented data transfers, and leverages double-buffered streamed recall to further improve efficiency. Experiments demonstrate that FreeKV achieves near-lossless accuracy across various scenarios and models, delivering up to 13$\times$ speedup compared to SOTA KV retrieval methods.

