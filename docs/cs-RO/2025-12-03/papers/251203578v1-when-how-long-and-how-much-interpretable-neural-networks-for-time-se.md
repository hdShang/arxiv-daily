---
layout: default
title: When, How Long and How Much? Interpretable Neural Networks for Time Series Regression by Learning to Mask and Aggregate
---

# When, How Long and How Much? Interpretable Neural Networks for Time Series Regression by Learning to Mask and Aggregate

**arXiv**: [2512.03578v1](https://arxiv.org/abs/2512.03578) | [PDF](https://arxiv.org/pdf/2512.03578.pdf)

**作者**: Florent Forest, Amaury Wei, Olga Fink

---

## 💡 一句话要点

**提出MAGNETS以解决时间序列回归中黑盒模型缺乏可解释性的问题。**

**关键词**: `时间序列回归` `可解释神经网络` `掩码聚合` `概念学习` `透明模型`

## 📋 核心要点

1. 核心问题：现有时间序列回归模型预测准确但可解释性差，后处理解释方法粗糙不稳定。
2. 方法要点：MAGNETS通过掩码聚合学习可解释概念，无需标注，透明组合预测。
3. 实验或效果：未知，但旨在提供清晰决策洞察，适用于高维多变量数据。

## 📄 摘要（原文）

> Time series extrinsic regression (TSER) refers to the task of predicting a continuous target variable from an input time series. It appears in many domains, including healthcare, finance, environmental monitoring, and engineering. In these settings, accurate predictions and trustworthy reasoning are both essential. Although state-of-the-art TSER models achieve strong predictive performance, they typically operate as black boxes, making it difficult to understand which temporal patterns drive their decisions. Post-hoc interpretability techniques, such as feature attribution, aim to to explain how the model arrives at its predictions, but often produce coarse, noisy, or unstable explanations. Recently, inherently interpretable approaches based on concepts, additive decompositions, or symbolic regression, have emerged as promising alternatives. However, these approaches remain limited: they require explicit supervision on the concepts themselves, often cannot capture interactions between time-series features, lack expressiveness for complex temporal patterns, and struggle to scale to high-dimensional multivariate data.
>   To address these limitations, we propose MAGNETS (Mask-and-AGgregate NEtwork for Time Series), an inherently interpretable neural architecture for TSER. MAGNETS learns a compact set of human-understandable concepts without requiring any annotations. Each concept corresponds to a learned, mask-based aggregation over selected input features, explicitly revealing both which features drive predictions and when they matter in the sequence. Predictions are formed as combinations of these learned concepts through a transparent, additive structure, enabling clear insight into the model's decision process.

