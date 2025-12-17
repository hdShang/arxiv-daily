---
layout: default
title: Sepsis Prediction Using Graph Convolutional Networks over Patient-Feature-Value Triplets
---

# Sepsis Prediction Using Graph Convolutional Networks over Patient-Feature-Value Triplets

**arXiv**: [2512.05416v1](https://arxiv.org/abs/2512.05416) | [PDF](https://arxiv.org/pdf/2512.05416.pdf)

**作者**: Bozhi Dan, Di Wu, Ji Xu, Xiang Liu, Yiziting Zhu, Xin Shu, Yujie Li, Bin Yi

---

## 💡 一句话要点

**提出Triplet-GCN模型，通过患者-特征-值三元组构建图卷积网络，用于重症监护中的脓毒症早期预测。**

**关键词**: `脓毒症预测` `图卷积网络` `电子健康记录` `患者嵌入` `三元组表示` `重症监护`

## 📋 核心要点

1. 核心问题：脓毒症预测受电子健康记录数据复杂、稀疏和异质性影响，及时检测困难。
2. 方法要点：将每次医疗接触表示为三元组，构建二分图，结合GCN和MLP学习患者嵌入，保留测量值于边。
3. 实验或效果：在回顾性多中心队列中，Triplet-GCN优于多种表格基线模型，提升判别能力和实用性。

## 📄 摘要（原文）

> In the intensive care setting, sepsis continues to be a major contributor to patient illness and death; however, its timely detection is hindered by the complex, sparse, and heterogeneous nature of electronic health record (EHR) data. We propose Triplet-GCN, a single-branch graph convolutional model that represents each encounter as patient--feature--value triplets, constructs a bipartite EHR graph, and learns patient embeddings via a Graph Convolutional Network (GCN) followed by a lightweight multilayer perceptron (MLP). The pipeline applies type-specific preprocessing -- median imputation and standardization for numeric variables, effect coding for binary features, and mode imputation with low-dimensional embeddings for rare categorical attributes -- and initializes patient nodes with summary statistics, while retaining measurement values on edges to preserve "who measured what and by how much". In a retrospective, multi-center Chinese cohort (N = 648; 70/30 train--test split) drawn from three tertiary hospitals, Triplet-GCN consistently outperforms strong tabular baselines (KNN, SVM, XGBoost, Random Forest) across discrimination and balanced error metrics, yielding a more favorable sensitivity--specificity trade-off and improved overall utility for early warning. These findings indicate that encoding EHR as triplets and propagating information over a patient--feature graph produce more informative patient representations than feature-independent models, offering a simple, end-to-end blueprint for deployable sepsis risk stratification.

