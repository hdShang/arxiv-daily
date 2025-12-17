---
layout: default
title: Real-Time Performance Analysis of Multi-Fidelity Residual Physics-Informed Neural Process-Based State Estimation for Robotic Systems
---

# Real-Time Performance Analysis of Multi-Fidelity Residual Physics-Informed Neural Process-Based State Estimation for Robotic Systems

**arXiv**: [2511.08231v1](https://arxiv.org/abs/2511.08231) | [PDF](https://arxiv.org/pdf/2511.08231.pdf)

**作者**: Devin Hunter, Chinwendu Enyioha

---

## 💡 一句话要点

**提出多保真残差物理信息神经过程方法，用于机器人系统实时状态估计**

**关键词**: `状态估计` `物理信息神经网络` `多保真学习` `不确定性建模` `机器人系统` `实时应用`

## 📋 核心要点

1. 核心问题：机器人状态估计中模型不匹配和不确定性影响实时性与安全性。
2. 方法要点：结合多保真残差学习和分形预测框架，提升估计精度与鲁棒性。
3. 实验或效果：在实时场景中优于卡尔曼滤波器变体，验证了方法的可行性。

## 📄 摘要（原文）

> Various neural network architectures are used in many of the state-of-the-art approaches for real-time nonlinear state estimation. With the ever-increasing incorporation of these data-driven models into the estimation domain, model predictions with reliable margins of error are a requirement -- especially for safety-critical applications. This paper discusses the application of a novel real-time, data-driven estimation approach based on the multi-fidelity residual physics-informed neural process (MFR-PINP) toward the real-time state estimation of a robotic system. Specifically, we address the model-mismatch issue of selecting an accurate kinematic model by tasking the MFR-PINP to also learn the residuals between simple, low-fidelity predictions and complex, high-fidelity ground-truth dynamics. To account for model uncertainty present in a physical implementation, robust uncertainty guarantees from the split conformal (SC) prediction framework are modeled in the training and inference paradigms. We provide implementation details of our MFR-PINP-based estimator for a hybrid online learning setting to validate our model's usage in real-time applications. Experimental results of our approach's performance in comparison to the state-of-the-art variants of the Kalman filter (i.e. unscented Kalman filter and deep Kalman filter) in estimation scenarios showed promising results for the MFR-PINP model as a viable option in real-time estimation tasks.

