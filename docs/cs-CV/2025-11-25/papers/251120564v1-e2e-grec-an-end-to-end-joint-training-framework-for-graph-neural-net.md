---
layout: default
title: E2E-GRec: An End-to-End Joint Training Framework for Graph Neural Networks and Recommender Systems
---

# E2E-GRec: An End-to-End Joint Training Framework for Graph Neural Networks and Recommender Systems

**arXiv**: [2511.20564v1](https://arxiv.org/abs/2511.20564) | [PDF](https://arxiv.org/pdf/2511.20564.pdf)

**作者**: Rui Xue, Shichao Zhu, Liang Qin, Guangmou Pan, Yang Song, Tianfu Wu

---

## 💡 一句话要点

**提出E2E-GRec端到端联合训练框架以解决推荐系统中GNN与推荐器分离问题**

**关键词**: `图神经网络` `推荐系统` `端到端训练` `子图采样` `动态损失平衡`

## 📋 核心要点

1. 核心问题：GNN与推荐系统分离导致高计算开销和缺乏联合优化
2. 方法要点：高效子图采样、图特征自编码器和动态损失平衡机制
3. 实验或效果：在线A/B测试显示用户停留时长提升和跳过视频数减少

## 📄 摘要（原文）

> Graph Neural Networks (GNNs) have emerged as powerful tools for modeling graph-structured data and have been widely used in recommender systems, such as for capturing complex user-item and item-item relations. However, most industrial deployments adopt a two-stage pipeline: GNNs are first pre-trained offline to generate node embeddings, which are then used as static features for downstream recommender systems. This decoupled paradigm leads to two key limitations: (1) high computational overhead, since large-scale GNN inference must be repeatedly executed to refresh embeddings; and (2) lack of joint optimization, as the gradient from the recommender system cannot directly influence the GNN learning process, causing the GNN to be suboptimally informative for the recommendation task. In this paper, we propose E2E-GRec, a novel end-to-end training framework that unifies GNN training with the recommender system. Our framework is characterized by three key components: (i) efficient subgraph sampling from a large-scale cross-domain heterogeneous graph to ensure training scalability and efficiency; (ii) a Graph Feature Auto-Encoder (GFAE) serving as an auxiliary self-supervised task to guide the GNN to learn structurally meaningful embeddings; and (iii) a two-level feature fusion mechanism combined with Gradnorm-based dynamic loss balancing, which stabilizes graph-aware multi-task end-to-end training. Extensive offline evaluations, online A/B tests (e.g., a +0.133% relative improvement in stay duration, a 0.3171% reduction in the average number of videos a user skips) on large-scale production data, together with theoretical analysis, demonstrate that E2E-GRec consistently surpasses traditional approaches, yielding significant gains across multiple recommendation metrics.

