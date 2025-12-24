---
layout: default
title: "CATP: Contextually Adaptive Token Pruning for Efficient and Enhanced Multimodal In-Context Learning"
---

# CATP: Contextually Adaptive Token Pruning for Efficient and Enhanced Multimodal In-Context Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07871" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07871v2</a>
  <a href="https://arxiv.org/pdf/2508.07871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07871v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07871v2', 'CATP: Contextually Adaptive Token Pruning for Efficient and Enhanced Multimodal In-Context Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanshu Li, Jianjiang Yang, Zhennan Shen, Ligong Han, Haoyan Xu, Ruixiang Tang

**分类**: cs.CV

**发布日期**: 2025-08-11 (更新: 2025-12-09)

**备注**: 14 pages, 12 figures, 6 tables

---

## 💡 一句话要点

**提出CATP以解决多模态上下文学习中的图像令牌冗余问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `图像令牌剪枝` `上下文自适应` `推理效率` `视觉语言模型`

## 📋 核心要点

1. 现有的图像令牌剪枝方法主要集中在单图像任务，未能有效应对多模态上下文学习中的高冗余性和效率需求。
2. 本文提出的上下文自适应令牌剪枝（CATP）方法，通过两阶段渐进剪枝，优化多模态ICL中的图像令牌使用。
3. 实验结果表明，CATP在去除77.8%图像令牌的情况下，平均性能提升0.6%，并且推理延迟减少10.78%。

## 📝 摘要（中文）

现代大型视觉语言模型（LVLMs）将每个输入图像转换为大量令牌，导致图像令牌冗余严重。虽然这提升了视觉感知，但也增加了推理成本。现有的图像令牌剪枝方法主要针对单图像任务，忽视了多模态上下文学习（ICL）中的冗余问题。为此，本文提出了上下文自适应令牌剪枝（CATP），一种无训练的剪枝方法，针对多模态ICL进行优化。CATP通过两个阶段的渐进剪枝，充分反映输入序列中的复杂跨模态交互。在去除77.8%的图像令牌后，CATP在四个LVLM和八个基准上实现了平均0.6%的性能提升，同时推理延迟平均减少10.78%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态上下文学习中图像令牌的冗余问题。现有剪枝方法在此场景下应用时，往往导致显著的准确率下降，无法满足高效推理的需求。

**核心思路**：CATP方法通过上下文自适应的方式进行令牌剪枝，设计了两个阶段的渐进剪枝策略，以充分考虑输入序列中复杂的跨模态交互。

**技术框架**：CATP的整体架构包括两个主要阶段：第一阶段为初步剪枝，通过分析令牌的重要性进行筛选；第二阶段则进一步优化，确保保留对推理最有价值的令牌。

**关键创新**：CATP的核心创新在于其训练无关的剪枝策略，能够在多模态ICL场景中有效减少冗余令牌，同时保持或提升模型性能。这一方法与传统的剪枝方法相比，显著提高了效率和准确性。

**关键设计**：CATP在剪枝过程中采用了动态阈值设定，以适应不同输入的特征。同时，设计了特定的损失函数来平衡剪枝后的性能与效率，确保模型在推理时的稳定性。

## 📊 实验亮点

CATP在去除77.8%图像令牌后，平均性能提升0.6%，并且推理延迟减少10.78%。这一结果显著优于所有基线方法，展示了其在多模态上下文学习中的有效性和优势。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在需要快速领域适应的多模态任务中，如图像描述生成、视觉问答等。通过提高推理效率和稳定性，CATP为未来的多模态学习提供了坚实的基础，推动相关技术的进步。

## 📄 摘要（原文）

> Modern large vision-language models (LVLMs) convert each input image into a large set of tokens that far outnumber the text tokens. Although this improves visual perception, it also introduces severe image token redundancy. Because image tokens contain sparse information, many contribute little to reasoning but greatly increase inference cost. Recent image token pruning methods address this issue by identifying important tokens and removing the rest. These methods improve efficiency with only small performance drops. However, most of them focus on single-image tasks and overlook multimodal in-context learning (ICL), where redundancy is higher and efficiency is more important. Redundant tokens weaken the advantage of multimodal ICL for rapid domain adaptation and lead to unstable performance. When existing pruning methods are applied in this setting, they cause large accuracy drops, which exposes a clear gap and the need for new approaches. To address this, we propose Contextually Adaptive Token Pruning (CATP), a training-free pruning method designed for multimodal ICL. CATP uses two stages of progressive pruning that fully reflect the complex cross-modal interactions in the input sequence. After removing 77.8% of the image tokens, CATP achieves an average performance gain of 0.6% over the vanilla model on four LVLMs and eight benchmarks, clearly outperforming all baselines. At the same time, it improves efficiency by reducing inference latency by an average of 10.78%. CATP strengthens the practical value of multimodal ICL and lays the foundation for future progress in interleaved image-text settings.

