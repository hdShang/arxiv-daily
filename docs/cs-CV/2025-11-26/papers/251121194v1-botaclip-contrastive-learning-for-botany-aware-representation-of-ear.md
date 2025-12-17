---
layout: default
title: BotaCLIP: Contrastive Learning for Botany-Aware Representation of Earth Observation Data
---

# BotaCLIP: Contrastive Learning for Botany-Aware Representation of Earth Observation Data

**arXiv**: [2511.21194v1](https://arxiv.org/abs/2511.21194) | [PDF](https://arxiv.org/pdf/2511.21194.pdf)

**作者**: Selene Cerna, Sara Si-Moussi, Wilfried Thuiller, Hadrien Hendrikx, Vincent Miele

---

## 💡 一句话要点

**提出BotaCLIP框架，通过对比学习将植物学知识注入地球观测模型，提升生态任务性能。**

**关键词**: `对比学习` `多模态表示` `地球观测数据` `植物学适应` `生态建模` `轻量框架`

## 📋 核心要点

1. 核心问题：预训练基础模型缺乏领域知识，难以适应生态数据稀缺场景。
2. 方法要点：轻量多模态对比框架，对齐高分辨率航拍图像与植物调查数据，防止灾难性遗忘。
3. 实验效果：在植物存在预测等任务中，性能优于DOFA和监督基线模型。

## 📄 摘要（原文）

> Foundation models have demonstrated a remarkable ability to learn rich, transferable representations across diverse modalities such as images, text, and audio. In modern machine learning pipelines, these representations often replace raw data as the primary input for downstream tasks. In this paper, we address the challenge of adapting a pre-trained foundation model to inject domain-specific knowledge, without retraining from scratch or incurring significant computational costs. To this end, we introduce BotaCLIP, a lightweight multimodal contrastive framework that adapts a pre-trained Earth Observation foundation model (DOFA) by aligning high-resolution aerial imagery with botanical relevés. Unlike generic embeddings, BotaCLIP internalizes ecological structure through contrastive learning with a regularization strategy that mitigates catastrophic forgetting. Once trained, the resulting embeddings serve as transferable representations for downstream predictors. Motivated by real-world applications in biodiversity modeling, we evaluated BotaCLIP representations in three ecological tasks: plant presence prediction, butterfly occurrence modeling, and soil trophic group abundance estimation. The results showed consistent improvements over those derived from DOFA and supervised baselines. More broadly, this work illustrates how domain-aware adaptation of foundation models can inject expert knowledge into data-scarce settings, enabling frugal representation learning.

