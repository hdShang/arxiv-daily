---
layout: default
title: Gaussian Semantic Field for One-shot LiDAR Global Localization
---

# Gaussian Semantic Field for One-shot LiDAR Global Localization

**arXiv**: [2510.12101v1](https://arxiv.org/abs/2510.12101) | [PDF](https://arxiv.org/pdf/2510.12101.pdf)

**作者**: Pengyu Yin, Shenghai Yuan, Haozhi Cao, Xingyu Ji, Ruofei Bai, Siyu Chen, Lihua Xie

---

## 💡 一句话要点

**提出高斯语义场以解决LiDAR全局定位中的语义歧义问题**

**关键词**: `LiDAR全局定位` `高斯语义场` `三层场景图` `语义分布建模` `一次性定位`

## 📋 核心要点

1. 核心问题：地标语义重复导致LiDAR全局定位对应关系建立困难
2. 方法要点：使用高斯过程学习连续语义分布，构建三层场景图
3. 实验或效果：在公开数据集上验证优于当前最优方法

## 📄 摘要（原文）

> We present a one-shot LiDAR global localization algorithm featuring semantic
> disambiguation ability based on a lightweight tri-layered scene graph. While
> landmark semantic registration-based methods have shown promising performance
> improvements in global localization compared with geometric-only methods,
> landmarks can be repetitive and misleading for correspondence establishment. We
> propose to mitigate this problem by modeling semantic distributions with
> continuous functions learned from a population of Gaussian processes. Compared
> with discrete semantic labels, the continuous functions capture finer-grained
> geo-semantic information and also provide more detailed metric information for
> correspondence establishment. We insert this continuous function as the middle
> layer between the object layer and the metric-semantic layer, forming a
> tri-layered 3D scene graph, serving as a light-weight yet performant backend
> for one-shot localization. We term our global localization pipeline Outram-GSF
> (Gaussian semantic field) and conduct a wide range of experiments on publicly
> available data sets, validating the superior performance against the current
> state-of-the-art.

