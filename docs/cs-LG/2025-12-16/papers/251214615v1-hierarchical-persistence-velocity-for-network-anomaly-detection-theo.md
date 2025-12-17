---
layout: default
title: Hierarchical Persistence Velocity for Network Anomaly Detection: Theory and Applications to Cryptocurrency Markets
---

# Hierarchical Persistence Velocity for Network Anomaly Detection: Theory and Applications to Cryptocurrency Markets

**arXiv**: [2512.14615v1](https://arxiv.org/abs/2512.14615) | [PDF](https://arxiv.org/pdf/2512.14615.pdf)

**作者**: Omid Khormali

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于重叠加权的层次化归一化持久性速度方法，用于时变网络异常检测，在加密货币市场预测中表现优异。**

🎯 **匹配领域**: **强化学习**

**关键词**: `拓扑数据分析` `持久图` `网络异常检测` `加密货币市场` `时变网络` `速度建模` `重叠加权` `数学稳定性`

## 📋 核心要点

1. 现有方法主要关注累积拓扑特征，难以捕捉动态网络中的快速结构变化，限制了异常检测的时效性和准确性。
2. 提出基于速度的持久图分析，通过重叠加权自动降噪，并证明方法的数学稳定性，确保可控和可预测的行为。
3. 在以太坊交易网络实验中，OW-HNPV实现高达10.4%的AUC增益，在中长期预测中表现最稳定，优于多种基线方法。

## 📝 摘要（中文）

我们引入了重叠加权层次化归一化持久性速度（OW-HNPV），这是一种用于检测时变网络异常的新型拓扑数据分析方法。与现有测量累积拓扑存在的方法不同，我们首次从速度角度分析持久图，测量特征出现和消失的速率，并通过基于重叠的加权自动降低噪声影响。我们还证明了OW-HNPV在数学上是稳定的，即使在比较具有不同特征类型的网络持久图时，其行为也是可控且可预测的。应用于以太坊交易网络（2017年5月至2018年5月），OW-HNPV在加密货币异常检测中表现出卓越性能，在7天价格变动预测中比基线模型实现了高达10.4%的AUC增益。与现有方法（如平均贝蒂向量、持久景观和持久图像）相比，基于速度的摘要在中长期预测（4-7天）中表现突出，OW-HNPV在不同预测时间范围内提供了最一致和稳定的性能。我们的结果表明，建模拓扑速度对于检测动态网络中的结构异常至关重要。

## 🔬 方法详解

整体框架基于拓扑数据分析，通过持久图捕捉网络拓扑特征。关键创新点包括：首次引入速度视角分析持久图，测量特征出现和消失的速率；提出重叠加权机制，自动降低噪声影响；证明方法的数学稳定性，确保鲁棒性。与现有方法（如VAB、持久景观）的主要区别在于，现有方法侧重于累积拓扑存在，而OW-HNPV专注于拓扑变化的速度，从而更敏感地检测动态网络中的结构异常。

## 📊 实验亮点

在以太坊交易网络实验中，OW-HNPV在7天价格变动预测中实现高达10.4%的AUC增益，优于VAB、持久景观等基线方法。在中长期预测（4-7天）中表现最稳定，验证了拓扑速度建模对异常检测的关键作用。

## 🎯 应用场景

该方法适用于时变网络的异常检测，如加密货币交易网络、社交网络动态分析、物联网设备通信监控等。实际价值在于提升中长期预测准确性，为金融风险管理和网络安全提供新工具。

## 📄 摘要（原文）

> We introduce the Overlap-Weighted Hierarchical Normalized Persistence Velocity (OW-HNPV), a novel topological data analysis method for detecting anomalies in time-varying networks. Unlike existing methods that measure cumulative topological presence, we introduce the first velocity-based perspective on persistence diagrams, measuring the rate at which features appear and disappear, automatically downweighting noise through overlap-based weighting. We also prove that OW-HNPV is mathematically stable. It behaves in a controlled, predictable way, even when comparing persistence diagrams from networks with different feature types. Applied to Ethereum transaction networks (May 2017-May 2018), OW-HNPV demonstrates superior performance for cryptocurrency anomaly detection, achieving up to 10.4% AUC gain over baseline models for 7-day price movement predictions. Compared with established methods, including Vector of Averaged Bettis (VAB), persistence landscapes, and persistence images, velocity-based summaries excel at medium- to long-range forecasting (4-7 days), with OW-HNPV providing the most consistent and stable performance across prediction horizons. Our results show that modeling topological velocity is crucial for detecting structural anomalies in dynamic networks.

