---
layout: default
title: Delta-XAI: A Unified Framework for Explaining Prediction Changes in Online Time Series Monitoring
---

# Delta-XAI: A Unified Framework for Explaining Prediction Changes in Online Time Series Monitoring

**arXiv**: [2511.23036v1](https://arxiv.org/abs/2511.23036) | [PDF](https://arxiv.org/pdf/2511.23036.pdf)

**作者**: Changhun Kim, Yechan Mun, Hyeongwon Jang, Eunseo Lee, Sangchul Hahn, Eunho Yang

---

## 💡 一句话要点

**提出Delta-XAI框架，通过包装现有方法和引入评估套件，解释在线时间序列监测中的预测变化。**

**关键词**: `在线时间序列监测` `可解释人工智能` `预测变化解释` `时间依赖分析` `评估套件`

## 📋 核心要点

1. 核心问题：现有XAI方法独立分析时间步，忽略时间依赖，难以解释预测变化和利用在线动态。
2. 方法要点：Delta-XAI包装14种现有XAI方法，提出SWING方法，通过整合过去观测捕捉时间依赖。
3. 实验或效果：实验显示梯度方法如IG在时间分析中表现优异，SWING在多种设置和指标下有效。

## 📄 摘要（原文）

> Explaining online time series monitoring models is crucial across sensitive domains such as healthcare and finance, where temporal and contextual prediction dynamics underpin critical decisions. While recent XAI methods have improved the explainability of time series models, they mostly analyze each time step independently, overlooking temporal dependencies. This results in further challenges: explaining prediction changes is non-trivial, methods fail to leverage online dynamics, and evaluation remains difficult. To address these challenges, we propose Delta-XAI, which adapts 14 existing XAI methods through a wrapper function and introduces a principled evaluation suite for the online setting, assessing diverse aspects, such as faithfulness, sufficiency, and coherence. Experiments reveal that classical gradient-based methods, such as Integrated Gradients (IG), can outperform recent approaches when adapted for temporal analysis. Building on this, we propose Shifted Window Integrated Gradients (SWING), which incorporates past observations in the integration path to systematically capture temporal dependencies and mitigate out-of-distribution effects. Extensive experiments consistently demonstrate the effectiveness of SWING across diverse settings with respect to diverse metrics. Our code is publicly available at https://anonymous.4open.science/r/Delta-XAI.

