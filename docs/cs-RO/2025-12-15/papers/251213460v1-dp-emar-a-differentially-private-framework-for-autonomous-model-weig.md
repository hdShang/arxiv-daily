---
layout: default
title: DP-EMAR: A Differentially Private Framework for Autonomous Model Weight Repair in Federated IoT Systems
---

# DP-EMAR: A Differentially Private Framework for Autonomous Model Weight Repair in Federated IoT Systems

**arXiv**: [2512.13460v1](https://arxiv.org/abs/2512.13460) | [PDF](https://arxiv.org/pdf/2512.13460.pdf)

**作者**: Chethana Prasad Kabgere, Shylaja S S

---

## 💡 一句话要点

**提出DP-EMAR框架，以差分隐私方式修复联邦物联网系统中的模型权重传输失真问题。**

**关键词**: `联邦学习` `差分隐私` `物联网系统` `模型修复` `安全聚合`

## 📋 核心要点

1. 核心问题：联邦物联网中模型权重因传输失真影响收敛，需在隐私保护下修复。
2. 方法要点：结合差分隐私与安全聚合，检测并自适应校正传输错误，区分噪声与真实失真。
3. 实验或效果：在异构数据集上验证，保持收敛稳定性和近基线性能，确保严格差分隐私保证。

## 📄 摘要（原文）

> Federated Learning (FL) enables decentralized model training without sharing raw data, but model weight distortion remains a major challenge in resource constrained IoT networks. In multi tier Federated IoT (Fed-IoT) systems, unstable connectivity and adversarial interference can silently alter transmitted parameters, degrading convergence. We propose DP-EMAR, a differentially private, error model based autonomous repair framework that detects and reconstructs transmission induced distortions during FL aggregation. DP-EMAR estimates corruption patterns and applies adaptive correction before privacy noise is added, enabling reliable in network repair without violating confidentiality. By integrating Differential Privacy (DP) with Secure Aggregation (SA), the framework distinguishes DP noise from genuine transmission errors. Experiments on heterogeneous IoT sensor and graph datasets show that DP-EMAR preserves convergence stability and maintains near baseline performance under communication corruption while ensuring strict (epsilon, delta)-DP guarantees. The framework enhances robustness, communication efficiency, and trust in privacy preserving Federated IoT learning.

