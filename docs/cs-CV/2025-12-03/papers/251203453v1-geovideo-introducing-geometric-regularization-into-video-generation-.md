---
layout: default
title: GeoVideo: Introducing Geometric Regularization into Video Generation Model
---

# GeoVideo: Introducing Geometric Regularization into Video Generation Model

**arXiv**: [2512.03453v1](https://arxiv.org/abs/2512.03453) | [PDF](https://arxiv.org/pdf/2512.03453.pdf)

**作者**: Yunpeng Bai, Shaoheng Fang, Chaohui Yu, Fan Wang, Qixing Huang

---

## 💡 一句话要点

**提出几何正则化损失以增强视频生成模型的时空一致性与结构合理性**

**关键词**: `视频生成` `几何正则化` `深度预测` `时空一致性` `扩散模型`

## 📋 核心要点

1. 现有视频生成方法缺乏3D结构建模，导致几何不一致与运动不合理
2. 通过每帧深度预测引入多视角几何损失，在共享3D坐标系中对齐深度图
3. 实验表明方法在多个数据集上显著提升几何一致性与物理合理性

## 📄 摘要（原文）

> Recent advances in video generation have enabled the synthesis of high-quality and visually realistic clips using diffusion transformer models. However, most existing approaches operate purely in the 2D pixel space and lack explicit mechanisms for modeling 3D structures, often resulting in temporally inconsistent geometries, implausible motions, and structural artifacts. In this work, we introduce geometric regularization losses into video generation by augmenting latent diffusion models with per-frame depth prediction. We adopted depth as the geometric representation because of the great progress in depth prediction and its compatibility with image-based latent encoders. Specifically, to enforce structural consistency over time, we propose a multi-view geometric loss that aligns the predicted depth maps across frames within a shared 3D coordinate system. Our method bridges the gap between appearance generation and 3D structure modeling, leading to improved spatio-temporal coherence, shape consistency, and physical plausibility. Experiments across multiple datasets show that our approach produces significantly more stable and geometrically consistent results than existing baselines.

