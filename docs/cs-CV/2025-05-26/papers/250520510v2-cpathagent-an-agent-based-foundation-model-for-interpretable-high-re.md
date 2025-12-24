---
layout: default
title: "CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic"
---

# CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20510" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20510v2</a>
  <a href="https://arxiv.org/pdf/2505.20510.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20510v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20510v2', 'CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists\' Diagnostic Logic')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Sun, Yixuan Si, Chenglu Zhu, Kai Zhang, Zhongyi Shui, Bowen Ding, Tao Lin, Lin Yang

**分类**: cs.CV

**发布日期**: 2025-05-26 (更新: 2025-10-28)

**备注**: 52 pages, 34 figures

---

## 💡 一句话要点

**提出CPathAgent以解决病理图像分析中的可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算病理学` `可解释性` `图像分析` `多阶段训练` `代理基础模型` `病理学家诊断`

## 📋 核心要点

1. 现有模型直接输出最终诊断，缺乏对病理学家诊断过程的解释，导致可解释性不足。
2. CPathAgent通过模仿病理学家的诊断工作流程，基于观察到的视觉特征自主导航全切片图像，提供透明的诊断总结。
3. 实验结果显示，CPathAgent在不同图像尺度的基准测试中表现优异，验证了其代理基础诊断方法的有效性。

## 📝 摘要（中文）

近年来，计算病理学的进展催生了众多基础模型，这些模型通常依赖于通用编码器进行全切片图像分类，或采用多模态方法直接从图像生成报告。然而，这些模型无法模拟病理学家的诊断方法。为此，本文提出CPathAgent，一种基于代理的创新方法，能够自主导航全切片图像，生成更透明和可解释的诊断摘要。我们开发了一个多阶段训练策略，将补丁级、区域级和全切片级能力统一在一个模型中。此外，构建了PathMMU-HR2，这是首个经过专家验证的大区域分析基准。大量实验表明，CPathAgent在三个不同图像尺度的基准测试中均优于现有方法，验证了其有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有病理图像分析模型缺乏可解释性的问题。现有方法通常直接给出最终诊断，未能展示病理学家的诊断逻辑和过程。

**核心思路**：CPathAgent通过模拟病理学家的工作流程，采用自主导航的方式分析全切片图像，从而生成更具透明度的诊断总结。这种设计使得模型能够在不同尺度上理解和推理图像信息。

**技术框架**：CPathAgent的整体架构包括多个阶段，分别处理补丁级、区域级和全切片级的图像信息。模型通过多阶段训练策略，逐步提升对图像的理解能力。

**关键创新**：CPathAgent的主要创新在于其代理基础的诊断方法，能够模拟病理学家的系统性检查过程，与现有模型直接输出诊断的方式有本质区别。

**关键设计**：在模型设计中，采用了多阶段训练策略，结合不同尺度的图像信息，确保模型能够有效地处理和理解大区域分析的需求。

## 📊 实验亮点

在实验中，CPathAgent在三个不同图像尺度的基准测试中均表现出色，超越了现有方法，具体性能提升幅度未知。这一结果验证了其代理基础诊断方法的有效性，为计算病理学提供了新的研究方向。

## 🎯 应用场景

CPathAgent的研究成果可广泛应用于计算病理学领域，尤其是在需要高分辨率图像分析的临床诊断中。其可解释性特征将帮助医生更好地理解模型的决策过程，提高诊断的可信度和准确性，未来可能推动智能医疗的发展。

## 📄 摘要（原文）

> Recent advances in computational pathology have led to the emergence of numerous foundation models. These models typically rely on general-purpose encoders with multi-instance learning for whole slide image (WSI) classification or apply multimodal approaches to generate reports directly from images. However, these models cannot emulate the diagnostic approach of pathologists, who systematically examine slides at low magnification to obtain an overview before progressively zooming in on suspicious regions to formulate comprehensive diagnoses. Instead, existing models directly output final diagnoses without revealing the underlying reasoning process. To address this gap, we introduce CPathAgent, an innovative agent-based approach that mimics pathologists' diagnostic workflow by autonomously navigating across WSI based on observed visual features, thereby generating substantially more transparent and interpretable diagnostic summaries. To achieve this, we develop a multi-stage training strategy that unifies patch-level, region-level, and WSI-level capabilities within a single model, which is essential for replicating how pathologists understand and reason across diverse image scales. Additionally, we construct PathMMU-HR2, the first expert-validated benchmark for large region analysis. This represents a critical intermediate scale between patches and whole slides, reflecting a key clinical reality where pathologists typically examine several key large regions rather than entire slides at once. Extensive experiments demonstrate that CPathAgent consistently outperforms existing approaches across benchmarks at three different image scales, validating the effectiveness of our agent-based diagnostic approach and highlighting a promising direction for computational pathology.

