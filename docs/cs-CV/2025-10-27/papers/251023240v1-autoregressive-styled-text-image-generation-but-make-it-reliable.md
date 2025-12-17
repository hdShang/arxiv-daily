---
layout: default
title: Autoregressive Styled Text Image Generation, but Make it Reliable
---

# Autoregressive Styled Text Image Generation, but Make it Reliable

**arXiv**: [2510.23240v1](https://arxiv.org/abs/2510.23240) | [PDF](https://arxiv.org/pdf/2510.23240.pdf)

**作者**: Carmine Zaccagnino, Fabio Quattrini, Vittorio Pippi, Silvia Cascianelli, Alessio Tonioni, Rita Cucchiara

---

## 💡 一句话要点

**提出Eruku方法以解决自回归风格文本图像生成中的内容可控性问题**

**关键词**: `风格文本图像生成` `自回归模型` `多模态提示` `分类器自由引导` `内容对齐` `手写文本生成`

## 📋 核心要点

1. 核心问题：自回归风格文本图像生成存在内容对齐差、缺乏停止机制和视觉伪影问题
2. 方法要点：将生成任务重构为多模态提示条件生成，引入特殊文本令牌和分类器自由引导策略
3. 实验或效果：Eruku减少输入需求，提升未见风格泛化能力和文本提示遵循度

## 📄 摘要（原文）

> Generating faithful and readable styled text images (especially for Styled
> Handwritten Text generation - HTG) is an open problem with several possible
> applications across graphic design, document understanding, and image editing.
> A lot of research effort in this task is dedicated to developing strategies
> that reproduce the stylistic characteristics of a given writer, with promising
> results in terms of style fidelity and generalization achieved by the recently
> proposed Autoregressive Transformer paradigm for HTG. However, this method
> requires additional inputs, lacks a proper stop mechanism, and might end up in
> repetition loops, generating visual artifacts. In this work, we rethink the
> autoregressive formulation by framing HTG as a multimodal prompt-conditioned
> generation task, and tackle the content controllability issues by introducing
> special textual input tokens for better alignment with the visual ones.
> Moreover, we devise a Classifier-Free-Guidance-based strategy for our
> autoregressive model. Through extensive experimental validation, we demonstrate
> that our approach, dubbed Eruku, compared to previous solutions requires fewer
> inputs, generalizes better to unseen styles, and follows more faithfully the
> textual prompt, improving content adherence.

