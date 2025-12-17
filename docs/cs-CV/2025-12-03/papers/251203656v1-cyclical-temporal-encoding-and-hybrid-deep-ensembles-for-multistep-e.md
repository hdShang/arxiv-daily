---
layout: default
title: Cyclical Temporal Encoding and Hybrid Deep Ensembles for Multistep Energy Forecasting
---

# Cyclical Temporal Encoding and Hybrid Deep Ensembles for Multistep Energy Forecasting

**arXiv**: [2512.03656v1](https://arxiv.org/abs/2512.03656) | [PDF](https://arxiv.org/pdf/2512.03656.pdf)

**作者**: Salim Khazem, Houssam Kanso

---

## 💡 一句话要点

**提出结合循环时间编码与混合深度集成模型的多步能源预测框架，以提升电力消耗预测精度。**

**关键词**: `能源预测` `循环时间编码` `混合深度学习` `LSTM-CNN集成` `多步预测` `智能电网`

## 📋 核心要点

1. 核心问题：电力消耗预测对需求管理和智能电网至关重要，需准确捕捉长期季节性和短期局部模式。
2. 方法要点：使用正弦余弦编码处理日历属性，集成LSTM、CNN和MLP元学习器，针对不同预测范围优化。
3. 实验或效果：在一年数据集上验证，相比基线方法，所有七个预测范围均实现RMSE和MAE降低。

## 📄 摘要（原文）

> Accurate electricity consumption forecasting is essential for demand management and smart grid operations. This paper introduces a unified deep learning framework that integrates cyclical temporal encoding with hybrid LSTM-CNN architectures to enhance multistep energy forecasting. We systematically transform calendar-based attributes using sine cosine encodings to preserve periodic structure and evaluate their predictive relevance through correlation analysis. To exploit both long-term seasonal effects and short-term local patterns, we employ an ensemble model composed of an LSTM, a CNN, and a meta-learner of MLP regressors specialized for each forecast horizon. Using a one year national consumption dataset, we conduct an extensive experimental study including ablation analyses with and without cyclical encodings and calendar features and comparisons with established baselines from the literature. Results demonstrate consistent improvements across all seven forecast horizons, with our hybrid model achieving lower RMSE and MAE than individual architectures and prior methods. These findings confirm the benefit of combining cyclical temporal representations with complementary deep learning structures. To our knowledge, this is the first work to jointly evaluate temporal encodings, calendar-based features, and hybrid ensemble architectures within a unified short-term energy forecasting framework.

