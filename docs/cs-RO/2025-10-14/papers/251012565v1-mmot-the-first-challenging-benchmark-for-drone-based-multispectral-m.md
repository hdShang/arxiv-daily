---
layout: default
title: MMOT: The First Challenging Benchmark for Drone-based Multispectral Multi-Object Tracking
---

# MMOT: The First Challenging Benchmark for Drone-based Multispectral Multi-Object Tracking

**arXiv**: [2510.12565v1](https://arxiv.org/abs/2510.12565) | [PDF](https://arxiv.org/pdf/2510.12565.pdf)

**作者**: Tianhao Li, Tingfa Xu, Ying Wang, Haolin Qin, Xu Lin, Jianan Li

---

## 💡 一句话要点

**提出MMOT基准与多光谱方案，以提升无人机多目标跟踪在复杂场景下的性能。**

**关键词**: `多光谱多目标跟踪` `无人机基准` `方向感知跟踪` `光谱特征提取` `小目标跟踪`

## 📋 核心要点

1. 核心问题：无人机多目标跟踪因目标小、遮挡严重和背景杂乱而不可靠，RGB方法依赖空间外观易退化。
2. 方法要点：引入大规模多光谱数据集MMOT，并设计光谱3D-Stem和方向感知跟踪方案增强特征提取。
3. 实验或效果：多光谱输入显著优于RGB基线，尤其在小目标和密集场景中提升跟踪性能。

## 📄 摘要（原文）

> Drone-based multi-object tracking is essential yet highly challenging due to
> small targets, severe occlusions, and cluttered backgrounds. Existing RGB-based
> tracking algorithms heavily depend on spatial appearance cues such as color and
> texture, which often degrade in aerial views, compromising reliability.
> Multispectral imagery, capturing pixel-level spectral reflectance, provides
> crucial cues that enhance object discriminability under degraded spatial
> conditions. However, the lack of dedicated multispectral UAV datasets has
> hindered progress in this domain. To bridge this gap, we introduce MMOT, the
> first challenging benchmark for drone-based multispectral multi-object
> tracking. It features three key characteristics: (i) Large Scale - 125 video
> sequences with over 488.8K annotations across eight categories; (ii)
> Comprehensive Challenges - covering diverse conditions such as extreme small
> targets, high-density scenarios, severe occlusions, and complex motion; and
> (iii) Precise Oriented Annotations - enabling accurate localization and reduced
> ambiguity under aerial perspectives. To better extract spectral features and
> leverage oriented annotations, we further present a multispectral and
> orientation-aware MOT scheme adapting existing methods, featuring: (i) a
> lightweight Spectral 3D-Stem integrating spectral features while preserving
> compatibility with RGB pretraining; (ii) an orientation-aware Kalman filter for
> precise state estimation; and (iii) an end-to-end orientation-adaptive
> transformer. Extensive experiments across representative trackers consistently
> show that multispectral input markedly improves tracking performance over RGB
> baselines, particularly for small and densely packed objects. We believe our
> work will advance drone-based multispectral multi-object tracking research. Our
> MMOT, code, and benchmarks are publicly available at
> https://github.com/Annzstbl/MMOT.

