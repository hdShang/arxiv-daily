---
layout: default
title: Recurrent Neural Networks with Linear Structures for Electricity Price Forecasting
---

# Recurrent Neural Networks with Linear Structures for Electricity Price Forecasting

**arXiv**: [2512.04690v1](https://arxiv.org/abs/2512.04690) | [PDF](https://arxiv.org/pdf/2512.04690.pdf)

**作者**: Souhir Ben Amor, Florian Ziel

---

## 💡 一句话要点

**提出结合线性结构的循环神经网络，用于日前电价预测以提高能源系统决策准确性。**

**关键词**: `电价预测` `循环神经网络` `线性结构` `可解释模型` `能源系统管理`

## 📋 核心要点

1. 核心问题：日前电价预测对能源系统短期决策至关重要，需捕捉市场复杂特征。
2. 方法要点：将专家模型和卡尔曼滤波器等线性结构嵌入循环神经网络，增强可解释性和计算效率。
3. 实验或效果：在欧洲最大电力市场数据上测试，模型比先进基准准确率提高约12%。

## 📄 摘要（原文）

> We present a novel recurrent neural network architecture designed explicitly for day-ahead electricity price forecasting, aimed at improving short-term decision-making and operational management in energy systems. Our combined forecasting model embeds linear structures, such as expert models and Kalman filters, into recurrent networks, enabling efficient computation and enhanced interpretability. The design leverages the strengths of both linear and non-linear model structures, allowing it to capture all relevant stylised price characteristics in power markets, including calendar and autoregressive effects, as well as influences from load, renewable energy, and related fuel and carbon markets. For empirical testing, we use hourly data from the largest European electricity market spanning 2018 to 2025 in a comprehensive forecasting study, comparing our model against state-of-the-art approaches, particularly high-dimensional linear and neural network models. The proposed model achieves approximately 12% higher accuracy than leading benchmarks. We evaluate the contributions of the interpretable model components and conclude on the impact of combining linear and non-linear structures.

