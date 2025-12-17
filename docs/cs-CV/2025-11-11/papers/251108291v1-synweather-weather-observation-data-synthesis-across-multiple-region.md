---
layout: default
title: SynWeather: Weather Observation Data Synthesis across Multiple Regions and Variables via a General Diffusion Transformer
---

# SynWeather: Weather Observation Data Synthesis across Multiple Regions and Variables via a General Diffusion Transformer

**arXiv**: [2511.08291v1](https://arxiv.org/abs/2511.08291) | [PDF](https://arxiv.org/pdf/2511.08291.pdf)

**作者**: Kaiyi Xu, Junchao Gong, Zhiwang Zhou, Zhangrui Li, Yuandong Pu, Yihao Liu, Ben Fei, Fenghua Ling, Wenlong Zhang, Lei Bei

---

## 💡 一句话要点

**提出SynWeatherDiff扩散变换器模型，解决多区域多变量天气观测数据合成中的过平滑问题。**

**关键词**: `天气数据合成` `扩散变换器` `多变量建模` `多区域分析` `概率模型` `观测数据`

## 📋 核心要点

1. 核心问题：现有方法局限于单变量单区域，忽略跨变量互补性，导致过平滑结果。
2. 方法要点：基于扩散变换器框架构建概率模型，实现统一多区域多变量天气数据合成。
3. 实验或效果：在SynWeather数据集上验证，优于任务特定和通用模型。

## 📄 摘要（原文）

> With the advancement of meteorological instruments, abundant data has become available. Current approaches are typically focus on single-variable, single-region tasks and primarily rely on deterministic modeling. This limits unified synthesis across variables and regions, overlooks cross-variable complementarity and often leads to over-smoothed results. To address above challenges, we introduce SynWeather, the first dataset designed for Unified Multi-region and Multi-variable Weather Observation Data Synthesis. SynWeather covers four representative regions: the Continental United States, Europe, East Asia, and Tropical Cyclone regions, as well as provides high-resolution observations of key weather variables, including Composite Radar Reflectivity, Hourly Precipitation, Visible Light, and Microwave Brightness Temperature. In addition, we introduce SynWeatherDiff, a general and probabilistic weather synthesis model built upon the Diffusion Transformer framework to address the over-smoothed problem. Experiments on the SynWeather dataset demonstrate the effectiveness of our network compared with both task-specific and general models.

