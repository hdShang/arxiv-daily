---
layout: default
title: Zero-Shot Vehicle Model Recognition via Text-Based Retrieval-Augmented Generation
---

# Zero-Shot Vehicle Model Recognition via Text-Based Retrieval-Augmented Generation

**arXiv**: [2510.18502v1](https://arxiv.org/abs/2510.18502) | [PDF](https://arxiv.org/pdf/2510.18502.pdf)

**作者**: Wei-Chia Chang, Yan-Ann Chen

---

## 💡 一句话要点

**提出基于检索增强生成的文本推理方法，以解决零样本车辆品牌型号识别问题。**

**关键词**: `零样本识别` `检索增强生成` `视觉语言模型` `车辆品牌型号识别` `智能交通系统`

## 📋 核心要点

1. 核心问题：现有方法难以适应新发布车型，CLIP模型需昂贵微调。
2. 方法要点：使用视觉语言模型提取图像属性，结合检索增强生成进行文本推理。
3. 实验或效果：相比CLIP基线，识别准确率提升近20%，支持快速更新。

## 📄 摘要（原文）

> Vehicle make and model recognition (VMMR) is an important task in intelligent
> transportation systems, but existing approaches struggle to adapt to newly
> released models. Contrastive Language-Image Pretraining (CLIP) provides strong
> visual-text alignment, yet its fixed pretrained weights limit performance
> without costly image-specific finetuning. We propose a pipeline that integrates
> vision language models (VLMs) with Retrieval-Augmented Generation (RAG) to
> support zero-shot recognition through text-based reasoning. A VLM converts
> vehicle images into descriptive attributes, which are compared against a
> database of textual features. Relevant entries are retrieved and combined with
> the description to form a prompt, and a language model (LM) infers the make and
> model. This design avoids large-scale retraining and enables rapid updates by
> adding textual descriptions of new vehicles. Experiments show that the proposed
> method improves recognition by nearly 20% over the CLIP baseline, demonstrating
> the potential of RAG-enhanced LM reasoning for scalable VMMR in smart-city
> applications.

