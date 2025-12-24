---
layout: default
title: "NEURAL: Attention-Guided Pruning for Unified Multimodal Resource-Constrained Clinical Evaluation"
---

# NEURAL: Attention-Guided Pruning for Unified Multimodal Resource-Constrained Clinical Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09715" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09715v1</a>
  <a href="https://arxiv.org/pdf/2508.09715.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09715v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09715v1', 'NEURAL: Attention-Guided Pruning for Unified Multimodal Resource-Constrained Clinical Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Devvrat Joshi, Islem Rekik

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-13

**🔗 代码/项目**: [GITHUB](https://github.com/basiralab/NEURAL)

---

## 💡 一句话要点

**提出NEURAL以解决资源受限临床环境中的多模态医学影像数据压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态医学影像` `数据压缩` `临床评估` `交叉注意力` `知识图` `深度学习` `放射学` `图形表示`

## 📋 核心要点

1. 多模态医学影像数据的快速增长导致存储和传输的挑战，尤其在资源受限的临床环境中。
2. NEURAL框架通过语义引导的数据压缩，利用交叉注意力分数对影像进行结构性修剪，保留关键诊断区域。
3. 在MIMIC-CXR和CheXpert Plus数据集上，NEURAL实现了93.4%-97.7%的数据大小减少，同时保持高达0.95的AUC性能。

## 📝 摘要（中文）

随着多模态医学影像数据的快速增长，存储和传输面临重大挑战，尤其是在资源受限的临床环境中。本文提出了NEURAL，一个通过语义引导的数据压缩框架，利用经过微调的生成视觉-语言模型中的交叉注意力分数，对胸部X光影像进行结构性修剪，仅保留诊断关键区域。该方法将影像转化为高度压缩的图形表示，并将修剪后的视觉图与来自临床报告的知识图融合，创建一个通用数据结构，简化后续建模。NEURAL在MIMIC-CXR和CheXpert Plus数据集上验证，图像数据大小减少93.4%-97.7%，同时保持0.88-0.95的高诊断性能，超越了使用未压缩数据的基线模型。

## 🔬 方法详解

**问题定义**：本文旨在解决在资源受限的临床环境中，多模态医学影像数据存储和传输的挑战。现有方法往往无法有效压缩数据，同时保持诊断性能。

**核心思路**：NEURAL通过利用经过微调的生成视觉-语言模型中的交叉注意力分数，进行影像的结构性修剪，保留诊断关键区域，从而实现高效的数据压缩。

**技术框架**：NEURAL的整体架构包括两个主要模块：首先是影像的结构性修剪，利用交叉注意力分数识别关键区域；其次是将修剪后的视觉图与知识图融合，形成一个统一的图形表示，简化后续的建模过程。

**关键创新**：NEURAL的核心创新在于将语义引导的压缩与图形表示结合，创建了一个通用的数据结构，解决了数据大小与临床实用性之间的权衡。与现有方法相比，NEURAL在保持高诊断性能的同时，显著减少了数据大小。

**关键设计**：在设计中，NEURAL采用了特定的损失函数以优化影像的压缩效果，并利用深度学习模型进行交叉注意力分数的计算，确保保留关键的诊断信息。

## 📊 实验亮点

NEURAL在MIMIC-CXR和CheXpert Plus数据集上实现了93.4%-97.7%的影像数据大小减少，同时维持了0.88-0.95的AUC性能，显著优于使用未压缩数据的基线模型，展示了其在多模态医学影像处理中的有效性和优势。

## 🎯 应用场景

NEURAL的研究成果在资源受限的临床环境中具有广泛的应用潜力，尤其是在远程放射学和高效工作流程中。通过有效压缩影像数据，NEURAL能够提高数据传输效率，降低存储成本，同时保持高水平的诊断性能，促进医疗服务的可及性和效率。

## 📄 摘要（原文）

> The rapid growth of multimodal medical imaging data presents significant storage and transmission challenges, particularly in resource-constrained clinical settings. We propose NEURAL, a novel framework that addresses this by using semantics-guided data compression. Our approach repurposes cross-attention scores between the image and its radiological report from a fine-tuned generative vision-language model to structurally prune chest X-rays, preserving only diagnostically critical regions. This process transforms the image into a highly compressed, graph representation. This unified graph-based representation fuses the pruned visual graph with a knowledge graph derived from the clinical report, creating a universal data structure that simplifies downstream modeling. Validated on the MIMIC-CXR and CheXpert Plus dataset for pneumonia detection, NEURAL achieves a 93.4-97.7\% reduction in image data size while maintaining a high diagnostic performance of 0.88-0.95 AUC, outperforming other baseline models that use uncompressed data. By creating a persistent, task-agnostic data asset, NEURAL resolves the trade-off between data size and clinical utility, enabling efficient workflows and teleradiology without sacrificing performance. Our NEURAL code is available at https://github.com/basiralab/NEURAL.

