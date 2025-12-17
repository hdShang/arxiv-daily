---
layout: default
title: Revisiting Evaluation of Deep Neural Networks for Pedestrian Detection
---

# Revisiting Evaluation of Deep Neural Networks for Pedestrian Detection

**arXiv**: [2511.10308v1](https://arxiv.org/abs/2511.10308) | [PDF](https://arxiv.org/pdf/2511.10308.pdf)

**作者**: Patrick Feifel, Benedikt Franke, Frank Bonarens, Frank Köster, Arne Raulf, Friedhelm Schwenker

---

## 💡 一句话要点

**提出基于图像分割的错误分类和新指标，以改进行人检测评估**

**关键词**: `行人检测` `评估指标` `图像分割` `错误分类` `深度神经网络` `自动驾驶`

## 📋 核心要点

1. 当前行人检测评估指标存在缺陷，无法真实反映深度神经网络性能
2. 利用图像分割自动区分八种错误类型，并设计新指标进行模型比较
3. 在CityPersons数据集上实现SOTA，展示更细粒度和安全关键性能评估

## 📄 摘要（原文）

> Reliable pedestrian detection represents a crucial step towards automated driving systems. However, the current performance benchmarks exhibit weaknesses. The currently applied metrics for various subsets of a validation dataset prohibit a realistic performance evaluation of a DNN for pedestrian detection. As image segmentation supplies fine-grained information about a street scene, it can serve as a starting point to automatically distinguish between different types of errors during the evaluation of a pedestrian detector. In this work, eight different error categories for pedestrian detection are proposed and new metrics are proposed for performance comparison along these error categories. We use the new metrics to compare various backbones for a simplified version of the APD, and show a more fine-grained and robust way to compare models with each other especially in terms of safety-critical performance. We achieve SOTA on CityPersons-reasonable (without extra training data) by using a rather simple architecture.

