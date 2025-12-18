---
layout: default
title: Dynamic Rebatching for Efficient Early-Exit Inference with DREX
---

# Dynamic Rebatching for Efficient Early-Exit Inference with DREX

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15705" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15705v1</a>
  <a href="https://arxiv.org/pdf/2512.15705.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15705v1" onclick="toggleFavorite(this, '2512.15705v1', 'Dynamic Rebatching for Efficient Early-Exit Inference with DREX')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuting Liu, Daniel Alexander, Siva Kesava Reddy Kakarla, Behnaz Arzani, Vincent Liu

**分类**: cs.DC, cs.LG

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出动态重批处理以解决早期退出推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `早期退出推理` `动态重批处理` `大型语言模型` `推理效率` `输出质量` `调度优化` `内存管理`

## 📋 核心要点

1. 现有的早期退出推理方法在批处理时无法有效利用不同请求的退出时机，导致效率低下。
2. 本文提出动态重批处理方法，通过在每个早期退出点动态重组批次，优化了推理过程。
3. DREX系统在实验中显示出2-12%的吞吐量提升，同时保持了输出质量，消除了非自愿退出现象。

## 📝 摘要（中文）

早期退出（EE）是一种大型语言模型（LLM）架构，通过仅使用模型的一部分层来加速推理。然而，传统的批处理框架不适合EE LLM，因为批次中的请求可能无法同时满足退出条件。现有解决方案要么强制对批次做出统一决策，忽视EE机会，要么通过强制提前退出降低输出质量。本文提出动态重批处理，在每个早期退出点动态重组批次，满足退出条件的请求立即处理，未满足的请求则被缓冲并重新分组。我们引入DREX，一个实现动态重批处理的早期退出推理系统，具有两个关键优化：1）无拷贝重批处理缓冲区，避免物理数据移动；2）EE和SLA感知调度器，分析预测重批处理操作的收益。实验表明，DREX的吞吐量比基线方法提高了2-12%，同时保持输出质量，完全消除了非自愿退出，确保了EE模型的输出质量。

## 🔬 方法详解

**问题定义**：本文解决的问题是如何在早期退出推理中有效利用批处理，现有方法无法同时满足不同请求的退出条件，导致效率低下和输出质量下降。

**核心思路**：论文提出动态重批处理的核心思路是，在每个早期退出点动态重组批次，满足退出条件的请求立即处理，而未满足的请求则被缓冲并重新分组，以提高推理效率。

**技术框架**：DREX系统的整体架构包括动态重批处理模块、无拷贝重批处理缓冲区和EE及SLA感知调度器。动态重批处理模块负责在每个退出点重组请求，调度器则根据预测分析重批处理的收益。

**关键创新**：DREX的关键创新在于引入无拷贝重批处理缓冲区，避免了物理数据移动，同时通过EE和SLA感知调度器优化了重批处理的决策过程，这与现有方法的静态批处理方式形成了鲜明对比。

**关键设计**：DREX的设计中，重批处理缓冲区采用无拷贝策略，减少了内存开销；调度器通过分析历史数据和当前请求状态，预测重批处理的收益，从而做出更智能的调度决策。实验中还使用了内存高效的状态拷贝技术来处理跳过层的KV缓存。

## 📊 实验亮点

实验结果显示，DREX在吞吐量上比基线方法提高了2-12%，同时完全消除了非自愿退出现象，确保了输出质量。这一成果表明，动态重批处理在早期退出推理中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和实时翻译等需要高效推理的场景。通过提高推理效率和保持输出质量，DREX能够在实际应用中显著提升用户体验，推动大型语言模型的广泛应用。

## 📄 摘要（原文）

> Early-Exit (EE) is a Large Language Model (LLM) architecture that accelerates inference by allowing easier tokens to be generated using only a subset of the model's layers. However, traditional batching frameworks are ill-suited for EE LLMs, as not all requests in a batch may be ready to exit at the same time. Existing solutions either force a uniform decision on the batch, which overlooks EE opportunities, or degrade output quality by forcing premature exits. We propose Dynamic Rebatching, a solution where we dynamically reorganize the batch at each early-exit point. Requests that meet the exit criteria are immediately processed, while those that continue are held in a buffer, re-grouped into a new batch, and forwarded to deeper layers. We introduce DREX, an early-exit inference system that implements Dynamic Rebatching with two key optimizations: 1) a copy-free rebatching buffer that avoids physical data movement, and 2) an EE and SLA-aware scheduler that analytically predicts whether a given rebatching operation will be profitable. DREX also efficiently handles the missing KV cache from skipped layers using memory-efficient state-copying. Our evaluation shows that DREX improves throughput by 2-12% compared to baseline approaches while maintaining output quality. Crucially, DREX completely eliminates involuntary exits, providing a key guarantee for preserving the output quality intended by the EE model.

