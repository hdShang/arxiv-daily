---
layout: default
title: Causal Inference in Energy Demand Prediction
---

# Causal Inference in Energy Demand Prediction

**arXiv**: [2512.11653v1](https://arxiv.org/abs/2512.11653) | [PDF](https://arxiv.org/pdf/2512.11653.pdf)

**作者**: Chutian Ma, Grigorii Pomazkin, Giacinto Paolo Saggese, Paul Smith

---

## 💡 一句话要点

**提出结构因果模型与贝叶斯模型，以提升能源需求预测的准确性和鲁棒性。**

**关键词**: `因果推断` `能源需求预测` `结构因果模型` `贝叶斯模型` `时间序列分析`

## 📋 核心要点

1. 核心问题：能源需求受天气和日历因素因果互依影响，传统相关学习方法难以充分处理。
2. 方法要点：构建结构因果模型揭示变量间因果关系，并基于此先验知识开发贝叶斯预测模型。
3. 实验或效果：在未见数据上测试，平均绝对百分比误差为3.84%，跨年交叉验证平均误差为3.88%。

## 📄 摘要（原文）

> Energy demand prediction is critical for grid operators, industrial energy
>   consumers, and service providers. Energy demand is influenced by multiple
>   factors, including weather conditions (e.g. temperature, humidity, wind
>   speed, solar radiation), and calendar information (e.g. hour of day and
>   month of year), which further affect daily work and life schedules. These
>   factors are causally interdependent, making the problem more complex than
>   simple correlation-based learning techniques satisfactorily allow for. We
>   propose a structural causal model that explains the causal relationship
>   between these variables. A full analysis is performed to validate our causal
>   beliefs, also revealing important insights consistent with prior studies.
>   For example, our causal model reveals that energy demand responds to
>   temperature fluctuations with season-dependent sensitivity. Additionally, we
>   find that energy demand exhibits lower variance in winter due to the
>   decoupling effect between temperature changes and daily activity patterns.
>   We then build a Bayesian model, which takes advantage of the causal insights
>   we learned as prior knowledge. The model is trained and tested on unseen
>   data and yields state-of-the-art performance in the form of a 3.84 percent MAPE on
>   the test set. The model also demonstrates strong robustness, as the
>   cross-validation across two years of data yields an average MAPE of 3.88 percent.

