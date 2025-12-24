---
layout: default
title: "The Next Layer: Augmenting Foundation Models with Structure-Preserving and Attention-Guided Learning for Local Patches to Global Context Awareness in Computational Pathology"
---

# The Next Layer: Augmenting Foundation Models with Structure-Preserving and Attention-Guided Learning for Local Patches to Global Context Awareness in Computational Pathology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19914" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19914v1</a>
  <a href="https://arxiv.org/pdf/2508.19914.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19914v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19914v1', 'The Next Layer: Augmenting Foundation Models with Structure-Preserving and Attention-Guided Learning for Local Patches to Global Context Awareness in Computational Pathology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Waqas, Rukhmini Bandyopadhyay, Eman Showkatian, Amgad Muneer, Anas Zafar, Frank Rojas Alvarez, Maricel Corredor Marin, Wentao Li, David Jaffray, Cara Haymaker, John Heymach, Natalie I Vokes, Luisa Maren Solis Soto, Jianjun Zhang, Jia Wu

**分类**: q-bio.QM, cs.AI, stat.ML

**发布日期**: 2025-08-27

**备注**: 43 pages, 7 main Figures, 8 Extended Data Figures

---

## 💡 一句话要点

**提出EAGLE-Net以增强基础模型在计算病理学中的局部与全局上下文理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算病理学` `基础模型` `多实例学习` `注意力机制` `肿瘤微环境` `生物标志物发现` `预后建模`

## 📋 核心要点

1. 现有基础模型在计算病理学中未能有效利用组织的全局空间结构和局部上下文关系，限制了对肿瘤微环境的理解。
2. EAGLE-Net通过结构保持和注意力引导的多实例学习框架，结合多尺度空间编码和邻域感知损失，提升了模型的预测能力和可解释性。
3. 在大规模癌症数据集上，EAGLE-Net在分类和生存预测任务中实现了最高3%的准确率提升，并在7种癌症类型中获得6个的最佳一致性指数。

## 📝 摘要（中文）

基础模型在计算病理学中作为强大的特征提取器，但通常缺乏利用组织的全局空间结构和局部上下文关系的机制。本文提出EAGLE-Net，一种结构保持、注意力引导的多实例学习架构，旨在增强预测和可解释性。EAGLE-Net集成了多尺度绝对空间编码，以捕捉全局组织结构，采用top-K邻域感知损失以关注局部微环境，并引入背景抑制损失以最小化假阳性。实验结果表明，EAGLE-Net在多个癌症类型的分类和生存预测任务中表现优异，达到了最高的分类准确率和一致性指数，生成的注意力图与专家标注高度一致，突出了侵袭前沿、坏死和免疫浸润等重要特征。

## 🔬 方法详解

**问题定义**：本研究旨在解决基础模型在计算病理学中未能有效利用全局组织结构和局部上下文关系的问题，导致对肿瘤微环境理解不足。

**核心思路**：EAGLE-Net通过引入结构保持和注意力引导的多实例学习框架，旨在增强模型的预测能力和可解释性，特别是在处理局部微环境时。

**技术框架**：EAGLE-Net的整体架构包括多尺度绝对空间编码模块、top-K邻域感知损失模块和背景抑制损失模块，形成一个综合的学习流程。

**关键创新**：EAGLE-Net的主要创新在于其结构保持和注意力引导的设计，使得模型能够更好地聚焦于局部微环境，同时有效捕捉全局组织结构，这与传统方法有本质区别。

**关键设计**：在损失函数设计上，EAGLE-Net采用了top-K邻域感知损失和背景抑制损失，以减少假阳性并增强局部特征的学习。此外，模型使用了三种不同的组织学基础网络（REMEDIES、Uni-V1、Uni2-h）进行基准测试。

## 📊 实验亮点

EAGLE-Net在大规模癌症数据集上表现出色，在分类任务中实现了最高3%的准确率提升，并在7种癌症类型中获得6个最佳一致性指数，生成的注意力图与专家标注高度一致，突出了关键的生物学特征。

## 🎯 应用场景

该研究的潜在应用领域包括肿瘤生物标志物的发现、预后建模和临床决策支持。EAGLE-Net的设计使其能够在不同癌症类型的病理图像分析中提供更准确的预测，进而改善患者的治疗方案和预后评估。

## 📄 摘要（原文）

> Foundation models have recently emerged as powerful feature extractors in computational pathology, yet they typically omit mechanisms for leveraging the global spatial structure of tissues and the local contextual relationships among diagnostically relevant regions - key elements for understanding the tumor microenvironment. Multiple instance learning (MIL) remains an essential next step following foundation model, designing a framework to aggregate patch-level features into slide-level predictions. We present EAGLE-Net, a structure-preserving, attention-guided MIL architecture designed to augment prediction and interpretability. EAGLE-Net integrates multi-scale absolute spatial encoding to capture global tissue architecture, a top-K neighborhood-aware loss to focus attention on local microenvironments, and background suppression loss to minimize false positives. We benchmarked EAGLE-Net on large pan-cancer datasets, including three cancer types for classification (10,260 slides) and seven cancer types for survival prediction (4,172 slides), using three distinct histology foundation backbones (REMEDIES, Uni-V1, Uni2-h). Across tasks, EAGLE-Net achieved up to 3% higher classification accuracy and the top concordance indices in 6 of 7 cancer types, producing smooth, biologically coherent attention maps that aligned with expert annotations and highlighted invasive fronts, necrosis, and immune infiltration. These results position EAGLE-Net as a generalizable, interpretable framework that complements foundation models, enabling improved biomarker discovery, prognostic modeling, and clinical decision support

