---
layout: default
title: Reproducing and Extending RaDelft 4D Radar with Camera-Assisted Labels
---

# Reproducing and Extending RaDelft 4D Radar with Camera-Assisted Labels

**arXiv**: [2512.02394v1](https://arxiv.org/abs/2512.02394) | [PDF](https://arxiv.org/pdf/2512.02394.pdf)

**作者**: Kejia Hu, Mohammed Alsakabi, John M. Dolan, Ozan K. Tonguz

---

## 💡 一句话要点

**提出相机辅助雷达标注方法，以解决4D雷达语义分割中开源标签稀缺问题。**

**关键词**: `4D雷达语义分割` `相机辅助标注` `雷达点云处理` `可复现框架` `雾天影响分析`

## 📋 核心要点

1. 核心问题：4D雷达语义分割因开源数据集和标签稀缺而受限，RaDelft数据集仅提供LiDAR标注。
2. 方法要点：通过将雷达点云投影到相机语义分割图并应用空间聚类，生成无需人工标注的雷达标签。
3. 实验或效果：该方法显著提升雷达标签准确性，建立可复现框架，并量化雾天对标注性能的影响。

## 📄 摘要（原文）

> Recent advances in 4D radar highlight its potential for robust environment perception under adverse conditions, yet progress in radar semantic segmentation remains constrained by the scarcity of open source datasets and labels. The RaDelft data set, although seminal, provides only LiDAR annotations and no public code to generate radar labels, limiting reproducibility and downstream research. In this work, we reproduce the numerical results of the RaDelft group and demonstrate that a camera-guided radar labeling pipeline can generate accurate labels for radar point clouds without relying on human annotations. By projecting radar point clouds into camera-based semantic segmentation and applying spatial clustering, we create labels that significantly enhance the accuracy of radar labels. These results establish a reproducible framework that allows the research community to train and evaluate the labeled 4D radar data. In addition, we study and quantify how different fog levels affect the radar labeling performance.

