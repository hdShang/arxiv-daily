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

**提出CITab框架以解决跨队列图像-表格自监督学习中的异构表格数据建模障碍问题。**

**关键词**: `自监督学习` `多模态融合` `医学图像分析` `表格数据处理` `跨队列学习` `异构数据建模` `阿尔茨海默病诊断` `语义感知建模`

## 📋 核心要点

1. 现有自监督学习方法在图像-表格多模态学习中面临跨队列迁移困难，主要由于异构表格数据的僵化建模机制阻碍了知识共享。
2. CITab框架通过语义感知的表格建模整合列标题作为语义线索，并引入原型引导的线性混合层模块，以专业化处理表格数据异构性。
3. 在阿尔茨海默病诊断任务中，CITab在三个公开队列上超越现有方法，验证了其有效性和可扩展性。

## 📝 摘要（中文）

近年来，整合医学图像和表格数据的多模态学习显著推动了临床决策的进步。自监督学习已成为在这些大规模未标记图像-表格数据上进行预训练的强大范式，旨在学习判别性表示。然而，现有的图像-表格表示学习自监督方法通常局限于特定数据队列，主要由于其在建模异构表格数据时采用僵化的表格建模机制。这种跨表格障碍阻碍了多模态自监督方法有效学习跨不同队列共享的可迁移医学知识。本文提出了一种新颖的自监督学习框架，即CITab，旨在以跨表格方式学习强大的多模态特征表示。我们从语义感知的角度设计表格建模机制，通过整合列标题作为语义线索，促进可迁移知识学习和利用多个数据源进行预训练的可扩展性。此外，我们提出了原型引导的线性混合层模块用于表格特征专业化，使模型能够有效处理表格数据的异构性并探索潜在的医学概念。我们在包含4,461名受试者的三个公开数据队列上对阿尔茨海默病诊断任务进行了全面评估。实验结果表明，CITab优于最先进的方法，为有效且可扩展的跨表格多模态学习铺平了道路。

## 🔬 方法详解

CITab是一个自监督学习框架，整体架构包括图像编码器、表格编码器和多模态融合模块。关键技术创新点在于：从语义感知角度设计表格建模机制，通过列标题作为语义线索增强跨队列知识迁移；引入原型引导的线性混合层模块，动态调整线性层以专业化处理表格数据的异构性，探索潜在医学概念。与现有方法的主要区别在于，它打破了跨表格障碍，通过更灵活的表格建模支持多源数据预训练，而传统方法通常依赖固定结构，限制了可扩展性和迁移能力。

## 📊 实验亮点

在包含4,461名受试者的三个公开阿尔茨海默病数据队列上，CITab在诊断任务中显著优于现有最先进方法，证明了其在跨队列场景下的优越性能和可扩展性，为多模态医学学习提供了有效解决方案。

## 🎯 应用场景

该研究主要应用于医学领域，如阿尔茨海默病等疾病的诊断和预测，通过整合医学图像和临床表格数据，提升临床决策的准确性和效率。潜在价值包括支持跨医院或研究队列的数据融合，促进大规模多模态医学AI模型的开发。

## 📄 摘要（原文）

> Multi-modal learning integrating medical images and tabular data has significantly advanced clinical decision-making in recent years. Self-Supervised Learning (SSL) has emerged as a powerful paradigm for pretraining these models on large-scale unlabeled image-tabular data, aiming to learn discriminative representations. However, existing SSL methods for image-tabular representation learning are often confined to specific data cohorts, mainly due to their rigid tabular modeling mechanisms when modeling heterogeneous tabular data. This inter-tabular barrier hinders the multi-modal SSL methods from effectively learning transferrable medical knowledge shared across diverse cohorts. In this paper, we propose a novel SSL framework, namely CITab, designed to learn powerful multi-modal feature representations in a cross-tabular manner. We design the tabular modeling mechanism from a semantic-awareness perspective by integrating column headers as semantic cues, which facilitates transferrable knowledge learning and the scalability in utilizing multiple data sources for pretraining. Additionally, we propose a prototype-guided mixture-of-linear layer (P-MoLin) module for tabular feature specialization, empowering the model to effectively handle the heterogeneity of tabular data and explore the underlying medical concepts. We conduct comprehensive evaluations on Alzheimer's disease diagnosis task across three publicly available data cohorts containing 4,461 subjects. Experimental results demonstrate that CITab outperforms state-of-the-art approaches, paving the way for effective and scalable cross-tabular multi-modal learning.

