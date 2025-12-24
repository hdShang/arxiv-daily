---
layout: default
title: Simple yet Effective Graph Distillation via Clustering
---

# Simple yet Effective Graph Distillation via Clustering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20807" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20807v1</a>
  <a href="https://arxiv.org/pdf/2505.20807.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20807v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20807v1', 'Simple yet Effective Graph Distillation via Clustering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yurui Lai, Taiyan Zhang, Renchi Yang

**分类**: cs.LG

**发布日期**: 2025-05-27

**备注**: This is the technical report of the paper "Simple yet Effective Graph Distillation via Clustering" accepted by KDD 2025

---

## 💡 一句话要点

**提出ClustGDD以解决图神经网络训练中的计算开销问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `图神经网络` `图数据蒸馏` `聚类方法` `节点分类` `计算效率` `深度学习`

## 📋 核心要点

1. 现有的图数据蒸馏方法多依赖启发式策略，导致训练效率低下和结果质量不佳。
2. ClustGDD通过快速聚类方法合成压缩图，优化同质性，提升了蒸馏质量。
3. 实验表明，ClustGDD在节点分类任务上性能优于现有GDD方法，且训练速度显著提高。

## 📝 摘要（中文）

尽管图表示学习在多个领域取得了显著成功，但图神经网络（GNN）的训练仍然面临巨大的计算开销。最近，图数据蒸馏（GDD）作为一种将大型图转化为紧凑且信息丰富的图的技术，展现了提高GNN训练效率的潜力。然而，现有的GDD方法多依赖启发式策略，导致结果质量下降或训练成本高昂。为此，本文提出了一种高效且有效的GDD方法ClustGDD，通过快速且理论基础扎实的聚类来合成压缩图和节点属性，优化了图的同质性。实验结果表明，基于ClustGDD生成的压缩图训练的GNN在五个基准数据集上的节点分类任务中，性能优于或可与最先进的GDD方法相媲美，同时训练速度显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决图神经网络训练中的计算开销问题，现有方法往往依赖启发式策略，导致训练效率低下和结果质量不佳。

**核心思路**：ClustGDD的核心思路是通过快速且理论基础扎实的聚类方法来合成压缩图和节点属性，最大化图的同质性，从而提高蒸馏质量。

**技术框架**：ClustGDD的整体架构包括数据预处理、聚类生成压缩图、节点属性优化和模型训练四个主要模块。聚类过程通过最小化聚类内平方和来实现。

**关键创新**：ClustGDD的主要创新在于将聚类与蒸馏质量的关系进行了理论分析，利用Fréchet Inception Distance作为质量度量，显著提升了压缩图的质量。

**关键设计**：在节点属性优化中，ClustGDD采用了类感知图采样和一致性损失，进一步改善了压缩图的节点属性，确保了训练过程的稳定性和有效性。

## 📊 实验亮点

实验结果显示，基于ClustGDD生成的压缩图训练的GNN在五个基准数据集上的节点分类任务中，性能优于或可与最先进的GDD方法相媲美，且训练速度提升了多个数量级，展示了其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括社交网络分析、推荐系统和生物信息学等，能够有效提升图神经网络在大规模图数据上的训练效率。未来，ClustGDD有望在更广泛的图学习任务中发挥重要作用，推动相关领域的研究进展。

## 📄 摘要（原文）

> Despite plentiful successes achieved by graph representation learning in various domains, the training of graph neural networks (GNNs) still remains tenaciously challenging due to the tremendous computational overhead needed for sizable graphs in practice. Recently, graph data distillation (GDD), which seeks to distill large graphs into compact and informative ones, has emerged as a promising technique to enable efficient GNN training. However, most existing GDD works rely on heuristics that align model gradients or representation distributions on condensed and original graphs, leading to compromised result quality, expensive training for distilling large graphs, or both. Motivated by this, this paper presents an efficient and effective GDD approach, ClustGDD. Under the hood, ClustGDD resorts to synthesizing the condensed graph and node attributes through fast and theoretically-grounded clustering that minimizes the within-cluster sum of squares and maximizes the homophily on the original graph. The fundamental idea is inspired by our empirical and theoretical findings unveiling the connection between clustering and empirical condensation quality using Fréchet Inception Distance, a well-known quality metric for synthetic images. Furthermore, to mitigate the adverse effects caused by the homophily-based clustering, ClustGDD refines the nodal attributes of the condensed graph with a small augmentation learned via class-aware graph sampling and consistency loss. Our extensive experiments exhibit that GNNs trained over condensed graphs output by ClustGDD consistently achieve superior or comparable performance to state-of-the-art GDD methods in terms of node classification on five benchmark datasets, while being orders of magnitude faster.

