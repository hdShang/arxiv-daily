---
layout: default
title: gHAWK: Local and Global Structure Encoding for Scalable Training of Graph Neural Networks on Knowledge Graphs
---

# gHAWK: Local and Global Structure Encoding for Scalable Training of Graph Neural Networks on Knowledge Graphs

**arXiv**: [2512.08274v1](https://arxiv.org/abs/2512.08274) | [PDF](https://arxiv.org/pdf/2512.08274.pdf)

**作者**: Humera Sabir, Fatima Farooq, Ashraf Aboulnaga

---

## 💡 一句话要点

**提出gHAWK框架，通过预计算局部与全局结构特征，解决知识图谱上大规模图神经网络训练的可扩展性问题。**

**关键词**: `知识图谱` `图神经网络` `可扩展训练` `结构编码` `预计算特征` `Open Graph Benchmark`

## 📋 核心要点

1. 核心问题：现有消息传递图神经网络在大规模知识图谱上训练效率低，受限于迭代消息传递过程。
2. 方法要点：预处理阶段计算Bloom过滤器编码局部邻域结构，TransE嵌入表示全局位置，融合特征以增强GNN训练。
3. 实验或效果：在Open Graph Benchmark数据集上实现最优准确率和更低训练时间，提升节点属性预测和链接预测任务性能。

## 📄 摘要（原文）

> Knowledge Graphs (KGs) are a rich source of structured, heterogeneous data, powering a wide range of applications. A common approach to leverage this data is to train a graph neural network (GNN) on the KG. However, existing message-passing GNNs struggle to scale to large KGs because they rely on the iterative message passing process to learn the graph structure, which is inefficient, especially under mini-batch training, where a node sees only a partial view of its neighborhood. In this paper, we address this problem and present gHAWK, a novel and scalable GNN training framework for large KGs. The key idea is to precompute structural features for each node that capture its local and global structure before GNN training even begins. Specifically, gHAWK introduces a preprocessing step that computes: (a)~Bloom filters to compactly encode local neighborhood structure, and (b)~TransE embeddings to represent each node's global position in the graph. These features are then fused with any domain-specific features (e.g., text embeddings), producing a node feature vector that can be incorporated into any GNN technique. By augmenting message-passing training with structural priors, gHAWK significantly reduces memory usage, accelerates convergence, and improves model accuracy. Extensive experiments on large datasets from the Open Graph Benchmark (OGB) demonstrate that gHAWK achieves state-of-the-art accuracy and lower training time on both node property prediction and link prediction tasks, topping the OGB leaderboard for three graphs.

