---
layout: default
title: Empower Words: DualGround for Structured Phrase and Sentence-Level Temporal Grounding
---

# Empower Words: DualGround for Structured Phrase and Sentence-Level Temporal Grounding

**arXiv**: [2510.20244v1](https://arxiv.org/abs/2510.20244) | [PDF](https://arxiv.org/pdf/2510.20244.pdf)

**作者**: Minseok Kang, Minhyeok Lee, Minjung Kim, Donghyeong Kim, Sangyoun Lee

---

## 💡 一句话要点

**提出DualGround以解决视频时序定位中语义角色忽视问题**

**关键词**: `视频时序定位` `双分支架构` `语义解耦` `短语级对齐` `句子级对齐`

## 📋 核心要点

1. 核心问题：现有方法统一处理文本令牌，忽略语义角色差异，导致细粒度对齐不足。
2. 方法要点：采用双分支架构，分离全局句子级和局部短语级语义，实现结构化解耦。
3. 实验或效果：在QVHighlights和Charades-STA基准上，实现最先进的时刻检索和高光检测性能。

## 📄 摘要（原文）

> Video Temporal Grounding (VTG) aims to localize temporal segments in long,
> untrimmed videos that align with a given natural language query. This task
> typically comprises two subtasks: Moment Retrieval (MR) and Highlight Detection
> (HD). While recent advances have been progressed by powerful pretrained
> vision-language models such as CLIP and InternVideo2, existing approaches
> commonly treat all text tokens uniformly during crossmodal attention,
> disregarding their distinct semantic roles. To validate the limitations of this
> approach, we conduct controlled experiments demonstrating that VTG models
> overly rely on [EOS]-driven global semantics while failing to effectively
> utilize word-level signals, which limits their ability to achieve fine-grained
> temporal alignment. Motivated by this limitation, we propose DualGround, a
> dual-branch architecture that explicitly separates global and local semantics
> by routing the [EOS] token through a sentence-level path and clustering word
> tokens into phrase-level units for localized grounding. Our method introduces
> (1) tokenrole- aware cross modal interaction strategies that align video
> features with sentence-level and phrase-level semantics in a structurally
> disentangled manner, and (2) a joint modeling framework that not only improves
> global sentence-level alignment but also enhances finegrained temporal
> grounding by leveraging structured phrase-aware context. This design allows the
> model to capture both coarse and localized semantics, enabling more expressive
> and context-aware video grounding. DualGround achieves state-of-the-art
> performance on both Moment Retrieval and Highlight Detection tasks across
> QVHighlights and Charades- STA benchmarks, demonstrating the effectiveness of
> disentangled semantic modeling in video-language alignment.

