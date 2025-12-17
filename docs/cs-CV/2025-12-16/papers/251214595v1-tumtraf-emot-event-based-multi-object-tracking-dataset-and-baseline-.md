---
layout: default
title: TUMTraf EMOT: Event-Based Multi-Object Tracking Dataset and Baseline for Traffic Scenarios
---

# TUMTraf EMOT: Event-Based Multi-Object Tracking Dataset and Baseline for Traffic Scenarios

**arXiv**: [2512.14595v1](https://arxiv.org/abs/2512.14595) | [PDF](https://arxiv.org/pdf/2512.14595.pdf)

**作者**: Mengyu Li, Xingcheng Zhou, Guang Chen, Alois Knoll, Hu Cao

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 10 pages, 9 figures

---

## 💡 一句话要点

**提出TUMTraf EMOT数据集与基准方法，解决交通场景中基于事件相机的多目标跟踪问题。**

**关键词**: `事件相机` `多目标跟踪` `智能交通系统` `数据集` `特征提取` `交通场景` `基准方法` `低延迟视觉`

## 📋 核心要点

1. 现有帧式相机在弱光和高速度运动条件下性能不佳，限制了智能交通系统的应用。
2. 论文提出基于事件相机的数据集和基准方法，通过专门的特征提取器提升跟踪性能。
3. 实验表明，该方法在交通场景中实现了优异的车辆和行人跟踪效果。

## 📝 摘要（中文）

在智能交通系统中，多目标跟踪主要基于帧式相机，但这些相机在弱光和高速度运动条件下性能较差。事件相机具有低延迟、高动态范围和高时间分辨率的特点，有潜力缓解这些问题。与基于帧的视觉相比，基于事件视觉的研究要少得多。为了填补这一研究空白，我们引入了一个专为基于事件的智能交通系统设计的初始试点数据集，涵盖车辆和行人的检测与跟踪。基于该数据集，我们建立了一个检测跟踪基准，并采用专门的特征提取器，实现了优异的性能。

## 🔬 方法详解

论文采用检测跟踪框架，核心是专门设计的事件特征提取器。整体框架包括事件数据预处理、特征提取和目标关联模块。关键技术创新在于针对事件相机数据特性优化特征表示，与现有方法相比，更注重事件流的高时间分辨率和动态范围优势，而非传统图像处理。

## 📊 实验亮点

基于TUMTraf EMOT数据集，论文的基准方法在车辆和行人跟踪任务中表现出色，验证了事件相机在交通场景中的潜力，为后续研究提供了可靠基础。

## 🎯 应用场景

该研究可应用于智能交通系统、自动驾驶和监控领域，特别是在弱光、高动态范围或高速运动场景中，提升多目标跟踪的鲁棒性和实时性。

## 📄 摘要（原文）

> In Intelligent Transportation Systems (ITS), multi-object tracking is primarily based on frame-based cameras. However, these cameras tend to perform poorly under dim lighting and high-speed motion conditions. Event cameras, characterized by low latency, high dynamic range and high temporal resolution, have considerable potential to mitigate these issues. Compared to frame-based vision, there are far fewer studies on event-based vision. To address this research gap, we introduce an initial pilot dataset tailored for event-based ITS, covering vehicle and pedestrian detection and tracking. We establish a tracking-by-detection benchmark with a specialized feature extractor based on this dataset, achieving excellent performance.

