---
layout: default
title: A Comparison of Lightweight Deep Learning Models for Particulate-Matter Nowcasting in the Indian Subcontinent & Surrounding Regions
---

# A Comparison of Lightweight Deep Learning Models for Particulate-Matter Nowcasting in the Indian Subcontinent & Surrounding Regions

**arXiv**: [2511.11185v1](https://arxiv.org/abs/2511.11185) | [PDF](https://arxiv.org/pdf/2511.11185.pdf)

**作者**: Ansh Kushwaha, Kaushik Gopalan

---

## 💡 一句话要点

**提出轻量深度学习模型以改进印度次大陆及周边地区颗粒物临近预报**

**关键词**: `颗粒物临近预报` `轻量深度学习模型` `CAMS数据` `印度次大陆` `系统偏差优化` `快速推理`

## 📋 核心要点

1. 核心问题：印度次大陆及周边地区PM1、PM2.5和PM10的6小时临近预报准确性不足
2. 方法要点：利用CAMS分析数据，开发三种轻量架构，优化精度并减少系统偏差
3. 实验或效果：在2024年数据上评估，RMSE、MAE等指标优于Aurora基础模型

## 📄 摘要（原文）

> This paper is a submission for the Weather4Cast~2025 complementary Pollution Task and presents an efficient framework for 6-hour lead-time nowcasting of PM$_1$, PM$_{2.5}$, and PM$_{10}$ across the Indian subcontinent and surrounding regions. The proposed approach leverages analysis fields from the Copernicus Atmosphere Monitoring Service (CAMS) Global Atmospheric Composition Forecasts at 0.4 degree resolution. A 256x256 spatial region, covering 28.4S-73.6N and 32E-134.0E, is used as the model input, while predictions are generated for the central 128x128 area spanning 2.8S-48N and 57.6E-108.4E, ensuring an India-centric forecast domain with sufficient synoptic-scale context. Models are trained on CAMS analyses from 2021-2023 using a shuffled 90/10 split and independently evaluated on 2024 data. Three lightweight parameter-specific architectures are developed to improve accuracy, minimize systematic bias, and enable rapid inference. Evaluation using RMSE, MAE, Bias, and SSIM demonstrates substantial performance gains over the Aurora foundation model, underscoring the effectiveness of compact & specialized deep learning models for short-range forecasts on limited spatial domains.

