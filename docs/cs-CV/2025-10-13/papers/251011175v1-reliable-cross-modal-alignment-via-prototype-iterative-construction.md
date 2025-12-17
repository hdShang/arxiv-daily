---
layout: default
title: Reliable Cross-modal Alignment via Prototype Iterative Construction
---

# Reliable Cross-modal Alignment via Prototype Iterative Construction

**arXiv**: [2510.11175v1](https://arxiv.org/abs/2510.11175) | [PDF](https://arxiv.org/pdf/2510.11175.pdf)

**作者**: Xiang Ma, Litian Xu, Lexin Fang, Caiming Zhang, Lizhen Cui

---

## 💡 一句话要点

**提出PICO框架以抑制风格干扰，提升跨模态对齐可靠性**

**关键词**: `跨模态对齐` `风格干扰抑制` `原型迭代构建` `语义概率量化` `嵌入交互加权`

## 📋 核心要点

1. 核心问题：跨模态对齐中非语义风格信息导致语义偏差或损失
2. 方法要点：通过原型迭代构建量化语义概率，加权嵌入交互
3. 实验或效果：在多个基准上优于SOTA方法5.2%-14.1%

## 📄 摘要（原文）

> Cross-modal alignment is an important multi-modal task, aiming to bridge the
> semantic gap between different modalities. The most reliable fundamention for
> achieving this objective lies in the semantic consistency between matched
> pairs. Conventional methods implicitly assume embeddings contain solely
> semantic information, ignoring the impact of non-semantic information during
> alignment, which inevitably leads to information bias or even loss. These
> non-semantic information primarily manifest as stylistic variations in the
> data, which we formally define as style information. An intuitive approach is
> to separate style from semantics, aligning only the semantic information.
> However, most existing methods distinguish them based on feature columns, which
> cannot represent the complex coupling relationship between semantic and style
> information. In this paper, we propose PICO, a novel framework for suppressing
> style interference during embedding interaction. Specifically, we quantify the
> probability of each feature column representing semantic information, and
> regard it as the weight during the embedding interaction. To ensure the
> reliability of the semantic probability, we propose a prototype iterative
> construction method. The key operation of this method is a performance
> feedback-based weighting function, and we have theoretically proven that the
> function can assign higher weight to prototypes that bring higher performance
> improvements. Extensive experiments on various benchmarks and model backbones
> demonstrate the superiority of PICO, outperforming state-of-the-art methods by
> 5.2\%-14.1\%.

