---
layout: default
title: MapSAM2: Adapting SAM2 for Automatic Segmentation of Historical Map Images and Time Series
---

# MapSAM2: Adapting SAM2 for Automatic Segmentation of Historical Map Images and Time Series

**arXiv**: [2510.27547v1](https://arxiv.org/abs/2510.27547) | [PDF](https://arxiv.org/pdf/2510.27547.pdf)

**作者**: Xue Xia, Randall Balestriero, Tao Zhang, Yixin Zhou, Andrew Ding, Dev Saini, Lorenz Hurni

---

## 💡 一句话要点

**提出MapSAM2框架，基于视觉基础模型自动分割历史地图图像与时间序列**

**关键词**: `历史地图分割` `视觉基础模型` `时间序列分析` `少样本微调` `伪视频生成`

## 📋 核心要点

1. 历史地图风格多变且标注数据稀缺，自动化分析困难
2. 将地图图像与时间序列视为视频，利用注意力机制提升分割精度
3. 实验显示在有限监督下能有效学习时间关联，准确分割建筑

## 📄 摘要（原文）

> Historical maps are unique and valuable archives that document geographic
> features across different time periods. However, automated analysis of
> historical map images remains a significant challenge due to their wide
> stylistic variability and the scarcity of annotated training data. Constructing
> linked spatio-temporal datasets from historical map time series is even more
> time-consuming and labor-intensive, as it requires synthesizing information
> from multiple maps. Such datasets are essential for applications such as dating
> buildings, analyzing the development of road networks and settlements, studying
> environmental changes etc. We present MapSAM2, a unified framework for
> automatically segmenting both historical map images and time series. Built on a
> visual foundation model, MapSAM2 adapts to diverse segmentation tasks with
> few-shot fine-tuning. Our key innovation is to treat both historical map images
> and time series as videos. For images, we process a set of tiles as a video,
> enabling the memory attention mechanism to incorporate contextual cues from
> similar tiles, leading to improved geometric accuracy, particularly for areal
> features. For time series, we introduce the annotated Siegfried Building Time
> Series Dataset and, to reduce annotation costs, propose generating pseudo time
> series from single-year maps by simulating common temporal transformations.
> Experimental results show that MapSAM2 learns temporal associations effectively
> and can accurately segment and link buildings in time series under limited
> supervision or using pseudo videos. We will release both our dataset and code
> to support future research.

