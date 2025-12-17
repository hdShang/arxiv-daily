---
layout: default
title: Observation-driven correction of numerical weather prediction for marine winds
---

# Observation-driven correction of numerical weather prediction for marine winds

**arXiv**: [2512.03606v1](https://arxiv.org/abs/2512.03606) | [PDF](https://arxiv.org/pdf/2512.03606.pdf)

**作者**: Matteo Peduto, Qidong Yang, Jonathan Giezendanner, Devis Tuia, Sherrie Wang

---

## 💡 一句话要点

**提出基于Transformer的观测驱动校正方法，以提升海洋风数值天气预报精度。**

**关键词**: `海洋风预报` `数值天气预报校正` `Transformer架构` `观测同化` `深度学习` `时空预测`

## 📋 核心要点

1. 核心问题：海洋风预报因观测稀疏、异质和时变而具挑战性。
2. 方法要点：通过掩码和集合注意力机制，利用最新观测校正全球预报系统输出。
3. 实验或效果：在大西洋评估中，模型在1小时和48小时预报分别降低RMSE 45%和13%。

## 📄 摘要（原文）

> Accurate marine wind forecasts are essential for safe navigation, ship routing, and energy operations, yet they remain challenging because observations over the ocean are sparse, heterogeneous, and temporally variable. We reformulate wind forecasting as observation-informed correction of a global numerical weather prediction (NWP) model. Rather than forecasting winds directly, we learn local correction patterns by assimilating the latest in-situ observations to adjust the Global Forecast System (GFS) output. We propose a transformer-based deep learning architecture that (i) handles irregular and time-varying observation sets through masking and set-based attention mechanisms, (ii) conditions predictions on recent observation-forecast pairs via cross-attention, and (iii) employs cyclical time embeddings and coordinate-aware location representations to enable single-pass inference at arbitrary spatial coordinates. We evaluate our model over the Atlantic Ocean using observations from the International Comprehensive Ocean-Atmosphere Data Set (ICOADS) as reference. The model reduces GFS 10-meter wind RMSE at all lead times up to 48 hours, achieving 45% improvement at 1-hour lead time and 13% improvement at 48-hour lead time. Spatial analyses reveal the most persistent improvements along coastlines and shipping routes, where observations are most abundant. The tokenized architecture naturally accommodates heterogeneous observing platforms (ships, buoys, tide gauges, and coastal stations) and produces both site-specific predictions and basin-scale gridded products in a single forward pass. These results demonstrate a practical, low-latency post-processing approach that complements NWP by learning to correct systematic forecast errors.

