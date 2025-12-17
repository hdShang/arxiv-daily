---
layout: default
title: SDE-Attention: Latent Attention in SDE-RNNs for Irregularly Sampled Time Series with Missing Data
---

# SDE-Attention: Latent Attention in SDE-RNNs for Irregularly Sampled Time Series with Missing Data

**arXiv**: [2511.23238v1](https://arxiv.org/abs/2511.23238) | [PDF](https://arxiv.org/pdf/2511.23238.pdf)

**作者**: Yuting Fang, Qouc Le Gia, Flora Salim

---

## 💡 一句话要点

**提出SDE-Attention，通过潜在注意力增强SDE-RNN，处理不规则采样和缺失数据的时间序列。**

**关键词**: `时间序列分析` `注意力机制` `缺失数据处理` `SDE-RNN` `不规则采样` `潜在状态建模`

## 📋 核心要点

1. 核心问题：处理医疗和传感器网络中不规则采样且大量缺失的时间序列数据。
2. 方法要点：在SDE-RNN的潜在状态引入通道级注意力，包括通道重校准、时变特征注意力和金字塔多尺度自注意力。
3. 实验或效果：在合成和真实数据集上，注意力模型优于基线，SDE-TVF-L在UCR数据集上平均准确率提升最高达10个百分点。

## 📄 摘要（原文）

> Irregularly sampled time series with substantial missing observations are common in healthcare and sensor networks. We introduce SDE-Attention, a family of SDE-RNNs equipped with channel-level attention on the latent pre-RNN state, including channel recalibration, time-varying feature attention, and pyramidal multi-scale self-attention. We therefore conduct a comparison on a synthetic periodic dataset and real-world benchmarks, under varying missing rate. Latent-space attention consistently improves over a vanilla SDE-RNN. On the univariate UCR datasets, the LSTM-based time-varying feature model SDE-TVF-L achieves the highest average accuracy, raising mean performance by approximately 4, 6, and 10 percentage points over the baseline at 30%, 60% and 90% missingness, respectively (averaged across datasets). On multivariate UEA benchmarks, attention-augmented models again outperform the backbone, with SDE-TVF-L yielding up to a 7% gain in mean accuracy under high missingness. Among the proposed mechanisms, time-varying feature attention is the most robust on univariate datasets. On multivariate datasets, different attention types excel on different tasks, showing that SDE-Attention can be flexibly adapted to the structure of each problem.

