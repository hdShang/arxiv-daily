---
layout: default
title: SnowyLane: Robust Lane Detection on Snow-covered Rural Roads Using Infrastructural Elements
---

# SnowyLane: Robust Lane Detection on Snow-covered Rural Roads Using Infrastructural Elements

**arXiv**: [2511.05108v1](https://arxiv.org/abs/2511.05108) | [PDF](https://arxiv.org/pdf/2511.05108.pdf)

**作者**: Jörg Gamerdinger, Benedict Wetzel, Patrick Schulz, Sven Teufel, Oliver Bringmann

---

## 💡 一句话要点

**提出基于路边柱状物的车道检测方法以解决雪天车道标记缺失问题**

**关键词**: `车道检测` `雪天驾驶` `贝塞尔曲线` `合成数据集` `路边特征检测`

## 📋 核心要点

1. 核心问题：雪天车道标记常被遮挡或缺失，导致传统车道检测失效。
2. 方法要点：检测路边柱状物作为间接车道指示，使用贝塞尔曲线拟合车道轨迹。
3. 实验或效果：在合成数据集上验证，雪天鲁棒性优于现有方法。

## 📄 摘要（原文）

> Lane detection for autonomous driving in snow-covered environments remains a
> major challenge due to the frequent absence or occlusion of lane markings. In
> this paper, we present a novel, robust and realtime capable approach that
> bypasses the reliance on traditional lane markings by detecting roadside
> features,specifically vertical roadside posts called delineators, as indirect
> lane indicators. Our method first perceives these posts, then fits a smooth
> lane trajectory using a parameterized Bezier curve model, leveraging spatial
> consistency and road geometry. To support training and evaluation in these
> challenging scenarios, we introduce SnowyLane, a new synthetic dataset
> containing 80,000 annotated frames capture winter driving conditions, with
> varying snow coverage, and lighting conditions. Compared to state-of-the-art
> lane detection systems, our approach demonstrates significantly improved
> robustness in adverse weather, particularly in cases with heavy snow occlusion.
> This work establishes a strong foundation for reliable lane detection in winter
> scenarios and contributes a valuable resource for future research in
> all-weather autonomous driving. The dataset is available at
> https://ekut-es.github.io/snowy-lane

