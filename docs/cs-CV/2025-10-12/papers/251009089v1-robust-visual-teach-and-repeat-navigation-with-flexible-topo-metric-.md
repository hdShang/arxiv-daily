---
layout: default
title: Robust Visual Teach-and-Repeat Navigation with Flexible Topo-metric Graph Map Representation
---

# Robust Visual Teach-and-Repeat Navigation with Flexible Topo-metric Graph Map Representation

**arXiv**: [2510.09089v1](https://arxiv.org/abs/2510.09089) | [PDF](https://arxiv.org/pdf/2510.09089.pdf)

**作者**: Jikai Wang, Yunqi Cheng, Kezhi Wang, Zonghai Chen

---

## 💡 一句话要点

**提出灵活拓扑-度量图表示以增强视觉教导-重复导航的鲁棒性**

**关键词**: `视觉教导-重复导航` `拓扑-度量图表示` `地点识别` `局部导航` `鲁棒性优化`

## 📋 核心要点

1. 核心问题：环境变化和动态物体导致视觉教导-重复导航轨迹重复不鲁棒。
2. 方法要点：使用拓扑-度量图表示、关键帧聚类和局部地图匹配提升地点识别。
3. 实验或效果：在移动平台上实验，系统在鲁棒性和有效性上优于基线方法。

## 📄 摘要（原文）

> Visual Teach-and-Repeat Navigation is a direct solution for mobile robot to
> be deployed in unknown environments. However, robust trajectory repeat
> navigation still remains challenged due to environmental changing and dynamic
> objects. In this paper, we propose a novel visual teach-and-repeat navigation
> system, which consists of a flexible map representation, robust map matching
> and a map-less local navigation module. During the teaching process, the
> recorded keyframes are formulated as a topo-metric graph and each node can be
> further extended to save new observations. Such representation also alleviates
> the requirement of globally consistent mapping. To enhance the place
> recognition performance during repeating process, instead of using
> frame-to-frame matching, we firstly implement keyframe clustering to aggregate
> similar connected keyframes into local map and perform place recognition based
> on visual frame-tolocal map matching strategy. To promote the local goal
> persistent tracking performance, a long-term goal management algorithm is
> constructed, which can avoid the robot getting lost due to environmental
> changes or obstacle occlusion. To achieve the goal without map, a local
> trajectory-control candidate optimization algorithm is proposed. Extensively
> experiments are conducted on our mobile platform. The results demonstrate that
> our system is superior to the baselines in terms of robustness and
> effectiveness.

