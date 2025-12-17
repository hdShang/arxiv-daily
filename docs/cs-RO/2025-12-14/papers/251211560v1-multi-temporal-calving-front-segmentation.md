---
layout: default
title: Multi-temporal Calving Front Segmentation
---

# Multi-temporal Calving Front Segmentation

**arXiv**: [2512.11560v1](https://arxiv.org/abs/2512.11560) | [PDF](https://arxiv.org/pdf/2512.11560.pdf)

**作者**: Marcel Dreier, Nora Gourmelon, Dakota Pyles, Fei Wu, Matthias Braun, Thorsten Seehaus, Andreas Maier, Vincent Christlein

---

## 💡 一句话要点

**提出多时相并行处理与特征交换方法，以提升合成孔径雷达影像中冰架崩解前缘分割的稳定性。**

**关键词**: `冰架崩解前缘分割` `合成孔径雷达影像` `多时相处理` `特征交换` `深度学习模型` `冰川监测`

## 📋 核心要点

1. 核心问题：现有深度学习模型在季节性条件如冰混合物或积雪覆盖区域分类困难。
2. 方法要点：并行处理同一冰川的卫星图像时间序列，并在特征图间交换时相信息以稳定预测。
3. 实验或效果：在CaFFe基准数据集上实现新最优性能，平均距离误差184.4米，平均交并比83.6%。

## 📄 摘要（原文）

> The calving fronts of marine-terminating glaciers undergo constant changes. These changes significantly affect the glacier's mass and dynamics, demanding continuous monitoring. To address this need, deep learning models were developed that can automatically delineate the calving front in Synthetic Aperture Radar imagery. However, these models often struggle to correctly classify areas affected by seasonal conditions such as ice melange or snow-covered surfaces. To address this issue, we propose to process multiple frames from a satellite image time series of the same glacier in parallel and exchange temporal information between the corresponding feature maps to stabilize each prediction. We integrate our approach into the current state-of-the-art architecture Tyrion and accomplish a new state-of-the-art performance on the CaFFe benchmark dataset. In particular, we achieve a Mean Distance Error of 184.4 m and a mean Intersection over Union of 83.6.

