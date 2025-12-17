---
layout: default
title: A Lightweight 3D Anomaly Detection Method with Rotationally Invariant Features
---

# A Lightweight 3D Anomaly Detection Method with Rotationally Invariant Features

**arXiv**: [2511.13115v1](https://arxiv.org/abs/2511.13115) | [PDF](https://arxiv.org/pdf/2511.13115.pdf)

**作者**: Hanzhe Liang, Jie Zhou, Can Gao, Bingyang Guo, Jinbao Wang, Linlin Shen

---

## 💡 一句话要点

**提出旋转不变特征框架以解决3D点云异常检测中的方向变化问题**

**关键词**: `3D异常检测` `旋转不变特征` `点云处理` `轻量网络` `迁移学习` `工业应用`

## 📋 核心要点

1. 3D异常检测中，点云方向和位置变化导致特征不稳定，影响检测性能。
2. 采用点坐标映射和轻量卷积变换网络，提取旋转不变特征并构建记忆库。
3. 在Anomaly-ShapeNet和Real3D-AD数据集上，P-AUROC指标显著提升，验证强泛化能力。

## 📄 摘要（原文）

> 3D anomaly detection (AD) is a crucial task in computer vision, aiming to identify anomalous points or regions from point cloud data. However, existing methods may encounter challenges when handling point clouds with changes in orientation and position because the resulting features may vary significantly. To address this problem, we propose a novel Rotationally Invariant Features (RIF) framework for 3D AD. Firstly, to remove the adverse effect of variations on point cloud data, we develop a Point Coordinate Mapping (PCM) technique, which maps each point into a rotationally invariant space to maintain consistency of representation. Then, to learn robust and discriminative features, we design a lightweight Convolutional Transform Feature Network (CTF-Net) to extract rotationally invariant features for the memory bank. To improve the ability of the feature extractor, we introduce the idea of transfer learning to pre-train the feature extractor with 3D data augmentation. Experimental results show that the proposed method achieves the advanced performance on the Anomaly-ShapeNet dataset, with an average P-AUROC improvement of 17.7\%, and also gains the best performance on the Real3D-AD dataset, with an average P-AUROC improvement of 1.6\%. The strong generalization ability of RIF has been verified by combining it with traditional feature extraction methods on anomaly detection tasks, demonstrating great potential for industrial applications.

