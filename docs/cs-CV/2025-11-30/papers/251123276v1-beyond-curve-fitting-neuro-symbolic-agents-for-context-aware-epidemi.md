---
layout: default
title: Beyond Curve Fitting: Neuro-Symbolic Agents for Context-Aware Epidemic Forecasting
---

# Beyond Curve Fitting: Neuro-Symbolic Agents for Context-Aware Epidemic Forecasting

**arXiv**: [2511.23276v1](https://arxiv.org/abs/2511.23276) | [PDF](https://arxiv.org/pdf/2511.23276.pdf)

**作者**: Joongwon Chae, Runming Wang, Chen Xiong, Gong Yunhan, Lian Zhang, Ji Jiansong, Dongmei Yu, Peiwu Qin

---

## 💡 一句话要点

**提出双智能体框架以解决手足口病预测中上下文因果推理不足的问题。**

**关键词**: `流行病预测` `神经符号AI` `上下文感知` `概率预测` `LLM应用`

## 📋 核心要点

1. 核心问题：传统模型缺乏语义推理能力，难以处理学校日历和天气等冲突驱动因素的因果交互。
2. 方法要点：使用LLM事件解释器处理异构信号，结合神经符号核心进行概率预测。
3. 实验或效果：在真实数据集上实现竞争性点预测精度，并提供稳健的预测区间和可解释性。

## 📄 摘要（原文）

> Effective surveillance of hand, foot and mouth disease (HFMD) requires forecasts accounting for epidemiological patterns and contextual drivers like school calendars and weather. While classical models and recent foundation models (e.g., Chronos, TimesFM) incorporate covariates, they often lack the semantic reasoning to interpret the causal interplay between conflicting drivers. In this work, we propose a two-agent framework decoupling contextual interpretation from probabilistic forecasting. An LLM "event interpreter" processes heterogeneous signals-including school schedules, meteorological summaries, and reports-into a scalar transmission-impact signal. A neuro-symbolic core then combines this with historical case counts to produce calibrated probabilistic forecasts. We evaluate the framework on real-world HFMD datasets from Hong Kong (2023-2024) and Lishui, China (2024). Compared to traditional and foundation-model baselines, our approach achieves competitive point forecasting accuracy while providing robust 90% prediction intervals (coverage 0.85-1.00) and human-interpretable rationales. Our results suggest that structurally integrating domain knowledge through LLMs can match state-of-the-art performance while yielding context-aware forecasts that align with public health workflows. Code is available at https://github.com/jw-chae/forecast_MED .

