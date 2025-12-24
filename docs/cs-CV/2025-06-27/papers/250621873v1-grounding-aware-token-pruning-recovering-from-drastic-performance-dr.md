---
layout: default
title: "Grounding-Aware Token Pruning: Recovering from Drastic Performance Drops in Visual Grounding Caused by Pruning"
---

# Grounding-Aware Token Pruning: Recovering from Drastic Performance Drops in Visual Grounding Caused by Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21873" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21873v1</a>
  <a href="https://arxiv.org/pdf/2506.21873.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21873v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21873v1', 'Grounding-Aware Token Pruning: Recovering from Drastic Performance Drops in Visual Grounding Caused by Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tzu-Chun Chien, Chieh-Kai Lin, Shiang-Feng Tsai, Ruei-Chi Lai, Hung-Jen Chen, Min Sun

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出基于定位感知的标记剪枝以解决视觉定位性能下降问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉定位` `多模态学习` `标记剪枝` `位置ID调整` `性能恢复`

## 📋 核心要点

1. 现有的标记剪枝方法在降低计算成本的同时，导致模型的视觉定位能力显著下降，影响了任务的准确性。
2. 本文提出的基于定位感知的标记剪枝（GAP）方法，通过调整位置ID来恢复模型的定位性能，解决了剪枝带来的问题。
3. 实验结果表明，GAP方法使得REC的准确率从15.34%恢复至51.42%，在多个模型上均实现了性能提升。

## 📝 摘要（中文）

近年来，多模态大型语言模型（MLLMs）在视觉定位任务中表现出色，成为各种视觉-语言应用的通用接口。然而，标记剪枝方法的应用显著削弱了模型的定位能力，导致预测错误和性能急剧下降。以Referring Expression Comprehension（REC）为例，剪枝使得LLaVA在RefCOCO验证集上的准确率从56.14%降至15.34%。分析表明，剪枝后位置ID的不对齐是性能下降的主要原因。为了解决这一问题，本文提出了基于定位感知的标记剪枝（GAP），通过简单有效的调整位置ID，使REC准确率恢复至51.42%，相当于原始性能的90%，且无需额外的训练、内存或计算开销。该方法在Shikra、MiniGPTv2和LLaVA系列模型上均表现出一致的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决标记剪枝导致的视觉定位性能下降问题。现有剪枝方法在降低计算成本的同时，显著削弱了模型的定位能力，导致预测错误和性能急剧下降。

**核心思路**：论文的核心解决思路是提出基于定位感知的标记剪枝（GAP），通过对位置ID进行简单有效的调整，恢复模型在视觉定位任务中的性能。这样的设计旨在保持位置ID的顺序和数值一致性，从而提升剪枝后的模型性能。

**技术框架**：整体架构包括对原始模型进行标记剪枝，然后通过GAP方法调整位置ID，最后评估模型在视觉定位任务上的性能。主要模块包括剪枝模块、位置ID调整模块和性能评估模块。

**关键创新**：最重要的技术创新点在于提出了GAP方法，通过调整位置ID来解决剪枝后性能下降的问题。这与现有方法的本质区别在于，GAP关注于位置ID的对齐，而不仅仅是剪枝的数量。

**关键设计**：在GAP方法中，关键设计包括对位置ID的重新排序和数值调整，确保在剪枝后模型仍能保持对输入的正确理解。此外，该方法无需额外的训练或计算开销，极大地提高了实用性。

## 📊 实验亮点

实验结果显示，GAP方法使得LLaVA在RefCOCO验证集上的准确率从15.34%提升至51.42%，恢复了90%的原始性能。此外，该方法在Shikra和MiniGPTv2等多个模型上均表现出一致的性能提升，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括视觉问答、图像标注和人机交互等多模态任务。通过提高剪枝后的模型性能，GAP方法能够在资源受限的环境中实现高效的视觉-语言处理，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent Multimodal Large Language Models (MLLMs) have demonstrated strong performance in visual grounding, establishing themselves as a general interface for various vision-language applications. This progress has driven the development of token pruning methods to mitigate the high computational costs associated with processing numerous visual tokens. However, we observe that pruning significantly weakens the model's grounding ability, leading to incorrect predictions and drastic performance degradation. In Referring Expression Comprehension (REC), for instance, pruning causes the accuracy of LLaVA on the RefCOCO validation set to drop from 56.14% to 15.34%. Our analysis identifies misaligned position IDs after pruning as the primary cause of this degradation, as both the order and value of these IDs are crucial for maintaining performance in grounding tasks. To address this issue, we propose Grounding-Aware Token Pruning (GAP), a simple yet effective adjustment to position IDs that recovers REC accuracy back to 51.42%, which is 90% of the original performance in the without pruning setting, all while requiring no additional training, memory, or computational overhead. Applied to models such as Shikra, MiniGPTv2, and the LLaVA series, our method consistently improves performance across various token pruning strategies.

