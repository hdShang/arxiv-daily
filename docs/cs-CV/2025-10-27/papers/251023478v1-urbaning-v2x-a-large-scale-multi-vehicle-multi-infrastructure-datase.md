---
layout: default
title: UrbanIng-V2X: A Large-Scale Multi-Vehicle, Multi-Infrastructure Dataset Across Multiple Intersections for Cooperative Perception
---

# UrbanIng-V2X: A Large-Scale Multi-Vehicle, Multi-Infrastructure Dataset Across Multiple Intersections for Cooperative Perception

**arXiv**: [2510.23478v1](https://arxiv.org/abs/2510.23478) | [PDF](https://arxiv.org/pdf/2510.23478.pdf)

**作者**: Karthikeyan Chandra Sekaran, Markus Geisler, Dominik Rößle, Adithya Mohan, Daniel Cremers, Wolfgang Utschick, Michael Botsch, Werner Huber, Torsten Schön

---

## 💡 一句话要点

**提出UrbanIng-V2X数据集以解决多交叉路口协同感知基准缺失问题**

**关键词**: `协同感知` `多模态数据集` `车辆到一切` `3D目标检测` `城市交叉路口` `数字孪生`

## 📋 核心要点

1. 现有协同感知数据集局限于单交叉路口或单车，易导致算法过拟合
2. UrbanIng-V2X包含三交叉路口多车辆与基础设施传感器数据，支持多模态感知
3. 提供712k 3D标注实例，并基于先进方法进行综合评估与代码发布

## 📄 摘要（原文）

> Recent cooperative perception datasets have played a crucial role in
> advancing smart mobility applications by enabling information exchange between
> intelligent agents, helping to overcome challenges such as occlusions and
> improving overall scene understanding. While some existing real-world datasets
> incorporate both vehicle-to-vehicle and vehicle-to-infrastructure interactions,
> they are typically limited to a single intersection or a single vehicle. A
> comprehensive perception dataset featuring multiple connected vehicles and
> infrastructure sensors across several intersections remains unavailable,
> limiting the benchmarking of algorithms in diverse traffic environments.
> Consequently, overfitting can occur, and models may demonstrate misleadingly
> high performance due to similar intersection layouts and traffic participant
> behavior. To address this gap, we introduce UrbanIng-V2X, the first
> large-scale, multi-modal dataset supporting cooperative perception involving
> vehicles and infrastructure sensors deployed across three urban intersections
> in Ingolstadt, Germany. UrbanIng-V2X consists of 34 temporally aligned and
> spatially calibrated sensor sequences, each lasting 20 seconds. All sequences
> contain recordings from one of three intersections, involving two vehicles and
> up to three infrastructure-mounted sensor poles operating in coordinated
> scenarios. In total, UrbanIng-V2X provides data from 12 vehicle-mounted RGB
> cameras, 2 vehicle LiDARs, 17 infrastructure thermal cameras, and 12
> infrastructure LiDARs. All sequences are annotated at a frequency of 10 Hz with
> 3D bounding boxes spanning 13 object classes, resulting in approximately 712k
> annotated instances across the dataset. We provide comprehensive evaluations
> using state-of-the-art cooperative perception methods and publicly release the
> codebase, dataset, HD map, and a digital twin of the complete data collection
> environment.

