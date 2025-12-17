---
layout: default
title: A Generalized Placeability Metric for Model-Free Unified Pick-and-Place Reasoning
---

# A Generalized Placeability Metric for Model-Free Unified Pick-and-Place Reasoning

**arXiv**: [2510.14584v1](https://arxiv.org/abs/2510.14584) | [PDF](https://arxiv.org/pdf/2510.14584.pdf)

**作者**: Benno Wingender, Nils Dengler, Rohit Menon, Sicong Pan, Maren Bennewitz

---

## 💡 一句话要点

**提出广义可放置性度量，用于无模型统一拾放推理，处理未知物体和噪声点云。**

**关键词**: `拾放推理` `可放置性度量` `点云处理` `稳定性预测` `无模型方法`

## 📋 核心要点

1. 核心问题：现有方法依赖物体先验或平面支撑假设，限制泛化和统一推理。
2. 方法要点：从噪声点云直接评估放置位姿，联合评分稳定性、可抓取性和间隙。
3. 实验或效果：在未知真实物体和非平面支撑上，预测稳定性损失精度与CAD相当。

## 📄 摘要（原文）

> To reliably pick and place unknown objects under real-world sensing noise
> remains a challenging task, as existing methods rely on strong object priors
> (e.g., CAD models), or planar-support assumptions, limiting generalization and
> unified reasoning between grasping and placing. In this work, we introduce a
> generalized placeability metric that evaluates placement poses directly from
> noisy point clouds, without any shape priors. The metric jointly scores
> stability, graspability, and clearance. From raw geometry, we extract the
> support surfaces of the object to generate diverse candidates for
> multi-orientation placement and sample contacts that satisfy collision and
> stability constraints. By conditioning grasp scores on each candidate
> placement, our proposed method enables model-free unified pick-and-place
> reasoning and selects grasp-place pairs that lead to stable, collision-free
> placements. On unseen real objects and non-planar object supports, our metric
> delivers CAD-comparable accuracy in predicting stability loss and generally
> produces more physically plausible placements than learning-based predictors.

