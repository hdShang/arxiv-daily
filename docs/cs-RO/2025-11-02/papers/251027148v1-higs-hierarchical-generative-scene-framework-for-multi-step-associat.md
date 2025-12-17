---
layout: default
title: HiGS: Hierarchical Generative Scene Framework for Multi-Step Associative Semantic Spatial Composition
---

# HiGS: Hierarchical Generative Scene Framework for Multi-Step Associative Semantic Spatial Composition

**arXiv**: [2510.27148v1](https://arxiv.org/abs/2510.27148) | [PDF](https://arxiv.org/pdf/2510.27148.pdf)

**作者**: Jiacheng Hong, Kunzhen Wu, Mingrui Yu, Yichao Gu, Shengze Xue, Shuangjiu Xiao, Deli Dong

---

## 💡 一句话要点

**提出HiGS分层生成框架，通过多步关联语义空间组合解决3D场景生成中复杂性与用户输入平衡问题**

**关键词**: `3D场景生成` `分层生成框架` `空间语义图` `多步生成` `用户可控生成`

## 📋 核心要点

1. 核心问题：现有单步3D场景生成方法难以平衡场景复杂性与最小用户输入
2. 方法要点：引入渐进分层空间语义图PHiSSG，动态组织空间关系和语义依赖
3. 实验效果：HiGS在布局合理性、风格一致性和用户偏好上优于单阶段方法

## 📄 摘要（原文）

> Three-dimensional scene generation holds significant potential in gaming,
> film, and virtual reality. However, most existing methods adopt a single-step
> generation process, making it difficult to balance scene complexity with
> minimal user input. Inspired by the human cognitive process in scene modeling,
> which progresses from global to local, focuses on key elements, and completes
> the scene through semantic association, we propose HiGS, a hierarchical
> generative framework for multi-step associative semantic spatial composition.
> HiGS enables users to iteratively expand scenes by selecting key semantic
> objects, offering fine-grained control over regions of interest while the model
> completes peripheral areas automatically. To support structured and coherent
> generation, we introduce the Progressive Hierarchical Spatial-Semantic Graph
> (PHiSSG), which dynamically organizes spatial relationships and semantic
> dependencies across the evolving scene structure. PHiSSG ensures spatial and
> geometric consistency throughout the generation process by maintaining a
> one-to-one mapping between graph nodes and generated objects and supporting
> recursive layout optimization. Experiments demonstrate that HiGS outperforms
> single-stage methods in layout plausibility, style consistency, and user
> preference, offering a controllable and extensible paradigm for efficient 3D
> scene construction.

