---
layout: default
title: TARA: Simple and Efficient Time Aware Retrieval Adaptation of MLLMs for Video Understanding
---

# TARA: Simple and Efficient Time Aware Retrieval Adaptation of MLLMs for Video Understanding

**arXiv**: [2512.13511v1](https://arxiv.org/abs/2512.13511) | [PDF](https://arxiv.org/pdf/2512.13511.pdf)

**作者**: Piyush Bagad, Andrew Zisserman

---

## 💡 一句话要点

**提出TARA方法，无需视频数据适配MLLMs为时间感知视频-文本检索模型**

**关键词**: `视频检索` `时间感知` `多模态大语言模型` `零样本性能` `嵌入模型`

## 📋 核心要点

1. 核心问题：构建通用时间感知视频-文本嵌入模型，用于视频检索。
2. 方法要点：通过简单高效配方TARA，适配多模态大语言模型，无需视频数据实现时间感知。
3. 实验或效果：在时间对立动作基准上超越现有模型，并在否定感知、动词副词理解方面表现优异。

## 📄 摘要（原文）

> Our objective is to build a general time-aware video-text embedding model for retrieval. To that end, we propose a simple and efficient recipe, dubbed TARA (Time Aware Retrieval Adaptation), to adapt Multimodal LLMs (MLLMs) to a time-aware video-text embedding model without using any video data at all. For evaluating time-awareness in retrieval, we propose a new benchmark with temporally opposite (chiral) actions as hard negatives and curated splits for chiral and non-chiral actions. We show that TARA outperforms all existing video-text models on this chiral benchmark while also achieving strong results on standard benchmarks. Furthermore, we discover additional benefits of TARA beyond time-awareness: (i) TARA embeddings are negation-aware as shown in NegBench benchmark that evaluates negation in video retrieval, (ii) TARA achieves state of the art performance on verb and adverb understanding in videos. Overall, TARA yields a strong, versatile, time-aware video-text embedding model with state of the art zero-shot performance.

