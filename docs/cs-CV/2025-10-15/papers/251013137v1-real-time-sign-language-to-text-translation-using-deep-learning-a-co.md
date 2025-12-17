---
layout: default
title: Real-Time Sign Language to text Translation using Deep Learning: A Comparative study of LSTM and 3D CNN
---

# Real-Time Sign Language to text Translation using Deep Learning: A Comparative study of LSTM and 3D CNN

**arXiv**: [2510.13137v1](https://arxiv.org/abs/2510.13137) | [PDF](https://arxiv.org/pdf/2510.13137.pdf)

**作者**: Madhumati Pol, Anvay Anturkar, Anushka Khot, Ayush Andure, Aniruddha Ghosh, Anvit Magadum, Anvay Bahadur

---

## 💡 一句话要点

**比较3D CNN与LSTM在实时美国手语识别中的性能，强调精度与效率权衡。**

**关键词**: `手语识别` `3D卷积神经网络` `长短期记忆网络` `实时系统` `边缘计算` `性能比较`

## 📋 核心要点

1. 核心问题：实时美国手语识别需平衡识别精度与计算效率。
2. 方法要点：评估3D CNN和LSTM在时空特征提取与序列建模中的表现。
3. 实验效果：3D CNN准确率92.4%，LSTM为86.7%，后者资源消耗更低。

## 📄 摘要（原文）

> This study investigates the performance of 3D Convolutional Neural Networks
> (3D CNNs) and Long Short-Term Memory (LSTM) networks for real-time American
> Sign Language (ASL) recognition. Though 3D CNNs are good at spatiotemporal
> feature extraction from video sequences, LSTMs are optimized for modeling
> temporal dependencies in sequential data. We evaluate both architectures on a
> dataset containing 1,200 ASL signs across 50 classes, comparing their accuracy,
> computational efficiency, and latency under similar training conditions.
> Experimental results demonstrate that 3D CNNs achieve 92.4% recognition
> accuracy but require 3.2% more processing time per frame compared to LSTMs,
> which maintain 86.7% accuracy with significantly lower resource consumption.
> The hybrid 3D CNNLSTM model shows decent performance, which suggests that
> context-dependent architecture selection is crucial for practical
> implementation.This project provides professional benchmarks for developing
> assistive technologies, highlighting trade-offs between recognition precision
> and real-time operational requirements in edge computing environments.

