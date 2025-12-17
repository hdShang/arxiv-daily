---
layout: default
title: DriveLiDAR4D: Sequential and Controllable LiDAR Scene Generation for Autonomous Driving
---

# DriveLiDAR4D: Sequential and Controllable LiDAR Scene Generation for Autonomous Driving

**arXiv**: [2511.13309v1](https://arxiv.org/abs/2511.13309) | [PDF](https://arxiv.org/pdf/2511.13309.pdf)

**作者**: Kaiwen Cai, Xinze Liu, Xia Zhou, Hengtong Hu, Jie Xiang, Luyao Zhang, Xueyang Zhang, Kun Zhan, Yifei Zhan, Xianpeng Lang

---

## 💡 一句话要点

**提出DriveLiDAR4D以解决自动驾驶中LiDAR场景序列生成与可控性问题**

**关键词**: `LiDAR点云生成` `自动驾驶仿真` `序列生成` `可控场景生成` `多模态条件` `噪声预测模型`

## 📋 核心要点

1. 现有LiDAR点云生成方法缺乏序列生成能力，且前景对象定位和背景真实性不足
2. 采用多模态条件和LiDAR4DNet模型，实现端到端可控序列生成
3. 在nuScenes数据集上FRD和FVD分数超越SOTA方法，性能提升显著

## 📄 摘要（原文）

> The generation of realistic LiDAR point clouds plays a crucial role in the development and evaluation of autonomous driving systems. Although recent methods for 3D LiDAR point cloud generation have shown significant improvements, they still face notable limitations, including the lack of sequential generation capabilities and the inability to produce accurately positioned foreground objects and realistic backgrounds. These shortcomings hinder their practical applicability. In this paper, we introduce DriveLiDAR4D, a novel LiDAR generation pipeline consisting of multimodal conditions and a novel sequential noise prediction model LiDAR4DNet, capable of producing temporally consistent LiDAR scenes with highly controllable foreground objects and realistic backgrounds. To the best of our knowledge, this is the first work to address the sequential generation of LiDAR scenes with full scene manipulation capability in an end-to-end manner. We evaluated DriveLiDAR4D on the nuScenes and KITTI datasets, where we achieved an FRD score of 743.13 and an FVD score of 16.96 on the nuScenes dataset, surpassing the current state-of-the-art (SOTA) method, UniScene, with an performance boost of 37.2% in FRD and 24.1% in FVD, respectively.

