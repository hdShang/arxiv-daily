---
layout: default
title: SPORTS: Simultaneous Panoptic Odometry, Rendering, Tracking and Segmentation for Urban Scenes Understanding
---

# SPORTS: Simultaneous Panoptic Odometry, Rendering, Tracking and Segmentation for Urban Scenes Understanding

**arXiv**: [2510.12749v1](https://arxiv.org/abs/2510.12749) | [PDF](https://arxiv.org/pdf/2510.12749.pdf)

**作者**: Zhiliu Yang, Jinyu Dai, Jianyuan Zhang, Zhu Yang

---

## 💡 一句话要点

**提出SPORTS框架以解决城市场景理解中的分割缺陷和动态干扰问题**

**关键词**: `视频全景分割` `视觉里程计` `场景渲染` `城市场景理解` `自适应注意力融合`

## 📋 核心要点

1. 核心问题：现有方法存在分割缺陷、动态对象干扰、数据稀疏和视角限制
2. 方法要点：集成视频全景分割、视觉里程计和场景渲染，采用自适应注意力特征融合
3. 实验或效果：在三个公开数据集上，在里程计、跟踪、分割和新视图合成任务中表现优异

## 📄 摘要（原文）

> The scene perception, understanding, and simulation are fundamental
> techniques for embodied-AI agents, while existing solutions are still prone to
> segmentation deficiency, dynamic objects' interference, sensor data sparsity,
> and view-limitation problems. This paper proposes a novel framework, named
> SPORTS, for holistic scene understanding via tightly integrating Video Panoptic
> Segmentation (VPS), Visual Odometry (VO), and Scene Rendering (SR) tasks into
> an iterative and unified perspective. Firstly, VPS designs an adaptive
> attention-based geometric fusion mechanism to align cross-frame features via
> enrolling the pose, depth, and optical flow modality, which automatically
> adjust feature maps for different decoding stages. And a post-matching strategy
> is integrated to improve identities tracking. In VO, panoptic segmentation
> results from VPS are combined with the optical flow map to improve the
> confidence estimation of dynamic objects, which enhances the accuracy of the
> camera pose estimation and completeness of the depth map generation via the
> learning-based paradigm. Furthermore, the point-based rendering of SR is
> beneficial from VO, transforming sparse point clouds into neural fields to
> synthesize high-fidelity RGB views and twin panoptic views. Extensive
> experiments on three public datasets demonstrate that our attention-based
> feature fusion outperforms most existing state-of-the-art methods on the
> odometry, tracking, segmentation, and novel view synthesis tasks.

