---
layout: default
title: FedAPA: Federated Learning with Adaptive Prototype Aggregation Toward Heterogeneous Wi-Fi CSI-based Crowd Counting
---

# FedAPA: Federated Learning with Adaptive Prototype Aggregation Toward Heterogeneous Wi-Fi CSI-based Crowd Counting

**arXiv**: [2511.21048v1](https://arxiv.org/abs/2511.21048) | [PDF](https://arxiv.org/pdf/2511.21048.pdf)

**作者**: Jingtao Guo, Yuyi Mao, Ivan Wang-Hei Ho

---

## 💡 一句话要点

**提出FedAPA联邦学习算法，通过自适应原型聚合解决异构Wi-Fi CSI人群计数问题**

**关键词**: `联邦学习` `Wi-Fi CSI感知` `自适应聚合` `人群计数` `异构数据` `通信优化`

## 📋 核心要点

1. 核心问题：异构Wi-Fi CSI数据和设备资源限制联邦学习大规模部署
2. 方法要点：自适应原型聚合分配权重，结合分类与对比学习优化本地训练
3. 实验效果：在真实场景中提升准确率、F1分数，降低MAE和通信开销

## 📄 摘要（原文）

> Wi-Fi channel state information (CSI)-based sensing provides a non-invasive, device-free approach for tasks such as human activity recognition and crowd counting, but large-scale deployment is hindered by the need for extensive site-specific training data. Federated learning (FL) offers a way to avoid raw data sharing but is challenged by heterogeneous sensing data and device resources. This paper proposes FedAPA, a collaborative Wi-Fi CSI-based sensing algorithm that uses adaptive prototype aggregation (APA) strategy to assign similarity-based weights to peer prototypes, enabling adaptive client contributions and yielding a personalized global prototype for each client instead of a fixed-weight aggregation. During local training, we adopt a hybrid objective that combines classification learning with representation contrastive learning to align local and global knowledge. We provide a convergence analysis of FedAPA and evaluate it in a real-world distributed Wi-Fi crowd counting scenario with six environments and up to 20 people. The results show that our method outperform multiple baselines in terms of accuracy, F1 score, mean absolute error (MAE), and communication overhead, with FedAPA achieving at least a 9.65% increase in accuracy, a 9% gain in F1 score, a 0.29 reduction in MAE, and a 95.94% reduction in communication overhead.

