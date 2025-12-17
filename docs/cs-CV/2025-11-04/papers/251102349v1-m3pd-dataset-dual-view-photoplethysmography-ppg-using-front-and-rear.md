---
layout: default
title: M3PD Dataset: Dual-view Photoplethysmography (PPG) Using Front-and-rear Cameras of Smartphones in Lab and Clinical Settings
---

# M3PD Dataset: Dual-view Photoplethysmography (PPG) Using Front-and-rear Cameras of Smartphones in Lab and Clinical Settings

**arXiv**: [2511.02349v1](https://arxiv.org/abs/2511.02349) | [PDF](https://arxiv.org/pdf/2511.02349.pdf)

**作者**: Jiankai Tang, Tao Zhang, Jia Li, Yiru Zhang, Mingyu Zhang, Kegang Wang, Yuming Hao, Bolin Wang, Haiyang Li, Xingyao Wang, Yuanchun Shi, Yuntao Wang, Sichong Qian

---

## 💡 一句话要点

**提出M3PD数据集和F3Mamba模型，通过双视图PPG提升智能手机心率监测的鲁棒性。**

**关键词**: `双视图光电容积描记` `智能手机生理监测` `Mamba时序建模` `心血管患者数据集` `心率估计` `运动伪影鲁棒性`

## 📋 核心要点

1. 核心问题：智能手机单视图PPG易受运动伪影、光照变化影响，缺乏心血管患者可靠数据集。
2. 方法要点：构建首个公开双视图PPG数据集，融合面部和指尖视频，使用Mamba进行时序建模。
3. 实验或效果：在60名参与者中，心率误差降低21.9-30.2%，增强真实场景鲁棒性。

## 📄 摘要（原文）

> Portable physiological monitoring is essential for early detection and
> management of cardiovascular disease, but current methods often require
> specialized equipment that limits accessibility or impose impractical postures
> that patients cannot maintain. Video-based photoplethysmography on smartphones
> offers a convenient noninvasive alternative, yet it still faces reliability
> challenges caused by motion artifacts, lighting variations, and single-view
> constraints. Few studies have demonstrated reliable application to
> cardiovascular patients, and no widely used open datasets exist for
> cross-device accuracy. To address these limitations, we introduce the M3PD
> dataset, the first publicly available dual-view mobile photoplethysmography
> dataset, comprising synchronized facial and fingertip videos captured
> simultaneously via front and rear smartphone cameras from 60 participants
> (including 47 cardiovascular patients). Building on this dual-view setting, we
> further propose F3Mamba, which fuses the facial and fingertip views through
> Mamba-based temporal modeling. The model reduces heart-rate error by 21.9 to
> 30.2 percent over existing single-view baselines while improving robustness in
> challenging real-world scenarios. Data and code:
> https://github.com/Health-HCI-Group/F3Mamba.

