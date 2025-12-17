---
layout: default
title: Evaluating Fundus-Specific Foundation Models for Diabetic Macular Edema Detection
---

# Evaluating Fundus-Specific Foundation Models for Diabetic Macular Edema Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07277" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07277v1</a>
  <a href="https://arxiv.org/pdf/2510.07277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07277v1" onclick="toggleFavorite(this, '2510.07277v1', 'Evaluating Fundus-Specific Foundation Models for Diabetic Macular Edema Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Franco Javier Arellano, José Ignacio Orlando

**分类**: cs.CV

**发布日期**: 2025-10-08

**备注**: Accepted for publication at SIPAIM 2025

---

## 💡 一句话要点

**评估眼底特有的基础模型在糖尿病黄斑水肿检测中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `糖尿病黄斑水肿检测` `眼底图像分析` `基础模型` `迁移学习` `深度学习` `卷积神经网络` `数据稀缺`

## 📋 核心要点

1. 深度学习在DME检测中受限于标注数据不足，影响了模型的泛化能力和实际应用效果。
2. 论文对比了眼底图像专用基础模型RETFound和FLAIR，以及EfficientNet-B0在DME检测中的性能。
3. 实验结果表明，在DME检测任务中，微调后的CNN模型通常优于基础模型，尤其是在数据稀缺的环境下。

## 📝 摘要（中文）

糖尿病黄斑水肿(DME)是糖尿病视网膜病变(DR)患者视力丧失的主要原因。虽然深度学习在自动检测眼底图像中的DME方面显示出希望，但由于带注释数据的有限性，其应用仍然具有挑战性。基础模型(FM)已成为一种替代解决方案。然而，尚不清楚它们是否能特别应对DME检测。本文系统地比较了不同的FM和标准迁移学习方法来完成这项任务。具体来说，我们比较了两种最流行的视网膜图像FM——RETFound和FLAIR——以及EfficientNet-B0骨干网络，在IDRiD、MESSIDOR-2和OCT-and-Eye-Fundus-Images (OEFI)中，跨不同的训练方案和评估设置进行比较。结果表明，尽管规模庞大，但在该任务中，FM并没有始终优于微调的CNN。特别是，在大多数评估设置中，EfficientNet-B0在ROC曲线和精确率/召回率曲线下的面积方面排名第一或第二，RETFound仅在OEFI中显示出有希望的结果。另一方面，FLAIR展示了有竞争力的零样本性能，在适当提示时实现了显著的AUC-PR分数。这些发现表明，即使在微调后，FM可能也不是用于DME检测等细粒度眼科任务的好工具，这表明轻量级CNN在数据稀缺环境中仍然是强大的基线。

## 🔬 方法详解

**问题定义**：论文旨在解决糖尿病黄斑水肿（DME）的自动检测问题。现有方法，特别是基于深度学习的方法，在数据量不足的情况下表现不佳，泛化能力受限。虽然基础模型在其他领域表现出色，但其在DME检测中的有效性尚不明确，需要系统评估。

**核心思路**：论文的核心思路是通过对比分析不同的基础模型（RETFound和FLAIR）以及传统的卷积神经网络（EfficientNet-B0）在DME检测任务中的性能，来评估基础模型是否能够有效解决数据稀缺问题。通过多种训练策略和评估设置，探究不同模型在不同数据集上的表现。

**技术框架**：论文采用的整体框架是比较不同模型在DME检测任务中的性能。主要包括以下几个阶段：1) 数据集准备：使用IDRiD、MESSIDOR-2和OEFI三个数据集。2) 模型选择：选择RETFound、FLAIR和EfficientNet-B0作为对比模型。3) 训练策略：采用不同的训练方案，包括微调和零样本学习。4) 评估指标：使用ROC曲线下面积（AUC）和精确率/召回率曲线下面积（AUC-PR）作为评估指标。5) 结果分析：对比不同模型在不同数据集和训练策略下的性能。

**关键创新**：论文的关键创新在于系统性地评估了眼底图像专用基础模型在DME检测任务中的性能，并与传统的卷积神经网络进行了对比。研究结果表明，在数据稀缺的环境下，基础模型并没有始终优于微调的CNN，这挑战了基础模型在所有视觉任务中都优于传统方法的普遍认知。

**关键设计**：论文的关键设计包括：1) 选择RETFound和FLAIR作为眼底图像专用基础模型，并与EfficientNet-B0进行对比。2) 在IDRiD、MESSIDOR-2和OEFI三个数据集上进行评估，以验证模型的泛化能力。3) 采用不同的训练策略，包括微调和零样本学习，以探究不同模型的最佳训练方式。4) 使用AUC和AUC-PR作为评估指标，全面评估模型的性能。

## 📊 实验亮点

实验结果表明，EfficientNet-B0在大多数评估设置中，其ROC曲线下面积和精确率/召回率曲线下面积排名第一或第二，优于RETFound和FLAIR。FLAIR在零样本学习中表现出竞争力，在适当提示下实现了显著的AUC-PR分数。这些结果表明，在DME检测任务中，微调的CNN模型可能比基础模型更有效。

## 🎯 应用场景

该研究成果可应用于眼科疾病的早期筛查和诊断，特别是糖尿病视网膜病变引起的黄斑水肿。通过自动检测DME，可以帮助医生更快速、准确地诊断病情，从而及早进行干预治疗，防止视力进一步恶化。该研究对于提升医疗诊断效率、降低医疗成本具有重要意义。

## 📄 摘要（原文）

> Diabetic Macular Edema (DME) is a leading cause of vision loss among patients with Diabetic Retinopathy (DR). While deep learning has shown promising results for automatically detecting this condition from fundus images, its application remains challenging due the limited availability of annotated data. Foundation Models (FM) have emerged as an alternative solution. However, it is unclear if they can cope with DME detection in particular. In this paper, we systematically compare different FM and standard transfer learning approaches for this task. Specifically, we compare the two most popular FM for retinal images--RETFound and FLAIR--and an EfficientNet-B0 backbone, across different training regimes and evaluation settings in IDRiD, MESSIDOR-2 and OCT-and-Eye-Fundus-Images (OEFI). Results show that despite their scale, FM do not consistently outperform fine-tuned CNNs in this task. In particular, an EfficientNet-B0 ranked first or second in terms of area under the ROC and precision/recall curves in most evaluation settings, with RETFound only showing promising results in OEFI. FLAIR, on the other hand, demonstrated competitive zero-shot performance, achieving notable AUC-PR scores when prompted appropriately. These findings reveal that FM might not be a good tool for fine-grained ophthalmic tasks such as DME detection even after fine-tuning, suggesting that lightweight CNNs remain strong baselines in data-scarce environments.

