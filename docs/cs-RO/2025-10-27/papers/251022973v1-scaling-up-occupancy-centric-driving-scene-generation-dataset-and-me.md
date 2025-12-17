---
layout: default
title: Scaling Up Occupancy-centric Driving Scene Generation: Dataset and Method
---

# Scaling Up Occupancy-centric Driving Scene Generation: Dataset and Method

**arXiv**: [2510.22973v1](https://arxiv.org/abs/2510.22973) | [PDF](https://arxiv.org/pdf/2510.22973.pdf)

**作者**: Bohan Li, Xin Jin, Hu Zhu, Hongsi Liu, Ruikai Li, Jiazhe Guo, Kaiwen Cai, Chao Ma, Yueming Jin, Hao Zhao, Xiaokang Yang, Wenjun Zeng

---

## 💡 一句话要点

**提出统一框架与Nuplan-Occ数据集，以解决驾驶场景生成中占用数据稀缺问题。**

**关键词**: `驾驶场景生成` `语义占用` `多模态合成` `LiDAR模拟` `时空解耦架构`

## 📋 核心要点

1. 核心问题：占用中心方法依赖稀缺的标注占用数据，限制驾驶场景生成性能。
2. 方法要点：开发统一框架，联合生成语义占用、多视角视频和LiDAR点云。
3. 实验或效果：在Nuplan-Occ数据集上验证，生成保真度和可扩展性优于现有方法。

## 📄 摘要（原文）

> Driving scene generation is a critical domain for autonomous driving,
> enabling downstream applications, including perception and planning evaluation.
> Occupancy-centric methods have recently achieved state-of-the-art results by
> offering consistent conditioning across frames and modalities; however, their
> performance heavily depends on annotated occupancy data, which still remains
> scarce. To overcome this limitation, we curate Nuplan-Occ, the largest semantic
> occupancy dataset to date, constructed from the widely used Nuplan benchmark.
> Its scale and diversity facilitate not only large-scale generative modeling but
> also autonomous driving downstream applications. Based on this dataset, we
> develop a unified framework that jointly synthesizes high-quality semantic
> occupancy, multi-view videos, and LiDAR point clouds. Our approach incorporates
> a spatio-temporal disentangled architecture to support high-fidelity spatial
> expansion and temporal forecasting of 4D dynamic occupancy. To bridge modal
> gaps, we further propose two novel techniques: a Gaussian splatting-based
> sparse point map rendering strategy that enhances multi-view video generation,
> and a sensor-aware embedding strategy that explicitly models LiDAR sensor
> properties for realistic multi-LiDAR simulation. Extensive experiments
> demonstrate that our method achieves superior generation fidelity and
> scalability compared to existing approaches, and validates its practical value
> in downstream tasks. Repo:
> https://github.com/Arlo0o/UniScene-Unified-Occupancy-centric-Driving-Scene-Generation/tree/v2

