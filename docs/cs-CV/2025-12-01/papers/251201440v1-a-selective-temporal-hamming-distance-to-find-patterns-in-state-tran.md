---
layout: default
title: A Selective Temporal Hamming distance to find patterns in state transition event timeseries, at scale
---

# A Selective Temporal Hamming distance to find patterns in state transition event timeseries, at scale

**arXiv**: [2512.01440v1](https://arxiv.org/abs/2512.01440) | [PDF](https://arxiv.org/pdf/2512.01440.pdf)

**作者**: Sylvain Marié, Pablo Knecht

---

## 💡 一句话要点

**提出选择性时序汉明距离以高效分析大规模状态转移事件时间序列**

**关键词**: `状态转移事件时间序列` `选择性时序汉明距离` `离散事件系统` `时间序列分析` `大规模数据处理`

## 📋 核心要点

1. 核心问题：离散事件系统分析中，传统方法忽略事件/状态双重性，导致重采样失真且计算成本高。
2. 方法要点：定义状态转移事件时间序列，利用转移时间和状态持续时间，避免重采样，提升精度和效率。
3. 实验或效果：在模拟和真实数据集上验证了距离度量在精度和计算时间上的优势。

## 📄 摘要（原文）

> Discrete event systems are present both in observations of nature, socio economical sciences, and industrial systems. Standard analysis approaches do not usually exploit their dual event / state nature: signals are either modeled as transition event sequences, emphasizing event order alignment, or as categorical or ordinal state timeseries, usually resampled a distorting and costly operation as the observation period and number of events grow. In this work we define state transition event timeseries (STE-ts) and propose a new Selective Temporal Hamming distance (STH) leveraging both transition time and duration-in-state, avoiding costly and distorting resampling on large databases. STH generalizes both resampled Hamming and Jaccard metrics with better precision and computation time, and an ability to focus on multiple states of interest. We validate these benefits on simulated and real-world datasets.

