---
layout: default
title: Beyond Accuracy: An Empirical Study of Uncertainty Estimation in Imputation
---

# Beyond Accuracy: An Empirical Study of Uncertainty Estimation in Imputation

**arXiv**: [2511.21607v1](https://arxiv.org/abs/2511.21607) | [PDF](https://arxiv.org/pdf/2511.21607.pdf)

**作者**: Zarin Tahia Hossain, Mostafa Milani

---

## 💡 一句话要点

**系统评估插补方法的不确定性估计，分析准确性与校准的错位**

**关键词**: `不确定性估计` `数据插补` `校准误差` `缺失数据处理` `深度生成模型`

## 📋 核心要点

1. 核心问题：插补方法的不确定性估计可靠性和校准性未知
2. 方法要点：比较统计、分布对齐和深度生成三类代表性方法
3. 实验或效果：多数据集实验显示高准确性不一定带来可靠不确定性

## 📄 摘要（原文）

> Handling missing data is a central challenge in data-driven analysis. Modern imputation methods not only aim for accurate reconstruction but also differ in how they represent and quantify uncertainty. Yet, the reliability and calibration of these uncertainty estimates remain poorly understood. This paper presents a systematic empirical study of uncertainty in imputation, comparing representative methods from three major families: statistical (MICE, SoftImpute), distribution alignment (OT-Impute), and deep generative (GAIN, MIWAE, TabCSDI). Experiments span multiple datasets, missingness mechanisms (MCAR, MAR, MNAR), and missingness rates. Uncertainty is estimated through three complementary routes: multi-run variability, conditional sampling, and predictive-distribution modeling, and evaluated using calibration curves and the Expected Calibration Error (ECE). Results show that accuracy and calibration are often misaligned: models with high reconstruction accuracy do not necessarily yield reliable uncertainty. We analyze method-specific trade-offs among accuracy, calibration, and runtime, identify stable configurations, and offer guidelines for selecting uncertainty-aware imputers in data cleaning and downstream machine learning pipelines.

