---
layout: default
title: Modeling Time-Lapse Trajectories to Characterize Cranberry Growth
---

# Modeling Time-Lapse Trajectories to Characterize Cranberry Growth

**arXiv**: [2510.08901v1](https://arxiv.org/abs/2510.08901) | [PDF](https://arxiv.org/pdf/2510.08901.pdf)

**作者**: Ronan John, Anis Chihoub, Ryan Meegan, Gina Sidelli, Jeffery Neyhart, Peter Oudemans, Kristin Dana

---

## 💡 一句话要点

**提出基于自监督ViT的时间轨迹建模方法，以自动化监测蔓越莓生长。**

**关键词**: `时间轨迹建模` `自监督学习` `视觉变换器` `作物监测` `时间序列分析`

## 📋 核心要点

1. 核心问题：蔓越莓生长监测依赖手动，耗时且需大量标注。
2. 方法要点：使用时间回归和类别预测的自监督ViT，学习植物外观的潜在空间。
3. 实验或效果：构建新数据集，模型可预测生长和区分品种时间差异。

## 📄 摘要（原文）

> Change monitoring is an essential task for cranberry farming as it provides
> both breeders and growers with the ability to analyze growth, predict yield,
> and make treatment decisions. However, this task is often done manually,
> requiring significant time on the part of a cranberry grower or breeder. Deep
> learning based change monitoring holds promise, despite the caveat of
> hard-to-interpret high dimensional features and hand-annotations for
> fine-tuning. To address this gap, we introduce a method for modeling crop
> growth based on fine-tuning vision transformers (ViTs) using a self-supervised
> approach that avoids tedious image annotations. We use a two-fold pretext task
> (time regression and class prediction) to learn a latent space for the
> time-lapse evolution of plant and fruit appearance. The resulting 2D temporal
> tracks provide an interpretable time-series model of crop growth that can be
> used to: 1) predict growth over time and 2) distinguish temporal differences of
> cranberry varieties. We also provide a novel time-lapse dataset of cranberry
> fruit featuring eight distinct varieties, observed 52 times over the growing
> season (span of around four months), annotated with information about fungicide
> application, yield, and rot. Our approach is general and can be applied to
> other crops and applications (code and dataset can be found at https://github.
> com/ronan-39/tlt/).

