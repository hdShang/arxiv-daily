---
layout: default
title: Align Your Query: Representation Alignment for Multimodality Medical Object Detection
---

# Align Your Query: Representation Alignment for Multimodality Medical Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02789" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02789v1</a>
  <a href="https://arxiv.org/pdf/2510.02789.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02789v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02789v1', 'Align Your Query: Representation Alignment for Multimodality Medical Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ara Seo, Bryan Sangwoo Kim, Hyungjin Chung, Jong Chul Ye

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-03

**备注**: Project page: https://araseo.github.io/alignyourquery/

**🔗 代码/项目**: [PROJECT_PAGE](https://araseo.github.io/alignyourquery/)

---

## 💡 一句话要点

**提出多模态上下文注意力机制以解决医学目标检测中的表示对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学目标检测` `多模态学习` `表示对齐` `自注意力机制` `深度学习` `医学影像` `对比学习`

## 📋 核心要点

1. 现有的医学目标检测方法在处理多种医学模态时，由于统计特征的异质性和表示空间的分离，表现不佳。
2. 本文提出了一种简单的检测器无关框架，通过引入模态标记和多模态上下文注意力机制来对齐目标查询的表示。
3. 实验结果显示，所提方法在多模态训练中显著提高了AP，且没有架构修改，提供了有效的多模态医学目标检测解决方案。

## 📝 摘要（中文）

医学目标检测在训练混合医学模态（如CXR、CT、MRI）时面临挑战，主要由于统计特征的异质性和表示空间的分离。为了解决这一问题，本文提出了一种表示对齐的方法，专注于对DETR风格目标查询的表示进行对齐。我们定义了模态标记，这是一种轻量级的文本派生嵌入，能够编码成像模态，并通过多模态上下文注意力机制（MoCA）将其整合到检测过程中。我们还引入了QueryREPA，一个短期预训练阶段，通过任务特定的对比目标对查询表示进行对齐。实验结果表明，该方法在多种模态下均能显著提高AP，且几乎没有额外开销，提供了一条实用的路径以实现稳健的多模态医学目标检测。

## 🔬 方法详解

**问题定义**：本文旨在解决医学目标检测中由于多种医学模态的异质性导致的表示对齐问题。现有方法在处理混合模态时，往往无法有效整合不同模态的特征，导致性能下降。

**核心思路**：论文的核心思路是通过引入模态标记和多模态上下文注意力机制（MoCA）来实现目标查询的表示对齐。这种设计旨在将不同模态的上下文信息有效地融入到目标查询中，从而提高检测性能。

**技术框架**：整体架构包括两个主要模块：模态标记的定义与生成，以及通过MoCA进行的查询表示对齐。模态标记是轻量级的文本派生嵌入，而MoCA则通过自注意力机制在查询集中传播模态上下文。

**关键创新**：最重要的技术创新点在于引入了模态标记和QueryREPA预训练阶段，使得目标查询能够有效地与其对应的模态信息对齐。这一方法与传统的单一检测器训练方式有本质区别。

**关键设计**：关键设计包括模态标记的生成方式、MoCA的实现细节，以及QueryREPA的对比损失函数设置。模态标记不需要额外注释，且在检测过程中增加的延迟极小。预训练阶段采用任务特定的对比目标，以确保查询表示与模态标记的有效对齐。

## 📊 实验亮点

实验结果表明，所提方法在多模态训练中显著提高了平均精度（AP），在不同模态下均表现出一致的性能提升。与基线方法相比，AP提升幅度达到了未知，且该方法几乎没有额外的计算开销，证明了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、临床辅助诊断和医疗机器人等。通过提高多模态医学目标检测的准确性和鲁棒性，该方法能够为医生提供更可靠的决策支持，进而改善患者的诊疗效果。未来，该技术有望推广至更广泛的医学应用场景，推动智能医疗的发展。

## 📄 摘要（原文）

> Medical object detection suffers when a single detector is trained on mixed medical modalities (e.g., CXR, CT, MRI) due to heterogeneous statistics and disjoint representation spaces. To address this challenge, we turn to representation alignment, an approach that has proven effective for bringing features from different sources into a shared space. Specifically, we target the representations of DETR-style object queries and propose a simple, detector-agnostic framework to align them with modality context. First, we define modality tokens: compact, text-derived embeddings encoding imaging modality that are lightweight and require no extra annotations. We integrate the modality tokens into the detection process via Multimodality Context Attention (MoCA), mixing object-query representations via self-attention to propagate modality context within the query set. This preserves DETR-style architectures and adds negligible latency while injecting modality cues into object queries. We further introduce QueryREPA, a short pretraining stage that aligns query representations to their modality tokens using a task-specific contrastive objective with modality-balanced batches. Together, MoCA and QueryREPA produce modality-aware, class-faithful queries that transfer effectively to downstream training. Across diverse modalities trained altogether, the proposed approach consistently improves AP with minimal overhead and no architectural modifications, offering a practical path toward robust multimodality medical object detection. Project page: https://araseo.github.io/alignyourquery/.

