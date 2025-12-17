---
layout: default
title: Watermarking for Factuality: Guiding Vision-Language Models Toward Truth via Tri-layer Contrastive Decoding
---

# Watermarking for Factuality: Guiding Vision-Language Models Toward Truth via Tri-layer Contrastive Decoding

**arXiv**: [2510.14304v1](https://arxiv.org/abs/2510.14304) | [PDF](https://arxiv.org/pdf/2510.14304.pdf)

**作者**: Kyungryul Back, Seongbeom Park, Milim Kim, Mincheol Kwon, SangHyeok Lee, Hyunyoung Lee, Junhee Cho, Seunghyun Park, Jinkyu Kim

---

## 💡 一句话要点

**提出基于水印的三层对比解码方法，以减少视觉语言模型的幻觉问题。**

**关键词**: `视觉语言模型` `幻觉减少` `对比解码` `视觉接地` `无训练方法`

## 📋 核心要点

1. 核心问题：视觉语言模型易产生幻觉，依赖单一模态或记忆训练数据。
2. 方法要点：无训练三层对比解码，选择成熟层、业余层和视觉接地支点层。
3. 实验或效果：在POPE等基准上实现SOTA，减少幻觉并增强视觉接地响应。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) have recently shown promising results on
> various multimodal tasks, even achieving human-comparable performance in
> certain cases. Nevertheless, LVLMs remain prone to hallucinations -- they often
> rely heavily on a single modality or memorize training data without properly
> grounding their outputs. To address this, we propose a training-free, tri-layer
> contrastive decoding with watermarking, which proceeds in three steps: (1)
> select a mature layer and an amateur layer among the decoding layers, (2)
> identify a pivot layer using a watermark-related question to assess whether the
> layer is visually well-grounded, and (3) apply tri-layer contrastive decoding
> to generate the final output. Experiments on public benchmarks such as POPE,
> MME and AMBER demonstrate that our method achieves state-of-the-art performance
> in reducing hallucinations in LVLMs and generates more visually grounded
> responses.

