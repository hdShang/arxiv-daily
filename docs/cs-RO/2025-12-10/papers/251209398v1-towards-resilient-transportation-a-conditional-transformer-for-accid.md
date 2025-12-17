---
layout: default
title: Towards Resilient Transportation: A Conditional Transformer for Accident-Informed Traffic Forecasting
---

# Towards Resilient Transportation: A Conditional Transformer for Accident-Informed Traffic Forecasting

**arXiv**: [2512.09398v1](https://arxiv.org/abs/2512.09398) | [PDF](https://arxiv.org/pdf/2512.09398.pdf)

**作者**: Hongjun Wang, Jiawei Yong, Jiawei Wang, Shintaro Fukushima, Renhe Jiang

---

## 💡 一句话要点

**提出ConFormer框架，结合事故与法规数据以提升交通预测准确性**

**关键词**: `交通预测` `条件Transformer` `时空数据挖掘` `事故数据集成` `图传播`

## 📋 核心要点

1. 核心问题：交通预测受事故和法规等外部因素影响，现有模型因数据整合不足而受限
2. 方法要点：引入条件Transformer，通过图传播和引导归一化层动态调整时空节点关系
3. 实验或效果：在东京和加州数据集上超越STAEFormer，预测性能更优且计算成本更低

## 📄 摘要（原文）

> Traffic prediction remains a key challenge in spatio-temporal data mining, despite progress in deep learning. Accurate forecasting is hindered by the complex influence of external factors such as traffic accidents and regulations, often overlooked by existing models due to limited data integration. To address these limitations, we present two enriched traffic datasets from Tokyo and California, incorporating traffic accident and regulation data. Leveraging these datasets, we propose ConFormer (Conditional Transformer), a novel framework that integrates graph propagation with guided normalization layer. This design dynamically adjusts spatial and temporal node relationships based on historical patterns, enhancing predictive accuracy. Our model surpasses the state-of-the-art STAEFormer in both predictive performance and efficiency, achieving lower computational costs and reduced parameter demands. Extensive evaluations demonstrate that ConFormer consistently outperforms mainstream spatio-temporal baselines across multiple metrics, underscoring its potential to advance traffic prediction research.

