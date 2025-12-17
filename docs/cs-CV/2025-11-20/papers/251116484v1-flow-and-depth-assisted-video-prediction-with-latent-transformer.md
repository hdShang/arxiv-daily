---
layout: default
title: Flow and Depth Assisted Video Prediction with Latent Transformer
---

# Flow and Depth Assisted Video Prediction with Latent Transformer

**arXiv**: [2511.16484v1](https://arxiv.org/abs/2511.16484) | [PDF](https://arxiv.org/pdf/2511.16484.pdf)

**作者**: Eliyas Suleyman, Paul Henderson, Eksan Firkat, Nicolas Pugeault

---

## 💡 一句话要点

**提出结合点流和深度辅助的潜在变换器模型，以提升遮挡场景下的视频预测性能。**

**关键词**: `视频预测` `遮挡处理` `点流辅助` `深度图` `潜在变换器` `运动分布评估`

## 📋 核心要点

1. 核心问题：视频预测中遮挡和背景运动导致性能下降，现有模型难以处理。
2. 方法要点：在潜在变换器架构中整合点流和深度图，提供运动和几何结构信息。
3. 实验或效果：在合成和真实数据集上评估，辅助模型在遮挡场景和背景运动预测更准确。

## 📄 摘要（原文）

> Video prediction is a fundamental task for various downstream applications, including robotics and world modeling. Although general video prediction models have achieved remarkable performance in standard scenarios, occlusion is still an inherent challenge in video prediction. We hypothesize that providing explicit information about motion (via point-flow) and geometric structure (via depth-maps) will enable video prediction models to perform better in situations with occlusion and the background motion. To investigate this, we present the first systematic study dedicated to occluded video prediction. We use a standard multi-object latent transformer architecture to predict future frames, but modify this to incorporate information from depth and point-flow. We evaluate this model in a controlled setting on both synthetic and real-world datasets with not only appearance-based metrics but also Wasserstein distances on object masks, which can effectively measure the motion distribution of the prediction. We find that when the prediction model is assisted with point flow and depth, it performs better in occluded scenarios and predicts more accurate background motion compared to models without the help of these modalities.

