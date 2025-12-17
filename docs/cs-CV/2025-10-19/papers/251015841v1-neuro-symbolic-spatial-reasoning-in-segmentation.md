---
layout: default
title: Neuro-Symbolic Spatial Reasoning in Segmentation
---

# Neuro-Symbolic Spatial Reasoning in Segmentation

**arXiv**: [2510.15841v1](https://arxiv.org/abs/2510.15841) | [PDF](https://arxiv.org/pdf/2510.15841.pdf)

**作者**: Jiayi Lin, Jiabo Huang, Shaogang Gong

---

## 💡 一句话要点

**提出神经符号空间推理方法以解决开放词汇语义分割中的空间关系理解问题**

**关键词**: `开放词汇语义分割` `神经符号推理` `空间关系建模` `一阶逻辑` `端到端学习` `分割性能提升`

## 📋 核心要点

1. 核心问题：开放词汇语义分割中，视觉语言模型缺乏对物体空间关系的理解，影响对未见类别的泛化。
2. 方法要点：引入神经符号空间推理，通过一阶逻辑公式在神经网络中施加空间关系约束，实现端到端学习。
3. 实验或效果：在四个基准数据集上达到平均mIoU最优，对多类别图像优势明显，仅增加一个辅助损失函数。

## 📄 摘要（原文）

> Open-Vocabulary Semantic Segmentation (OVSS) assigns pixel-level labels from
> an open set of categories, requiring generalization to unseen and unlabelled
> objects. Using vision-language models (VLMs) to correlate local image patches
> with potential unseen object categories suffers from a lack of understanding of
> spatial relations of objects in a scene. To solve this problem, we introduce
> neuro-symbolic (NeSy) spatial reasoning in OVSS. In contrast to contemporary
> VLM correlation-based approaches, we propose Relational Segmentor (RelateSeg)
> to impose explicit spatial relational constraints by first order logic (FOL)
> formulated in a neural network architecture. This is the first attempt to
> explore NeSy spatial reasoning in OVSS. Specifically, RelateSeg automatically
> extracts spatial relations, e.g., <cat, to-right-of, person>, and encodes them
> as first-order logic formulas using our proposed pseudo categories. Each pixel
> learns to predict both a semantic category (e.g., "cat") and a spatial pseudo
> category (e.g., "right of person") simultaneously, enforcing relational
> constraints (e.g., a "cat" pixel must lie to the right of a "person"). Finally,
> these logic constraints are formulated in a deep network architecture by fuzzy
> logic relaxation, enabling end-to-end learning of spatial-relationally
> consistent segmentation. RelateSeg achieves state-of-the-art performance in
> terms of average mIoU across four benchmark datasets and particularly shows
> clear advantages on images containing multiple categories, with the cost of
> only introducing a single auxiliary loss function and no additional parameters,
> validating the effectiveness of NeSy spatial reasoning in OVSS.

