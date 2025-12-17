---
layout: default
title: SDG-Track: A Heterogeneous Observer-Follower Framework for High-Resolution UAV Tracking on Embedded Platforms
---

# SDG-Track: A Heterogeneous Observer-Follower Framework for High-Resolution UAV Tracking on Embedded Platforms

**arXiv**: [2512.04883v1](https://arxiv.org/abs/2512.04883) | [PDF](https://arxiv.org/pdf/2512.04883.pdf)

**作者**: Jiawen Wen, Yu Hu, Suixuan Qiu, Jinshan Huang, Xiaowen Chu

---

## 💡 一句话要点

**提出SDG-Track异构观察者-跟随者框架，以解决嵌入式平台高分辨率无人机跟踪中的分辨率-速度冲突。**

**关键词**: `无人机跟踪` `异构计算` `稀疏光流` `嵌入式系统` `目标检测` `实时处理`

## 📋 核心要点

1. 核心问题：高分辨率无人机跟踪在边缘设备上存在分辨率与速度的冲突，导致小目标特征丢失或处理延迟。
2. 方法要点：采用异构观察者-跟随者架构，结合低频GPU检测与高频CPU稀疏光流插值，并引入无训练的双空间恢复机制。
3. 实验或效果：在NVIDIA Jetson Orin Nano上实现35.1 FPS系统吞吐量，保持97.2%的逐帧检测精度，成功跟踪敏捷FPV无人机。

## 📄 摘要（原文）

> Real-time tracking of small unmanned aerial vehicles (UAVs) on edge devices faces a fundamental resolution-speed conflict. Downsampling high-resolution imagery to standard detector input sizes causes small target features to collapse below detectable thresholds. Yet processing native 1080p frames on resource-constrained platforms yields insufficient throughput for smooth gimbal control. We propose SDG-Track, a Sparse Detection-Guided Tracker that adopts an Observer-Follower architecture to reconcile this conflict. The Observer stream runs a high-capacity detector at low frequency on the GPU to provide accurate position anchors from 1920x1080 frames. The Follower stream performs high-frequency trajectory interpolation via ROI-constrained sparse optical flow on the CPU. To handle tracking failures from occlusion or model drift caused by spectrally similar distractors, we introduce Dual-Space Recovery, a training-free re-acquisition mechanism combining color histogram matching with geometric consistency constraints. Experiments on a ground-to-air tracking station demonstrate that SDG-Track achieves 35.1 FPS system throughput while retaining 97.2\% of the frame-by-frame detection precision. The system successfully tracks agile FPV drones under real-world operational conditions on an NVIDIA Jetson Orin Nano. Our paper code is publicly available at https://github.com/Jeffry-wen/SDG-Track

