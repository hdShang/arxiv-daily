---
layout: default
title: InternSVG: Towards Unified SVG Tasks with Multimodal Large Language Models
---

# InternSVG: Towards Unified SVG Tasks with Multimodal Large Language Models

**arXiv**: [2510.11341v1](https://arxiv.org/abs/2510.11341) | [PDF](https://arxiv.org/pdf/2510.11341.pdf)

**作者**: Haomin Wang, Jinhui Yin, Qi Wei, Wenguang Zeng, Lixin Gu, Shenglong Ye, Zhangwei Gao, Yaohui Wang, Yanting Zhang, Yuanqi Li, Yanwen Guo, Wenhai Wang, Kai Chen, Yu Qiao, Hongjie Zhang

---

## 💡 一句话要点

**提出InternSVG以统一SVG任务，利用MLLM实现理解、编辑和生成。**

**关键词**: `SVG统一建模` `多模态大语言模型` `SVG数据集` `SVG基准` `SVG生成` `SVG编辑`

## 📋 核心要点

1. 核心问题：SVG建模因数据集碎片化、方法迁移性差和结构复杂而具挑战性。
2. 方法要点：构建SAgoge数据集和SArena基准，采用SVG专用令牌和两阶段训练策略。
3. 实验或效果：在SArena和先前基准上，InternSVG显著优于现有开源和专有模型。

## 📄 摘要（原文）

> General SVG modeling remains challenging due to fragmented datasets, limited
> transferability of methods across tasks, and the difficulty of handling
> structural complexity. In response, we leverage the strong transfer and
> generalization capabilities of multimodal large language models (MLLMs) to
> achieve unified modeling for SVG understanding, editing, and generation. We
> present the InternSVG family, an integrated data-benchmark-model suite. At its
> core is SAgoge, the largest and most comprehensive multimodal dataset for SVG
> tasks, encompassing both static graphics and dynamic animations. It covers
> icons, long-sequence illustrations, scientific diagrams, and dynamic
> animations, supporting tasks of varied difficulty levels and providing deeper
> hierarchies with richer attributes compared to previous datasets. Based on this
> resource, we introduce SArena, a companion benchmark with comprehensive task
> definitions and standardized evaluation that aligns with the domains and
> difficulty spectrum covered by SAgoge. Building on these foundations, we
> propose InternSVG, a unified MLLM for SVG understanding, editing, and
> generation with SVG-specific special tokens, subword-based embedding
> initialization, and a two-stage training strategy that progresses from short
> static SVGs to long-sequence illustrations and complex animations. This unified
> formulation induces positive transfer and improves overall performance.
> Experiments on SArena and prior benchmark confirm that InternSVG achieves
> substantial gains and consistently outperforms leading open and proprietary
> counterparts.

