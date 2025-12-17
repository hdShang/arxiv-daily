---
layout: default
title: Incorporating Fairness in Neighborhood Graphs for Fair Spectral Clustering
---

# Incorporating Fairness in Neighborhood Graphs for Fair Spectral Clustering

**arXiv**: [2512.09810v1](https://arxiv.org/abs/2512.09810) | [PDF](https://arxiv.org/pdf/2512.09810.pdf)

**作者**: Adithya K Moorthy, V Vijaya Saradhi, Bhanu Prasad

---

## 💡 一句话要点

**提出公平k近邻和ε邻域图构建方法以解决谱聚类中的图构建偏见问题**

**关键词**: `公平谱聚类` `图构建` `邻域图` `无监督学习` `公平性约束` `拓扑公平`

## 📋 核心要点

1. 传统图聚类方法在构建邻域图时可能因不公平的边选择而传播偏见，导致聚类结果不公
2. 通过在图构建早期阶段引入公平约束，确保每个节点的邻域中敏感特征群体比例均衡，同时保持几何一致性
3. 在合成、表格和图像数据集上实验证明，该方法在公平性上优于现有基线，无需修改聚类算法本身

## 📄 摘要（原文）

> Graph clustering plays a pivotal role in unsupervised learning methods like spectral clustering, yet traditional methods for graph clustering often perpetuate bias through unfair graph constructions that may underrepresent some groups. The current research introduces novel approaches for constructing fair k-nearest neighbor (kNN) and fair epsilon-neighborhood graphs that proactively enforce demographic parity during graph formation. By incorporating fairness constraints at the earliest stage of neighborhood selection steps, our approaches incorporate proportional representation of sensitive features into the local graph structure while maintaining geometric consistency.Our work addresses a critical gap in pre-processing for fair spectral clustering, demonstrating that topological fairness in graph construction is essential for achieving equitable clustering outcomes. Widely used graph construction methods like kNN and epsilon-neighborhood graphs propagate edge based disparate impact on sensitive groups, leading to biased clustering results. Providing representation of each sensitive group in the neighborhood of every node leads to fairer spectral clustering results because the topological features of the graph naturally reflect equitable group ratios. This research fills an essential shortcoming in fair unsupervised learning, by illustrating how topological fairness in graph construction inherently facilitates fairer spectral clustering results without the need for changes to the clustering algorithm itself. Thorough experiments on three synthetic datasets, seven real-world tabular datasets, and three real-world image datasets prove that our fair graph construction methods surpass the current baselines in graph clustering tasks.

