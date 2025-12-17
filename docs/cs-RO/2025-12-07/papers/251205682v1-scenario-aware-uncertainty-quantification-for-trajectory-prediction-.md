---
layout: default
title: Scenario-aware Uncertainty Quantification for Trajectory Prediction with Statistical Guarantees
---

# Scenario-aware Uncertainty Quantification for Trajectory Prediction with Statistical Guarantees

**arXiv**: [2512.05682v1](https://arxiv.org/abs/2512.05682) | [PDF](https://arxiv.org/pdf/2512.05682.pdf)

**作者**: Yiming Shu, Jiahui Xu, Linghuan Kong, Fangni Zhang, Guodong Yin, Chen Sun

---

## 💡 一句话要点

**提出场景感知不确定性量化框架，为轨迹预测提供统计保证的预测区间和可靠性评估。**

**关键词**: `轨迹预测` `不确定性量化` `自动驾驶` `保形预测` `场景感知` `可靠性评估`

## 📋 核心要点

1. 核心问题：现有深度学习轨迹预测器缺乏适应异构场景的不确定性量化框架，影响自动驾驶系统安全。
2. 方法要点：使用CopulaCPTS进行保形校准，生成场景特定预测区间；结合轨迹可靠性判别器分析误差与置信区间，建立可靠性模型。
3. 实验或效果：在nuPlan数据集上验证，有效实现场景感知不确定性量化和可靠性评估，提升下游规划模块的可靠性信息。

## 📄 摘要（原文）

> Reliable uncertainty quantification in trajectory prediction is crucial for safety-critical autonomous driving systems, yet existing deep learning predictors lack uncertainty-aware frameworks adaptable to heterogeneous real-world scenarios. To bridge this gap, we propose a novel scenario-aware uncertainty quantification framework to provide the predicted trajectories with prediction intervals and reliability assessment. To begin with, predicted trajectories from the trained predictor and their ground truth are projected onto the map-derived reference routes within the Frenet coordinate system. We then employ CopulaCPTS as the conformal calibration method to generate temporal prediction intervals for distinct scenarios as the uncertainty measure. Building upon this, within the proposed trajectory reliability discriminator (TRD), mean error and calibrated confidence intervals are synergistically analyzed to establish reliability models for different scenarios. Subsequently, the risk-aware discriminator leverages a joint risk model that integrates longitudinal and lateral prediction intervals within the Frenet coordinate to identify critical points. This enables segmentation of trajectories into reliable and unreliable segments, holding the advantage of informing downstream planning modules with actionable reliability results. We evaluated our framework using the real-world nuPlan dataset, demonstrating its effectiveness in scenario-aware uncertainty quantification and reliability assessment across diverse driving contexts.

