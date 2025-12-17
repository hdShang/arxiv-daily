---
layout: default
title: Language-Guided Invariance Probing of Vision-Language Models
---

# Language-Guided Invariance Probing of Vision-Language Models

**arXiv**: [2511.13494v1](https://arxiv.org/abs/2511.13494) | [PDF](https://arxiv.org/pdf/2511.13494.pdf)

**作者**: Jae Joong Lee

---

## 💡 一句话要点

**提出语言引导不变性探测以评估视觉语言模型的语言鲁棒性**

**关键词**: `视觉语言模型` `语言鲁棒性` `不变性探测` `语义翻转` `零样本性能` `模型诊断`

## 📋 核心要点

1. 核心问题：视觉语言模型对语言扰动的响应可靠性未知，标准检索指标可能掩盖缺陷
2. 方法要点：自动生成释义和语义翻转，定义不变性误差和语义敏感度差距指标
3. 实验或效果：EVA02-CLIP和大型OpenCLIP变体表现稳健，SigLIP系列易偏好翻转描述

## 📄 摘要（原文）

> Recent vision-language models (VLMs) such as CLIP, OpenCLIP, EVA02-CLIP and SigLIP achieve strong zero-shot performance, but it is unclear how reliably they respond to controlled linguistic perturbations. We introduce Language-Guided Invariance Probing (LGIP), a benchmark that measures (i) invariance to meaning-preserving paraphrases and (ii) sensitivity to meaning-changing semantic flips in image-text matching. Using 40k MS COCO images with five human captions each, we automatically generate paraphrases and rule-based flips that alter object category, color or count, and summarize model behavior with an invariance error, a semantic sensitivity gap and a positive-rate statistic.
>   Across nine VLMs, EVA02-CLIP and large OpenCLIP variants lie on a favorable invariance-sensitivity frontier, combining low paraphrase-induced variance with consistently higher scores for original captions than for their flipped counterparts. In contrast, SigLIP and SigLIP2 show much larger invariance error and often prefer flipped captions to the human descriptions, especially for object and color edits. These failures are largely invisible to standard retrieval metrics, indicating that LGIP provides a model-agnostic diagnostic for the linguistic robustness of VLMs beyond conventional accuracy scores.

