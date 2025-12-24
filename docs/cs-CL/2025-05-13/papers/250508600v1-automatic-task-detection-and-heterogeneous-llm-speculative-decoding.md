---
layout: default
title: Automatic Task Detection and Heterogeneous LLM Speculative Decoding
---

# Automatic Task Detection and Heterogeneous LLM Speculative Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08600" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08600v1</a>
  <a href="https://arxiv.org/pdf/2505.08600.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08600v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08600v1', 'Automatic Task Detection and Heterogeneous LLM Speculative Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Danying Ge, Jianhua Gao, Qizhi Jiang, Yifei Feng, Weixing Ji

**分类**: cs.CL

**发布日期**: 2025-05-13

**备注**: 10 pages, 10 figures, 2 tables

---

## 💡 一句话要点

**提出自动任务检测与异构LLM推测解码以优化下游任务**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推测解码` `大型语言模型` `任务优化` `异构模型` `在线分类器`

## 📋 核心要点

1. 现有推测解码方法在下游任务中面临接受率与解码速度之间的权衡，效率难以保证。
2. 本文提出了一种自动任务划分与分配的方法，将下游任务分配给异构草稿模型以优化推测解码。
3. 实验结果显示，所提方法在草稿准确性上提升6%至50%，推理速度加快1.10倍至2.64倍。

## 📝 摘要（中文）

推测解码结合了草稿模型与目标模型，成为加速大型语言模型（LLM）推理的有效方法。然而，现有方法在接受率与解码速度之间存在权衡，尤其在下游任务中，由于草稿模型的能力有限，难以确保效率。为了解决这一问题，本文提出了一种针对下游任务优化的推测解码算法，包括自动任务划分与分配方法，能够将下游任务自动分类为不同子任务，并分配给一组异构草稿模型。每个草稿模型使用任务特定数据与目标模型对齐，从而增强推理结果的一致性。此外，本文还引入了一种在线轻量级提示分类器，动态将提示路由到合适的草稿模型。实验结果表明，所提方法在草稿准确性上比传统推测解码提高了6%至50%，同时在LLM推理中实现了1.10倍至2.64倍的加速。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推测解码方法在下游任务中效率不足的问题，尤其是在接受率与解码速度之间的权衡。现有草稿模型能力有限，导致难以适应多样化的任务需求。

**核心思路**：提出一种针对下游任务优化的推测解码算法，通过自动任务划分与分配，将任务分配给异构草稿模型，以提高推测解码的准确性和速度。

**技术框架**：整体架构包括任务自动分类、草稿模型分配和在线提示分类器三个主要模块。任务首先被自动划分为子任务，然后根据任务特性分配给不同的草稿模型，最后通过提示分类器动态路由。

**关键创新**：最重要的创新在于引入了异构草稿模型与在线提示分类器的结合，使得推测解码能够针对不同任务进行优化，从而显著提升了准确性与推理速度。

**关键设计**：在设计中，草稿模型与目标模型使用任务特定数据进行对齐，确保推理结果的一致性。同时，在线提示分类器的设计使得模型能够根据实时输入动态调整，提升了系统的灵活性。

## 📊 实验亮点

实验结果表明，所提方法在草稿准确性上比传统推测解码提高了6%至50%，同时在LLM推理中实现了1.10倍至2.64倍的加速，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过优化推测解码，能够显著提高大型语言模型在实际应用中的响应速度和准确性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Speculative decoding, which combines a draft model with a target model, has emerged as an effective approach to accelerate large language model (LLM) inference. However, existing methods often face a trade-off between the acceptance rate and decoding speed in downstream tasks due to the limited capacity of the draft model, making it difficult to ensure efficiency across diverse tasks. To address this problem, we propose a speculative decoding algorithm tailored for downstream task optimization. It includes an automatic task partitioning and assigning method, which automatically categorizes downstream tasks into different sub-tasks and assigns them to a set of heterogeneous draft models. Each draft model is aligned with the target model using task-specific data, thereby enhancing the consistency of inference results. In addition, our proposed method incorporates an online lightweight prompt classifier to dynamically route prompts to the appropriate draft model. Experimental results demonstrate that the proposed method improves draft accuracy by 6% to 50% over vanilla speculative decoding, while achieving a speedup of 1.10x to 2.64x in LLM inference.

