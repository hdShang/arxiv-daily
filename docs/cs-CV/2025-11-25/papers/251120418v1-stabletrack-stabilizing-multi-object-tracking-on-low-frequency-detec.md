---
layout: default
title: StableTrack: Stabilizing Multi-Object Tracking on Low-Frequency Detections
---

# StableTrack: Stabilizing Multi-Object Tracking on Low-Frequency Detections

**arXiv**: [2511.20418v1](https://arxiv.org/abs/2511.20418) | [PDF](https://arxiv.org/pdf/2511.20418.pdf)

**作者**: Matvei Shelukhan, Timur Mamedov, Karina Kvanchiani

---

## 💡 一句话要点

**提出StableTrack以稳定低频检测下的多目标跟踪质量**

**关键词**: `多目标跟踪` `低频检测` `两阶段匹配` `Bbox-Based距离` `Kalman滤波器` `Re-ID模型`

## 📋 核心要点

1. 核心问题：多目标跟踪在计算资源受限时，低频检测导致跟踪质量下降。
2. 方法要点：引入两阶段匹配策略和Bbox-Based距离，改进检测关联。
3. 实验效果：在1Hz下MOT17-val的HOTA提升11.6%，标准基准保持竞争力。

## 📄 摘要（原文）

> Multi-object tracking (MOT) is one of the most challenging tasks in computer vision, where it is important to correctly detect objects and associate these detections across frames. Current approaches mainly focus on tracking objects in each frame of a video stream, making it almost impossible to run the model under conditions of limited computing resources. To address this issue, we propose StableTrack, a novel approach that stabilizes the quality of tracking on low-frequency detections. Our method introduces a new two-stage matching strategy to improve the cross-frame association between low-frequency detections. We propose a novel Bbox-Based Distance instead of the conventional Mahalanobis distance, which allows us to effectively match objects using the Re-ID model. Furthermore, we integrate visual tracking into the Kalman Filter and the overall tracking pipeline. Our method outperforms current state-of-the-art trackers in the case of low-frequency detections, achieving $\textit{11.6%}$ HOTA improvement at $\textit{1}$ Hz on MOT17-val, while keeping up with the best approaches on the standard MOT17, MOT20, and DanceTrack benchmarks with full-frequency detections.

