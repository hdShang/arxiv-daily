---
layout: default
title: Machine learning in an expectation-maximisation framework for nowcasting
---

# Machine learning in an expectation-maximisation framework for nowcasting

**arXiv**: [2512.07335v1](https://arxiv.org/abs/2512.07335) | [PDF](https://arxiv.org/pdf/2512.07335.pdf)

**作者**: Paul Wilsens, Katrien Antonio, Gerda Claeskens

---

## 💡 一句话要点

**提出基于期望最大化框架的机器学习方法，用于处理事件报告延迟的实时预测问题。**

**关键词**: `实时预测` `期望最大化框架` `机器学习建模` `事件报告延迟` `高维协变量` `XGBoost`

## 📋 核心要点

1. 核心问题：决策中信息不完整导致风险估计偏差，源于事件发生与报告过程的延迟。
2. 方法要点：在EM框架中集成机器学习模型，如神经网络和XGBoost，以建模高维协变量和非线性效应。
3. 实验或效果：模拟实验验证有效性，应用于阿根廷新冠病例报告，XGBoost方法表现最优。

## 📄 摘要（原文）

> Decision making often occurs in the presence of incomplete information, leading to the under- or overestimation of risk. Leveraging the observable information to learn the complete information is called nowcasting. In practice, incomplete information is often a consequence of reporting or observation delays. In this paper, we propose an expectation-maximisation (EM) framework for nowcasting that uses machine learning techniques to model both the occurrence as well as the reporting process of events. We allow for the inclusion of covariate information specific to the occurrence and reporting periods as well as characteristics related to the entity for which events occurred. We demonstrate how the maximisation step and the information flow between EM iterations can be tailored to leverage the predictive power of neural networks and (extreme) gradient boosting machines (XGBoost). With simulation experiments, we show that we can effectively model both the occurrence and reporting of events when dealing with high-dimensional covariate information. In the presence of non-linear effects, we show that our methodology outperforms existing EM-based nowcasting frameworks that use generalised linear models in the maximisation step. Finally, we apply the framework to the reporting of Argentinian Covid-19 cases, where the XGBoost-based approach again is most performant.

