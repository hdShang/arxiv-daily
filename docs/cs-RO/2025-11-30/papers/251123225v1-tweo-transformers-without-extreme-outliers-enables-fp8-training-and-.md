---
layout: default
title: TWEO: Transformers Without Extreme Outliers Enables FP8 Training And Quantization For Dummies
---

# TWEO: Transformers Without Extreme Outliers Enables FP8 Training And Quantization For Dummies

**arXiv**: [2511.23225v1](https://arxiv.org/abs/2511.23225) | [PDF](https://arxiv.org/pdf/2511.23225.pdf)

**作者**: Guang Liang, Jie Shao, Ningyuan Tang, Xinyao Liu, Jianxin Wu

---

## 💡 一句话要点

**提出TWEO损失函数以解决Transformer训练中极端异常值问题，实现FP8训练与量化**

**关键词**: `Transformer训练` `FP8量化` `异常值抑制` `损失函数设计` `硬件加速` `模型压缩`

## 📋 核心要点

1. 核心问题：Transformer训练中极端激活异常值阻碍FP8硬件支持，传统方法依赖复杂工程或架构修改
2. 方法要点：基于权重矩阵共线性分析，提出非侵入性TWEO损失函数，简单有效抑制异常值
3. 实验或效果：TWEO使FP8训练性能媲美BF16基线，提升训练吞吐量36%，并实现W8A8量化SOTA性能

## 📄 摘要（原文）

> Native FP8 support in modern hardware is essential for training large Transformers, but is severely hindered by extreme activation outliers. Existing solutions either rely on complex mixed-precision engineering or invasive architectural modifications. This paper fundamentally challenges the conventional wisdom that outliers are data-driven. We demonstrate that extreme outliers are a data-independent, mechanically-produced artifact of training, originating from specific structural properties of the weight matrices (i.e., colinearity). Based on this insight, we propose TWEO (Transformers Without Extreme Outliers), a novel, non-invasive loss function. TWEO effectively prevents extreme outliers via a very simple loss term, which reduces outliers from 10000+ to less than 20. TWEO then enables full-model FP8 pre-training with neither engineering tricks nor architectural changes for both LLM and ViT. When standard FP8 training catastrophically collapses, TWEO achieves performance comparable to the BF16 baseline while delivering a 36% increase in training throughput. Also, TWEO enables a new quantization paradigm. Hardware-friendly W8A8 per-tensor static quantization of LLMs, previously considered completely unusable due to outliers, achieves SOTA performance for the first time on TWEO-trained models.

