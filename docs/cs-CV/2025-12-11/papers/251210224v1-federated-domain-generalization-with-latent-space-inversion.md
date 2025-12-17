---
layout: default
title: Federated Domain Generalization with Latent Space Inversion
---

# Federated Domain Generalization with Latent Space Inversion

**arXiv**: [2512.10224v1](https://arxiv.org/abs/2512.10224) | [PDF](https://arxiv.org/pdf/2512.10224.pdf)

**作者**: Ragja Palakkadavath, Hung Le, Thanh Nguyen-Tang, Svetha Venkatesh, Sunil Gupta

---

## 💡 一句话要点

**提出潜在空间反转与重要权重聚合以解决联邦域泛化中的隐私与异构问题**

**关键词**: `联邦学习` `域泛化` `隐私保护` `模型聚合` `异构数据` `潜在空间反转`

## 📋 核心要点

1. 核心问题：联邦域泛化中现有方法通过共享客户端数据统计危及隐私，且异构客户端聚合可能丢弃本地适配
2. 方法要点：使用潜在空间反转增强本地模型域不变性以保护隐私，并设计重要权重聚合策略优先关键参数
3. 实验或效果：实验显示方法在减少通信开销下优于现有技术，提升泛化能力

## 📄 摘要（原文）

> Federated domain generalization (FedDG) addresses distribution shifts among clients in a federated learning framework. FedDG methods aggregate the parameters of locally trained client models to form a global model that generalizes to unseen clients while preserving data privacy. While improving the generalization capability of the global model, many existing approaches in FedDG jeopardize privacy by sharing statistics of client data between themselves. Our solution addresses this problem by contributing new ways to perform local client training and model aggregation. To improve local client training, we enforce (domain) invariance across local models with the help of a novel technique, \textbf{latent space inversion}, which enables better client privacy. When clients are not \emph{i.i.d}, aggregating their local models may discard certain local adaptations. To overcome this, we propose an \textbf{important weight} aggregation strategy to prioritize parameters that significantly influence predictions of local models during aggregation. Our extensive experiments show that our approach achieves superior results over state-of-the-art methods with less communication overhead.

