---
layout: default
title: "RT-Cache: Training-Free Retrieval for Real-Time Manipulation"
---

# RT-Cache: Training-Free Retrieval for Real-Time Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09040" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09040v3</a>
  <a href="https://arxiv.org/pdf/2505.09040.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09040v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09040v3', 'RT-Cache: Training-Free Retrieval for Real-Time Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Owen Kwon, Abraham George, Alison Bartsch, Amir Barati Farimani

**分类**: cs.RO, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-05-14 (更新: 2025-08-25)

**备注**: 8 pages, 6 figures. 2025 IEEE-RAS 24th International Conference on Humanoid Robots

**🔗 代码/项目**: [PROJECT_PAGE](https://rt-cache.github.io/)

---

## 💡 一句话要点

**提出RT-Cache以解决实时操作中的训练需求问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实时控制` `无训练检索` `机器人操作` `向量内存` `分层搜索` `多步动作重放` `智能制造`

## 📋 核心要点

1. 现有方法在新环境中重复行为时，通常需要大量的推理计算或微调，导致实时控制的效率低下。
2. RT-Cache通过缓存多样的图像动作轨迹，利用检索机制替代每步模型调用，实现无训练的控制。
3. 实验表明，RT-Cache在真实机器人任务中成功率提高约2倍，完成时间减少约30%，显示出显著的性能提升。

## 📝 摘要（中文）

真实机器人在新环境中重复相同行为时，往往需要极少的新数据。然而，现代控制器通常面临每步推理开销大或需在部署时进行微调的问题。本文提出RT-Cache，这是一种无训练的检索控制管道，通过在统一的向量内存中缓存多样的图像动作轨迹，在测试时嵌入当前帧以检索和重放多步片段，从而替代每步模型调用。分层搜索使得在百万规模下的查找保持在亚秒级，降低了计算成本，支持在中等性能GPU上实现实时控制。在真实机器人任务和大型开放日志中，RT-Cache的成功率比强基线高出约2倍，完成时间快约30%。

## 🔬 方法详解

**问题定义**：本文解决的问题是如何在新环境中实现真实机器人的高效重复行为，现有方法在此过程中面临高计算开销和微调需求的挑战。

**核心思路**：RT-Cache的核心思路是通过缓存多样的图像动作轨迹，利用检索机制在测试时快速重放多步动作，避免了每步都调用模型的高成本。

**技术框架**：RT-Cache的整体架构包括统一的向量内存用于存储动作轨迹，分层搜索机制用于快速检索，以及嵌入当前帧以获取相关动作片段的流程。

**关键创新**：RT-Cache的主要创新在于将经验转化为仅追加的内存结构，显著降低了计算需求，同时实现了实时控制，区别于传统需要大量推理的控制方法。

**关键设计**：关键设计包括高效的向量内存管理、分层搜索算法的实现，以及在检索过程中对当前帧的嵌入方式，这些设计确保了系统在百万规模下的快速响应。

## 📊 实验亮点

实验结果显示，RT-Cache在真实机器人任务中成功率提高约2倍，完成时间减少约30%。与强基线相比，RT-Cache在性能上表现出显著优势，证明了其在实时控制中的有效性。

## 🎯 应用场景

RT-Cache的研究成果在机器人操作、自动化控制和智能制造等领域具有广泛的应用潜力。其无训练的特性使得机器人能够快速适应新环境，降低了部署成本和时间，未来可能推动更复杂任务的实时控制能力。

## 📄 摘要（原文）

> Real robots are expected to repeat the same behavior in new environments with very little new data, yet modern controllers either incur heavy per-step inference or require deployment-time fine-tuning. We propose RT-Cache, a training-free retrieval-as-control pipeline that caches diverse image action trajectories in a unified vector memory and, at test time, embeds the current frame to retrieve and replay multi-step snippets, replacing per-step model calls. A hierarchical search keeps lookups sub-second at million scale, shifting cost from compute to storage and enabling real-time control on modest GPUs. Across real-robot tasks and large open logs, RT-Cache achieves higher success and lower completion time than strong retrieval baselines (approximately x2 higher success and ~30% faster in our settings), and a single-episode anchoring study shows immediate adaptation to a more complex, contact-rich task without fine-tuning. RT-Cache turns experience into an append-only memory, offering a simple, scalable path to few-shot deployment today and a foundation for multimodal keys and optional integration with high-level policies. Project page: https://rt-cache.github.io/.

