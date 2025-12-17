---
layout: default
title: Multi-View MRI Approach for Classification of MGMT Methylation in Glioblastoma Patients
---

# Multi-View MRI Approach for Classification of MGMT Methylation in Glioblastoma Patients

**arXiv**: [2512.14232v1](https://arxiv.org/abs/2512.14232) | [PDF](https://arxiv.org/pdf/2512.14232.pdf)

**作者**: Rawan Alyahya, Asrar Alruwayqi, Atheer Alqarni, Asma Alkhaldi, Metab Alkubeyyer, Xin Gao, Mona Alshahrani

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出多视图MRI方法，利用空间关系检测胶质母细胞瘤MGMT甲基化状态，避免复杂3D模型问题。**

**关键词**: `胶质母细胞瘤` `MGMT甲基化检测` `多视图MRI` `放射基因组学` `深度学习模型` `非侵入性诊断` `精准医学` `肿瘤切片提取`

## 📋 核心要点

1. 核心问题：现有MGMT甲基化检测依赖侵入性活检，缺乏高效非侵入性方法，且复杂3D模型存在参数多、收敛慢、内存需求大等问题。
2. 方法要点：提出多视图MRI方法，利用空间关系整合三个视图信息，避免复杂3D模型，并引入新肿瘤切片提取技术提升性能。
3. 实验或效果：通过对比实验，新方法在多个评估指标上优于现有方法，验证了其有效性和非侵入性检测潜力。

## 📝 摘要（中文）

MGMT启动子甲基化的存在显著影响胶质母细胞瘤（GBM）患者化疗效果。目前，MGMT启动子甲基化的确认依赖于侵入性脑肿瘤组织活检。本研究探索了放射基因组学技术，这是一种在精准医学中具有前景的方法，旨在从医学图像中识别遗传标记。利用MRI扫描和深度学习模型，我们提出了一种新的多视图方法，考虑MRI视图之间的空间关系来检测MGMT甲基化状态。重要的是，我们的方法从所有三个视图中提取信息，而不使用复杂的3D深度学习模型，避免了高参数数量、收敛缓慢和大量内存需求等问题。我们还引入了一种新的肿瘤切片提取技术，并基于多个评估指标展示了其优于现有方法的优势。通过将我们的方法与最先进的模型进行比较，我们证明了该方法的有效性。此外，我们分享了已发表模型的可重复流程，鼓励透明度和稳健诊断工具的开发。我们的研究突出了非侵入性方法识别MGMT启动子甲基化的潜力，并有助于推进GBM治疗中的精准医学。

## 🔬 方法详解

整体框架基于多视图MRI和深度学习模型，核心思想是通过整合轴向、冠状和矢状三个MRI视图的空间关系来检测MGMT甲基化状态。关键技术创新点包括：采用多视图方法而非复杂3D模型，避免了高参数和内存问题；引入新的肿瘤切片提取技术，优化了图像预处理步骤。与现有方法的主要区别在于，该方法不依赖3D卷积神经网络，而是通过多视图融合捕捉空间信息，从而在保持性能的同时降低了计算复杂度，提高了实用性和可扩展性。

## 📊 实验亮点

最重要的实验结果：新方法在多个评估指标上优于现有最先进模型，验证了多视图方法的有效性；新肿瘤切片提取技术显著提升了性能，展示了技术优势；整体方法避免了3D模型的复杂性问题，实现了高效且稳健的MGMT甲基化状态检测。

## 🎯 应用场景

该研究主要应用于胶质母细胞瘤的精准医疗领域，潜在价值包括：为非侵入性MGMT甲基化检测提供新工具，辅助化疗方案制定；推动放射基因组学在临床诊断中的应用，减少患者侵入性活检风险；促进透明和可重复的AI诊断流程开发，提升医疗AI的可靠性和普及性。

## 📄 摘要（原文）

> The presence of MGMT promoter methylation significantly affects how well chemotherapy works for patients with Glioblastoma Multiforme (GBM). Currently, confirmation of MGMT promoter methylation relies on invasive brain tumor tissue biopsies. In this study, we explore radiogenomics techniques, a promising approach in precision medicine, to identify genetic markers from medical images. Using MRI scans and deep learning models, we propose a new multi-view approach that considers spatial relationships between MRI views to detect MGMT methylation status. Importantly, our method extracts information from all three views without using a complicated 3D deep learning model, avoiding issues associated with high parameter count, slow convergence, and substantial memory demands. We also introduce a new technique for tumor slice extraction and show its superiority over existing methods based on multiple evaluation metrics. By comparing our approach to state-of-the-art models, we demonstrate the efficacy of our method. Furthermore, we share a reproducible pipeline of published models, encouraging transparency and the development of robust diagnostic tools. Our study highlights the potential of non-invasive methods for identifying MGMT promoter methylation and contributes to advancing precision medicine in GBM treatment.

