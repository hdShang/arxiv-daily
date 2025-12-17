---
layout: default
title: PFF-Net: Patch Feature Fitting for Point Cloud Normal Estimation
---

# PFF-Net: Patch Feature Fitting for Point Cloud Normal Estimation

**arXiv**: [2511.21365v1](https://arxiv.org/abs/2511.21365) | [PDF](https://arxiv.org/pdf/2511.21365.pdf)

**作者**: Qing Li, Huifang Feng, Kanle Shi, Yue Gao, Yi Fang, Yu-Shen Liu, Zhizhong Han

---

## 💡 一句话要点

**提出PFF-Net通过多尺度特征融合解决点云法向量估计中的邻域尺寸选择难题**

**关键词**: `点云法向量估计` `多尺度特征融合` `特征聚合` `特征补偿` `尺度自适应`

## 📋 核心要点

1. 核心问题：点云法向量估计中难以确定合适的邻域尺寸以适应不同数据或几何形状
2. 方法要点：使用多尺度特征聚合和跨尺度特征补偿来近似最优几何描述
3. 实验或效果：在合成和真实数据集上实现SOTA性能，参数和运行时间更少

## 📄 摘要（原文）

> Estimating the normal of a point requires constructing a local patch to provide center-surrounding context, but determining the appropriate neighborhood size is difficult when dealing with different data or geometries. Existing methods commonly employ various parameter-heavy strategies to extract a full feature description from the input patch. However, they still have difficulties in accurately and efficiently predicting normals for various point clouds. In this work, we present a new idea of feature extraction for robust normal estimation of point clouds. We use the fusion of multi-scale features from different neighborhood sizes to address the issue of selecting reasonable patch sizes for various data or geometries. We seek to model a patch feature fitting (PFF) based on multi-scale features to approximate the optimal geometric description for normal estimation and implement the approximation process via multi-scale feature aggregation and cross-scale feature compensation. The feature aggregation module progressively aggregates the patch features of different scales to the center of the patch and shrinks the patch size by removing points far from the center. It not only enables the network to precisely capture the structure characteristic in a wide range, but also describes highly detailed geometries. The feature compensation module ensures the reusability of features from earlier layers of large scales and reveals associated information in different patch sizes. Our approximation strategy based on aggregating the features of multiple scales enables the model to achieve scale adaptation of varying local patches and deliver the optimal feature description. Extensive experiments demonstrate that our method achieves state-of-the-art performance on both synthetic and real-world datasets with fewer network parameters and running time.

