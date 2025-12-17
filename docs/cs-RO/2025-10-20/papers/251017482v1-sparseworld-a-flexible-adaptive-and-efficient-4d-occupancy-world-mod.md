---
layout: default
title: SparseWorld: A Flexible, Adaptive, and Efficient 4D Occupancy World Model Powered by Sparse and Dynamic Queries
---

# SparseWorld: A Flexible, Adaptive, and Efficient 4D Occupancy World Model Powered by Sparse and Dynamic Queries

**arXiv**: [2510.17482v1](https://arxiv.org/abs/2510.17482) | [PDF](https://arxiv.org/pdf/2510.17482.pdf)

**作者**: Chenxu Dang, Haiyan Liu, Guangjun Bao, Pei An, Xinyue Tang, Jie Ma, Bingchuan Sun, Yan Wang

---

## 💡 一句话要点

**提出SparseWorld 4D占用世界模型，通过稀疏动态查询解决感知灵活性与动态场景对齐问题。**

**关键词**: `4D占用世界模型` `稀疏动态查询` `范围自适应感知` `状态条件预测` `自动驾驶场景` `自监督训练`

## 📋 核心要点

1. 现有占用世界模型依赖静态嵌入或网格，限制感知灵活性且与动态场景不匹配。
2. 引入范围自适应感知和状态条件预测模块，使用动态查询实现扩展感知和连续环境对齐。
3. 实验显示在感知、预测和规划任务中达到先进水平，验证了灵活性、适应性和效率。

## 📄 摘要（原文）

> Semantic occupancy has emerged as a powerful representation in world models
> for its ability to capture rich spatial semantics. However, most existing
> occupancy world models rely on static and fixed embeddings or grids, which
> inherently limit the flexibility of perception. Moreover, their ``in-place
> classification" over grids exhibits a potential misalignment with the dynamic
> and continuous nature of real scenarios.In this paper, we propose SparseWorld,
> a novel 4D occupancy world model that is flexible, adaptive, and efficient,
> powered by sparse and dynamic queries. We propose a Range-Adaptive Perception
> module, in which learnable queries are modulated by the ego vehicle states and
> enriched with temporal-spatial associations to enable extended-range
> perception. To effectively capture the dynamics of the scene, we design a
> State-Conditioned Forecasting module, which replaces classification-based
> forecasting with regression-guided formulation, precisely aligning the dynamic
> queries with the continuity of the 4D environment. In addition, We specifically
> devise a Temporal-Aware Self-Scheduling training strategy to enable smooth and
> efficient training. Extensive experiments demonstrate that SparseWorld achieves
> state-of-the-art performance across perception, forecasting, and planning
> tasks. Comprehensive visualizations and ablation studies further validate the
> advantages of SparseWorld in terms of flexibility, adaptability, and
> efficiency. The code is available at https://github.com/MSunDYY/SparseWorld.

