---
layout: default
title: Super-Resolved Canopy Height Mapping from Sentinel-2 Time Series Using LiDAR HD Reference Data across Metropolitan France
---

# Super-Resolved Canopy Height Mapping from Sentinel-2 Time Series Using LiDAR HD Reference Data across Metropolitan France

**arXiv**: [2512.11524v1](https://arxiv.org/abs/2512.11524) | [PDF](https://arxiv.org/pdf/2512.11524.pdf)

**作者**: Ekaterina Kalinicheva, Florian Helen, Stéphane Mermoz, Florian Mouret, Milena Planells

---

## 💡 一句话要点

**提出THREASURE-Net框架，利用Sentinel-2时序数据和LiDAR参考实现森林冠层高度超分辨率制图**

**关键词**: `森林冠层高度制图` `超分辨率` `深度学习` `Sentinel-2时序数据` `LiDAR参考数据` `端到端框架`

## 📋 核心要点

1. 核心问题：精细尺度森林监测需高分辨率冠层高度图，以评估碳储量、生物多样性和森林健康。
2. 方法要点：THREASURE-Net为端到端深度学习框架，整合光谱、时空信号，从LiDAR高度数据学习超分辨率，无需预训练模型或高分辨率光学影像。
3. 实验或效果：在法国大都市区评估，生成2.5米、5米和10米分辨率高度图，平均绝对误差分别为2.62米、2.72米和2.88米，优于现有方法。

## 📄 摘要（原文）

> Fine-scale forest monitoring is essential for understanding canopy structure and its dynamics, which are key indicators of carbon stocks, biodiversity, and forest health. Deep learning is particularly effective for this task, as it integrates spectral, temporal, and spatial signals that jointly reflect the canopy structure. To address this need, we introduce THREASURE-Net, a novel end-to-end framework for Tree Height Regression And Super-Resolution. The model is trained on Sentinel-2 time series using reference height metrics derived from LiDAR HD data at multiple spatial resolutions over Metropolitan France to produce annual height maps. We evaluate three model variants, producing tree-height predictions at 2.5 m, 5 m, and 10 m resolution. THREASURE-Net does not rely on any pretrained model nor on reference very high resolution optical imagery to train its super-resolution module; instead, it learns solely from LiDAR-derived height information. Our approach outperforms existing state-of-the-art methods based on Sentinel data and is competitive with methods based on very high resolution imagery. It can be deployed to generate high-precision annual canopy-height maps, achieving mean absolute errors of 2.62 m, 2.72 m, and 2.88 m at 2.5 m, 5 m, and 10 m resolution, respectively. These results highlight the potential of THREASURE-Net for scalable and cost-effective structural monitoring of temperate forests using only freely available satellite data. The source code for THREASURE-Net is available at: https://github.com/Global-Earth-Observation/threasure-net.

