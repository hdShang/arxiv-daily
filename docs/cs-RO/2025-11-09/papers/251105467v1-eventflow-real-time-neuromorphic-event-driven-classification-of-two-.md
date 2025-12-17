---
layout: default
title: EventFlow: Real-Time Neuromorphic Event-Driven Classification of Two-Phase Boiling Flow Regimes
---

# EventFlow: Real-Time Neuromorphic Event-Driven Classification of Two-Phase Boiling Flow Regimes

**arXiv**: [2511.05467v1](https://arxiv.org/abs/2511.05467) | [PDF](https://arxiv.org/pdf/2511.05467.pdf)

**作者**: Sanghyeon Chang, Srikar Arani, Nishant Sai Nuthalapati, Youngjoon Suh, Nicholas Choi, Siavash Khodakarami, Md Rakibul Hasan Roni, Nenad Miljkovic, Aparna Chandramowlishwaran, Yoonjin Won

---

## 💡 一句话要点

**提出EventFlow框架，基于神经形态传感器实时分类两相沸腾流态，以解决传统光学方法延迟高的问题。**

**关键词**: `神经形态传感器` `事件驱动分类` `两相沸腾流态` `实时监测` `长短期记忆模型` `异步处理`

## 📋 核心要点

1. 核心问题：传统光学成像方法计算需求高、时间分辨率不足，无法捕捉瞬态流态变化。
2. 方法要点：使用神经形态传感器的事件数据，开发分类模型，包括事件LSTM模型。
3. 实验或效果：事件LSTM模型准确率达97.6%，处理时间0.28毫秒，支持低延迟实时预测。

## 📄 摘要（原文）

> Flow boiling is an efficient heat transfer mechanism capable of dissipating
> high heat loads with minimal temperature variation, making it an ideal thermal
> management method. However, sudden shifts between flow regimes can disrupt
> thermal performance and system reliability, highlighting the need for accurate
> and low-latency real-time monitoring. Conventional optical imaging methods are
> limited by high computational demands and insufficient temporal resolution,
> making them inadequate for capturing transient flow behavior. To address this,
> we propose a real-time framework based on signals from neuromorphic sensors for
> flow regime classification. Neuromorphic sensors detect changes in brightness
> at individual pixels, which typically correspond to motion at edges, enabling
> fast and efficient detection without full-frame reconstruction, providing
> event-based information. We develop five classification models using both
> traditional image data and event-based data, demonstrating that models
> leveraging event data outperform frame-based approaches due to their
> sensitivity to dynamic flow features. Among these models, the event-based long
> short-term memory model provides the best balance between accuracy and speed,
> achieving 97.6% classification accuracy with a processing time of 0.28 ms. Our
> asynchronous processing pipeline supports continuous, low-latency predictions
> and delivers stable output through a majority voting mechanisms, enabling
> reliable real-time feedback for experimental control and intelligent thermal
> management.

