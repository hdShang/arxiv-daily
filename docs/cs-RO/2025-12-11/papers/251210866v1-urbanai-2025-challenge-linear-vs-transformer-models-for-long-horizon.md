---
layout: default
title: UrbanAI 2025 Challenge: Linear vs Transformer Models for Long-Horizon Exogenous Temperature Forecasting
---

# UrbanAI 2025 Challenge: Linear vs Transformer Models for Long-Horizon Exogenous Temperature Forecasting

**arXiv**: [2512.10866v1](https://arxiv.org/abs/2512.10866) | [PDF](https://arxiv.org/pdf/2512.10866.pdf)

**作者**: Ruslan Gokhman

---

## 💡 一句话要点

**在线性模型与Transformer模型对比中，DLinear在仅外生长时温度预测中表现最佳。**

**关键词**: `时间序列预测` `长时预测` `线性模型` `Transformer模型` `外生变量预测` `温度预测`

## 📋 核心要点

1. 研究仅使用历史室内温度进行长时预测的挑战性单变量设置。
2. 评估线性模型（Linear、NLinear、DLinear）和Transformer模型（Transformer、Informer、Autoformer）在标准化数据集上的性能。
3. 结果显示线性基线模型普遍优于复杂Transformer架构，DLinear在所有分割中达到最高准确度。

## 📄 摘要（原文）

> We study long-horizon exogenous-only temperature forecasting - a challenging univariate setting where only the past values of the indoor temperature are used for prediction - using linear and Transformer-family models. We evaluate Linear, NLinear, DLinear, Transformer, Informer, and Autoformer under standardized train, validation, and test splits. Results show that linear baselines (Linear, NLinear, DLinear) consistently outperform more complex Transformer-family architectures, with DLinear achieving the best overall accuracy across all splits. These findings highlight that carefully designed linear models remain strong baselines for time series forecasting in challenging exogenous-only settings.

