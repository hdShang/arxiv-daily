---
layout: default
title: Hybrid Quantum-Classical Autoencoders for Unsupervised Network Intrusion Detection
---

# Hybrid Quantum-Classical Autoencoders for Unsupervised Network Intrusion Detection

**arXiv**: [2512.05069v1](https://arxiv.org/abs/2512.05069) | [PDF](https://arxiv.org/pdf/2512.05069.pdf)

**作者**: Mohammad Arif Rasyidi, Omar Alhussein, Sami Muhaidat, Ernesto Damiani

---

## 💡 一句话要点

**提出混合量子-经典自编码器用于无监督网络入侵检测，首次大规模评估其性能与设计因素。**

**关键词**: `混合量子-经典自编码器` `无监督网络入侵检测` `量子设计选择` `零日评估` `噪声模拟`

## 📋 核心要点

1. 核心问题：无监督异常检测需模型泛化至未见攻击模式，传统方法可能受限。
2. 方法要点：构建统一框架，迭代量子层放置、测量方式等关键设计选择，探索变分与非变分形式。
3. 实验或效果：在三个基准数据集上，最佳配置可匹配或超越经典性能，零日评估中泛化更强更稳定。

## 📄 摘要（原文）

> Unsupervised anomaly-based intrusion detection requires models that can generalize to attack patterns not observed during training. This work presents the first large-scale evaluation of hybrid quantum-classical (HQC) autoencoders for this task. We construct a unified experimental framework that iterates over key quantum design choices, including quantum-layer placement, measurement approach, variational and non-variational formulations, and latent-space regularization. Experiments across three benchmark NIDS datasets show that HQC autoencoders can match or exceed classical performance in their best configurations, although they exhibit higher sensitivity to architectural decisions. Under zero-day evaluation, well-configured HQC models provide stronger and more stable generalization than classical and supervised baselines. Simulated gate-noise experiments reveal early performance degradation, indicating the need for noise-aware HQC designs. These results provide the first data-driven characterization of HQC autoencoder behavior for network intrusion detection and outline key factors that govern their practical viability. All experiment code and configurations are available at https://github.com/arasyi/hqcae-network-intrusion-detection.

