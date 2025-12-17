---
layout: default
title: Interpretable Air Pollution Forecasting by Physics-Guided Spatiotemporal Decoupling
---

# Interpretable Air Pollution Forecasting by Physics-Guided Spatiotemporal Decoupling

**arXiv**: [2511.20257v1](https://arxiv.org/abs/2511.20257) | [PDF](https://arxiv.org/pdf/2511.20257.pdf)

**作者**: Zhiguo Zhang, Xiaoliang Ma, Daniel Schlesinger

---

## 💡 一句话要点

**提出物理引导时空解耦框架以提升空气污染预测的准确性与可解释性**

**关键词**: `空气污染预测` `时空解耦` `物理引导学习` `可解释性` `注意力机制`

## 📋 核心要点

1. 核心问题：空气污染预测模型在性能与可解释性之间存在权衡
2. 方法要点：将时空行为分解为物理引导传输核和可解释注意力机制
3. 实验或效果：在斯德哥尔摩数据集上优于现有基线，支持实际应用

## 📄 摘要（原文）

> Accurate and interpretable air pollution forecasting is crucial for public health, but most models face a trade-off between performance and interpretability. This study proposes a physics-guided, interpretable-by-design spatiotemporal learning framework. The model decomposes the spatiotemporal behavior of air pollutant concentrations into two transparent, additive modules. The first is a physics-guided transport kernel with directed weights conditioned on wind and geography (advection). The second is an explainable attention mechanism that learns local responses and attributes future concentrations to specific historical lags and exogenous drivers. Evaluated on a comprehensive dataset from the Stockholm region, our model consistently outperforms state-of-the-art baselines across multiple forecasting horizons. Our model's integration of high predictive performance and spatiotemporal interpretability provides a more reliable foundation for operational air-quality management in real-world applications.

