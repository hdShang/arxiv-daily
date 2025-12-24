---
layout: default
title: "GLASS: Test-Time Acceleration for LLMs via Global-Local Neural Importance Aggregation"
---

# GLASS: Test-Time Acceleration for LLMs via Global-Local Neural Importance Aggregation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14302" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14302v1</a>
  <a href="https://arxiv.org/pdf/2508.14302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14302v1', 'GLASS: Test-Time Acceleration for LLMs via Global-Local Neural Importance Aggregation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amirmohsen Sattarifard, Sepehr Lavasani, Ehsan Imani, Kunlin Zhang, Hanlin Xu, Fengyu Sun, Negar Hassanpour, Chao Gao

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出A/I-GLASS以解决LLMs在边缘硬件上的动态剪枝问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态剪枝` `大型语言模型` `边缘计算` `神经网络` `推理效率`

## 📋 核心要点

1. 现有方法在动态剪枝时存在锁定单一稀疏模式或增加运行时开销的问题，导致性能受限。
2. 本文提出A/I-GLASS，通过激活和影响的全局-局部神经重要性聚合，动态选择前馈网络单元，避免了训练过程。
3. 实验结果显示，GLASS在长文本生成场景中显著提升性能，超越了以往的训练无关方法。

## 📝 摘要（中文）

在边缘硬件上部署大型语言模型（LLMs）需要进行激进的、及时感知的动态剪枝，以减少计算量而不降低质量。现有的静态或基于预测的方法要么锁定单一稀疏模式，要么增加额外的运行时开销，而最近依赖单一提示统计的零-shot方法在短提示或长生成场景中表现不佳。本文提出了A/I-GLASS：基于激活和影响的全局-局部神经重要性聚合，用于前馈网络的稀疏化，这是一种无需训练的方法，通过对提示局部和模型内在全局神经元统计的排名聚合，动态选择前馈网络单元。实验证明，GLASS在多个LLMs和基准测试中显著优于以往的训练无关方法，尤其是在具有挑战性的长文本生成场景中，且不依赖辅助预测器或增加推理开销。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在边缘硬件上部署时的动态剪枝问题。现有方法要么固定稀疏模式，导致灵活性不足，要么增加额外的运行时开销，影响推理效率。

**核心思路**：A/I-GLASS通过聚合提示局部和模型全局神经元的统计信息，动态选择前馈网络单元，避免了依赖训练的过程，从而提高了模型的推理效率和灵活性。

**技术框架**：该方法的整体架构包括两个主要模块：激活基于的选择和影响基于的选择。首先，通过对提示的局部信息进行分析，识别出重要的神经元；其次，结合模型的全局信息，进行重要性聚合，最终动态选择前馈网络的单元。

**关键创新**：A/I-GLASS的核心创新在于其训练无关的动态选择机制，通过全局和局部信息的结合，克服了传统方法的局限性，显著提升了在长文本生成场景中的表现。

**关键设计**：在设计上，A/I-GLASS使用了特定的聚合算法来处理神经元的重要性评分，并且在选择过程中没有引入额外的预测器，从而保持了推理的高效性。

## 📊 实验亮点

实验结果表明，GLASS在多个大型语言模型和基准测试中表现优异，尤其在长文本生成任务中，相较于以往的训练无关方法，性能提升幅度达到显著水平，且没有增加推理开销。

## 🎯 应用场景

该研究的潜在应用领域包括边缘计算设备上的自然语言处理任务，如智能助手、实时翻译和内容生成等。通过提高大型语言模型的推理效率，A/I-GLASS能够在资源受限的环境中实现更高效的应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Deploying Large Language Models (LLMs) on edge hardware demands aggressive, prompt-aware dynamic pruning to reduce computation without degrading quality. Static or predictor-based schemes either lock in a single sparsity pattern or incur extra runtime overhead, and recent zero-shot methods that rely on statistics from a single prompt fail on short prompt and/or long generation scenarios. We introduce A/I-GLASS: Activation- and Impact-based Global-Local neural importance Aggregation for feed-forward network SparSification, two training-free methods that dynamically select FFN units using a rank-aggregation of prompt local and model-intrinsic global neuron statistics. Empirical results across multiple LLMs and benchmarks demonstrate that GLASS significantly outperforms prior training-free methods, particularly in challenging long-form generation scenarios, without relying on auxiliary predictors or adding any inference overhead.

