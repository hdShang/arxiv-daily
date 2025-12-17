---
layout: default
title: Data-Driven Learnability Transition of Measurement-Induced Entanglement
---

# Data-Driven Learnability Transition of Measurement-Induced Entanglement

**arXiv**: [2512.01317v1](https://arxiv.org/abs/2512.01317) | [PDF](https://arxiv.org/pdf/2512.01317.pdf)

**作者**: Dongheng Qian, Jing Wang

---

## 💡 一句话要点

**提出数据驱动方法以解决测量诱导纠缠的经典可学习性评估问题**

**关键词**: `测量诱导纠缠` `数据驱动学习` `量子神经网络` `可学习性转变` `随机电路` `量子计算`

## 📋 核心要点

1. 核心问题：测量诱导纠缠的直接评估需大量后选择，资源消耗高，其经典可学习性未知
2. 方法要点：基于测量记录，以自监督方式训练神经网络预测纠缠不确定性度量
3. 实验或效果：在一维全连接和二维最近邻随机电路中揭示可学习性转变，并在噪声量子设备上验证

## 📄 摘要（原文）

> Measurement-induced entanglement (MIE) captures how local measurements generate long-range quantum correlations and drive dynamical phase transitions in many-body systems. Yet estimating MIE experimentally remains challenging: direct evaluation requires extensive post-selection over measurement outcomes, raising the question of whether MIE is accessible with only polynomial resources. We address this challenge by reframing MIE detection as a data-driven learning problem that assumes no prior knowledge of state preparation. Using measurement records alone, we train a neural network in a self-supervised manner to predict the uncertainty metric for MIE--the gap between upper and lower bounds of the average post-measurement bipartite entanglement. Applied to random circuits with one-dimensional all-to-all connectivity and two-dimensional nearest-neighbor coupling, our method reveals a learnability transition with increasing circuit depth: below a threshold, the uncertainty is small and decreases with polynomial measurement data and model parameters, while above it the uncertainty remains large despite increasing resources. We further verify this transition experimentally on current noisy quantum devices, demonstrating its robustness to realistic noise. These results highlight the power of data-driven approaches for learning MIE and delineate the practical limits of its classical learnability.

