---
layout: default
title: Multilingual Text-to-Image Person Retrieval via Bidirectional Relation Reasoning and Aligning
---

# Multilingual Text-to-Image Person Retrieval via Bidirectional Relation Reasoning and Aligning

**arXiv**: [2510.17685v1](https://arxiv.org/abs/2510.17685) | [PDF](https://arxiv.org/pdf/2510.17685.pdf)

**作者**: Min Cao, Xinyu Zhou, Ding Jiang, Bo Du, Mang Ye, Min Zhang

---

## 💡 一句话要点

**提出Bi-IRRA框架以解决多语言文本到图像行人检索中的模态异质性问题**

**关键词**: `多语言文本到图像检索` `模态对齐` `行人检索` `双向推理` `隐式关系建模`

## 📋 核心要点

1. 核心问题：文本与图像模态异质性及英语中心化限制多语言应用
2. 方法要点：双向隐式关系推理模块和多维全局对齐模块实现跨语言模态对齐
3. 实验或效果：在多语言TIPR数据集上达到新最优结果，提供数据和代码

## 📄 摘要（原文）

> Text-to-image person retrieval (TIPR) aims to identify the target person
> using textual descriptions, facing challenge in modality heterogeneity. Prior
> works have attempted to address it by developing cross-modal global or local
> alignment strategies. However, global methods typically overlook fine-grained
> cross-modal differences, whereas local methods require prior information to
> explore explicit part alignments. Additionally, current methods are
> English-centric, restricting their application in multilingual contexts. To
> alleviate these issues, we pioneer a multilingual TIPR task by developing a
> multilingual TIPR benchmark, for which we leverage large language models for
> initial translations and refine them by integrating domain-specific knowledge.
> Correspondingly, we propose Bi-IRRA: a Bidirectional Implicit Relation
> Reasoning and Aligning framework to learn alignment across languages and
> modalities. Within Bi-IRRA, a bidirectional implicit relation reasoning module
> enables bidirectional prediction of masked image and text, implicitly enhancing
> the modeling of local relations across languages and modalities, a
> multi-dimensional global alignment module is integrated to bridge the modality
> heterogeneity. The proposed method achieves new state-of-the-art results on all
> multilingual TIPR datasets. Data and code are presented in
> https://github.com/Flame-Chasers/Bi-IRRA.

