---
layout: default
title: SEGA: A Stepwise Evolution Paradigm for Content-Aware Layout Generation with Design Prior
---

# SEGA: A Stepwise Evolution Paradigm for Content-Aware Layout Generation with Design Prior

**arXiv**: [2510.15749v1](https://arxiv.org/abs/2510.15749) | [PDF](https://arxiv.org/pdf/2510.15749.pdf)

**作者**: Haoran Wang, Bo Zhao, Jinghui Wang, Hanzhang Wang, Huan Yang, Wei Ji, Hao Liu, Xinyan Xiao

---

## 💡 一句话要点

**提出SEGA逐步进化范式以解决内容感知布局生成中的复杂规划问题**

**关键词**: `内容感知布局生成` `逐步进化范式` `分层推理` `布局设计先验` `海报数据集`

## 📋 核心要点

1. 核心问题：现有单步推理方法在复杂元素布局规划中失败率高，缺乏反馈自校正机制。
2. 方法要点：采用分层推理框架，先粗估布局，再精细推理，并融入布局设计先验知识。
3. 实验或效果：在多个基准数据集上实现最先进结果，并发布GenPoster-100K大规模海报数据集。

## 📄 摘要（原文）

> In this paper, we study the content-aware layout generation problem, which
> aims to automatically generate layouts that are harmonious with a given
> background image. Existing methods usually deal with this task with a
> single-step reasoning framework. The lack of a feedback-based self-correction
> mechanism leads to their failure rates significantly increasing when faced with
> complex element layout planning. To address this challenge, we introduce SEGA,
> a novel Stepwise Evolution Paradigm for Content-Aware Layout Generation.
> Inspired by the systematic mode of human thinking, SEGA employs a hierarchical
> reasoning framework with a coarse-to-fine strategy: first, a coarse-level
> module roughly estimates the layout planning results; then, another refining
> module performs fine-level reasoning regarding the coarse planning results.
> Furthermore, we incorporate layout design principles as prior knowledge into
> the model to enhance its layout planning ability. Besides, we present
> GenPoster-100K that is a new large-scale poster dataset with rich
> meta-information annotation. The experiments demonstrate the effectiveness of
> our approach by achieving the state-of-the-art results on multiple benchmark
> datasets. Our project page is at: https://brucew91.github.io/SEGA.github.io/

