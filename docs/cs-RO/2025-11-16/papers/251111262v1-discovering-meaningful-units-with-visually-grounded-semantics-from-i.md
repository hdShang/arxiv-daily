---
layout: default
title: Discovering Meaningful Units with Visually Grounded Semantics from Image Captions
---

# Discovering Meaningful Units with Visually Grounded Semantics from Image Captions

**arXiv**: [2511.11262v1](https://arxiv.org/abs/2511.11262) | [PDF](https://arxiv.org/pdf/2511.11262.pdf)

**作者**: Melika Behjati, James Henderson

---

## 💡 一句话要点

**提出分组标记模型以提升视觉语言模型的细粒度理解**

**关键词**: `视觉语言模型` `细粒度表示` `标记分组` `语义对齐` `图像标题`

## 📋 核心要点

1. 核心问题：图像块和单个标记缺乏视觉可接地语义，影响细粒度知识获取。
2. 方法要点：模型在架构中分组标题标记，对齐图像编码器发现的物体表示。
3. 实验或效果：分组标记提升模型理解，发现组与可接地短语高度相似。

## 📄 摘要（原文）

> Fine-grained knowledge is crucial for vision-language models to obtain a better understanding of the real world. While there has been work trying to acquire this kind of knowledge in the space of vision and language, it has mostly focused on aligning the image patches with the tokens on the language side. However, image patches do not have any meaning to the human eye, and individual tokens do not necessarily carry groundable information in the image. It is groups of tokens which describe different aspects of the scene. In this work, we propose a model which groups the caption tokens as part of its architecture in order to capture a fine-grained representation of the language. We expect our representations to be at the level of objects present in the image, and therefore align our representations with the output of an image encoder trained to discover objects. We show that by learning to group the tokens, the vision-language model has a better fine-grained understanding of vision and language. In addition, the token groups that our model discovers are highly similar to groundable phrases in text, both qualitatively and quantitatively.

