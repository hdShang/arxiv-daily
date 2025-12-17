---
layout: default
title: VOST-SGG: VLM-Aided One-Stage Spatio-Temporal Scene Graph Generation
---

# VOST-SGG: VLM-Aided One-Stage Spatio-Temporal Scene Graph Generation

**arXiv**: [2512.05524v1](https://arxiv.org/abs/2512.05524) | [PDF](https://arxiv.org/pdf/2512.05524.pdf)

**作者**: Chinthani Sugandhika, Chen Li, Deepu Rajan, Basura Fernando

---

## 💡 一句话要点

**提出VOST-SGG框架，通过视觉语言模型增强单阶段时空场景图生成，解决查询语义缺失和谓词分类单模态限制问题。**

**关键词**: `时空场景图生成` `视觉语言模型` `单阶段检测` `多模态融合` `查询初始化` `视频理解`

## 📋 核心要点

1. 核心问题：现有单阶段ST-SGG模型存在查询语义未初始化及谓词分类仅依赖视觉特征的局限性。
2. 方法要点：引入双源查询初始化策略和多模态特征库，融合视觉、文本和空间线索以提升性能。
3. 实验或效果：在Action Genome数据集上实现最先进性能，验证了VLM集成和多模态特征的有效性。

## 📄 摘要（原文）

> Spatio-temporal scene graph generation (ST-SGG) aims to model objects and their evolving relationships across video frames, enabling interpretable representations for downstream reasoning tasks such as video captioning and visual question answering. Despite recent advancements in DETR-style single-stage ST-SGG models, they still suffer from several key limitations. First, while these models rely on attention-based learnable queries as a core component, these learnable queries are semantically uninformed and instance-agnostically initialized. Second, these models rely exclusively on unimodal visual features for predicate classification. To address these challenges, we propose VOST-SGG, a VLM-aided one-stage ST-SGG framework that integrates the common sense reasoning capabilities of vision-language models (VLMs) into the ST-SGG pipeline. First, we introduce the dual-source query initialization strategy that disentangles what to attend to from where to attend, enabling semantically grounded what-where reasoning. Furthermore, we propose a multi-modal feature bank that fuses visual, textual, and spatial cues derived from VLMs for improved predicate classification. Extensive experiments on the Action Genome dataset demonstrate that our approach achieves state-of-the-art performance, validating the effectiveness of integrating VLM-aided semantic priors and multi-modal features for ST-SGG. We will release the code at https://github.com/LUNAProject22/VOST.

