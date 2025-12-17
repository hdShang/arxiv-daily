---
layout: default
title: Grazing Detection using Deep Learning and Sentinel-2 Time Series Data
---

# Grazing Detection using Deep Learning and Sentinel-2 Time Series Data

**arXiv**: [2510.14493v1](https://arxiv.org/abs/2510.14493) | [PDF](https://arxiv.org/pdf/2510.14493.pdf)

**作者**: Aleksis Pirinen, Delia Fano Yela, Smita Chakraborty, Erik Källman

---

## 💡 一句话要点

**提出基于CNN-LSTM集成模型的放牧检测方法，利用Sentinel-2时序数据优化资源分配。**

**关键词**: `放牧检测` `时序数据分析` `CNN-LSTM模型` `卫星遥感` `资源优化`

## 📋 核心要点

1. 核心问题：放牧监测缺乏可扩展方法，影响农业和生物多样性管理。
2. 方法要点：使用Sentinel-2 L2A时序影像，训练CNN-LSTM集成模型进行二元分类。
3. 实验或效果：平均F1分数77%，召回率90%，资源分配效率提升17.2倍。

## 📄 摘要（原文）

> Grazing shapes both agricultural production and biodiversity, yet scalable
> monitoring of where grazing occurs remains limited. We study seasonal grazing
> detection from Sentinel-2 L2A time series: for each polygon-defined field
> boundary, April-October imagery is used for binary prediction (grazed / not
> grazed). We train an ensemble of CNN-LSTM models on multi-temporal reflectance
> features, and achieve an average F1 score of 77 percent across five validation
> splits, with 90 percent recall on grazed pastures. Operationally, if inspectors
> can visit at most 4 percent of sites annually, prioritising fields predicted by
> our model as non-grazed yields 17.2 times more confirmed non-grazing sites than
> random inspection. These results indicate that coarse-resolution, freely
> available satellite data can reliably steer inspection resources for
> conservation-aligned land-use compliance. Code and models have been made
> publicly available.

