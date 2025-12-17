---
layout: default
title: CAT: Can Trust be Predicted with Context-Awareness in Dynamic Heterogeneous Networks?
---

# CAT: Can Trust be Predicted with Context-Awareness in Dynamic Heterogeneous Networks?

**arXiv**: [2512.11352v1](https://arxiv.org/abs/2512.11352) | [PDF](https://arxiv.org/pdf/2512.11352.pdf)

**作者**: Jie Wang, Zheng Yan, Jiahe Lan, Xuyan Li, Elisa Bertino

---

## 💡 一句话要点

**提出CAT模型以解决动态异构网络中上下文感知的信任预测问题**

**关键词**: `信任预测` `图神经网络` `动态图` `异构网络` `上下文感知` `注意力机制`

## 📋 核心要点

1. 核心问题：现有GNN信任预测模型忽略动态性、异构性和上下文感知，导致预测粗糙
2. 方法要点：CAT结合连续时间表示、异构注意力机制和元路径提取上下文特征，实现动态异构网络的上下文感知信任预测
3. 实验或效果：在三个真实数据集上优于五组基线，展现强可扩展性和对攻击的鲁棒性

## 📄 摘要（原文）

> Trust prediction provides valuable support for decision-making, risk mitigation, and system security enhancement. Recently, Graph Neural Networks (GNNs) have emerged as a promising approach for trust prediction, owing to their ability to learn expressive node representations that capture intricate trust relationships within a network. However, current GNN-based trust prediction models face several limitations: (i) Most of them fail to capture trust dynamicity, leading to questionable inferences. (ii) They rarely consider the heterogeneous nature of real-world networks, resulting in a loss of rich semantics. (iii) None of them support context-awareness, a basic property of trust, making prediction results coarse-grained.
>   To this end, we propose CAT, the first Context-Aware GNN-based Trust prediction model that supports trust dynamicity and accurately represents real-world heterogeneity. CAT consists of a graph construction layer, an embedding layer, a heterogeneous attention layer, and a prediction layer. It handles dynamic graphs using continuous-time representations and captures temporal information through a time encoding function. To model graph heterogeneity and leverage semantic information, CAT employs a dual attention mechanism that identifies the importance of different node types and nodes within each type. For context-awareness, we introduce a new notion of meta-paths to extract contextual features. By constructing context embeddings and integrating a context-aware aggregator, CAT can predict both context-aware trust and overall trust. Extensive experiments on three real-world datasets demonstrate that CAT outperforms five groups of baselines in trust prediction, while exhibiting strong scalability to large-scale graphs and robustness against both trust-oriented and GNN-oriented attacks.

