---
layout: default
title: "A$^2$LC: Active and Automated Label Correction for Semantic Segmentation"
---

# A$^2$LC: Active and Automated Label Correction for Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11599" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11599v2</a>
  <a href="https://arxiv.org/pdf/2506.11599.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11599v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11599v2', 'A$^2$LC: Active and Automated Label Correction for Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youjin Jeon, Kyusik Cho, Suhan Woo, Euntai Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-13 (更新: 2025-12-03)

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**提出A$^2$LC框架以解决语义分割中的标签纠错问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `主动标签纠错` `语义分割` `自动化标注` `机器学习` `深度学习`

## 📋 核心要点

1. 现有的手动像素级标注方法成本高且容易出错，导致语义分割中的标签质量问题。
2. A$^2$LC框架通过级联的手动和自动纠错阶段，结合人类反馈，提升了标签纠错的效率和准确性。
3. 在Cityscapes数据集上，A$^2$LC以仅20%的预算超越了之前的方法，并在相同预算下实现了27.23%的性能提升。

## 📝 摘要（中文）

主动标签纠错（ALC）作为一种解决语义分割中人工像素级标注高成本和高错误率的有效方法，通过主动识别和纠正错误标注的数据。尽管近期研究通过基础模型生成伪标签提高了纠错效率，但仍存在显著低效。本文提出A$^2$LC，一个主动和自动化的标签纠错框架，手动和自动纠错阶段以级联方式运作。自动纠错阶段利用人类反馈将标签纠正扩展到查询样本之外，从而最大化成本效率。此外，我们引入了一种自适应平衡的获取函数，强调代表性不足的尾部类别，与自动纠错阶段强协同。大量在Cityscapes和PASCAL VOC 2012上的实验表明，A$^2$LC显著优于之前的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决语义分割中手动标注的高成本和错误率问题，现有方法在纠错效率上仍存在显著不足。

**核心思路**：A$^2$LC框架通过级联的手动和自动纠错阶段，利用人类反馈扩展标签纠正范围，从而提高整体成本效率。

**技术框架**：该框架包括两个主要阶段：手动纠错阶段和自动纠错阶段。手动阶段由专家进行初步的标签纠正，而自动阶段则利用人类反馈对未查询样本进行标签扩展。

**关键创新**：A$^2$LC的创新在于自适应平衡的获取函数，特别强调尾部类别的纠错，与传统方法相比，能够更有效地处理类别不平衡问题。

**关键设计**：在参数设置上，框架通过动态调整获取函数的权重，确保在纠错过程中对少数类的关注，同时采用特定的损失函数来优化标签纠正的准确性。整体网络结构设计上，结合了基础模型与人类反馈机制，形成了高效的纠错流程。

## 📊 实验亮点

在Cityscapes数据集上，A$^2$LC以仅20%的预算超越了之前的最先进方法，并在相同预算下实现了27.23%的性能提升，显示出其高效性和有效性。

## 🎯 应用场景

A$^2$LC框架在自动驾驶、医学影像分析和城市环境监测等领域具有广泛的应用潜力。通过提高语义分割的标签质量和效率，该研究能够显著降低人工标注成本，并提升模型的整体性能，推动相关领域的技术进步。

## 📄 摘要（原文）

> Active Label Correction (ALC) has emerged as a promising solution to the high cost and error-prone nature of manual pixel-wise annotation in semantic segmentation, by actively identifying and correcting mislabeled data. Although recent work has improved correction efficiency by generating pseudo-labels using foundation models, substantial inefficiencies still remain. In this paper, we introduce A$^2$LC, an Active and Automated Label Correction framework for semantic segmentation, where manual and automatic correction stages operate in a cascaded manner. Specifically, the automatic correction stage leverages human feedback to extend label corrections beyond the queried samples, thereby maximizing cost efficiency. In addition, we introduce an adaptively balanced acquisition function that emphasizes underrepresented tail classes, working in strong synergy with the automatic correction stage. Extensive experiments on Cityscapes and PASCAL VOC 2012 demonstrate that A$^2$LC significantly outperforms previous state-of-the-art methods. Notably, A$^2$LC exhibits high efficiency by outperforming previous methods with only 20% of their budget, and shows strong effectiveness by achieving a 27.23% performance gain under the same budget on Cityscapes.

