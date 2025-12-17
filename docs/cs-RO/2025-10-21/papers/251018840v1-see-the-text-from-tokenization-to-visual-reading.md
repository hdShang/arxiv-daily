---
layout: default
title: See the Text: From Tokenization to Visual Reading
---

# See the Text: From Tokenization to Visual Reading

**arXiv**: [2510.18840v1](https://arxiv.org/abs/2510.18840) | [PDF](https://arxiv.org/pdf/2510.18840.pdf)

**作者**: Ling Xing, Alex Jinpeng Wang, Rui Yan, Hongyu Qu, Zechao Li, Jinhui Tang

---

## 💡 一句话要点

**提出SeeTok方法，通过视觉化文本处理解决子词分词在低资源语言中的过分割问题。**

**关键词**: `视觉文本处理` `多模态大模型` `子词分词` `低资源语言` `计算效率优化`

## 📋 核心要点

1. 核心问题：子词分词在低资源语言中过分割，导致序列长、计算量大且语义缺失。
2. 方法要点：将文本渲染为图像，利用预训练多模态大模型进行视觉读取。
3. 实验或效果：在多个语言任务中，减少70.5% FLOPs，提升跨语言泛化和抗噪能力。

## 📄 摘要（原文）

> People see text. Humans read by recognizing words as visual objects,
> including their shapes, layouts, and patterns, before connecting them to
> meaning, which enables us to handle typos, distorted fonts, and various scripts
> effectively. Modern large language models (LLMs), however, rely on subword
> tokenization, fragmenting text into pieces from a fixed vocabulary. While
> effective for high-resource languages, this approach over-segments low-resource
> languages, yielding long, linguistically meaningless sequences and inflating
> computation. In this work, we challenge this entrenched paradigm and move
> toward a vision-centric alternative. Our method, SeeTok, renders text as images
> (visual-text) and leverages pretrained multimodal LLMs to interpret them,
> reusing strong OCR and text-vision alignment abilities learned from large-scale
> multimodal training. Across three different language tasks, SeeTok matches or
> surpasses subword tokenizers while requiring 4.43 times fewer tokens and
> reducing FLOPs by 70.5%, with additional gains in cross-lingual generalization,
> robustness to typographic noise, and linguistic hierarchy. SeeTok signals a
> shift from symbolic tokenization to human-like visual reading, and takes a step
> toward more natural and cognitively inspired language models.

