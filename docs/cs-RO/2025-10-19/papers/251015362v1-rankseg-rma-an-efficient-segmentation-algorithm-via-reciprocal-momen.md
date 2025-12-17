---
layout: default
title: RankSEG-RMA: An Efficient Segmentation Algorithm via Reciprocal Moment Approximation
---

# RankSEG-RMA: An Efficient Segmentation Algorithm via Reciprocal Moment Approximation

**arXiv**: [2510.15362v1](https://arxiv.org/abs/2510.15362) | [PDF](https://arxiv.org/pdf/2510.15362.pdf)

**作者**: Zixun Wang, Ben Dai

---

## 💡 一句话要点

**提出RankSEG-RMA以高效优化语义分割指标并扩展至非重叠场景**

**关键词**: `语义分割` `指标优化` `计算复杂度` `互反矩近似` `非重叠分割`

## 📋 核心要点

1. 核心问题：RankSEG优化分割指标但计算复杂度高且仅适用于重叠分割
2. 方法要点：使用互反矩近似降低复杂度至O(d)，并开发像素级评分函数
3. 实验或效果：复杂度降低，性能保持，支持非重叠分割设置

## 📄 摘要（原文）

> Semantic segmentation labels each pixel in an image with its corresponding
> class, and is typically evaluated using the Intersection over Union (IoU) and
> Dice metrics to quantify the overlap between predicted and ground-truth
> segmentation masks. In the literature, most existing methods estimate
> pixel-wise class probabilities, then apply argmax or thresholding to obtain the
> final prediction. These methods have been shown to generally lead to
> inconsistent or suboptimal results, as they do not directly maximize
> segmentation metrics. To address this issue, a novel consistent segmentation
> framework, RankSEG, has been proposed, which includes RankDice and RankIoU
> specifically designed to optimize the Dice and IoU metrics, respectively.
> Although RankSEG almost guarantees improved performance, it suffers from two
> major drawbacks. First, it is its computational expense-RankDice has a
> complexity of O(d log d) with a substantial constant factor (where d represents
> the number of pixels), while RankIoU exhibits even higher complexity O(d^2),
> thus limiting its practical application. For instance, in LiTS, prediction with
> RankSEG takes 16.33 seconds compared to just 0.01 seconds with the argmax rule.
> Second, RankSEG is only applicable to overlapping segmentation settings, where
> multiple classes can occupy the same pixel, which contrasts with standard
> benchmarks that typically assume non-overlapping segmentation. In this paper,
> we overcome these two drawbacks via a reciprocal moment approximation (RMA) of
> RankSEG with the following contributions: (i) we improve RankSEG using RMA,
> namely RankSEG-RMA, reduces the complexity of both algorithms to O(d) while
> maintaining comparable performance; (ii) inspired by RMA, we develop a
> pixel-wise score function that allows efficient implementation for
> non-overlapping segmentation settings.

