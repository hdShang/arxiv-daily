---
layout: default
title: Can Image-To-Video Models Simulate Pedestrian Dynamics?
---

# Can Image-To-Video Models Simulate Pedestrian Dynamics?

**arXiv**: [2510.17731v1](https://arxiv.org/abs/2510.17731) | [PDF](https://arxiv.org/pdf/2510.17731.pdf)

**作者**: Aaron Appelle, Jerome P. Lynch

---

## 💡 一句话要点

**评估图像到视频模型模拟拥挤场景中行人动态的能力**

**关键词**: `图像到视频模型` `行人动态模拟` `扩散变换器` `轨迹预测` `关键帧条件化`

## 📋 核心要点

1. 核心问题：图像到视频模型能否生成真实的行人运动模式
2. 方法要点：基于关键帧条件化扩散变换器模型进行视频生成
3. 实验或效果：使用行人轨迹基准进行定量评估动态性能

## 📄 摘要（原文）

> Recent high-performing image-to-video (I2V) models based on variants of the
> diffusion transformer (DiT) have displayed remarkable inherent world-modeling
> capabilities by virtue of training on large scale video datasets. We
> investigate whether these models can generate realistic pedestrian movement
> patterns in crowded public scenes. Our framework conditions I2V models on
> keyframes extracted from pedestrian trajectory benchmarks, then evaluates their
> trajectory prediction performance using quantitative measures of pedestrian
> dynamics.

