---
layout: default
title: StockMem: An Event-Reflection Memory Framework for Stock Forecasting
---

# StockMem: An Event-Reflection Memory Framework for Stock Forecasting

**arXiv**: [2512.02720v1](https://arxiv.org/abs/2512.02720) | [PDF](https://arxiv.org/pdf/2512.02720.pdf)

**作者**: He Wang, Wenyilin Xiao, Songqiao Han, Hailiang Huang

---

## 💡 一句话要点

**提出StockMem事件-反思双记忆框架以提升股票预测的准确性和可解释性**

**关键词**: `股票预测` `事件挖掘` `记忆框架` `可解释性` `金融分析`

## 📋 核心要点

1. 核心问题：股票预测受市场波动和实时事件影响，现有方法难以从噪声新闻中提取关键驱动因素。
2. 方法要点：构建事件知识库和反思知识库，通过横向整合和纵向跟踪挖掘事件演化与价格动态。
3. 实验或效果：实验显示StockMem优于现有记忆架构，提供可解释推理，增强金融预测决策透明度。

## 📄 摘要（原文）

> Stock price prediction is challenging due to market volatility and its sensitivity to real-time events. While large language models (LLMs) offer new avenues for text-based forecasting, their application in finance is hindered by noisy news data and the lack of explicit answers in text. General-purpose memory architectures struggle to identify the key drivers of price movements. To address this, we propose StockMem, an event-reflection dual-layer memory framework. It structures news into events and mines them along two dimensions: horizontal consolidation integrates daily events, while longitudinal tracking captures event evolution to extract incremental information reflecting market expectation discrepancies. This builds a temporal event knowledge base. By analyzing event-price dynamics, the framework further forms a reflection knowledge base of causal experiences. For prediction, it retrieves analogous historical scenarios and reasons with current events, incremental data, and past experiences. Experiments show StockMem outperforms existing memory architectures and provides superior, explainable reasoning by tracing the information chain affecting prices, enhancing decision transparency in financial forecasting.

