---
layout: default
title: "EVENT-Retriever: Event-Aware Multimodal Image Retrieval for Realistic Captions"
---

# EVENT-Retriever: Event-Aware Multimodal Image Retrieval for Realistic Captions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00751" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00751v1</a>
  <a href="https://arxiv.org/pdf/2509.00751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00751v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00751v1', 'EVENT-Retriever: Event-Aware Multimodal Image Retrieval for Realistic Captions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dinh-Khoi Vo, Van-Loc Nguyen, Minh-Triet Tran, Trung-Nghia Le

**分类**: cs.CV

**发布日期**: 2025-08-31

**备注**: ACM Multimedia 2025

**DOI**: [10.1145/3746027.3762038](https://doi.org/10.1145/3746027.3762038)

**🔗 代码/项目**: [GITHUB](https://github.com/vdkhoi20/EVENT-Retriever)

---

## 💡 一句话要点

**提出EVENT-Retriever以解决基于事件的多模态图像检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `事件感知` `语言模型` `图像理解` `信息检索` `深度学习` `上下文对齐`

## 📋 核心要点

1. 现有的视觉-语言检索方法在处理抽象事件和复杂叙述时表现不佳，难以理解潜在的事件语义和上下文。
2. 本文提出了一种多阶段检索框架，结合文章检索、语言模型重排序和图像评分，增强了检索的准确性和鲁棒性。
3. 系统在EVENTA 2025 Grand Challenge中取得了最高分，证明了其在复杂图像理解中的有效性和创新性。

## 📝 摘要（中文）

基于事件的图像检索面临重大挑战：模型不仅需理解视觉特征，还需掌握潜在事件语义、上下文及现实世界知识。传统的视觉-语言检索方法在处理抽象事件、隐含因果关系、时间上下文或复杂叙述时常显不足。为此，本文提出了一种多阶段检索框架，结合密集文章检索、事件感知语言模型重排序和高效图像集合，随后进行基于标题的语义匹配和排名感知选择。我们利用Qwen3进行文章搜索，Qwen3-Reranker进行上下文对齐，Qwen2-VL进行精确图像评分。通过使用互惠排名融合（RRF）进一步提升性能和鲁棒性。我们的系统在EVENTA 2025 Grand Challenge的私有测试集Track 2上取得了最高分，展示了语言推理与多模态检索结合在复杂现实图像理解中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决基于事件的多模态图像检索问题，现有方法在处理复杂叙述和隐含因果关系时存在显著不足，难以有效理解图像与文本之间的关系。

**核心思路**：提出一种多阶段检索框架，通过结合密集文章检索和事件感知语言模型重排序，提升检索的准确性和上下文理解能力。

**技术框架**：整体架构包括多个主要模块：首先进行密集文章检索，然后通过Qwen3-Reranker进行上下文对齐，接着利用Qwen2-VL进行图像评分，最后通过标题引导的语义匹配和排名感知选择。

**关键创新**：最重要的创新在于将语言推理与多模态检索相结合，特别是在处理复杂的现实场景时，显著提升了检索的准确性和鲁棒性。

**关键设计**：在参数设置上，采用了互惠排名融合（RRF）技术，以融合来自不同配置的输出，增强系统的整体性能和稳定性。

## 📊 实验亮点

在EVENTA 2025 Grand Challenge的私有测试集Track 2中，系统取得了最高分，展示了与基线方法相比的显著性能提升，具体提升幅度未知，表明了其在复杂图像理解任务中的有效性。

## 🎯 应用场景

该研究在多模态图像检索领域具有广泛的应用潜力，尤其适用于需要理解复杂叙述和事件语义的场景，如社交媒体内容检索、新闻图像检索和智能监控等。未来，该技术可为图像理解和信息检索提供更高效的解决方案，推动相关领域的发展。

## 📄 摘要（原文）

> Event-based image retrieval from free-form captions presents a significant challenge: models must understand not only visual features but also latent event semantics, context, and real-world knowledge. Conventional vision-language retrieval approaches often fall short when captions describe abstract events, implicit causality, temporal context, or contain long, complex narratives. To tackle these issues, we introduce a multi-stage retrieval framework combining dense article retrieval, event-aware language model reranking, and efficient image collection, followed by caption-guided semantic matching and rank-aware selection. We leverage Qwen3 for article search, Qwen3-Reranker for contextual alignment, and Qwen2-VL for precise image scoring. To further enhance performance and robustness, we fuse outputs from multiple configurations using Reciprocal Rank Fusion (RRF). Our system achieves the top-1 score on the private test set of Track 2 in the EVENTA 2025 Grand Challenge, demonstrating the effectiveness of combining language-based reasoning and multimodal retrieval for complex, real-world image understanding. The code is available at https://github.com/vdkhoi20/EVENT-Retriever.

