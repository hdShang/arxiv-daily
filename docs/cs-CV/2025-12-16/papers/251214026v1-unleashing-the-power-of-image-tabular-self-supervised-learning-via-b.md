---
layout: default
title: Unleashing the Power of Image-Tabular Self-Supervised Learning via Breaking Cross-Tabular Barriers
---

# Unleashing the Power of Image-Tabular Self-Supervised Learning via Breaking Cross-Tabular Barriers

**arXiv**: [2512.14026v1](https://arxiv.org/abs/2512.14026) | [PDF](https://arxiv.org/pdf/2512.14026.pdf)

**作者**: Yibing Fu, Yunpeng Zhao, Zhitao Zeng, Cheng Chen, Yueming Jin

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出CITab框架以解决跨队列图像-表格自监督学习中的表格异构性障碍问题**

🎯 **匹配领域**: **强化学习**

**关键词**: `自监督学习` `多模态融合` `医学图像分析` `表格数据处理` `跨队列学习` `表征学习` `阿尔茨海默病诊断` `语义感知建模`

## 📋 核心要点

1. 现有自监督学习方法因僵化的表格建模机制，难以处理异构表格数据，导致跨队列知识迁移受限。
2. 提出CITab框架，通过语义感知的表格建模和原型引导的线性混合层，实现跨表格多模态表征学习。
3. 在阿尔茨海默病诊断任务中，CITab在三个公开队列上超越现有方法，验证了其有效性和可扩展性。

## 📝 摘要（中文）

近年来，整合医学图像和表格数据的多模态学习显著推动了临床决策的进步。自监督学习已成为在这些大规模未标记图像-表格数据上进行预训练的强大范式，旨在学习判别性表征。然而，现有的图像-表格表征学习自监督方法通常局限于特定数据队列，主要原因是其建模异构表格数据时采用僵化的表格建模机制。这种跨表格障碍阻碍了多模态自监督方法有效学习跨不同队列共享的可迁移医学知识。本文提出了一种新颖的自监督学习框架CITab，旨在以跨表格方式学习强大的多模态特征表征。我们从语义感知的角度设计表格建模机制，通过整合列标题作为语义线索，促进可迁移知识学习以及利用多个数据源进行预训练的可扩展性。此外，我们提出了原型引导的线性混合层模块用于表格特征专业化，使模型能够有效处理表格数据的异构性并探索潜在的医学概念。我们在包含4,461名受试者的三个公开数据队列上对阿尔茨海默病诊断任务进行了全面评估。实验结果表明，CITab优于最先进的方法，为有效且可扩展的跨表格多模态学习铺平了道路。

## 🔬 方法详解

CITab是一个跨表格自监督学习框架，核心创新包括：1）语义感知的表格建模机制，将列标题作为语义线索整合，增强模型对表格结构的理解；2）原型引导的线性混合层模块，通过原型聚类和线性组合实现表格特征专业化，以处理数据异构性。整体框架结合图像和表格模态，通过自监督预训练学习共享表征。与现有方法相比，CITab突破了跨表格障碍，支持多数据源预训练，提升了可迁移性和泛化能力。

## 📊 实验亮点

在包含4,461名受试者的三个公开阿尔茨海默病数据队列上，CITab在诊断任务中显著优于现有最先进方法，证明了其在跨表格多模态学习中的有效性和性能提升。

## 🎯 应用场景

该研究主要应用于医学领域，特别是阿尔茨海默病等疾病的诊断和预测，通过整合医学图像和临床表格数据，提升临床决策的准确性和效率。其跨队列学习能力可扩展到其他多模态医疗数据分析任务。

## 📄 摘要（原文）

> Multi-modal learning integrating medical images and tabular data has significantly advanced clinical decision-making in recent years. Self-Supervised Learning (SSL) has emerged as a powerful paradigm for pretraining these models on large-scale unlabeled image-tabular data, aiming to learn discriminative representations. However, existing SSL methods for image-tabular representation learning are often confined to specific data cohorts, mainly due to their rigid tabular modeling mechanisms when modeling heterogeneous tabular data. This inter-tabular barrier hinders the multi-modal SSL methods from effectively learning transferrable medical knowledge shared across diverse cohorts. In this paper, we propose a novel SSL framework, namely CITab, designed to learn powerful multi-modal feature representations in a cross-tabular manner. We design the tabular modeling mechanism from a semantic-awareness perspective by integrating column headers as semantic cues, which facilitates transferrable knowledge learning and the scalability in utilizing multiple data sources for pretraining. Additionally, we propose a prototype-guided mixture-of-linear layer (P-MoLin) module for tabular feature specialization, empowering the model to effectively handle the heterogeneity of tabular data and explore the underlying medical concepts. We conduct comprehensive evaluations on Alzheimer's disease diagnosis task across three publicly available data cohorts containing 4,461 subjects. Experimental results demonstrate that CITab outperforms state-of-the-art approaches, paving the way for effective and scalable cross-tabular multi-modal learning.

