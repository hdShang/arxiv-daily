---
layout: default
title: scCluBench: Comprehensive Benchmarking of Clustering Algorithms for Single-Cell RNA Sequencing
---

# scCluBench: Comprehensive Benchmarking of Clustering Algorithms for Single-Cell RNA Sequencing

**arXiv**: [2512.02471v1](https://arxiv.org/abs/2512.02471) | [PDF](https://arxiv.org/pdf/2512.02471.pdf)

**作者**: Ping Xu, Zaitian Wang, Zhirui Wang, Pengjiang Li, Jiajia Wang, Ran Zhang, Pengfei Wang, Yuanchun Zhou

---

## 💡 一句话要点

**提出scCluBench以解决单细胞RNA测序聚类方法基准测试的标准化与全面性问题**

**关键词**: `单细胞RNA测序` `聚类算法` `基准测试` `生物信息学` `人工智能模型` `数据标准化`

## 📋 核心要点

1. 核心问题：单细胞RNA测序聚类方法基准测试缺乏标准化协议，未整合人工智能最新进展，导致评估碎片化。
2. 方法要点：提供36个统一处理的scRNA-seq数据集，收集并复现传统、深度学习、图基和生物基础模型等多种聚类方法。
3. 实验或效果：通过定量指标、可视化分析和下游生物任务（如标记基因识别）评估方法性能，系统分析模型鲁棒性和适用边界。

## 📄 摘要（原文）

> Cell clustering is crucial for uncovering cellular heterogeneity in single-cell RNA sequencing (scRNA-seq) data by identifying cell types and marker genes. Despite its importance, benchmarks for scRNA-seq clustering methods remain fragmented, often lacking standardized protocols and failing to incorporate recent advances in artificial intelligence. To fill these gaps, we present scCluBench, a comprehensive benchmark of clustering algorithms for scRNA-seq data. First, scCluBench provides 36 scRNA-seq datasets collected from diverse public sources, covering multiple tissues, which are uniformly processed and standardized to ensure consistency for systematic evaluation and downstream analyses. To evaluate performance, we collect and reproduce a range of scRNA-seq clustering methods, including traditional, deep learning-based, graph-based, and biological foundation models. We comprehensively evaluate each method both quantitatively and qualitatively, using core performance metrics as well as visualization analyses. Furthermore, we construct representative downstream biological tasks, such as marker gene identification and cell type annotation, to further assess the practical utility. scCluBench then investigates the performance differences and applicability boundaries of various clustering models across diverse analytical tasks, systematically assessing their robustness and scalability in real-world scenarios. Overall, scCluBench offers a standardized and user-friendly benchmark for scRNA-seq clustering, with curated datasets, unified evaluation protocols, and transparent analyses, facilitating informed method selection and providing valuable insights into model generalizability and application scope.

