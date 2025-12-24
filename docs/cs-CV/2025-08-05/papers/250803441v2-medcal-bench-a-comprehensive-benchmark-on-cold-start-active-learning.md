---
layout: default
title: "MedCAL-Bench: A Comprehensive Benchmark on Cold-Start Active Learning with Foundation Models for Medical Image Analysis"
---

# MedCAL-Bench: A Comprehensive Benchmark on Cold-Start Active Learning with Foundation Models for Medical Image Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03441" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03441v2</a>
  <a href="https://arxiv.org/pdf/2508.03441.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03441v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03441v2', 'MedCAL-Bench: A Comprehensive Benchmark on Cold-Start Active Learning with Foundation Models for Medical Image Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ning Zhu, Xiaochuan Ma, Shaoting Zhang, Guotai Wang

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-10-10)

**备注**: 23 pages, 6 figures, 10 tables

**🔗 代码/项目**: [GITHUB](https://github.com/HiLab-git/MedCAL-Bench)

---

## 💡 一句话要点

**提出MedCAL-Bench以解决医疗图像分析中的冷启动主动学习问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `冷启动主动学习` `医疗图像分析` `基础模型` `特征提取` `样本选择` `自监督学习` `基准评估`

## 📋 核心要点

1. 现有的冷启动主动学习方法依赖自监督学习进行特征提取，效率低且特征表示不足。
2. 论文提出MedCAL-Bench，作为第一个系统的基于基础模型的CSAL基准，评估特征提取和样本选择阶段。
3. 实验结果显示，大多数基础模型在CSAL中有效，DINO系列在分割任务中表现最佳，ALPS在分割中效果最佳。

## 📝 摘要（中文）

冷启动主动学习（CSAL）旨在在没有先验知识的情况下选择信息丰富的样本进行标注，这对于在有限的标注预算下提高医疗图像分析的标注效率和模型性能至关重要。现有的CSAL方法大多依赖于目标数据集上的自监督学习（SSL）进行特征提取，效率低且受限于特征表示不足。最近，预训练的基础模型（FMs）在特征提取方面表现出强大的能力，具有更好CSAL的潜力。然而，这一范式鲜有研究，缺乏用于比较FMs在CSAL任务中的基准。为此，我们提出了MedCAL-Bench，这是第一个系统的基于FM的CSAL基准，用于医疗图像分析。我们在不同标注预算下评估了14个FMs和7种CSAL策略，涵盖了来自多种医疗模态的分类和分割任务。

## 🔬 方法详解

**问题定义**：本论文旨在解决医疗图像分析中的冷启动主动学习（CSAL）问题，现有方法在特征提取上效率低下，且缺乏有效的基准进行比较。

**核心思路**：提出MedCAL-Bench基准，利用预训练的基础模型（FMs）进行特征提取，并评估其在CSAL中的表现，以提高标注效率和模型性能。

**技术框架**：整体架构包括特征提取和样本选择两个主要阶段，首先使用FMs提取特征，然后应用不同的CSAL策略选择样本进行标注。

**关键创新**：MedCAL-Bench是第一个系统的基于FM的CSAL基准，首次同时评估特征提取和样本选择阶段，填补了这一领域的研究空白。

**关键设计**：在实验中评估了14个FMs和7种CSAL策略，涵盖了不同的标注预算和任务类型，特别关注DINO系列和ALPS策略的表现。

## 📊 实验亮点

实验结果显示，大多数基础模型在冷启动主动学习中表现良好，DINO系列在分割任务中表现最佳，ALPS策略在分割任务中效果最佳，RepDiv在分类任务中领先。整体上，分割任务中基础模型的性能差异较大，而分类任务中差异较小，表明不同任务对样本选择策略的需求不同。

## 🎯 应用场景

该研究的潜在应用领域包括医疗图像分析、疾病诊断和治疗规划等。通过提高标注效率，能够在有限的资源下更快地训练高性能模型，从而提升医疗服务质量和效率。未来，该基准可能推动更多基于基础模型的主动学习研究，促进医疗领域的智能化发展。

## 📄 摘要（原文）

> Cold-Start Active Learning (CSAL) aims to select informative samples for annotation without prior knowledge, which is important for improving annotation efficiency and model performance under a limited annotation budget in medical image analysis. Most existing CSAL methods rely on Self-Supervised Learning (SSL) on the target dataset for feature extraction, which is inefficient and limited by insufficient feature representation. Recently, pre-trained Foundation Models (FMs) have shown powerful feature extraction ability with a potential for better CSAL. However, this paradigm has been rarely investigated, with a lack of benchmarks for comparison of FMs in CSAL tasks. To this end, we propose MedCAL-Bench, the first systematic FM-based CSAL benchmark for medical image analysis. We evaluate 14 FMs and 7 CSAL strategies across 7 datasets under different annotation budgets, covering classification and segmentation tasks from diverse medical modalities. It is also the first CSAL benchmark that evaluates both the feature extraction and sample selection stages. Our experimental results reveal that: 1) Most FMs are effective feature extractors for CSAL, with DINO family performing the best in segmentation; 2) The performance differences of these FMs are large in segmentation tasks, while small for classification; 3) Different sample selection strategies should be considered in CSAL on different datasets, with Active Learning by Processing Surprisal (ALPS) performing the best in segmentation while RepDiv leading for classification. The code is available at https://github.com/HiLab-git/MedCAL-Bench.

