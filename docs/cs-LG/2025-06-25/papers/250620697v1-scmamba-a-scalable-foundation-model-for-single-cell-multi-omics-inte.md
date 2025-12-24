---
layout: default
title: "scMamba: A Scalable Foundation Model for Single-Cell Multi-Omics Integration Beyond Highly Variable Feature Selection"
---

# scMamba: A Scalable Foundation Model for Single-Cell Multi-Omics Integration Beyond Highly Variable Feature Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20697" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20697v1</a>
  <a href="https://arxiv.org/pdf/2506.20697.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20697v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20697v1', 'scMamba: A Scalable Foundation Model for Single-Cell Multi-Omics Integration Beyond Highly Variable Feature Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhen Yuan, Shaoqing Jiao, Yihang Xiao, Jiajie Peng

**分类**: q-bio.CB, cs.LG

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出scMamba以解决单细胞多组学整合中的特征选择问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `单细胞分析` `多组学整合` `对比学习` `生物信息学` `深度学习`

## 📋 核心要点

1. 现有单细胞多组学整合方法依赖于高度变异特征选择，可能导致重要生物信息的丢失。
2. scMamba通过补丁式细胞标记策略，无需特征选择，直接整合多组学数据，保留基因组位置信息。
3. 实验结果显示，scMamba在多个数据集上显著优于现有方法，提升了生物变异的保留和组学层的对齐效果。

## 📝 摘要（中文）

单细胞多组学技术的出现使得在单个细胞内同时分析多种组学层成为可能。然而，现有方法通常依赖于选择高度变异的基因或峰值进行预处理，这可能会无意中丢失重要的生物信息。为此，本文提出了scMamba，一个无需事先特征选择的基础模型，旨在整合单细胞多组学数据，同时保留基因组位置信息。scMamba采用基于补丁的细胞标记策略，将基因组区域视为单词（标记），细胞视为句子。通过状态空间对偶性，scMamba从高维、稀疏的单细胞多组学数据中提取丰富的生物学见解。此外，结合余弦相似度正则化的对比学习方法，使得不同组学层之间的对齐优于传统方法。系统的基准测试表明，scMamba在保留生物变异、对齐组学层以及增强聚类、细胞类型注释和轨迹推断等下游任务方面显著优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文解决的是单细胞多组学数据整合中的特征选择问题。现有方法通常依赖于选择高度变异的基因或峰值，这可能导致重要的生物信息被丢弃，影响分析结果的准确性。

**核心思路**：scMamba的核心思路是通过补丁式细胞标记策略，直接将基因组区域视为单词（标记），细胞视为句子，从而避免了特征选择的步骤，保留了更多的生物信息。

**技术框架**：scMamba的整体架构包括数据预处理、补丁式细胞标记、对比学习和结果输出等主要模块。数据预处理阶段负责清洗和标准化输入数据，补丁式细胞标记将基因组区域转化为标记，接着通过对比学习方法进行组学层的对齐，最后输出分析结果。

**关键创新**：scMamba的主要创新在于其补丁式细胞标记策略和结合余弦相似度正则化的对比学习方法。这种设计使得模型能够在不依赖特征选择的情况下，提取和对齐多组学数据中的生物信息。

**关键设计**：在模型设计中，scMamba采用了特定的损失函数来优化组学层之间的对齐，并引入了余弦相似度正则化以增强模型的稳定性和准确性。网络结构方面，scMamba使用了深度学习框架，以处理高维稀疏数据。

## 📊 实验亮点

在多个数据集的系统基准测试中，scMamba在保留生物变异、对齐组学层和增强下游任务（如聚类、细胞类型注释和轨迹推断）方面显著优于现有最先进的方法，提升幅度达到XX%。

## 🎯 应用场景

scMamba在单细胞多组学数据整合方面具有广泛的应用潜力，能够帮助研究人员深入理解细胞身份、调控过程及疾病机制。其强大的数据处理能力使其适用于大规模细胞图谱的分析，推动生物学发现的进展。

## 📄 摘要（原文）

> The advent of single-cell multi-omics technologies has enabled the simultaneous profiling of diverse omics layers within individual cells. Integrating such multimodal data provides unprecedented insights into cellular identity, regulatory processes, and disease mechanisms. However, it remains challenging, as current methods often rely on selecting highly variable genes or peaks during preprocessing, which may inadvertently discard crucial biological information. Here, we present scMamba, a foundation model designed to integrate single-cell multi-omics data without the need for prior feature selection while preserving genomic positional information. scMamba introduces a patch-based cell tokenization strategy that treats genomics regions as words (tokens) and cells as sentences. Building upon the concept of state space duality, scMamba distills rich biological insights from high-dimensional, sparse single-cell multi-omics data. Additionally, our novel contrastive learning approach, enhanced with cosine similarity regularization, enables superior alignment across omics layers compared to traditional methods. Systematic benchmarking across multiple datasets demonstrates that scMamba significantly outperforms state-of-the-art methods in preserving biological variation, aligning omics layers, and enhancing key downstream tasks such as clustering, cell type annotation, and trajectory inference. Our findings position scMamba as a powerful tool for large-scale single-cell multi-omics integration, capable of handling large-scale atlases and advancing biological discovery.

