---
layout: default
title: CYPRESS: Crop Yield Prediction via Regression on Prithvi's Encoder for Satellite Sensing
---

# CYPRESS: Crop Yield Prediction via Regression on Prithvi's Encoder for Satellite Sensing

**arXiv**: [2510.26609v1](https://arxiv.org/abs/2510.26609) | [PDF](https://arxiv.org/pdf/2510.26609.pdf)

**作者**: Shayan Nejadshamsi, Yuanyuan Zhang, Shadi Zaki, Brock Porth, Lysa Porth, Vahab Khoshdel

---

## 💡 一句话要点

**提出CYPRESS模型，通过回归预测作物产量，用于精准农业管理。**

**关键词**: `作物产量预测` `卫星遥感` `回归模型` `基础模型微调` `精准农业`

## 📋 核心要点

1. 核心问题：传统作物产量预测方法缺乏可扩展性和精细度，影响精准农业。
2. 方法要点：利用预训练地理空间基础模型，将多时相卫星图像转换为像素级产量图。
3. 实验或效果：在加拿大草原数据集上表现优于现有模型，验证了基础模型微调的有效性。

## 📄 摘要（原文）

> Accurate and timely crop yield prediction is crucial for global food security
> and modern agricultural management. Traditional methods often lack the
> scalability and granularity required for precision farming. This paper
> introduces CYPRESS (Crop Yield Prediction via Regression on Prithvi's Encoder
> for Satellite Sensing), a deep learning model designed for high-resolution,
> intra-field canola yield prediction. CYPRESS leverages a pre-trained,
> large-scale geospatial foundation model (Prithvi-EO-2.0-600M) and adapts it for
> a continuous regression task, transforming multi-temporal satellite imagery
> into dense, pixel-level yield maps. Evaluated on a comprehensive dataset from
> the Canadian Prairies, CYPRESS demonstrates superior performance over existing
> deep learning-based yield prediction models, highlighting the effectiveness of
> fine-tuning foundation models for specialized agricultural applications. By
> providing a continuous, high-resolution output, CYPRESS offers a more
> actionable tool for precision agriculture than conventional classification or
> county-level aggregation methods. This work validates a novel approach that
> bridges the gap between large-scale Earth observation and on-farm
> decision-making, offering a scalable solution for detailed agricultural
> monitoring.

