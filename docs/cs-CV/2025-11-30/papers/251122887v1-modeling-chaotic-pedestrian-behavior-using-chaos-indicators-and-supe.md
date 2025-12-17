---
layout: default
title: Modeling Chaotic Pedestrian Behavior Using Chaos Indicators and Supervised Learning
---

# Modeling Chaotic Pedestrian Behavior Using Chaos Indicators and Supervised Learning

**arXiv**: [2511.22887v1](https://arxiv.org/abs/2511.22887) | [PDF](https://arxiv.org/pdf/2511.22887.pdf)

**作者**: Md. Muhtashim Shahrier, Nazmul Haque, Md Asif Raihan, Md. Hadiuzzaman

---

## 💡 一句话要点

**提出基于混沌指标与监督学习的框架，以建模现实场景中行人行为的混沌性。**

**关键词**: `行人行为建模` `混沌指标` `监督学习` `计算机视觉` `轨迹分析` `风险评估`

## 📋 核心要点

1. 核心问题：城市步行性与安全提升需理解行人行为的不可预测性，但现有方法可能不足。
2. 方法要点：使用计算机视觉提取轨迹，量化混沌指标，通过PCA整合并训练回归模型预测混沌分数。
3. 实验或效果：CatBoost模型在日间和夜间分别达到R^2约0.83和0.86，SHAP分析识别关键特征如移动距离和速度变异性。

## 📄 摘要（原文）

> As cities around the world aim to improve walkability and safety, understanding the irregular and unpredictable nature of pedestrian behavior has become increasingly important. This study introduces a data-driven framework for modeling chaotic pedestrian movement using empirically observed trajectory data and supervised learning. Videos were recorded during both daytime and nighttime conditions to capture pedestrian dynamics under varying ambient and traffic contexts. Pedestrian trajectories were extracted through computer vision techniques, and behavioral chaos was quantified using four chaos metrics: Approximate Entropy and Lyapunov Exponent, each computed for both velocity and direction change. A Principal Component Analysis (PCA) was then applied to consolidate these indicators into a unified chaos score. A comprehensive set of individual, group-level, and contextual traffic features was engineered and used to train Random Forest and CatBoost regression models. CatBoost models consistently achieved superior performance. The best daytime PCA-based CatBoost model reached an R^2 of 0.8319, while the nighttime PCA-based CatBoost model attained an R^2 of 0.8574. SHAP analysis highlighted that features such as distance travel, movement duration, and speed variability were robust contributors to chaotic behavior. The proposed framework enables practitioners to quantify and anticipate behavioral instability in real-world settings. Planners and engineers can use chaos scores to identify high-risk pedestrian zones, apprise infrastructure improvements, and calibrate realistic microsimulation models. The approach also supports adaptive risk assessment in automated vehicle systems by capturing short-term motion unpredictability grounded in observable, interpretable features.

