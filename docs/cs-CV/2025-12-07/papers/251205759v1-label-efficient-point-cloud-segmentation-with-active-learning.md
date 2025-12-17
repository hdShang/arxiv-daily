---
layout: default
title: Label-Efficient Point Cloud Segmentation with Active Learning
---

# Label-Efficient Point Cloud Segmentation with Active Learning

**arXiv**: [2512.05759v1](https://arxiv.org/abs/2512.05759) | [PDF](https://arxiv.org/pdf/2512.05759.pdf)

**作者**: Johannes Meyer, Jasper Hoffmann, Felix Schulz, Dominik Merkle, Daniel Buescher, Alexander Reiterer, Joschka Boedecker, Wolfram Burgard

---

## 💡 一句话要点

**提出基于2D网格分割和网络集成不确定性的主动学习策略，以降低3D点云语义分割的标注成本。**

**关键词**: `3D点云语义分割` `主动学习` `标注效率` `不确定性估计` `网络集成` `2D网格分割`

## 📋 核心要点

1. 核心问题：3D点云语义分割标注成本高，需高效选择标注数据。
2. 方法要点：使用2D网格将点云分割为柱状区域，结合网络集成估计不确定性以选择标注样本。
3. 实验或效果：在S3DIS、Toronto-3D和Freiburg数据集上评估，性能媲美或优于复杂方法，并探讨标注面积作为衡量指标。

## 📄 摘要（原文）

> Semantic segmentation of 3D point cloud data often comes with high annotation costs. Active learning automates the process of selecting which data to annotate, reducing the total amount of annotation needed to achieve satisfactory performance. Recent approaches to active learning for 3D point clouds are often based on sophisticated heuristics for both, splitting point clouds into annotatable regions and selecting the most beneficial for further neural network training. In this work, we propose a novel and easy-to-implement strategy to separate the point cloud into annotatable regions. In our approach, we utilize a 2D grid to subdivide the point cloud into columns. To identify the next data to be annotated, we employ a network ensemble to estimate the uncertainty in the network output. We evaluate our method on the S3DIS dataset, the Toronto-3D dataset, and a large-scale urban 3D point cloud of the city of Freiburg, which we labeled in parts manually. The extensive evaluation shows that our method yields performance on par with, or even better than, complex state-of-the-art methods on all datasets. Furthermore, we provide results suggesting that in the context of point clouds the annotated area can be a more meaningful measure for active learning algorithms than the number of annotated points.

