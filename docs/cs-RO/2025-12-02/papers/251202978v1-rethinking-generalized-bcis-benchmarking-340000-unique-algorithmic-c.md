---
layout: default
title: Rethinking Generalized BCIs: Benchmarking 340,000+ Unique Algorithmic Configurations for EEG Mental Command Decoding
---

# Rethinking Generalized BCIs: Benchmarking 340,000+ Unique Algorithmic Configurations for EEG Mental Command Decoding

**arXiv**: [2512.02978v1](https://arxiv.org/abs/2512.02978) | [PDF](https://arxiv.org/pdf/2512.02978.pdf)

**作者**: Paul Barbaste, Olivier Oullier, Xavier Vasques

---

## 💡 一句话要点

**大规模基准测试340,000+算法配置，评估EEG脑机接口中个体化解码方法**

**关键词**: `脑机接口` `EEG解码` `基准测试` `个体化算法` `黎曼几何` `功能连接`

## 📋 核心要点

1. 核心问题：EEG脑机接口因个体间和个体内变异性，在真实世界应用中解码稳健性不足。
2. 方法要点：结合CSP、黎曼几何、功能连接及非线性特征，在三个开放数据集上评估多频段算法组合。
3. 实验或效果：cov-tgsp和CSP平均准确率最高，但效果依赖数据集，非线性方法对特定个体更优，强调个性化选择。

## 📄 摘要（原文）

> Robust decoding and classification of brain patterns measured with electroencephalography (EEG) remains a major challenge for real-world (i.e. outside scientific lab and medical facilities) brain-computer interface (BCI) applications due to well documented inter- and intra-participant variability. Here, we present a large-scale benchmark evaluating over 340,000+ unique combinations of spatial and nonlinear EEG classification. Our methodological pipeline consists in combinations of Common Spatial Patterns (CSP), Riemannian geometry, functional connectivity, and fractal- or entropy-based features across three open-access EEG datasets. Unlike prior studies, our analysis operates at the per-participant level and across multiple frequency bands (8-15 Hz and 8-30 Hz), enabling direct assessment of both group-level performance and individual variability. Covariance tangent space projection (cov-tgsp) and CSP consistently achieved the highest average classification accuracies. However, their effectiveness was strongly dataset-dependent, and marked participant-level differences persisted, particularly in the most heterogeneous of the datasets. Importantly, nonlinear methods outperformed spatial approaches for specific individuals, underscoring the need for personalized pipeline selection. Our findings highlight that no universal 'one-size-fits-all' method can optimally decode EEG motor imagery patterns across all users or datasets. Future work will require adaptive, multimodal, and possibly novel approaches to fully address neurophysiological variability in practical BCI applications where the system can automatically adapt to what makes each user unique.

