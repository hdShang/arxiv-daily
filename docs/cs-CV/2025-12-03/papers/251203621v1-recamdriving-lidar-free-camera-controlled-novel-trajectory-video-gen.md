---
layout: default
title: ReCamDriving: LiDAR-Free Camera-Controlled Novel Trajectory Video Generation
---

# ReCamDriving: LiDAR-Free Camera-Controlled Novel Trajectory Video Generation

**arXiv**: [2512.03621v1](https://arxiv.org/abs/2512.03621) | [PDF](https://arxiv.org/pdf/2512.03621.pdf)

**作者**: Yaokun Li, Shuaixian Wang, Mantang Guo, Jiehui Huang, Taojun Ding, Mu Hu, Kaixuan Wang, Shaojie Shen, Guang Tan

---

## 💡 一句话要点

**提出ReCamDriving，基于纯视觉和3DGS渲染实现相机可控的新轨迹视频生成。**

**关键词**: `视频生成` `相机控制` `3D高斯溅射` `轨迹生成` `纯视觉方法`

## 📋 核心要点

1. 核心问题：现有方法难以恢复复杂伪影或依赖稀疏LiDAR，导致相机控制精度不足。
2. 方法要点：采用两阶段训练，先相机姿态粗控，后3DGS渲染细控，结合跨轨迹数据策略消除训练-测试差距。
3. 实验或效果：在ParaDrive数据集上验证，实现最先进的相机可控性和结构一致性。

## 📄 摘要（原文）

> We propose ReCamDriving, a purely vision-based, camera-controlled novel-trajectory video generation framework. While repair-based methods fail to restore complex artifacts and LiDAR-based approaches rely on sparse and incomplete cues, ReCamDriving leverages dense and scene-complete 3DGS renderings for explicit geometric guidance, achieving precise camera-controllable generation. To mitigate overfitting to restoration behaviors when conditioned on 3DGS renderings, ReCamDriving adopts a two-stage training paradigm: the first stage uses camera poses for coarse control, while the second stage incorporates 3DGS renderings for fine-grained viewpoint and geometric guidance. Furthermore, we present a 3DGS-based cross-trajectory data curation strategy to eliminate the train-test gap in camera transformation patterns, enabling scalable multi-trajectory supervision from monocular videos. Based on this strategy, we construct the ParaDrive dataset, containing over 110K parallel-trajectory video pairs. Extensive experiments demonstrate that ReCamDriving achieves state-of-the-art camera controllability and structural consistency.

