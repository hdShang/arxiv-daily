---
layout: default
title: CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking
---

# CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking

**arXiv**: [2511.15580v1](https://arxiv.org/abs/2511.15580) | [PDF](https://arxiv.org/pdf/2511.15580.pdf)

**作者**: Sifan Zhou, Yichao Cao, Jiahao Nie, Yuqian Fu, Ziyu Zhao, Xiaobo Lu, Shuo Wang

---

## 💡 一句话要点

**提出CompTrack框架以解决点云跟踪中的空间和信息冗余问题**

**关键词**: `点云跟踪` `信息瓶颈` `低秩近似` `动态令牌压缩` `实时处理`

## 📋 核心要点

1. 核心问题：点云稀疏性导致背景噪声和前景信息冗余，影响跟踪精度与效率
2. 方法要点：使用空间前景预测器过滤背景，基于信息瓶颈动态压缩前景令牌
3. 实验效果：在KITTI等数据集上实现高性能实时跟踪，达90 FPS

## 📄 摘要（原文）

> 3D single object tracking (SOT) in LiDAR point clouds is a critical task in computer vision and autonomous driving. Despite great success having been achieved, the inherent sparsity of point clouds introduces a dual-redundancy challenge that limits existing trackers: (1) vast spatial redundancy from background noise impairs accuracy, and (2) informational redundancy within the foreground hinders efficiency. To tackle these issues, we propose CompTrack, a novel end-to-end framework that systematically eliminates both forms of redundancy in point clouds. First, CompTrack incorporates a Spatial Foreground Predictor (SFP) module to filter out irrelevant background noise based on information entropy, addressing spatial redundancy. Subsequently, its core is an Information Bottleneck-guided Dynamic Token Compression (IB-DTC) module that eliminates the informational redundancy within the foreground. Theoretically grounded in low-rank approximation, this module leverages an online SVD analysis to adaptively compress the redundant foreground into a compact and highly informative set of proxy tokens. Extensive experiments on KITTI, nuScenes and Waymo datasets demonstrate that CompTrack achieves top-performing tracking performance with superior efficiency, running at a real-time 90 FPS on a single RTX 3090 GPU.

