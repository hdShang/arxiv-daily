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

**提出多视图MRI方法，利用空间关系和深度学习非侵入性检测胶质母细胞瘤MGMT甲基化状态。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `放射基因组学` `多视图MRI` `深度学习` `MGMT甲基化检测` `胶质母细胞瘤` `非侵入性诊断` `精准医学` `肿瘤切片提取`

## 📋 核心要点

1. 核心问题：现有MGMT甲基化检测依赖侵入性活检，风险高且耗时，而传统3D深度学习模型参数多、收敛慢、内存需求大。
2. 方法要点：提出多视图MRI方法，结合空间关系和深度学习，从三个视图提取信息，避免复杂3D模型，并引入新肿瘤切片提取技术。
3. 实验或效果：新方法在多个评估指标上优于现有方法，展示了非侵入性检测的潜力，并提供了可复现流程。

## 📝 摘要（中文）

MGMT启动子甲基化的存在显著影响胶质母细胞瘤（GBM）患者化疗效果。目前，确认MGMT启动子甲基化依赖于侵入性脑肿瘤组织活检。本研究探索了放射基因组学技术，这是一种在精准医学中前景广阔的方法，旨在从医学图像中识别遗传标记。利用MRI扫描和深度学习模型，我们提出了一种新的多视图方法，考虑MRI视图之间的空间关系来检测MGMT甲基化状态。重要的是，我们的方法从所有三个视图中提取信息，而不使用复杂的3D深度学习模型，避免了高参数数量、收敛慢和大量内存需求等问题。我们还引入了一种新的肿瘤切片提取技术，并基于多个评估指标展示了其优于现有方法的性能。通过将我们的方法与最先进模型进行比较，我们证明了该方法的有效性。此外，我们分享了已发表模型的可复现流程，鼓励透明度和稳健诊断工具的开发。我们的研究突出了非侵入性方法识别MGMT启动子甲基化的潜力，并有助于推进GBM治疗中的精准医学。

## 🔬 方法详解

论文提出一个多视图MRI框架，用于MGMT甲基化分类。整体框架基于深度学习模型，从MRI的三个视图（如轴向、冠状、矢状）提取特征，并考虑视图间的空间关系进行融合，以增强信息表示。关键技术创新点包括：避免使用复杂3D模型，通过多视图方法减少参数和内存需求；引入新的肿瘤切片提取技术，提高数据预处理效率。与现有方法的主要区别在于：传统方法常依赖单一视图或复杂3D模型，而本方法通过多视图融合和简化架构，在保持性能的同时降低了计算负担。

## 📊 实验亮点

实验结果显示，新方法在MGMT甲基化分类任务中，基于多个评估指标（如准确率、灵敏度）优于现有最先进模型。肿瘤切片提取技术的引入显著提升了性能，同时多视图框架避免了3D模型的高计算成本，实现了高效且稳健的检测。

## 🎯 应用场景

该研究在精准医学领域有重要应用，特别是胶质母细胞瘤（GBM）治疗。通过非侵入性MRI扫描检测MGMT甲基化状态，可辅助临床决策，优化化疗方案，减少患者活检风险。此外，方法可推广至其他脑肿瘤或癌症的遗传标记检测，推动个性化医疗发展。

## 📄 摘要（原文）

> The presence of MGMT promoter methylation significantly affects how well chemotherapy works for patients with Glioblastoma Multiforme (GBM). Currently, confirmation of MGMT promoter methylation relies on invasive brain tumor tissue biopsies. In this study, we explore radiogenomics techniques, a promising approach in precision medicine, to identify genetic markers from medical images. Using MRI scans and deep learning models, we propose a new multi-view approach that considers spatial relationships between MRI views to detect MGMT methylation status. Importantly, our method extracts information from all three views without using a complicated 3D deep learning model, avoiding issues associated with high parameter count, slow convergence, and substantial memory demands. We also introduce a new technique for tumor slice extraction and show its superiority over existing methods based on multiple evaluation metrics. By comparing our approach to state-of-the-art models, we demonstrate the efficacy of our method. Furthermore, we share a reproducible pipeline of published models, encouraging transparency and the development of robust diagnostic tools. Our study highlights the potential of non-invasive methods for identifying MGMT promoter methylation and contributes to advancing precision medicine in GBM treatment.

