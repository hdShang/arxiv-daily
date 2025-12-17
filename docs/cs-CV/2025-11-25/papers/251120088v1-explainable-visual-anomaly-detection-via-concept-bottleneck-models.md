---
layout: default
title: Explainable Visual Anomaly Detection via Concept Bottleneck Models
---

# Explainable Visual Anomaly Detection via Concept Bottleneck Models

**arXiv**: [2511.20088v1](https://arxiv.org/abs/2511.20088) | [PDF](https://arxiv.org/pdf/2511.20088.pdf)

**作者**: Arianna Stropeni, Valentina Zaccaria, Francesco Borsatti, Davide Dalle Pezze, Manuel Barusco, Gian Antonio Susto

---

## 💡 一句话要点

**提出概念瓶颈模型扩展以解决视觉异常检测中解释缺乏语义意义的问题**

**关键词**: `视觉异常检测` `概念瓶颈模型` `可解释人工智能` `语义解释` `异常合成`

## 📋 核心要点

1. 核心问题：现有视觉异常检测模型提供视觉解释但缺乏直接语义解释，影响用户理解
2. 方法要点：扩展概念瓶颈模型，学习有意义概念以生成人类可解释的异常描述
3. 实验或效果：CONVAD方法性能与经典方法相当，提供更丰富概念驱动解释，增强可解释性和信任

## 📄 摘要（原文）

> In recent years, Visual Anomaly Detection (VAD) has gained significant attention due to its ability to identify anomalous images using only normal images during training. Many VAD models work without supervision but are still able to provide visual explanations by highlighting the anomalous regions within an image. However, although these visual explanations can be helpful, they lack a direct and semantically meaningful interpretation for users. To address this limitation, we propose extending Concept Bottleneck Models (CBMs) to the VAD setting. By learning meaningful concepts, the network can provide human-interpretable descriptions of anomalies, offering a novel and more insightful way to explain them. Our contributions are threefold: (i) we develop a Concept Dataset to support research on CBMs for VAD; (ii) we improve the CBM architecture to generate both concept-based and visual explanations, bridging semantic and localization interpretability; and (iii) we introduce a pipeline for synthesizing artificial anomalies, preserving the VAD paradigm of minimizing dependence on rare anomalous samples. Our approach, Concept-Aware Visual Anomaly Detection (CONVAD), achieves performance comparable to classic VAD methods while providing richer, concept-driven explanations that enhance interpretability and trust in VAD systems.

