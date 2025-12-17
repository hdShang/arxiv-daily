---
layout: default
title: KGOT: Unified Knowledge Graph and Optimal Transport Pseudo-Labeling for Molecule-Protein Interaction Prediction
---

# KGOT: Unified Knowledge Graph and Optimal Transport Pseudo-Labeling for Molecule-Protein Interaction Prediction

**arXiv**: [2512.09365v1](https://arxiv.org/abs/2512.09365) | [PDF](https://arxiv.org/pdf/2512.09365.pdf)

**作者**: Jiayu Qin, Zhengquan Luo, Guy Tadmor, Changyou Chen, David Zeevi, Zhiqiang Xu

---

## 💡 一句话要点

**提出KGOT框架，结合知识图谱与最优传输伪标签，以解决分子-蛋白质相互作用预测中的数据稀缺与多模态整合问题。**

**关键词**: `分子-蛋白质相互作用预测` `知识图谱` `最优传输` `伪标签生成` `多模态学习` `药物发现`

## 📋 核心要点

1. 核心问题：分子-蛋白质相互作用预测面临标注数据稀缺和现有方法忽略基因、通路等生物背景信息。
2. 方法要点：整合多源生物数据构建知识图谱，并基于最优传输生成高质量伪标签以利用未标注数据。
3. 实验或效果：在多个数据集上验证，预测准确性和零样本能力显著优于现有方法，提升药物发现应用。

## 📄 摘要（原文）

> Predicting molecule-protein interactions (MPIs) is a fundamental task in computational biology, with crucial applications in drug discovery and molecular function annotation. However, existing MPI models face two major challenges. First, the scarcity of labeled molecule-protein pairs significantly limits model performance, as available datasets capture only a small fraction of biological relevant interactions. Second, most methods rely solely on molecular and protein features, ignoring broader biological context such as genes, metabolic pathways, and functional annotations that could provide essential complementary information. To address these limitations, our framework first aggregates diverse biological datasets, including molecular, protein, genes and pathway-level interactions, and then develop an optimal transport-based approach to generate high-quality pseudo-labels for unlabeled molecule-protein pairs, leveraging the underlying distribution of known interactions to guide label assignment. By treating pseudo-labeling as a mechanism for bridging disparate biological modalities, our approach enables the effective use of heterogeneous data to enhance MPI prediction. We evaluate our framework on multiple MPI datasets including virtual screening tasks and protein retrieval tasks, demonstrating substantial improvements over state-of-the-art methods in prediction accuracies and zero shot ability across unseen interactions. Beyond MPI prediction, our approach provides a new paradigm for leveraging diverse biological data sources to tackle problems traditionally constrained by single- or bi-modal learning, paving the way for future advances in computational biology and drug discovery.

