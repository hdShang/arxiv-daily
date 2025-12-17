---
layout: default
title: Difference Vector Equalization for Robust Fine-tuning of Vision-Language Models
---

# Difference Vector Equalization for Robust Fine-tuning of Vision-Language Models

**arXiv**: [2511.09973v1](https://arxiv.org/abs/2511.09973) | [PDF](https://arxiv.org/pdf/2511.09973.pdf)

**作者**: Satoshi Suzuki, Shin'ya Yamaguchi, Shoichiro Takeda, Taiga Yamane, Naoki Makishima, Naotaka Kawata, Mana Ihori, Tomohiro Tanaka, Shota Orihashi, Ryo Masumura

---

## 💡 一句话要点

**提出差异向量均衡化以在微调中保持视觉语言模型的泛化能力**

**关键词**: `视觉语言模型` `鲁棒微调` `几何结构保持` `差异向量均衡化` `零样本学习`

## 📋 核心要点

1. 现有微调方法扭曲嵌入几何结构，限制分布外和零样本性能
2. 通过约束差异向量相等来全局和局部保持几何结构
3. 实验显示在分布内、分布外和零样本指标上取得强结果

## 📄 摘要（原文）

> Contrastive pre-trained vision-language models, such as CLIP, demonstrate strong generalization abilities in zero-shot classification by leveraging embeddings extracted from image and text encoders. This paper aims to robustly fine-tune these vision-language models on in-distribution (ID) data without compromising their generalization abilities in out-of-distribution (OOD) and zero-shot settings. Current robust fine-tuning methods tackle this challenge by reusing contrastive learning, which was used in pre-training, for fine-tuning. However, we found that these methods distort the geometric structure of the embeddings, which plays a crucial role in the generalization of vision-language models, resulting in limited OOD and zero-shot performance. To address this, we propose Difference Vector Equalization (DiVE), which preserves the geometric structure during fine-tuning. The idea behind DiVE is to constrain difference vectors, each of which is obtained by subtracting the embeddings extracted from the pre-trained and fine-tuning models for the same data sample. By constraining the difference vectors to be equal across various data samples, we effectively preserve the geometric structure. Therefore, we introduce two losses: average vector loss (AVL) and pairwise vector loss (PVL). AVL preserves the geometric structure globally by constraining difference vectors to be equal to their weighted average. PVL preserves the geometric structure locally by ensuring a consistent multimodal alignment. Our experiments demonstrate that DiVE effectively preserves the geometric structure, achieving strong results across ID, OOD, and zero-shot metrics.

