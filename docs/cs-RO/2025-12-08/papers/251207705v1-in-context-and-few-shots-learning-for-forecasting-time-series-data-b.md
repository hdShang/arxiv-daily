---
layout: default
title: In-Context and Few-Shots Learning for Forecasting Time Series Data based on Large Language Models
---

# In-Context and Few-Shots Learning for Forecasting Time Series Data based on Large Language Models

**arXiv**: [2512.07705v1](https://arxiv.org/abs/2512.07705) | [PDF](https://arxiv.org/pdf/2512.07705.pdf)

**作者**: Saroj Gopali, Bipin Chhetri, Deepika Giri, Sima Siami-Namini, Akbar Siami Namin

---

## 💡 一句话要点

**评估大语言模型在时间序列预测中的上下文与少样本学习性能**

**关键词**: `时间序列预测` `大语言模型` `上下文学习` `少样本学习` `基础模型` `深度学习`

## 📋 核心要点

1. 核心问题：比较大语言模型与传统方法在时间序列预测中的性能
2. 方法要点：使用上下文学习、零样本和少样本学习训练LLM，并对比TimesFM、TCN和LSTM
3. 实验或效果：TimesFM表现最佳，RMSE最低为0.3023，推理时间266秒

## 📄 摘要（原文）

> Existing data-driven approaches in modeling and predicting time series data include ARIMA (Autoregressive Integrated Moving Average), Transformer-based models, LSTM (Long Short-Term Memory) and TCN (Temporal Convolutional Network). These approaches, and in particular deep learning-based models such as LSTM and TCN, have shown great results in predicting time series data. With the advancement of leveraging pre-trained foundation models such as Large Language Models (LLMs) and more notably Google's recent foundation model for time series data, {\it TimesFM} (Time Series Foundation Model), it is of interest to investigate whether these foundation models have the capability of outperforming existing modeling approaches in analyzing and predicting time series data.
>   This paper investigates the performance of using LLM models for time series data prediction. We investigate the in-context learning methodology in the training of LLM models that are specific to the underlying application domain. More specifically, the paper explores training LLMs through in-context, zero-shot and few-shot learning and forecasting time series data with OpenAI {\tt o4-mini} and Gemini 2.5 Flash Lite, as well as the recent Google's Transformer-based TimesFM, a time series-specific foundation model, along with two deep learning models, namely TCN and LSTM networks. The findings indicate that TimesFM has the best overall performance with the lowest RMSE value (0.3023) and the competitive inference time (266 seconds). Furthermore, OpenAI's o4-mini also exhibits a good performance based on Zero Shot learning.
>   These findings highlight pre-trained time series foundation models as a promising direction for real-time forecasting, enabling accurate and scalable deployment with minimal model adaptation.

