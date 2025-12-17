---
layout: default
title: Context-measure: Contextualizing Metric for Camouflage
---

# Context-measure: Contextualizing Metric for Camouflage

**arXiv**: [2512.07076v1](https://arxiv.org/abs/2512.07076) | [PDF](https://arxiv.org/pdf/2512.07076.pdf)

**作者**: Chen-Yang Wang, Gepeng Ji, Song Shao, Ming-Ming Cheng, Deng-Ping Fan

---

## 💡 一句话要点

**提出Context-measure以解决伪装场景中现有度量忽略上下文依赖的问题。**

**关键词**: `伪装对象分割` `上下文度量` `概率像素感知` `空间依赖` `评估基准` `计算机视觉应用`

## 📋 核心要点

1. 核心问题：现有伪装度量基于空间上下文无关假设，不符合伪装依赖上下文的特点。
2. 方法要点：基于概率像素感知相关框架，融入空间依赖性和像素级伪装量化。
3. 实验或效果：在三个伪装对象分割数据集上验证，比现有度量更可靠且更符合人类感知。

## 📄 摘要（原文）

> Camouflage is primarily context-dependent yet current metrics for camouflaged scenarios overlook this critical factor. Instead, these metrics are originally designed for evaluating general or salient objects, with an inherent assumption of uncorrelated spatial context. In this paper, we propose a new contextualized evaluation paradigm, Context-measure, built upon a probabilistic pixel-aware correlation framework. By incorporating spatial dependencies and pixel-wise camouflage quantification, our measure better aligns with human perception. Extensive experiments across three challenging camouflaged object segmentation datasets show that Context-measure delivers more reliability than existing context-independent metrics. Our measure can provide a foundational evaluation benchmark for various computer vision applications involving camouflaged patterns, such as agricultural, industrial, and medical scenarios. Code is available at https://github.com/pursuitxi/Context-measure.

