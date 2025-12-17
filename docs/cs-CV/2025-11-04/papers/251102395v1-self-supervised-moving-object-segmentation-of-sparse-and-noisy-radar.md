---
layout: default
title: Self-Supervised Moving Object Segmentation of Sparse and Noisy Radar Point Clouds
---

# Self-Supervised Moving Object Segmentation of Sparse and Noisy Radar Point Clouds

**arXiv**: [2511.02395v1](https://arxiv.org/abs/2511.02395) | [PDF](https://arxiv.org/pdf/2511.02395.pdf)

**作者**: Leon Schwarzer, Matthias Zeller, Daniel Casado Herraez, Simon Dierl, Michael Heidingsfeld, Cyrill Stachniss

---

## 💡 一句话要点

**提出自监督对比学习与聚类损失方法，以解决稀疏噪声雷达点云的运动目标分割问题。**

**关键词**: `运动目标分割` `雷达点云` `自监督学习` `对比学习` `聚类损失` `标签效率`

## 📋 核心要点

1. 核心问题：雷达点云稀疏噪声导致监督学习标注成本高，且需单次扫描分割运动目标。
2. 方法要点：采用两阶段自监督表示学习与监督微调，引入聚类对比损失和动态点移除。
3. 实验或效果：自监督预训练提升标签效率，微调后超越现有最佳性能。

## 📄 摘要（原文）

> Moving object segmentation is a crucial task for safe and reliable autonomous
> mobile systems like self-driving cars, improving the reliability and robustness
> of subsequent tasks like SLAM or path planning. While the segmentation of
> camera or LiDAR data is widely researched and achieves great results, it often
> introduces an increased latency by requiring the accumulation of temporal
> sequences to gain the necessary temporal context. Radar sensors overcome this
> problem with their ability to provide a direct measurement of a point's Doppler
> velocity, which can be exploited for single-scan moving object segmentation.
> However, radar point clouds are often sparse and noisy, making data annotation
> for use in supervised learning very tedious, time-consuming, and
> cost-intensive. To overcome this problem, we address the task of
> self-supervised moving object segmentation of sparse and noisy radar point
> clouds. We follow a two-step approach of contrastive self-supervised
> representation learning with subsequent supervised fine-tuning using limited
> amounts of annotated data. We propose a novel clustering-based contrastive loss
> function with cluster refinement based on dynamic points removal to pretrain
> the network to produce motion-aware representations of the radar data. Our
> method improves label efficiency after fine-tuning, effectively boosting
> state-of-the-art performance by self-supervised pretraining.

