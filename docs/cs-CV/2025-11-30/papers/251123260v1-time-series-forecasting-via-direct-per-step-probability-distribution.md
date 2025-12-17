---
layout: default
title: Time Series Forecasting via Direct Per-Step Probability Distribution Modeling
---

# Time Series Forecasting via Direct Per-Step Probability Distribution Modeling

**arXiv**: [2511.23260v1](https://arxiv.org/abs/2511.23260) | [PDF](https://arxiv.org/pdf/2511.23260.pdf)

**作者**: Linghao Kong, Xiaopeng Hong

---

## 💡 一句话要点

**提出interPDN模型，通过直接建模每步概率分布解决时间序列预测中的不确定性量化问题。**

**关键词**: `时间序列预测` `概率分布建模` `不确定性量化` `双分支架构` `自监督学习`

## 📋 核心要点

1. 核心问题：深度神经网络时间序列预测模型难以量化预测不确定性，因直接输出标量值。
2. 方法要点：引入interPDN，直接构建每步离散概率分布，采用双分支架构和交错支持集以缓解异常。
3. 实验或效果：在多个真实数据集上验证了interPDN的优越性能，通过自监督一致性约束提升预测准确性。

## 📄 摘要（原文）

> Deep neural network-based time series prediction models have recently demonstrated superior capabilities in capturing complex temporal dependencies. However, it is challenging for these models to account for uncertainty associated with their predictions, because they directly output scalar values at each time step. To address such a challenge, we propose a novel model named interleaved dual-branch Probability Distribution Network (interPDN), which directly constructs discrete probability distributions per step instead of a scalar. The regression output at each time step is derived by computing the expectation of the predictive distribution on a predefined support set. To mitigate prediction anomalies, a dual-branch architecture is introduced with interleaved support sets, augmented by coarse temporal-scale branches for long-term trend forecasting. Outputs from another branch are treated as auxiliary signals to impose self-supervised consistency constraints on the current branch's prediction. Extensive experiments on multiple real-world datasets demonstrate the superior performance of interPDN.

