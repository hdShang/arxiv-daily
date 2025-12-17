---
layout: default
title: Rethinking Semi-Supervised Node Classification with Self-Supervised Graph Clustering
---

# Rethinking Semi-Supervised Node Classification with Self-Supervised Graph Clustering

**arXiv**: [2511.19976v1](https://arxiv.org/abs/2511.19976) | [PDF](https://arxiv.org/pdf/2511.19976.pdf)

**作者**: Songbo Wang, Renchi Yang, Yurui Lai, Xiaoyang Lin, Tsz Nam Chan

---

## 💡 一句话要点

**提出NCGC框架，结合自监督图聚类与半监督分类以提升节点分类性能**

**关键词**: `图神经网络` `半监督节点分类` `自监督图聚类` `软正交GNN` `多任务学习`

## 📋 核心要点

1. 核心问题：真实图中节点常形成紧密社区，但现有方法未利用这些信号缓解标签稀缺问题
2. 方法要点：开发软正交GNN，统一优化目标，并集成自监督聚类模块生成平衡软伪标签
3. 实验或效果：在七个真实图上，NCGC显著优于流行GNN模型和基线方法

## 📄 摘要（原文）

> The emergence of graph neural networks (GNNs) has offered a powerful tool for semi-supervised node classification tasks. Subsequent studies have achieved further improvements through refining the message passing schemes in GNN models or exploiting various data augmentation techniques to mitigate limited supervision. In real graphs, nodes often tend to form tightly-knit communities/clusters, which embody abundant signals for compensating label scarcity in semi-supervised node classification but are not explored in prior methods.
>   Inspired by this, this paper presents NCGC that integrates self-supervised graph clustering and semi-supervised classification into a unified framework. Firstly, we theoretically unify the optimization objectives of GNNs and spectral graph clustering, and based on that, develop soft orthogonal GNNs (SOGNs) that leverage a refined message passing paradigm to generate node representations for both classification and clustering. On top of that, NCGC includes a self-supervised graph clustering module that enables the training of SOGNs for learning representations of unlabeled nodes in a self-supervised manner. Particularly, this component comprises two non-trivial clustering objectives and a Sinkhorn-Knopp normalization that transforms predicted cluster assignments into balanced soft pseudo-labels. Through combining the foregoing clustering module with the classification model using a multi-task objective containing the supervised classification loss on labeled data and self-supervised clustering loss on unlabeled data, NCGC promotes synergy between them and achieves enhanced model capacity. Our extensive experiments showcase that the proposed NCGC framework consistently and considerably outperforms popular GNN models and recent baselines for semi-supervised node classification on seven real graphs, when working with various classic GNN backbones.

