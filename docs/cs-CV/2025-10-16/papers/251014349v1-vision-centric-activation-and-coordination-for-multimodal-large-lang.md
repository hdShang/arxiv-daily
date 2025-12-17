---
layout: default
title: Vision-Centric Activation and Coordination for Multimodal Large Language Models
---

# Vision-Centric Activation and Coordination for Multimodal Large Language Models

**arXiv**: [2510.14349v1](https://arxiv.org/abs/2510.14349) | [PDF](https://arxiv.org/pdf/2510.14349.pdf)

**作者**: Yunnan Wang, Fan Lu, Kecheng Zheng, Ziyuan Huang, Ziqiang Li, Wenjun Zeng, Xin Jin

---

## 💡 一句话要点

**提出VaCo方法以优化多模态大语言模型的视觉中心表示**

**关键词**: `多模态大语言模型` `视觉中心激活` `视觉基础模型` `表示优化` `视觉理解` `模块化任务查询`

## 📋 核心要点

1. 主流MLLMs仅监督文本标记预测，忽视视觉中心信息，影响分析能力
2. 引入视觉判别对齐、模块化任务查询和视觉对齐层，协调多视觉基础模型特征
3. 实验显示VaCo显著提升多种MLLMs在视觉理解基准上的性能

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) integrate image features from visual
> encoders with LLMs, demonstrating advanced comprehension capabilities. However,
> mainstream MLLMs are solely supervised by the next-token prediction of textual
> tokens, neglecting critical vision-centric information essential for analytical
> abilities. To track this dilemma, we introduce VaCo, which optimizes MLLM
> representations through Vision-Centric activation and Coordination from
> multiple vision foundation models (VFMs). VaCo introduces visual discriminative
> alignment to integrate task-aware perceptual features extracted from VFMs,
> thereby unifying the optimization of both textual and visual outputs in MLLMs.
> Specifically, we incorporate the learnable Modular Task Queries (MTQs) and
> Visual Alignment Layers (VALs) into MLLMs, activating specific visual signals
> under the supervision of diverse VFMs. To coordinate representation conflicts
> across VFMs, the crafted Token Gateway Mask (TGM) restricts the information
> flow among multiple groups of MTQs. Extensive experiments demonstrate that VaCo
> significantly improves the performance of different MLLMs on various
> benchmarks, showcasing its superior capabilities in visual comprehension.

