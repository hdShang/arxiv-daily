---
layout: default
title: Hierarchical Spatio-Temporal Attention Network with Adaptive Risk-Aware Decision for Forward Collision Warning in Complex Scenarios
---

# Hierarchical Spatio-Temporal Attention Network with Adaptive Risk-Aware Decision for Forward Collision Warning in Complex Scenarios

**arXiv**: [2511.19952v1](https://arxiv.org/abs/2511.19952) | [PDF](https://arxiv.org/pdf/2511.19952.pdf)

**作者**: Haoran Hu, Junren Shi, Shuo Jiang, Kun Cheng, Xia Yang, Changhao Piao

---

## 💡 一句话要点

**提出分层时空注意力网络与动态风险阈值调整算法，以提升复杂场景前向碰撞预警性能。**

**关键词**: `前向碰撞预警` `时空注意力网络` `动态风险阈值` `图注意力网络` `预测区间` `复杂场景`

## 📋 核心要点

1. 核心问题：现有方法计算成本高、交互建模不足，导致高误报率和部署困难。
2. 方法要点：采用图注意力网络和GRU自注意力分层建模时空交互，结合自适应风险阈值。
3. 实验效果：在NGSIM数据集上，推理时间12.3毫秒，F1分数0.912，误报率8.2%。

## 📄 摘要（原文）

> Forward Collision Warning systems are crucial for vehicle safety and autonomous driving, yet current methods often fail to balance precise multi-agent interaction modeling with real-time decision adaptability, evidenced by the high computational cost for edge deployment and the unreliability stemming from simplified interaction models.To overcome these dual challenges-computational complexity and modeling insufficiency-along with the high false alarm rates of traditional static-threshold warnings, this paper introduces an integrated FCW framework that pairs a Hierarchical Spatio-Temporal Attention Network with a Dynamic Risk Threshold Adjustment algorithm. HSTAN employs a decoupled architecture (Graph Attention Network for spatial, cascaded GRU with self-attention for temporal) to achieve superior performance and efficiency, requiring only 12.3 ms inference time (73% faster than Transformer methods) and reducing the Average Displacement Error (ADE) to 0.73m (42.2% better than Social_LSTM) on the NGSIM dataset. Furthermore, Conformalized Quantile Regression enhances reliability by generating prediction intervals (91.3% coverage at 90% confidence), which the DTRA module then converts into timely warnings via a physics-informed risk potential function and an adaptive threshold mechanism inspired by statistical process control.Tested across multi-scenario datasets, the complete system demonstrates high efficacy, achieving an F1 score of 0.912, a low false alarm rate of 8.2%, and an ample warning lead time of 2.8 seconds, validating the framework's superior performance and practical deployment feasibility in complex environments.

