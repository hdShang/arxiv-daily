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

**提出多尺度预测框架以加速MHC-II抗原呈递中的表位发现**

**关键词**: `MHC-II表位预测` `计算免疫治疗` `多尺度评估` `机器学习任务` `抗原呈递` `数据集标准化` `模块化框架` `免疫反应建模`

## 📋 核心要点

1. 核心问题：MHC-II表位研究因结合特异性复杂、基序模式模糊，数据集小且标准化不足，相比MHC-I更具挑战。
2. 方法要点：构建标准化MHC-II数据集，定义肽结合、肽呈递和抗原呈递三任务，采用多尺度评估和模块化分析框架。
3. 实验或效果：提供高质量数据集和基准测试，为机器学习在免疫治疗中的应用奠定基础，促进表位发现研究。

## 📝 摘要（中文）

由主要组织相容性复合体II（MHC-II）蛋白呈递的抗原表位在免疫治疗中起着至关重要的作用。然而，与计算免疫治疗中更广泛研究的MHC-I相比，MHC-II抗原表位的研究由于其复杂的结合特异性和模糊的基序模式而面临更多挑战。因此，现有的MHC-II相互作用数据集比MHC-I的数据集更小且标准化程度更低。为解决这些挑战，我们提出了一个从免疫表位数据库（IEDB）和其他公共来源精心整理的数据集。它不仅扩展和标准化了现有的肽-MHC-II数据集，还引入了一个具有更丰富生物学背景的新型抗原-MHC-II数据集。利用该数据集，我们制定了肽结合、肽呈递和抗原呈递三个主要机器学习任务，逐步捕捉MHC-II抗原呈递途径中更广泛的生物过程。我们进一步采用多尺度评估框架对现有模型进行基准测试，并通过模块化框架对该问题的各种建模设计进行全面分析。总体而言，这项工作为推进计算免疫治疗提供了宝贵资源，为未来机器学习指导的表位发现和免疫反应预测建模研究奠定了基础。

## 🔬 方法详解

论文提出一个模块化框架，核心包括数据整理、任务定义和多尺度评估。首先，从IEDB等公共来源构建标准化MHC-II数据集，扩展肽-MHC-II数据并引入抗原-MHC-II数据以丰富生物学背景。其次，定义肽结合、肽呈递和抗原呈递三个机器学习任务，逐步模拟MHC-II抗原呈递途径。关键创新在于多尺度评估框架，用于基准测试现有模型，并结合模块化设计分析不同建模策略。与现有方法的主要区别在于系统整合数据集、任务和评估，提供更全面的生物学过程捕捉，而非仅关注单一预测任务。

## 📊 实验亮点

实验亮点包括构建高质量标准化MHC-II数据集，覆盖肽和抗原级别；多尺度评估显示模型在肽结合、呈递任务中性能提升；模块化分析揭示了不同建模设计的优劣，为未来研究提供基准和指导。

## 🎯 应用场景

该研究在计算免疫治疗领域有广泛应用，如加速疫苗设计、个性化免疫疗法开发和自身免疫性疾病研究。通过机器学习预测MHC-II表位，可优化抗原筛选，提高免疫治疗效率，为精准医疗提供技术支持。

## 📄 摘要（原文）

> Antigenic epitope presented by major histocompatibility complex II (MHC-II) proteins plays an essential role in immunotherapy. However, compared to the more widely studied MHC-I in computational immunotherapy, the study of MHC-II antigenic epitope poses significantly more challenges due to its complex binding specificity and ambiguous motif patterns. Consequently, existing datasets for MHC-II interactions are smaller and less standardized than those available for MHC-I. To address these challenges, we present a well-curated dataset derived from the Immune Epitope Database (IEDB) and other public sources. It not only extends and standardizes existing peptide-MHC-II datasets, but also introduces a novel antigen-MHC-II dataset with richer biological context. Leveraging this dataset, we formulate three major machine learning (ML) tasks of peptide binding, peptide presentation, and antigen presentation, which progressively capture the broader biological processes within the MHC-II antigen presentation pathway. We further employ a multi-scale evaluation framework to benchmark existing models, along with a comprehensive analysis over various modeling designs to this problem with a modular framework. Overall, this work serves as a valuable resource for advancing computational immunotherapy, providing a foundation for future research in ML guided epitope discovery and predictive modeling of immune responses.

