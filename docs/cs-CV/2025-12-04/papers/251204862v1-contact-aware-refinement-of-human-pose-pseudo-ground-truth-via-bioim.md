---
layout: default
title: Contact-Aware Refinement of Human Pose Pseudo-Ground Truth via Bioimpedance Sensing
---

# Contact-Aware Refinement of Human Pose Pseudo-Ground Truth via Bioimpedance Sensing

**arXiv**: [2512.04862v1](https://arxiv.org/abs/2512.04862) | [PDF](https://arxiv.org/pdf/2512.04862.pdf)

**作者**: Maria-Paola Forte, Nikos Athanasiou, Giulia Ballardini, Jan Ulrich Bartels, Katherine J. Kuchenbecker, Michael J. Black

---

## 💡 一句话要点

**提出BioTUCH框架，结合生物阻抗传感优化自接触场景下的3D人体姿态估计**

**关键词**: `3D人体姿态估计` `生物阻抗传感` `自接触优化` `姿态重建` `多模态数据融合`

## 📋 核心要点

1. 核心问题：视频姿态估计在自接触场景（如手触脸）中常不准确，缺乏真实接触数据。
2. 方法要点：利用生物阻抗传感测量皮肤接触，通过接触感知优化初始化姿态，最小化重投影误差和偏差。
3. 实验或效果：在同步数据集上验证，平均重建精度提升11.7%，并开发微型传感器用于大规模数据收集。

## 📄 摘要（原文）

> Capturing accurate 3D human pose in the wild would provide valuable data for training pose estimation and motion generation methods. While video-based estimation approaches have become increasingly accurate, they often fail in common scenarios involving self-contact, such as a hand touching the face. In contrast, wearable bioimpedance sensing can cheaply and unobtrusively measure ground-truth skin-to-skin contact. Consequently, we propose a novel framework that combines visual pose estimators with bioimpedance sensing to capture the 3D pose of people by taking self-contact into account. Our method, BioTUCH, initializes the pose using an off-the-shelf estimator and introduces contact-aware pose optimization during measured self-contact: reprojection error and deviations from the input estimate are minimized while enforcing vertex proximity constraints. We validate our approach using a new dataset of synchronized RGB video, bioimpedance measurements, and 3D motion capture. Testing with three input pose estimators, we demonstrate an average of 11.7% improvement in reconstruction accuracy. We also present a miniature wearable bioimpedance sensor that enables efficient large-scale collection of contact-aware training data for improving pose estimation and generation using BioTUCH. Code and data are available at biotuch.is.tue.mpg.de

