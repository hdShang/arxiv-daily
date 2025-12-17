---
layout: default
title: CNN-Based Automated Parameter Extraction Framework for Modeling Memristive Devices
---

# CNN-Based Automated Parameter Extraction Framework for Modeling Memristive Devices

**arXiv**: [2511.07926v1](https://arxiv.org/abs/2511.07926) | [PDF](https://arxiv.org/pdf/2511.07926.pdf)

**作者**: Akif Hamid, Orchi Hassan

---

## 💡 一句话要点

**提出基于CNN的自动化参数提取框架，以解决RRAM建模中参数手动调优耗时问题。**

**关键词**: `RRAM建模` `参数提取` `卷积神经网络` `启发式优化` `非易失性存储器`

## 📋 核心要点

1. 核心问题：RRAM紧凑模型参数提取依赖手动调优，过程耗时且适应性差。
2. 方法要点：使用CNN生成初始参数估计，并通过启发式优化块进行误差最小化。
3. 实验或效果：在多个NVM指标上实现低误差，验证框架的快速性和鲁棒性。

## 📄 摘要（原文）

> Resistive random access memory (RRAM) is a promising candidate for next-generation nonvolatile memory (NVM) and in-memory computing applications. Compact models are essential for analyzing the circuit and system-level performance of experimental RRAM devices. However, most existing RRAM compact models rely on multiple fitting parameters to reproduce the device I-V characteristics, and in most cases, as the parameters are not directly related to measurable quantities, their extraction requires extensive manual tuning, making the process time-consuming and limiting adaptability across different devices. This work presents an automated framework for extracting the fitting parameters of the widely used Stanford RRAM model directly from the device I-V characteristics. The framework employs a convolutional neural network (CNN) trained on a synthetic dataset to generate initial parameter estimates, which are then refined through three heuristic optimization blocks that minimize errors via adaptive binary search in the parameter space. We evaluated the framework using four key NVM metrics: set voltage, reset voltage, hysteresis loop area, and low resistance state (LRS) slope. Benchmarking against RRAM device characteristics derived from previously reported Stanford model fits, other analytical models, and experimental data shows that the framework achieves low error across diverse device characteristics, offering a fast, reliable, and robust solution for RRAM modeling.

