---
layout: default
title: Identifying counterfactual probabilities using bivariate distributions and uplift modeling
---

# Identifying counterfactual probabilities using bivariate distributions and uplift modeling

**arXiv**: [2512.08805v1](https://arxiv.org/abs/2512.08805) | [PDF](https://arxiv.org/pdf/2512.08805.pdf)

**作者**: Théo Verhelst, Gianluca Bontempi

---

## 💡 一句话要点

**提出基于双变量Beta分布和提升建模的反事实概率估计方法，应用于电信客户流失分析。**

**关键词**: `反事实估计` `提升建模` `双变量分布` `因果推断` `客户流失分析`

## 📋 核心要点

1. 核心问题：反事实识别需估计干预下潜在结果的联合分布，比提升建模更复杂但信息更丰富。
2. 方法要点：利用提升模型预测分数拟合双变量Beta分布，生成反事实结果的后验分布，无需额外因果假设。
3. 实验或效果：模拟验证方法有效性，在电信客户流失问题中揭示标准机器学习或提升模型无法提供的洞察。

## 📄 摘要（原文）

> Uplift modeling estimates the causal effect of an intervention as the difference between potential outcomes under treatment and control, whereas counterfactual identification aims to recover the joint distribution of these potential outcomes (e.g., "Would this customer still have churned had we given them a marketing offer?"). This joint counterfactual distribution provides richer information than the uplift but is harder to estimate. However, the two approaches are synergistic: uplift models can be leveraged for counterfactual estimation. We propose a counterfactual estimator that fits a bivariate beta distribution to predicted uplift scores, yielding posterior distributions over counterfactual outcomes. Our approach requires no causal assumptions beyond those of uplift modeling. Simulations show the efficacy of the approach, which can be applied, for example, to the problem of customer churn in telecom, where it reveals insights unavailable to standard ML or uplift models alone.

