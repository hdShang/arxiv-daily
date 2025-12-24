---
layout: default
title: "HyperKD: Distilling Cross-Spectral Knowledge in Masked Autoencoders via Inverse Domain Shift with Spatial-Aware Masking and Specialized Loss"
---

# HyperKD: Distilling Cross-Spectral Knowledge in Masked Autoencoders via Inverse Domain Shift with Spatial-Aware Masking and Specialized Loss

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09453" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09453v1</a>
  <a href="https://arxiv.org/pdf/2508.09453.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09453v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09453v1', 'HyperKD: Distilling Cross-Spectral Knowledge in Masked Autoencoders via Inverse Domain Shift with Spatial-Aware Masking and Specialized Loss')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdul Matin, Tanjim Bin Faruk, Shrideep Pallickara, Sangmi Lee Pallickara

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出HyperKD以解决高光谱遥感中的知识蒸馏问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `高光谱遥感` `知识蒸馏` `逆域适应` `特征对齐` `空间特征掩蔽` `基础模型` `遥感分析`

## 📋 核心要点

1. 现有知识蒸馏方法在高光谱遥感中面临光谱差异和观测数据稀缺的挑战，限制了基础模型的有效应用。
2. HyperKD通过逆向知识转移，利用简单的教师模型指导复杂的学生模型，提出了一种新的知识蒸馏框架。
3. 实验结果表明，HyperKD在MAE的表示学习上显著提升了重建精度，并在多个下游任务中表现出更强的鲁棒性。

## 📝 摘要（中文）

随着基础模型的普及，利用大规模无标签数据集进行预训练已成为创建可适应和可重用架构的有效方法。然而，直接应用于高光谱遥感面临光谱差异和观测稀缺的挑战。本文提出HyperKD，一个新颖的知识蒸馏框架，能够将教师模型的学习表示有效转移到学生模型中，促进高光谱图像的基础模型开发。HyperKD通过引入基于特征的策略，解决了光谱间隙的逆域适应问题，显著提升了MAE的表示学习效果，并在土地覆盖分类、作物类型识别和土壤有机碳预测等下游任务中表现出更强的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决高光谱遥感中知识蒸馏的逆域适应问题，现有方法在光谱差异和数据稀缺情况下难以有效迁移知识。

**核心思路**：HyperKD通过引入简单教师模型指导复杂学生模型，采用逆向知识转移的方式，克服了光谱间隙带来的挑战。

**技术框架**：HyperKD基于Masked Autoencoder构建，主要包括特征对齐、空间特征引导掩蔽和针对高光谱图像的增强损失函数等模块。

**关键创新**：HyperKD的核心创新在于其逆向知识转移机制和特征基础策略，区别于传统的知识蒸馏方法，能够有效处理光谱域间隙。

**关键设计**：在设计中，HyperKD采用了光谱范围基础的通道对齐技术，结合空间特征引导的掩蔽策略，并设计了适用于高光谱图像的损失函数，以提高模型的学习效果。

## 📊 实验亮点

实验结果显示，HyperKD在MAE的表示学习上显著提高了重建精度，相较于基线模型，土地覆盖分类任务的准确率提升了X%，作物类型识别任务的F1分数提升了Y%，展现了知识蒸馏框架在高光谱图像分析中的巨大潜力。

## 🎯 应用场景

HyperKD的研究成果在高光谱遥感领域具有广泛的应用潜力，能够有效提升土地覆盖分类、作物类型识别和土壤有机碳预测等任务的准确性。这一框架为遥感分析提供了新的思路，未来可进一步推广至其他领域的多模态数据处理。

## 📄 摘要（原文）

> The proliferation of foundation models, pretrained on large-scale unlabeled datasets, has emerged as an effective approach in creating adaptable and reusable architectures that can be leveraged for various downstream tasks using satellite observations. However, their direct application to hyperspectral remote sensing remains challenging due to inherent spectral disparities and the scarcity of available observations. In this work, we present HyperKD, a novel knowledge distillation framework that enables transferring learned representations from a teacher model into a student model for effective development of a foundation model on hyperspectral images. Unlike typical knowledge distillation frameworks, which use a complex teacher to guide a simpler student, HyperKD enables an inverse form of knowledge transfer across different types of spectral data, guided by a simpler teacher model. Building upon a Masked Autoencoder, HyperKD distills knowledge from the Prithvi foundational model into a student tailored for EnMAP hyperspectral imagery. HyperKD addresses the inverse domain adaptation problem with spectral gaps by introducing a feature-based strategy that includes spectral range-based channel alignment, spatial feature-guided masking, and an enhanced loss function tailored for hyperspectral images. HyperKD bridges the substantial spectral domain gap, enabling the effective use of pretrained foundation models for geospatial applications. Extensive experiments show that HyperKD significantly improves representation learning in MAEs, leading to enhanced reconstruction fidelity and more robust performance on downstream tasks such as land cover classification, crop type identification, and soil organic carbon prediction, underpinning the potential of knowledge distillation frameworks in remote sensing analytics with hyperspectral imagery.

