---
layout: default
title: SpectralKrum: A Spectral-Geometric Defense Against Byzantine Attacks in Federated Learning
---

# SpectralKrum: A Spectral-Geometric Defense Against Byzantine Attacks in Federated Learning

**arXiv**: [2512.11760v1](https://arxiv.org/abs/2512.11760) | [PDF](https://arxiv.org/pdf/2512.11760.pdf)

**作者**: Aditya Tripathi, Karan Sharma, Rahul Mishra, Tapas Kumar Maiti

---

## 💡 一句话要点

**提出SpectralKrum防御方法，结合谱子空间估计与几何邻居选择，以应对联邦学习中的拜占庭攻击。**

**关键词**: `联邦学习` `拜占庭攻击防御` `谱子空间估计` `鲁棒聚合` `非独立同分布数据` `模型更新过滤`

## 📋 核心要点

1. 核心问题：联邦学习在非独立同分布数据下，现有鲁棒聚合方法对拜占庭攻击的防御效果显著下降。
2. 方法要点：通过历史聚合估计低维流形，将更新投影到子空间，结合Krum选择和残差能量阈值过滤。
3. 实验或效果：在CIFAR-10非独立同分布数据上评估，对方向性和子空间感知攻击有效，但对标签翻转和最小最大攻击优势有限。

## 📄 摘要（原文）

> Federated Learning (FL) distributes model training across clients who retain their data locally, but this architecture exposes a fundamental vulnerability: Byzantine clients can inject arbitrarily corrupted updates that degrade or subvert the global model. While robust aggregation methods (including Krum, Bulyan, and coordinate-wise defenses) offer theoretical guarantees under idealized assumptions, their effectiveness erodes substantially when client data distributions are heterogeneous (non-IID) and adversaries can observe or approximate the defense mechanism.
>   This paper introduces SpectralKrum, a defense that fuses spectral subspace estimation with geometric neighbor-based selection. The core insight is that benign optimization trajectories, despite per-client heterogeneity, concentrate near a low-dimensional manifold that can be estimated from historical aggregates. SpectralKrum projects incoming updates into this learned subspace, applies Krum selection in compressed coordinates, and filters candidates whose orthogonal residual energy exceeds a data-driven threshold. The method requires no auxiliary data, operates entirely on model updates, and preserves FL privacy properties.
>   We evaluate SpectralKrum against eight robust baselines across seven attack scenarios on CIFAR-10 with Dirichlet-distributed non-IID partitions (alpha = 0.1). Experiments spanning over 56,000 training rounds show that SpectralKrum is competitive against directional and subspace-aware attacks (adaptive-steer, buffer-drift), but offers limited advantage under label-flip and min-max attacks where malicious updates remain spectrally indistinguishable from benign ones.

