---
layout: default
title: MAPS: Masked Attribution-based Probing of Strategies- A computational framework to align human and model explanations
---

# MAPS: Masked Attribution-based Probing of Strategies- A computational framework to align human and model explanations

**arXiv**: [2510.12141v1](https://arxiv.org/abs/2510.12141) | [PDF](https://arxiv.org/pdf/2510.12141.pdf)

**作者**: Sabine Muzellec, Yousif Kashef Alghetaa, Simon Kornblith, Kohitij Kar

---

## 💡 一句话要点

**提出MAPS框架以对齐人类与模型解释，评估神经网络解释方法。**

**关键词**: `视觉解释对齐` `归因图分析` `行为验证` `神经网络解释` `计算框架`

## 📋 核心要点

1. 核心问题：人类视觉策略难以直接测量，需对齐人工神经网络解释。
2. 方法要点：将归因图转换为解释掩码图像，比较人类在有限像素图像上的准确率。
3. 实验或效果：验证MAPS在模型间恢复真实相似性，并识别与生物视觉对齐的解释方法。

## 📄 摘要（原文）

> Human core object recognition depends on the selective use of visual
> information, but the strategies guiding these choices are difficult to measure
> directly. We present MAPS (Masked Attribution-based Probing of Strategies), a
> behaviorally validated computational tool that tests whether explanations
> derived from artificial neural networks (ANNs) can also explain human vision.
> MAPS converts attribution maps into explanation-masked images (EMIs) and
> compares image-by-image human accuracies on these minimal images with limited
> pixel budgets with accuracies on the full stimuli. MAPS provides a principled
> way to evaluate and choose among competing ANN interpretability methods. In
> silico, EMI-based behavioral similarity between models reliably recovers the
> ground-truth similarity computed from their attribution maps, establishing
> which explanation methods best capture the model's strategy. When applied to
> humans and macaques, MAPS identifies ANN-explanation combinations whose
> explanations align most closely with biological vision, achieving the
> behavioral validity of Bubble masks while requiring far fewer behavioral
> trials. Because it needs only access to model attributions and a modest set of
> behavioral data on the original images, MAPS avoids exhaustive psychophysics
> while offering a scalable tool for adjudicating explanations and linking human
> behavior, neural activity, and model decisions under a common standard.

