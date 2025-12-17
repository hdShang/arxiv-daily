---
layout: default
title: An unscented Kalman filter method for real time input-parameter-state estimation
---

# An unscented Kalman filter method for real time input-parameter-state estimation

**arXiv**: [2511.02717v1](https://arxiv.org/abs/2511.02717) | [PDF](https://arxiv.org/pdf/2511.02717.pdf)

**作者**: Marios Impraimakis, Andrew W. Smyth

---

## 💡 一句话要点

**提出无迹卡尔曼滤波器方法，用于实时联合估计输入、参数和状态。**

**关键词**: `无迹卡尔曼滤波` `输入估计` `参数识别` `状态估计` `实时系统` `扰动分析`

## 📋 核心要点

1. 核心问题：在线性和非线性系统中，如何实时估计未知输入、参数和动态状态。
2. 方法要点：采用两阶段估计，先预测输入，再结合测量校正状态和参数。
3. 实验或效果：扰动分析表明，系统在已知输入下可唯一识别，优于传统输出策略。

## 📄 摘要（原文）

> The input-parameter-state estimation capabilities of a novel unscented Kalman
> filter is examined herein on both linear and nonlinear systems. The unknown
> input is estimated in two stages within each time step. Firstly, the predicted
> dynamic states and the system parameters provide an estimation of the input.
> Secondly, the corrected with measurements states and parameters provide a final
> estimation. Importantly, it is demonstrated using the perturbation analysis
> that, a system with at least a zero or a non-zero known input can potentially
> be uniquely identified. This output-only methodology allows for a better
> understanding of the system compared to classical output-only parameter
> identification strategies, given that all the dynamic states, the parameters,
> and the input are estimated jointly and in real-time.

