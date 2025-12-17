---
layout: default
title: Monitoring Horses in Stalls: From Object to Event Detection
---

# Monitoring Horses in Stalls: From Object to Event Detection

**arXiv**: [2510.17409v1](https://arxiv.org/abs/2510.17409) | [PDF](https://arxiv.org/pdf/2510.17409.pdf)

**作者**: Dmitrii Galimzianov, Viacheslav Vyshegorodtsev, Ivan Nezhivykh

---

## 💡 一句话要点

**提出基于视觉的监控系统以自动检测马厩中马匹和人的行为事件**

**关键词**: `目标检测` `多目标跟踪` `事件检测` `马匹监控` `自定义数据集`

## 📋 核心要点

1. 核心问题：马厩马匹行为监控依赖人工，耗时且效率低，需自动化早期健康问题检测。
2. 方法要点：使用YOLOv11和BoT-SORT进行目标检测与跟踪，结合轨迹和空间关系推断事件状态。
3. 实验或效果：定性评估显示马相关事件检测可靠，但人员检测因数据不足存在局限。

## 📄 摘要（原文）

> Monitoring the behavior of stalled horses is essential for early detection of
> health and welfare issues but remains labor-intensive and time-consuming. In
> this study, we present a prototype vision-based monitoring system that
> automates the detection and tracking of horses and people inside stables using
> object detection and multi-object tracking techniques. The system leverages
> YOLOv11 and BoT-SORT for detection and tracking, while event states are
> inferred based on object trajectories and spatial relations within the stall.
> To support development, we constructed a custom dataset annotated with
> assistance from foundation models CLIP and GroundingDINO. The system
> distinguishes between five event types and accounts for the camera's blind
> spots. Qualitative evaluation demonstrated reliable performance for
> horse-related events, while highlighting limitations in detecting people due to
> data scarcity. This work provides a foundation for real-time behavioral
> monitoring in equine facilities, with implications for animal welfare and
> stable management.

