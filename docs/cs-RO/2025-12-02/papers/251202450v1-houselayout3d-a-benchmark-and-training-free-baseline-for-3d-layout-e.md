---
layout: default
title: HouseLayout3D: A Benchmark and Training-Free Baseline for 3D Layout Estimation in the Wild
---

# HouseLayout3D: A Benchmark and Training-Free Baseline for 3D Layout Estimation in the Wild

**arXiv**: [2512.02450v1](https://arxiv.org/abs/2512.02450) | [PDF](https://arxiv.org/pdf/2512.02450.pdf)

**作者**: Valentin Bieri, Marie-Julie Rakotosaona, Keisuke Tateno, Francis Engelmann, Leonidas Guibas

---

## 💡 一句话要点

**提出HouseLayout3D基准与MultiFloor3D基线，以解决真实建筑多楼层3D布局估计问题。**

**关键词**: `3D布局估计` `多楼层建筑` `真实世界基准` `无训练基线` `场景理解` `建筑规模估计`

## 📋 核心要点

1. 当前3D布局估计模型依赖合成数据，难以处理多楼层建筑，需分割场景丢失全局空间上下文。
2. 引入HouseLayout3D真实世界基准，支持全建筑规模布局估计，包括多楼层和复杂空间。
3. 提出MultiFloor3D无训练基线，利用现有场景理解方法，在新基准和现有数据集上优于现有模型。

## 📄 摘要（原文）

> Current 3D layout estimation models are primarily trained on synthetic datasets containing simple single room or single floor environments. As a consequence, they cannot natively handle large multi floor buildings and require scenes to be split into individual floors before processing, which removes global spatial context that is essential for reasoning about structures such as staircases that connect multiple levels. In this work, we introduce HouseLayout3D, a real world benchmark designed to support progress toward full building scale layout estimation, including multiple floors and architecturally intricate spaces. We also present MultiFloor3D, a simple training free baseline that leverages recent scene understanding methods and already outperforms existing 3D layout estimation models on both our benchmark and prior datasets, highlighting the need for further research in this direction. Data and code are available at: https://houselayout3d.github.io.

