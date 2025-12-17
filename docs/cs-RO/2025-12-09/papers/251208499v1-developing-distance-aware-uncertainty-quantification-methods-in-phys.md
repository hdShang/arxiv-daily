---
layout: default
title: Developing Distance-Aware Uncertainty Quantification Methods in Physics-Guided Neural Networks for Reliable Bearing Health Prediction
---

# Developing Distance-Aware Uncertainty Quantification Methods in Physics-Guided Neural Networks for Reliable Bearing Health Prediction

**arXiv**: [2512.08499v1](https://arxiv.org/abs/2512.08499) | [PDF](https://arxiv.org/pdf/2512.08499.pdf)

**作者**: Waleed Razzaq, Yun-Bo Zhao

---

## 💡 一句话要点

**提出基于谱归一化的距离感知不确定性量化方法，用于物理引导神经网络以提升轴承健康预测的可靠性。**

**关键词**: `不确定性量化` `物理引导神经网络` `轴承健康预测` `谱归一化` `距离感知` `分布外泛化`

## 📋 核心要点

1. 现有不确定性方法在置信度校准、计算成本、距离感知和分布外泛化方面存在不足。
2. 引入PG-SNGP和PG-SNER两种方法，通过谱归一化保持输入到潜在空间的距离，结合高斯过程或深度证据回归进行不确定性建模。
3. 在PRONOSTIA数据集上测试，显示方法提高预测精度，在分布外条件下可靠泛化，并对对抗攻击和噪声保持鲁棒性。

## 📄 摘要（原文）

> Accurate and uncertainty-aware degradation estimation is essential for predictive maintenance in safety-critical systems like rotating machinery with rolling-element bearings. Many existing uncertainty methods lack confidence calibration, are costly to run, are not distance-aware, and fail to generalize under out-of-distribution data. We introduce two distance-aware uncertainty methods for deterministic physics-guided neural networks: PG-SNGP, based on Spectral Normalization Gaussian Process, and PG-SNER, based on Deep Evidential Regression. We apply spectral normalization to the hidden layers so the network preserves distances from input to latent space. PG-SNGP replaces the final dense layer with a Gaussian Process layer for distance-sensitive uncertainty, while PG-SNER outputs Normal Inverse Gamma parameters to model uncertainty in a coherent probabilistic form. We assess performance using standard accuracy metrics and a new distance-aware metric based on the Pearson Correlation Coefficient, which measures how well predicted uncertainty tracks the distance between test and training samples. We also design a dynamic weighting scheme in the loss to balance data fidelity and physical consistency. We test our methods on rolling-element bearing degradation using the PRONOSTIA dataset and compare them with Monte Carlo and Deep Ensemble PGNNs. Results show that PG-SNGP and PG-SNER improve prediction accuracy, generalize reliably under OOD conditions, and remain robust to adversarial attacks and noise.

