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

**提出基于重叠加权的分层归一化持久性速度方法，用于时变网络异常检测，在加密货币市场预测中实现显著性能提升。**

**关键词**: `拓扑数据分析` `持久图` `网络异常检测` `动态网络` `加密货币市场` `速度建模` `重叠加权` `数学稳定性`

## 📋 核心要点

1. 现有方法主要关注累积拓扑存在，缺乏对特征动态变化速率的建模，难以有效区分噪声与真实异常。
2. 提出基于速度的持久图分析视角，引入重叠加权机制自动降噪，并证明方法的数学稳定性。
3. 在以太坊交易网络异常检测中，OW-HNPV实现高达10.4%的AUC提升，在中长期预测中表现最稳定。

## 📝 摘要（中文）

我们引入了重叠加权分层归一化持久性速度，这是一种用于检测时变网络异常的新型拓扑数据分析方法。与现有测量累积拓扑存在的方法不同，我们首次从速度角度分析持久图，测量特征出现和消失的速率，并通过基于重叠的加权自动降低噪声影响。我们还证明了OW-HNPV在数学上是稳定的，即使在比较具有不同特征类型的网络的持久图时，其行为也是可控且可预测的。应用于以太坊交易网络，OW-HNPV在加密货币异常检测方面表现出优越性能，在7天价格变动预测中比基线模型实现了高达10.4%的AUC增益。与向量平均贝蒂数、持久景观和持久图像等现有方法相比，基于速度的摘要在中长期预测中表现优异，OW-HNPV在不同预测时间范围内提供了最一致和稳定的性能。我们的结果表明，建模拓扑速度对于检测动态网络中的结构异常至关重要。

## 🔬 方法详解

整体框架基于拓扑数据分析，将时变网络转化为持久图序列，通过计算特征出现和消失的速率来量化拓扑速度。关键技术创新包括：首次引入速度视角分析持久图，提出重叠加权机制自动降低噪声影响，并证明方法的数学稳定性。与现有方法如向量平均贝蒂数、持久景观等相比，主要区别在于从累积测量转向动态速率测量，更关注特征变化过程而非静态存在。

## 📊 实验亮点

在以太坊交易网络7天价格预测中，OW-HNPV比基线模型实现高达10.4%的AUC增益；在中长期预测中表现最优，提供最一致稳定的性能，验证了拓扑速度建模的有效性。

## 🎯 应用场景

该方法适用于动态网络异常检测，如加密货币交易网络监控、社交网络动态分析、生物网络变化追踪等领域，为金融风控、网络安全和系统监控提供新工具。

## 📄 摘要（原文）

> We introduce the Overlap-Weighted Hierarchical Normalized Persistence Velocity (OW-HNPV), a novel topological data analysis method for detecting anomalies in time-varying networks. Unlike existing methods that measure cumulative topological presence, we introduce the first velocity-based perspective on persistence diagrams, measuring the rate at which features appear and disappear, automatically downweighting noise through overlap-based weighting. We also prove that OW-HNPV is mathematically stable. It behaves in a controlled, predictable way, even when comparing persistence diagrams from networks with different feature types. Applied to Ethereum transaction networks (May 2017-May 2018), OW-HNPV demonstrates superior performance for cryptocurrency anomaly detection, achieving up to 10.4% AUC gain over baseline models for 7-day price movement predictions. Compared with established methods, including Vector of Averaged Bettis (VAB), persistence landscapes, and persistence images, velocity-based summaries excel at medium- to long-range forecasting (4-7 days), with OW-HNPV providing the most consistent and stable performance across prediction horizons. Our results show that modeling topological velocity is crucial for detecting structural anomalies in dynamic networks.

