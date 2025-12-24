---
layout: default
title: "BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute"
---

# BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22716" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22716v1</a>
  <a href="https://arxiv.org/pdf/2506.22716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22716v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22716v1', 'BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dujian Ding, Ankur Mallick, Shaokun Zhang, Chi Wang, Daniel Madrigal, Mirian Del Carmen Hipolito Garcia, Menglin Xia, Laks V. S. Lakshmanan, Qingyun Wu, Victor Rühle

**分类**: cs.LG, cs.AI, cs.CL, cs.DB

**发布日期**: 2025-06-28

**备注**: Accepted to ICML 2025 (main conference)

---

## 💡 一句话要点

**提出BEST-Route以优化LLM查询路由问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `查询路由` `成本优化` `响应生成` `动态选择`

## 📋 核心要点

1. 现有的LLM查询路由方法仅生成单一响应，导致大模型的过度使用，未能实现成本节约。
2. BEST-Route通过从小模型生成多个响应并选择最佳响应，优化了查询路由的效率和质量。
3. 实验表明，BEST-Route在降低成本的同时，性能几乎不受影响，展示了其实际应用潜力。

## 📝 摘要（中文）

大型语言模型（LLMs）是强大的工具，但在大规模部署时成本高昂。LLM查询路由通过动态分配查询到不同成本和质量的模型来实现所需的权衡。以往的查询路由方法仅从选定模型生成一个响应，而小模型的单一响应往往无法超越大模型的响应，导致大模型的过度使用。本文提出BEST-Route，一个新颖的路由框架，根据查询难度和质量阈值选择模型及其响应数量。实验结果表明，该方法在性能下降不到1%的情况下，成本降低了多达60%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在查询路由中的高成本问题。现有方法仅生成单一响应，导致对大模型的过度依赖，未能充分利用小模型的潜力。

**核心思路**：BEST-Route的核心思想是根据查询的难度和预设的质量阈值，动态选择模型及其响应数量。通过从小模型生成多个响应并选择最佳响应，提升了响应质量，同时降低了成本。

**技术框架**：该方法的整体架构包括查询分析模块、模型选择模块和响应生成模块。首先分析查询的难度，然后选择合适的模型及其响应数量，最后生成并评估响应。

**关键创新**：最重要的创新点在于引入了动态响应生成机制，使得小模型能够通过多次生成响应来提升质量，从而有效减少对大模型的依赖。

**关键设计**：在参数设置上，论文定义了查询难度和质量阈值的计算方式，并设计了损失函数以优化响应选择过程。网络结构方面，采用了轻量级模型以保证在成本和性能之间的平衡。

## 📊 实验亮点

实验结果显示，BEST-Route在真实数据集上的应用能够将成本降低多达60%，而性能仅下降不到1%。这一显著的成本效益比为LLM的实际部署提供了新的可能性，展示了其在实际应用中的优势。

## 🎯 应用场景

BEST-Route具有广泛的应用潜力，特别是在需要高效处理大量查询的场景，如在线客服、智能助手和内容生成等领域。通过优化查询路由，该方法能够显著降低运营成本，同时保持高质量的响应，未来可能推动LLM在更多商业应用中的普及。

## 📄 摘要（原文）

> Large language models (LLMs) are powerful tools but are often expensive to deploy at scale. LLM query routing mitigates this by dynamically assigning queries to models of varying cost and quality to obtain a desired trade-off. Prior query routing approaches generate only one response from the selected model and a single response from a small (inexpensive) model was often not good enough to beat a response from a large (expensive) model due to which they end up overusing the large model and missing out on potential cost savings. However, it is well known that for small models, generating multiple responses and selecting the best can enhance quality while remaining cheaper than a single large-model response. We leverage this idea to propose BEST-Route, a novel routing framework that chooses a model and the number of responses to sample from it based on query difficulty and the quality thresholds. Experiments on real-world datasets demonstrate that our method reduces costs by up to 60% with less than 1% performance drop.

