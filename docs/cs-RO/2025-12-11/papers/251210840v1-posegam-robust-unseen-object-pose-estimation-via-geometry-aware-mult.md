---
layout: default
title: PoseGAM: Robust Unseen Object Pose Estimation via Geometry-Aware Multi-View Reasoning
---

# PoseGAM: Robust Unseen Object Pose Estimation via Geometry-Aware Multi-View Reasoning

**arXiv**: [2512.10840v1](https://arxiv.org/abs/2512.10840) | [PDF](https://arxiv.org/pdf/2512.10840.pdf)

**作者**: Jianqi Chen, Biao Zhang, Xiangjun Tang, Peter Wonka

---

## 💡 一句话要点

**提出PoseGAM框架，通过几何感知多视图推理解决未见物体6D姿态估计问题。**

**关键词**: `6D姿态估计` `未见物体` `多视图推理` `几何感知` `合成数据集`

## 📋 核心要点

1. 核心问题：未见物体的6D姿态估计，现有方法依赖显式特征匹配，泛化能力有限。
2. 方法要点：基于多视图基础模型，结合显式点几何与几何表示网络特征，无需显式匹配。
3. 实验或效果：构建大规模合成数据集，在多个基准测试中实现SOTA，平均AR提升5.1%。

## 📄 摘要（原文）

> 6D object pose estimation, which predicts the transformation of an object relative to the camera, remains challenging for unseen objects. Existing approaches typically rely on explicitly constructing feature correspondences between the query image and either the object model or template images. In this work, we propose PoseGAM, a geometry-aware multi-view framework that directly predicts object pose from a query image and multiple template images, eliminating the need for explicit matching. Built upon recent multi-view-based foundation model architectures, the method integrates object geometry information through two complementary mechanisms: explicit point-based geometry and learned features from geometry representation networks. In addition, we construct a large-scale synthetic dataset containing more than 190k objects under diverse environmental conditions to enhance robustness and generalization. Extensive evaluations across multiple benchmarks demonstrate our state-of-the-art performance, yielding an average AR improvement of 5.1% over prior methods and achieving up to 17.6% gains on individual datasets, indicating strong generalization to unseen objects. Project page: https://windvchen.github.io/PoseGAM/ .

