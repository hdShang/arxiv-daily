---
layout: default
title: ReLaX: Reasoning with Latent Exploration for Large Reasoning Models
---

# ReLaX: Reasoning with Latent Exploration for Large Reasoning Models

**arXiv**: [2512.07558v1](https://arxiv.org/abs/2512.07558) | [PDF](https://arxiv.org/pdf/2512.07558.pdf)

**作者**: Shimin Zhang, Xianwei Chen, Yufan Shen, Ziyuan Ye, Jibin Wu

---

## 💡 一句话要点

**提出ReLaX范式，通过调控潜在动态以解决大型推理模型中的熵崩溃问题。**

**关键词**: `大型推理模型` `强化学习` `潜在动态分析` `探索与利用平衡` `Koopman算子理论`

## 📋 核心要点

1. 核心问题：RLVR导致熵崩溃，引发策略早熟收敛和性能饱和。
2. 方法要点：利用Koopman算子理论线性化潜在动态，引入DSD指标量化探索，提出ReLaX调控探索与利用。
3. 实验或效果：在多模态和纯文本推理基准上显著缓解早熟收敛，实现SOTA性能。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has recently demonstrated remarkable potential in enhancing the reasoning capability of Large Reasoning Models (LRMs). However, RLVR often leads to entropy collapse, resulting in premature policy convergence and performance saturation. While manipulating token-level entropy has proven effective for promoting policy exploration, we argue that the latent dynamics underlying token generation encode a far richer computational structure for steering policy optimization toward a more effective exploration-exploitation tradeoff. To enable tractable analysis and intervention of the latent dynamics of LRMs, we leverage Koopman operator theory to obtain a linearized representation of their hidden-state dynamics. This enables us to introduce Dynamic Spectral Dispersion (DSD), a new metric to quantify the heterogeneity of the model's latent dynamics, serving as a direct indicator of policy exploration. Building upon these foundations, we propose Reasoning with Latent eXploration (ReLaX), a paradigm that explicitly incorporates latent dynamics to regulate exploration and exploitation during policy optimization. Comprehensive experiments across a wide range of multimodal and text-only reasoning benchmarks show that ReLaX significantly mitigates premature convergence and consistently achieves state-of-the-art performance.

