---
layout: default
title: Into the Unknown: Towards using Generative Models for Sampling Priors of Environment Uncertainty for Planning in Configuration Spaces
---

# Into the Unknown: Towards using Generative Models for Sampling Priors of Environment Uncertainty for Planning in Configuration Spaces

**arXiv**: [2510.11014v1](https://arxiv.org/abs/2510.11014) | [PDF](https://arxiv.org/pdf/2510.11014.pdf)

**作者**: Subhransu S. Bhattacharjee, Hao Lu, Dylan Campbell, Rahul Shome

---

## 💡 一句话要点

**提出基于生成模型的采样管道，为零样本环境不确定性提供先验，用于配置空间规划。**

**关键词**: `生成模型` `配置空间规划` `环境不确定性` `RGB-D点云` `零样本学习`

## 📋 核心要点

1. 核心问题：部分可观测下规划的先验难以获取，需处理环境不确定性和空间语义关系。
2. 方法要点：利用预训练生成模型，从部分观测恢复完整RGB-D点云，包含占用和目标语义。
3. 实验效果：在Matterport3D基准上，生成的点云具有常识空间语义，可用于运动规划。

## 📄 摘要（原文）

> Priors are vital for planning under partial observability, yet difficult to
> obtain in practice. We present a sampling-based pipeline that leverages
> large-scale pretrained generative models to produce probabilistic priors
> capturing environmental uncertainty and spatio-semantic relationships in a
> zero-shot manner. Conditioned on partial observations, the pipeline recovers
> complete RGB-D point cloud samples with occupancy and target semantics,
> formulated to be directly useful in configuration-space planning. We establish
> a Matterport3D benchmark of rooms partially visible through doorways, where a
> robot must navigate to an unobserved target object. Effective priors for this
> setting must represent both occupancy and target-location uncertainty in
> unobserved regions. Experiments show that our approach recovers commonsense
> spatial semantics consistent with ground truth, yielding diverse, clean 3D
> point clouds usable in motion planning, highlight the promise of generative
> models as a rich source of priors for robotic planning.

