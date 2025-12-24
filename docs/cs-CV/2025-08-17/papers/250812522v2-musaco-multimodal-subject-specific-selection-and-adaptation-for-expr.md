---
layout: default
title: "MuSACo: Multimodal Subject-Specific Selection and Adaptation for Expression Recognition with Co-Training"
---

# MuSACo: Multimodal Subject-Specific Selection and Adaptation for Expression Recognition with Co-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12522" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12522v2</a>
  <a href="https://arxiv.org/pdf/2508.12522.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12522v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12522v2', 'MuSACo: Multimodal Subject-Specific Selection and Adaptation for Expression Recognition with Co-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Osama Zeeshan, Natacha Gillet, Alessandro Lameiras Koerich, Marco Pedersoli, Francois Bremond, Eric Granger

**分类**: cs.CV

**发布日期**: 2025-08-17 (更新: 2025-12-08)

**备注**: WACV 2026

---

## 💡 一句话要点

**提出MuSACo以解决个性化表情识别中的多模态适应问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化表情识别` `多模态适应` `协同训练` `情感计算` `数字健康` `源选择` `特征对齐`

## 📋 核心要点

1. 现有的多源领域适应方法往往忽视多模态信息，限制了个体特征的捕捉与利用。
2. MuSACo通过协同训练方法，结合多模态信息和源领域，进行个体特定的适应与选择。
3. 在BioVid、StressID和BAH等多模态ER数据集上，MuSACo的表现优于传统的UDA和最新的MSDA方法。

## 📝 摘要（中文）

个性化表情识别（ER）涉及将机器学习模型适应于特定个体的数据，以提高对具有显著人际差异的表情的识别能力。现有的多源领域适应（MSDA）方法往往忽视多模态信息，限制了个体多样性。为了解决这些问题，本文提出了MuSACo，这是一种基于协同训练的多模态个体特定选择与适应方法。MuSACo利用多个模态和源领域的互补信息进行个体特定适应，特别适用于数字健康中的情感计算应用，如针对患者的压力或疼痛评估。实验结果表明，MuSACo在多个挑战性多模态ER数据集上优于现有的MSDA方法。

## 🔬 方法详解

**问题定义**：本文旨在解决个性化表情识别中的多模态适应问题。现有方法通常将多个源融合为单一领域，未能有效捕捉个体特征，导致识别准确性不足。

**核心思路**：MuSACo通过协同训练，利用多个模态的互补信息进行个体特定的选择与适应。该方法强调在不同模态间的特征对齐，以增强模型的个体适应能力。

**技术框架**：MuSACo的整体架构包括源选择、伪标签生成和特征对齐三个主要模块。首先，选择与目标个体相关的源个体；其次，利用主导模态生成伪标签；最后，对源特征进行对齐，并仅结合自信的目标特征。

**关键创新**：MuSACo的创新在于其多模态选择与适应机制，能够在保留个体特征的同时，避免信息的过度融合。这一设计使得模型在处理个体差异时更加灵活和有效。

**关键设计**：MuSACo采用了类感知损失与类无关损失的结合，确保模型在处理不确定样本时仍能学习有效特征。此外，特征对齐策略确保了不同模态间的信息互补性。

## 📊 实验亮点

在BioVid、StressID和BAH等多个挑战性多模态ER数据集上，MuSACo的表现显著优于传统的UDA方法和最新的MSDA方法，具体提升幅度达到XX%（具体数据未知），展示了其在个性化表情识别中的有效性与优势。

## 🎯 应用场景

MuSACo在数字健康领域具有广泛的应用潜力，尤其是在患者特定的情感评估中，如压力和疼痛的识别。通过提高个体特征的捕捉能力，该方法能够为医疗决策提供更精准的支持，促进个性化医疗的发展。

## 📄 摘要（原文）

> Personalized expression recognition (ER) involves adapting a machine learning model to subject-specific data for improved recognition of expressions with considerable interpersonal variability. Subject-specific ER can benefit significantly from multi-source domain adaptation (MSDA) methods, where each domain corresponds to a specific subject to improve model accuracy and robustness. Despite promising results, state-of-the-art MSDA approaches often overlook multimodal information or blend sources into a single domain, limiting subject diversity and failing to explicitly capture unique subject-specific characteristics. To address these limitations, we introduce MuSACo, a multimodal subject-specific selection and adaptation method for ER based on co-training. It leverages complementary information across multiple modalities and multiple source domains for subject-specific adaptation. This makes MuSACo particularly relevant for affective computing applications in digital health, such as patient-specific assessment for stress or pain, where subject-level nuances are crucial. MuSACo selects source subjects relevant to the target and generates pseudo-labels using the dominant modality for class-aware learning, in conjunction with a class-agnostic loss to learn from less confident target samples. Finally, source features from each modality are aligned, while only confident target features are combined. Experimental results on challenging multimodal ER datasets: BioVid, StressID, and BAH show that MuSACo outperforms UDA (blending) and state-of-the-art MSDA methods.

