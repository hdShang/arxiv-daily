---
layout: default
title: Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks
---

# Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks

**arXiv**: [2512.05868v1](https://arxiv.org/abs/2512.05868) | [PDF](https://arxiv.org/pdf/2512.05868.pdf)

**作者**: Brian Ezinwoke, Oliver Rhodes

---

## 💡 一句话要点

**提出基于脉冲神经网络的惩罚性脉冲准确率优化方法，用于高频金融数据价格尖峰预测。**

**关键词**: `脉冲神经网络` `高频交易` `价格尖峰预测` `贝叶斯优化` `惩罚性脉冲准确率`

## 📋 核心要点

1. 高频交易中价格尖峰预测困难，传统模型难以捕捉毫秒级时间结构。
2. 采用脉冲神经网络处理离散事件，通过贝叶斯优化和惩罚性脉冲准确率目标进行超参数调优。
3. 实验显示优化模型在模拟交易中实现最高累计回报76.8%，显著优于基线。

## 📄 摘要（原文）

> Modern high-frequency trading (HFT) environments are characterized by sudden price spikes that present both risk and opportunity, but conventional financial models often fail to capture the required fine temporal structure. Spiking Neural Networks (SNNs) offer a biologically inspired framework well-suited to these challenges due to their natural ability to process discrete events and preserve millisecond-scale timing. This work investigates the application of SNNs to high-frequency price-spike forecasting, enhancing performance via robust hyperparameter tuning with Bayesian Optimization (BO). This work converts high-frequency stock data into spike trains and evaluates three architectures: an established unsupervised STDP-trained SNN, a novel SNN with explicit inhibitory competition, and a supervised backpropagation network. BO was driven by a novel objective, Penalized Spike Accuracy (PSA), designed to ensure a network's predicted price spike rate aligns with the empirical rate of price events. Simulated trading demonstrated that models optimized with PSA consistently outperformed their Spike Accuracy (SA)-tuned counterparts and baselines. Specifically, the extended SNN model with PSA achieved the highest cumulative return (76.8%) in simple backtesting, significantly surpassing the supervised alternative (42.54% return). These results validate the potential of spiking networks, when robustly tuned with task-specific objectives, for effective price spike forecasting in HFT.

