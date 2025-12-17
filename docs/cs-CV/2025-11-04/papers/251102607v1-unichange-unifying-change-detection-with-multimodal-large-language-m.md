---
layout: default
title: UniChange: Unifying Change Detection with Multimodal Large Language Model
---

# UniChange: Unifying Change Detection with Multimodal Large Language Model

**arXiv**: [2511.02607v1](https://arxiv.org/abs/2511.02607) | [PDF](https://arxiv.org/pdf/2511.02607.pdf)

**作者**: Xu Zhang, Danyang Li, Xiaohang Dong, Tianhao Wu, Hualong Yu, Jianye Wang, Qicheng Li, Xiang Li

---

## 💡 一句话要点

**提出UniChange模型，利用多模态大语言模型统一变化检测任务。**

**关键词**: `变化检测` `多模态大语言模型` `统一框架` `语义变化检测` `二进制变化检测`

## 📋 核心要点

1. 核心问题：现有变化检测模型泛化性差，无法统一利用多源数据集。
2. 方法要点：引入特殊令牌和文本提示，统一二进制和语义变化检测。
3. 实验或效果：在四个基准测试中实现SOTA性能，IoU得分显著提升。

## 📄 摘要（原文）

> Change detection (CD) is a fundamental task for monitoring and analyzing land
> cover dynamics. While recent high performance models and high quality datasets
> have significantly advanced the field, a critical limitation persists. Current
> models typically acquire limited knowledge from single-type annotated data and
> cannot concurrently leverage diverse binary change detection (BCD) and semantic
> change detection (SCD) datasets. This constraint leads to poor generalization
> and limited versatility. The recent advancements in Multimodal Large Language
> Models (MLLMs) introduce new possibilities for a unified CD framework. We
> leverage the language priors and unification capabilities of MLLMs to develop
> UniChange, the first MLLM-based unified change detection model. UniChange
> integrates generative language abilities with specialized CD functionalities.
> Our model successfully unifies both BCD and SCD tasks through the introduction
> of three special tokens: [T1], [T2], and [CHANGE]. Furthermore, UniChange
> utilizes text prompts to guide the identification of change categories,
> eliminating the reliance on predefined classification heads. This design allows
> UniChange to effectively acquire knowledge from multi-source datasets, even
> when their class definitions conflict. Experiments on four public benchmarks
> (WHU-CD, S2Looking, LEVIR-CD+, and SECOND) demonstrate SOTA performance,
> achieving IoU scores of 90.41, 53.04, 78.87, and 57.62, respectively,
> surpassing all previous methods. The code is available at
> https://github.com/Erxucomeon/UniChange.

