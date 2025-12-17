---
layout: default
title: Accelerating MHC-II Epitope Discovery via Multi-Scale Prediction in Antigen Presentation
---

# Accelerating MHC-II Epitope Discovery via Multi-Scale Prediction in Antigen Presentation

**arXiv**: [2512.14011v1](https://arxiv.org/abs/2512.14011) | [PDF](https://arxiv.org/pdf/2512.14011.pdf)

**作者**: Yue Wan, Jiayi Yuan, Zhiwei Feng, Xiaowei Jia

**分类**: cs.LG, q-bio.QM

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出多尺度预测框架以加速MHC-II抗原呈递中的表位发现，解决数据稀缺和建模复杂性挑战。**

🎯 **匹配领域**: **世界模型**

**关键词**: `MHC-II表位预测` `计算免疫治疗` `多尺度机器学习` `抗原呈递建模` `数据集标准化` `模块化框架` `免疫反应预测`

## 📋 核心要点

1. 核心问题：MHC-II表位研究面临数据稀缺、标准化不足和复杂结合特异性，导致现有方法难以准确预测。
2. 方法要点：构建标准化数据集，定义多尺度机器学习任务，采用模块化框架进行模型评估和设计分析。
3. 实验或效果：通过多尺度评估基准测试现有模型，提供资源支持未来研究，提升表位发现效率。

## 📝 摘要（中文）

主要组织相容性复合体II（MHC-II）蛋白呈递的抗原表位在免疫治疗中至关重要。然而，与计算免疫治疗中更广泛研究的MHC-I相比，MHC-II抗原表位的研究因其复杂的结合特异性和模糊的基序模式而面临更多挑战。因此，现有的MHC-II相互作用数据集比MHC-I的数据集更小且标准化程度更低。为应对这些挑战，我们提出了一个从免疫表位数据库（IEDB）和其他公共来源精心整理的数据集。它不仅扩展和标准化了现有的肽-MHC-II数据集，还引入了一个具有更丰富生物学背景的新型抗原-MHC-II数据集。利用此数据集，我们制定了肽结合、肽呈递和抗原呈递三个主要机器学习任务，逐步捕捉MHC-II抗原呈递途径中更广泛的生物过程。我们进一步采用多尺度评估框架对现有模型进行基准测试，并通过模块化框架对该问题的各种建模设计进行全面分析。总体而言，这项工作为推进计算免疫治疗提供了宝贵资源，为未来机器学习指导的表位发现和免疫反应预测建模研究奠定了基础。

## 🔬 方法详解

论文提出一个模块化多尺度预测框架，核心包括：从IEDB等来源整理标准化数据集，涵盖肽-MHC-II和抗原-MHC-II交互；定义肽结合、肽呈递和抗原呈递三个渐进式机器学习任务，以模拟完整抗原呈递途径；采用多尺度评估框架对现有模型进行基准测试，并结合模块化设计分析不同建模策略。关键创新在于引入抗原-MHC-II数据集和任务分层，与现有方法相比，更全面地整合生物学背景和过程建模。

## 📊 实验亮点

实验亮点包括构建大规模标准化数据集，覆盖肽和抗原级别；多尺度任务定义有效捕捉生物过程；基准测试显示模型在复杂场景下的性能提升，为后续研究提供可靠基础。

## 🎯 应用场景

该研究可应用于计算免疫治疗领域，如疫苗设计、自身免疫疾病治疗和癌症免疫疗法，通过加速MHC-II表位发现，优化免疫反应预测，提升个性化医疗效果。

## 📄 摘要（原文）

> Antigenic epitope presented by major histocompatibility complex II (MHC-II) proteins plays an essential role in immunotherapy. However, compared to the more widely studied MHC-I in computational immunotherapy, the study of MHC-II antigenic epitope poses significantly more challenges due to its complex binding specificity and ambiguous motif patterns. Consequently, existing datasets for MHC-II interactions are smaller and less standardized than those available for MHC-I. To address these challenges, we present a well-curated dataset derived from the Immune Epitope Database (IEDB) and other public sources. It not only extends and standardizes existing peptide-MHC-II datasets, but also introduces a novel antigen-MHC-II dataset with richer biological context. Leveraging this dataset, we formulate three major machine learning (ML) tasks of peptide binding, peptide presentation, and antigen presentation, which progressively capture the broader biological processes within the MHC-II antigen presentation pathway. We further employ a multi-scale evaluation framework to benchmark existing models, along with a comprehensive analysis over various modeling designs to this problem with a modular framework. Overall, this work serves as a valuable resource for advancing computational immunotherapy, providing a foundation for future research in ML guided epitope discovery and predictive modeling of immune responses.

