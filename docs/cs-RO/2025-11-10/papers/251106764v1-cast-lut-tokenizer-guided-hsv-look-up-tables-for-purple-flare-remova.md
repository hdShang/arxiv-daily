---
layout: default
title: CAST-LUT: Tokenizer-Guided HSV Look-Up Tables for Purple Flare Removal
---

# CAST-LUT: Tokenizer-Guided HSV Look-Up Tables for Purple Flare Removal

**arXiv**: [2511.06764v1](https://arxiv.org/abs/2511.06764) | [PDF](https://arxiv.org/pdf/2511.06764.pdf)

**作者**: Pu Wang, Shuning Sun, Jialang Lu, Chen Wu, Zhihua Zhang, Youshan Zhang, Chenggang Shan, Dianjie Lu, Guijuan Zhang, Zhuoran Zheng

---

## 💡 一句话要点

**提出CAST-LUT方法以解决图像紫边伪影去除问题**

**关键词**: `紫边去除` `HSV查找表` `颜色校正` `语义令牌` `图像增强` `两阶段网络`

## 📋 核心要点

1. 紫边伪影是图像高光区域常见的色差问题，严重影响色调过渡和颜色质量
2. 采用解耦HSV查找表和两阶段架构，通过语义令牌动态生成校正曲线
3. 构建大规模数据集和新评估指标，实验显示在视觉和量化指标上优于现有方法

## 📄 摘要（原文）

> Purple flare, a diffuse chromatic aberration artifact commonly found around
> highlight areas, severely degrades the tone transition and color of the image.
> Existing traditional methods are based on hand-crafted features, which lack
> flexibility and rely entirely on fixed priors, while the scarcity of paired
> training data critically hampers deep learning. To address this issue, we
> propose a novel network built upon decoupled HSV Look-Up Tables (LUTs). The
> method aims to simplify color correction by adjusting the Hue (H), Saturation
> (S), and Value (V) components independently. This approach resolves the
> inherent color coupling problems in traditional methods. Our model adopts a
> two-stage architecture: First, a Chroma-Aware Spectral Tokenizer (CAST)
> converts the input image from RGB space to HSV space and independently encodes
> the Hue (H) and Value (V) channels into a set of semantic tokens describing the
> Purple flare status; second, the HSV-LUT module takes these tokens as input and
> dynamically generates independent correction curves (1D-LUTs) for the three
> channels H, S, and V. To effectively train and validate our model, we built the
> first large-scale purple flare dataset with diverse scenes. We also proposed
> new metrics and a loss function specifically designed for this task. Extensive
> experiments demonstrate that our model not only significantly outperforms
> existing methods in visual effects but also achieves state-of-the-art
> performance on all quantitative metrics.

