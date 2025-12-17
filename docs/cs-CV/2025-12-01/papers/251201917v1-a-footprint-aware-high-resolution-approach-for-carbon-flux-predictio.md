---
layout: default
title: A Footprint-Aware, High-Resolution Approach for Carbon Flux Prediction Across Diverse Ecosystems
---

# A Footprint-Aware, High-Resolution Approach for Carbon Flux Prediction Across Diverse Ecosystems

**arXiv**: [2512.01917v1](https://arxiv.org/abs/2512.01917) | [PDF](https://arxiv.org/pdf/2512.01917.pdf)

**作者**: Jacob Searcy, Anish Dulal, Scott Bridgham, Ashley Cordes, Lillian Aoki, Brendan Bohannan, Qing Zhu, Lucas C. R. Silva

---

## 💡 一句话要点

**提出Footprint-Aware Regression以解决大范围生态系统碳通量预测中空间尺度不匹配问题**

**关键词**: `碳通量预测` `深度学习框架` `空间足迹建模` `高分辨率遥感` `生态系统监测` `AMERI-FAR25数据集`

## 📋 核心要点

1. 核心问题：卫星测量空间尺度小于通量塔足迹，导致碳通量预测模型精度受限
2. 方法要点：开发深度学习框架FAR，同时预测空间足迹和30米像素级碳通量
3. 实验或效果：基于AMERI-FAR25数据集训练，测试集上预测月净生态系统交换R2达0.78

## 📄 摘要（原文）

> Natural climate solutions (NCS) offer an approach to mitigating carbon dioxide (CO2) emissions. However, monitoring the carbon drawdown of ecosystems over large geographic areas remains challenging. Eddy-flux covariance towers provide ground truth for predictive 'upscaling' models derived from satellite products, but many satellites now produce measurements on spatial scales smaller than a flux tower's footprint. We introduce Footprint-Aware Regression (FAR), a first-of-its-kind, deep-learning framework that simultaneously predicts spatial footprints and pixel-level (30 m scale) estimates of carbon flux. FAR is trained on our AMERI-FAR25 dataset which combines 439 site years of tower data with corresponding Landsat scenes. Our model produces high-resolution predictions and achieves R2 = 0.78 when predicting monthly net ecosystem exchange on test sites from a variety of ecosystems.

