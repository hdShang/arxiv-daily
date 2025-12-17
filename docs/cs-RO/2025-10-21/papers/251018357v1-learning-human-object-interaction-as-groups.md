---
layout: default
title: Learning Human-Object Interaction as Groups
---

# Learning Human-Object Interaction as Groups

**arXiv**: [2510.18357v1](https://arxiv.org/abs/2510.18357) | [PDF](https://arxiv.org/pdf/2510.18357.pdf)

**作者**: Jiajun Hong, Jianan Wei, Wenguan Wang

---

## 💡 一句话要点

**提出GroupHOI框架，通过分组建模解决人类-物体交互检测中的集体行为问题**

**关键词**: `人类-物体交互检测` `分组建模` `几何邻近` `语义相似性` `自注意力机制` `非语言交互检测`

## 📋 核心要点

1. 核心问题：现有方法关注成对关系，忽略现实场景中多人类和物体参与的集体交互行为。
2. 方法要点：基于几何邻近和语义相似性分组，使用可学习邻近估计器和自注意力传播上下文信息。
3. 实验或效果：在HICO-DET和V-COCO基准上优于现有方法，并在NVI-DET任务中表现领先。

## 📄 摘要（原文）

> Human-Object Interaction Detection (HOI-DET) aims to localize human-object
> pairs and identify their interactive relationships. To aggregate contextual
> cues, existing methods typically propagate information across all detected
> entities via self-attention mechanisms, or establish message passing between
> humans and objects with bipartite graphs. However, they primarily focus on
> pairwise relationships, overlooking that interactions in real-world scenarios
> often emerge from collective behaviors (multiple humans and objects engaging in
> joint activities). In light of this, we revisit relation modeling from a group
> view and propose GroupHOI, a framework that propagates contextual information
> in terms of geometric proximity and semantic similarity. To exploit the
> geometric proximity, humans and objects are grouped into distinct clusters
> using a learnable proximity estimator based on spatial features derived from
> bounding boxes. In each group, a soft correspondence is computed via
> self-attention to aggregate and dispatch contextual cues. To incorporate the
> semantic similarity, we enhance the vanilla transformer-based interaction
> decoder with local contextual cues from HO-pair features. Extensive experiments
> on HICO-DET and V-COCO benchmarks demonstrate the superiority of GroupHOI over
> the state-of-the-art methods. It also exhibits leading performance on the more
> challenging Nonverbal Interaction Detection (NVI-DET) task, which involves
> varied forms of higher-order interactions within groups.

