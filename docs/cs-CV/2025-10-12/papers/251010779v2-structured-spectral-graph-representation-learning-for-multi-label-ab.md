---
layout: default
title: Structured Spectral Graph Representation Learning for Multi-label Abnormality Analysis from 3D CT Scans
---

# Structured Spectral Graph Representation Learning for Multi-label Abnormality Analysis from 3D CT Scans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10779" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10779v2</a>
  <a href="https://arxiv.org/pdf/2510.10779.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10779v2" onclick="toggleFavorite(this, '2510.10779v2', 'Structured Spectral Graph Representation Learning for Multi-label Abnormality Analysis from 3D CT Scans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Theo Di Piazza, Carole Lazarus, Olivier Nempont, Loic Boussel

**分类**: cs.CV

**发布日期**: 2025-10-12 (更新: 2025-10-23)

**备注**: 24 pages, 15 figures

---

## 💡 一句话要点

**提出基于结构化谱图表示学习的3D CT多标签异常分析方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D CT扫描` `多标签分类` `谱图卷积` `医学影像分析` `异常检测`

## 📋 核心要点

1. 3D CT多标签异常分析面临挑战，现有3D CNN难以捕捉长程依赖，Vision Transformer依赖大规模预训练。
2. 提出一种基于结构化图的2.5D方法，将3D CT表示为图，利用谱图卷积处理切片间依赖。
3. 在三个数据集上验证，实现跨数据集泛化，性能与SOTA视觉编码器相当，并扩展到报告生成。

## 📝 摘要（中文）

随着CT检查数量的增长，对自动化工具（如器官分割、异常检测和报告生成）的需求日益增加，以支持放射科医生管理临床工作量。3D胸部CT扫描的多标签分类仍然是一个关键但具有挑战性的问题，因为容积数据中固有的复杂空间关系和异常的广泛变异性。现有的基于3D卷积神经网络的方法难以捕捉长程依赖关系，而Vision Transformers通常需要在大规模、特定领域的数据集上进行广泛的预训练才能表现出竞争力。本文提出了一种2.5D替代方案，引入了一种新的基于图的框架，该框架将3D CT体数据表示为结构化图，其中轴向切片三元组作为节点，通过谱图卷积进行处理，使模型能够推理切片间的依赖关系，同时保持与临床部署兼容的复杂度。我们的方法在来自独立机构的3个数据集上进行训练和评估，实现了强大的跨数据集泛化，并显示出与最先进的视觉编码器相比具有竞争力的性能。我们进一步进行了全面的消融研究，以评估各种聚合策略、边缘加权方案和图连接模式的影响。此外，我们通过在自动放射报告生成和腹部CT数据上的迁移实验，证明了我们方法的更广泛适用性。

## 🔬 方法详解

**问题定义**：论文旨在解决3D CT扫描图像中多标签异常分析的问题。现有方法，如3D CNN，难以捕捉CT图像中存在的长程依赖关系，而Vision Transformer需要大量特定领域的数据进行预训练，这在实际应用中可能难以满足。因此，需要一种能够有效建模长程依赖关系，同时对数据量需求较低的方法。

**核心思路**：论文的核心思路是将3D CT体数据转换为结构化的图表示，利用图神经网络来建模切片之间的依赖关系。通过将相邻的轴向切片三元组作为图的节点，并利用谱图卷积来处理这些节点，模型可以有效地学习切片之间的空间关系和长程依赖。这种方法在降低计算复杂度的同时，保留了3D信息的关键特征。

**技术框架**：该方法主要包含以下几个阶段：1) **数据预处理**：将3D CT扫描数据分割成一系列轴向切片。2) **图构建**：将相邻的三个轴向切片组成一个节点，构建图结构。节点之间的连接方式可以根据不同的策略进行选择，例如k近邻或全连接。3) **谱图卷积**：使用谱图卷积神经网络对图进行处理，学习节点的表示。4) **分类**：将学习到的节点表示输入到分类器中，预测每个CT扫描图像的多标签异常。

**关键创新**：该方法的关键创新在于使用结构化的谱图表示来建模3D CT数据。与传统的3D CNN相比，该方法能够更好地捕捉长程依赖关系，并且计算复杂度更低。与Vision Transformer相比，该方法不需要大规模的预训练数据，更适用于实际应用。

**关键设计**：在图构建方面，论文研究了不同的连接策略，例如k近邻和全连接。在谱图卷积方面，论文使用了ChebNets，这是一种高效的谱图卷积方法。在损失函数方面，论文使用了二元交叉熵损失函数，用于多标签分类任务。此外，论文还研究了不同的聚合策略和边缘加权方案，以进一步提高模型的性能。

## 📊 实验亮点

该方法在三个独立机构的数据集上进行了评估，实现了强大的跨数据集泛化能力，并且性能与最先进的视觉编码器相比具有竞争力。消融研究表明，不同的聚合策略、边缘加权方案和图连接模式对模型性能有显著影响。迁移实验证明了该方法在自动放射报告生成和腹部CT数据上的适用性。

## 🎯 应用场景

该研究成果可应用于医学影像分析领域，辅助放射科医生进行疾病诊断和报告生成，提高诊断效率和准确性。该方法具有良好的跨数据集泛化能力，有望在不同医疗机构的CT数据上推广应用。此外，该方法还可以扩展到其他3D医学影像数据，如MRI和PET，具有广泛的应用前景。

## 📄 摘要（原文）

> With the growing volume of CT examinations, there is an increasing demand for automated tools such as organ segmentation, abnormality detection, and report generation to support radiologists in managing their clinical workload. Multi-label classification of 3D Chest CT scans remains a critical yet challenging problem due to the complex spatial relationships inherent in volumetric data and the wide variability of abnormalities. Existing methods based on 3D convolutional neural networks struggle to capture long-range dependencies, while Vision Transformers often require extensive pre-training on large-scale, domain-specific datasets to perform competitively. In this work of academic research, we propose a 2.5D alternative by introducing a new graph-based framework that represents 3D CT volumes as structured graphs, where axial slice triplets serve as nodes processed through spectral graph convolution, enabling the model to reason over inter-slice dependencies while maintaining complexity compatible with clinical deployment. Our method, trained and evaluated on 3 datasets from independent institutions, achieves strong cross-dataset generalization, and shows competitive performance compared to state-of-the-art visual encoders. We further conduct comprehensive ablation studies to evaluate the impact of various aggregation strategies, edge-weighting schemes, and graph connectivity patterns. Additionally, we demonstrate the broader applicability of our approach through transfer experiments on automated radiology report generation and abdominal CT data.

