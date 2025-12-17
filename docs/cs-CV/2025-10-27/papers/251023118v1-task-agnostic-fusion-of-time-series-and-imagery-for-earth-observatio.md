---
layout: default
title: Task-Agnostic Fusion of Time Series and Imagery for Earth Observation
---

# Task-Agnostic Fusion of Time Series and Imagery for Earth Observation

**arXiv**: [2510.23118v1](https://arxiv.org/abs/2510.23118) | [PDF](https://arxiv.org/pdf/2510.23118.pdf)

**作者**: Gianfranco Basile, Johannes Jakubik, Benedikt Blumenstiel, Thomas Brunschwiler, Juan Bernabe Moreno

---

## 💡 一句话要点

**提出任务无关框架融合时间序列与图像，用于地球观测中的跨模态生成与下游任务。**

**关键词**: `多模态融合` `时间序列量化` `掩码相关学习` `地球观测` `任务无关预训练` `跨模态生成`

## 📋 核心要点

1. 核心问题：如何任务无关地融合时间序列和单时间点图像，提升地球观测的鲁棒性。
2. 方法要点：采用时间序列量化与掩码相关学习，对齐图像和时间序列标记于统一表示空间。
3. 实验或效果：预训练模型在R²和RMSE指标上优于任务特定融合和基线方法，并验证了模型鲁棒性。

## 📄 摘要（原文）

> We propose a task-agnostic framework for multimodal fusion of time series and
> single timestamp images, enabling cross-modal generation and robust downstream
> performance. Our approach explores deterministic and learned strategies for
> time series quantization and then leverages a masked correlation learning
> objective, aligning discrete image and time series tokens in a unified
> representation space. Instantiated in the Earth observation domain, the
> pretrained model generates consistent global temperature profiles from
> satellite imagery and is validated through counterfactual experiments. Across
> downstream tasks, our task-agnostic pretraining outperforms task-specific
> fusion by 6\% in R$^2$ and 2\% in RMSE on average, and exceeds baseline methods
> by 50\% in R$^2$ and 12\% in RMSE. Finally, we analyze gradient sensitivity
> across modalities, providing insights into model robustness. Code, data, and
> weights will be released under a permissive license.

