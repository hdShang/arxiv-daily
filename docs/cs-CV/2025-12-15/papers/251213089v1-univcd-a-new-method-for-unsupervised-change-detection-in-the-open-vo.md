---
layout: default
title: UniVCD: A New Method for Unsupervised Change Detection in the Open-Vocabulary Era
---

# UniVCD: A New Method for Unsupervised Change Detection in the Open-Vocabulary Era

**arXiv**: [2512.13089v1](https://arxiv.org/abs/2512.13089) | [PDF](https://arxiv.org/pdf/2512.13089.pdf)

**作者**: Ziqiang Zhu, Bowei Yang

---

## 💡 一句话要点

**提出UniVCD方法，基于冻结SAM2和CLIP实现无监督开放词汇变化检测。**

**关键词**: `无监督变化检测` `开放词汇` `多模态对齐` `轻量模型` `语义感知`

## 📋 核心要点

1. 现有变化检测方法依赖监督学习，标注成本高且泛化能力差。
2. UniVCD结合SAM2的空间细节和CLIP的语义先验，通过轻量特征对齐模块实现高分辨率变化估计。
3. 在多个公开基准测试中，UniVCD在F1和IoU等关键指标上表现优异，匹配或超越现有开放词汇方法。

## 📄 摘要（原文）

> Change detection (CD) identifies scene changes from multi-temporal observations and is widely used in urban development and environmental monitoring. Most existing CD methods rely on supervised learning, making performance strongly dataset-dependent and incurring high annotation costs; they typically focus on a few predefined categories and generalize poorly to diverse scenes. With the rise of vision foundation models such as SAM2 and CLIP, new opportunities have emerged to relax these constraints. We propose Unified Open-Vocabulary Change Detection (UniVCD), an unsupervised, open-vocabulary change detection method built on frozen SAM2 and CLIP. UniVCD detects category-agnostic changes across diverse scenes and imaging geometries without any labeled data or paired change images. A lightweight feature alignment module is introduced to bridge the spatially detailed representations from SAM2 and the semantic priors from CLIP, enabling high-resolution, semantically aware change estimation while keeping the number of trainable parameters small. On top of this, a streamlined post-processing pipeline is further introduced to suppress noise and pseudo-changes, improving the detection accuracy for objects with well-defined boundaries. Experiments on several public BCD (Binary Change Detection) and SCD (Semantic Change Detection) benchmarks show that UniVCD achieves consistently strong performance and matches or surpasses existing open-vocabulary CD methods in key metrics such as F1 and IoU. The results demonstrate that unsupervised change detection with frozen vision foundation models and lightweight multi-modal alignment is a practical and effective paradigm for open-vocabulary CD. Code and pretrained models will be released at https://github.com/Die-Xie/UniVCD.

