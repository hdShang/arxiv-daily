---
layout: default
title: STG: Spatiotemporal Graph Neural Network with Fusion and Spatiotemporal Decoupling Learning for Prognostic Prediction of Colorectal Cancer Liver Metastasis
---

# STG: Spatiotemporal Graph Neural Network with Fusion and Spatiotemporal Decoupling Learning for Prognostic Prediction of Colorectal Cancer Liver Metastasis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03123" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03123v1</a>
  <a href="https://arxiv.org/pdf/2505.03123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03123v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03123v1', 'STG: Spatiotemporal Graph Neural Network with Fusion and Spatiotemporal Decoupling Learning for Prognostic Prediction of Colorectal Cancer Liver Metastasis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiran Zhu, Wei Yang, Yan su, Zesheng Li, Chengchang Pan, Honggang Qi

**分类**: eess.IV, cs.CV, cs.MM

**发布日期**: 2025-05-06

**备注**: 9 pages, 4 figures, 5 tables

---

## 💡 一句话要点

**提出STG框架以解决结直肠癌肝转移预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时空图神经网络` `结直肠癌` `肝转移` `多模态数据` `预测模型` `个性化治疗` `对比学习` `GraphSAGE`

## 📋 核心要点

1. 现有的临床模型未能有效整合肿瘤的空间异质性和动态演变，导致预测准确性不足。
2. 本文提出的STG框架通过异构图结构联合建模肿瘤分布与时间演变，提升了模型的预测能力。
3. 在MSKCC CRLM数据集上，模型实现了85%的准确率和1.1005的平均绝对误差，显著优于现有方法。

## 📝 摘要（中文）

本文提出了一种多模态时空图神经网络（STG）框架，用于预测结直肠癌肝转移（CRLM）的进展。现有临床模型未能有效整合肿瘤的空间异质性、动态演变及复杂的多模态数据关系，限制了预测准确性。STG框架将术前CT影像和临床数据结合成异构图结构，通过空间拓扑和跨模态边缘实现肿瘤分布与时间演变的联合建模。该框架利用GraphSAGE聚合时空邻域信息，并采用监督学习和对比学习策略增强模型捕捉时间特征的能力。模型的轻量化版本减少了78.55%的参数数量，同时保持接近最先进的性能。实验结果显示，该模型在MSKCC CRLM数据集上的时间邻接准确率达到85%，平均绝对误差为1.1005，显著优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决结直肠癌肝转移的预测问题，现有方法在整合肿瘤空间异质性和动态演变方面存在不足，限制了预测的准确性。

**核心思路**：STG框架通过构建异构图，将术前CT影像与临床数据结合，利用空间拓扑和跨模态边缘实现肿瘤分布与时间演变的联合建模，从而提升预测能力。

**技术框架**：该框架主要包括异构图构建、GraphSAGE聚合时空邻域信息、监督学习与对比学习策略等模块，整体流程为数据输入、图结构构建、特征聚合与模型训练。

**关键创新**：创新性地提出了异构图构建和时空解耦机制，能够有效揭示动态肿瘤微环境变化与预后的关联，提供个性化治疗决策的量化支持。

**关键设计**：模型采用GraphSAGE进行特征聚合，结合监督损失和对比损失，提升特征表示的可区分性和跨模态一致性，同时轻量化版本减少了78.55%的参数数量。

## 📊 实验亮点

实验结果显示，STG框架在MSKCC CRLM数据集上实现了85%的时间邻接准确率和1.1005的平均绝对误差，显著优于现有方法，展示了其在肿瘤预测中的有效性与优势。

## 🎯 应用场景

该研究在肿瘤学领域具有重要的应用潜力，能够为结直肠癌肝转移患者提供更精准的预后预测，辅助临床医生制定个性化治疗方案。未来，该方法有望推广至其他类型癌症的预测与治疗决策支持中。

## 📄 摘要（原文）

> We propose a multimodal spatiotemporal graph neural network (STG) framework to predict colorectal cancer liver metastasis (CRLM) progression. Current clinical models do not effectively integrate the tumor's spatial heterogeneity, dynamic evolution, and complex multimodal data relationships, limiting their predictive accuracy. Our STG framework combines preoperative CT imaging and clinical data into a heterogeneous graph structure, enabling joint modeling of tumor distribution and temporal evolution through spatial topology and cross-modal edges. The framework uses GraphSAGE to aggregate spatiotemporal neighborhood information and leverages supervised and contrastive learning strategies to enhance the model's ability to capture temporal features and improve robustness. A lightweight version of the model reduces parameter count by 78.55%, maintaining near-state-of-the-art performance. The model jointly optimizes recurrence risk regression and survival analysis tasks, with contrastive loss improving feature representational discriminability and cross-modal consistency. Experimental results on the MSKCC CRLM dataset show a time-adjacent accuracy of 85% and a mean absolute error of 1.1005, significantly outperforming existing methods. The innovative heterogeneous graph construction and spatiotemporal decoupling mechanism effectively uncover the associations between dynamic tumor microenvironment changes and prognosis, providing reliable quantitative support for personalized treatment decisions.

