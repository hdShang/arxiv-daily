---
layout: default
title: Frailty-Aware Transformer for Recurrent Survival Modeling of Driver Retention in Ride-Hailing Platforms
---

# Frailty-Aware Transformer for Recurrent Survival Modeling of Driver Retention in Ride-Hailing Platforms

**arXiv**: [2511.19893v1](https://arxiv.org/abs/2511.19893) | [PDF](https://arxiv.org/pdf/2511.19893.pdf)

**作者**: Shuoyan Xu, Yu Zhang, Eric J. Miller

---

## 💡 一句话要点

**提出脆弱性感知Transformer，用于网约车平台司机保留的复发生存建模**

**关键词**: `生存分析` `Transformer模型` `复发事件建模` `网约车平台` `司机保留`

## 📋 核心要点

1. 核心问题：网约车平台中司机空闲行为的复发事件建模未被充分探索。
2. 方法要点：使用Transformer框架，结合因果掩码和司机嵌入捕捉长期依赖与异质性。
3. 实验或效果：在Toronto数据上，模型在C指数和Brier分数上优于基线方法。

## 📄 摘要（原文）

> Ride-hailing platforms are characterized by high-frequency, behavior-driven environments. Although survival analysis has been applied to recurrent events in other domains, its use in modeling ride-hailing driver behavior remains largely unexplored. This study formulates idle behavior as a recurrent survival process using large-scale platform data and proposes a Transformer-based framework that captures long-term temporal dependencies with causal masking and incorporates driver-specific embeddings to model latent heterogeneity. Results on Toronto ride-hailing data demonstrate that the proposed Frailty-Aware Cox Transformer (FACT) achieves the highest time-dependent C-indices and lowest Brier Scores, outperforming classical and deep learning survival models. This approach enables more accurate risk estimation, supports platform retention strategies, and provides policy-relevant insights.

