---
layout: default
title: Enhancing Spatio-Temporal Zero-shot Action Recognition with Language-driven Description Attributes
---

# Enhancing Spatio-Temporal Zero-shot Action Recognition with Language-driven Description Attributes

**arXiv**: [2510.27255v1](https://arxiv.org/abs/2510.27255) | [PDF](https://arxiv.org/pdf/2510.27255.pdf)

**作者**: Yehna Kim andYoung-Eun Kim, Seong-Whan Lee

---

## 💡 一句话要点

**提出语言驱动描述属性方法以增强时空零样本动作识别**

**关键词**: `零样本动作识别` `视觉语言模型` `时空交互模块` `描述属性提取` `多语义词处理`

## 📋 核心要点

1. 核心问题：仅依赖动作类易因多语义词引入歧义，影响语义理解。
2. 方法要点：利用网络爬取描述和大语言模型提取关键词，减少人工标注需求。
3. 实验或效果：在UCF-101、HMDB-51和Kinetics-600上分别达到81.0%、53.1%和68.9%准确率。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have demonstrated impressive capabilities in
> zero-shot action recognition by learning to associate video embeddings with
> class embeddings. However, a significant challenge arises when relying solely
> on action classes to provide semantic context, particularly due to the presence
> of multi-semantic words, which can introduce ambiguity in understanding the
> intended concepts of actions. To address this issue, we propose an innovative
> approach that harnesses web-crawled descriptions, leveraging a large-language
> model to extract relevant keywords. This method reduces the need for human
> annotators and eliminates the laborious manual process of attribute data
> creation. Additionally, we introduce a spatio-temporal interaction module
> designed to focus on objects and action units, facilitating alignment between
> description attributes and video content. In our zero-shot experiments, our
> model achieves impressive results, attaining accuracies of 81.0%, 53.1%, and
> 68.9% on UCF-101, HMDB-51, and Kinetics-600, respectively, underscoring the
> model's adaptability and effectiveness across various downstream tasks.

