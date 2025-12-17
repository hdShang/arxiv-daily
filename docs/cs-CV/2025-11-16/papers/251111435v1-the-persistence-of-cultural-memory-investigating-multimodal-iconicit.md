---
layout: default
title: The Persistence of Cultural Memory: Investigating Multimodal Iconicity in Diffusion Models
---

# The Persistence of Cultural Memory: Investigating Multimodal Iconicity in Diffusion Models

**arXiv**: [2511.11435v1](https://arxiv.org/abs/2511.11435) | [PDF](https://arxiv.org/pdf/2511.11435.pdf)

**作者**: Maria-Teresa De Rosa Palmini, Eva Cetinic

---

## 💡 一句话要点

**提出多模态图标性框架以评估扩散模型对文化记忆的识别与实现**

**关键词**: `扩散模型` `多模态图标性` `文化记忆评估` `文本到图像生成` `记忆与泛化`

## 📋 核心要点

1. 核心问题：扩散模型在泛化与记忆间的模糊性，聚焦文化共享关联的多模态图标性。
2. 方法要点：引入评估框架，区分文化参考的识别与实现，量化复制与转化。
3. 实验或效果：评估五个模型，显示框架优于相似性方法，并分析文化对齐因素。

## 📄 摘要（原文）

> Our work addresses the ambiguity between generalization and memorization in text-to-image diffusion models, focusing on a specific case we term multimodal iconicity. This refers to instances where images and texts evoke culturally shared associations, such as when a title recalls a familiar artwork or film scene. While prior research on memorization and unlearning emphasizes forgetting, we examine what is remembered and how, focusing on the balance between recognizing cultural references and reproducing them. We introduce an evaluation framework that separates recognition, whether a model identifies a reference, from realization, how it depicts it through replication or reinterpretation, quantified through measures capturing both dimensions. By evaluating five diffusion models across 767 Wikidata-derived cultural references spanning static and dynamic imagery, we show that our framework distinguishes replication from transformation more effectively than existing similarity-based methods. To assess linguistic sensitivity, we conduct prompt perturbation experiments using synonym substitutions and literal image descriptions, finding that models often reproduce iconic visual structures even when textual cues are altered. Finally, our analysis shows that cultural alignment correlates not only with training data frequency, but also textual uniqueness, reference popularity, and creation date. Our work reveals that the value of diffusion models lies not only in what they reproduce but in how they transform and recontextualize cultural knowledge, advancing evaluation beyond simple text-image matching toward richer contextual understanding.

