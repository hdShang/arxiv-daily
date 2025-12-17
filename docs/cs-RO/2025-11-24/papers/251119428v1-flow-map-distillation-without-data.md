---
layout: default
title: Flow Map Distillation Without Data
---

# Flow Map Distillation Without Data

**arXiv**: [2511.19428v1](https://arxiv.org/abs/2511.19428) | [PDF](https://arxiv.org/pdf/2511.19428.pdf)

**作者**: Shangyuan Tong, Nanye Ma, Saining Xie, Tommi Jaakkola

---

## 💡 一句话要点

**提出无数据流映射蒸馏方法，避免教师-数据不匹配风险。**

**关键词**: `流映射蒸馏` `无数据学习` `生成模型加速` `教师-数据不匹配` `先验分布采样`

## 📋 核心要点

1. 核心问题：传统流映射蒸馏依赖外部数据，易导致教师-数据不匹配。
2. 方法要点：仅从先验分布采样，主动纠正误差，确保高保真度。
3. 实验效果：在ImageNet上FID达1.45，超越所有数据方法。

## 📄 摘要（原文）

> State-of-the-art flow models achieve remarkable quality but require slow, iterative sampling. To accelerate this, flow maps can be distilled from pre-trained teachers, a procedure that conventionally requires sampling from an external dataset. We argue that this data-dependency introduces a fundamental risk of Teacher-Data Mismatch, as a static dataset may provide an incomplete or even misaligned representation of the teacher's full generative capabilities. This leads us to question whether this reliance on data is truly necessary for successful flow map distillation. In this work, we explore a data-free alternative that samples only from the prior distribution, a distribution the teacher is guaranteed to follow by construction, thereby circumventing the mismatch risk entirely. To demonstrate the practical viability of this philosophy, we introduce a principled framework that learns to predict the teacher's sampling path while actively correcting for its own compounding errors to ensure high fidelity. Our approach surpasses all data-based counterparts and establishes a new state-of-the-art by a significant margin. Specifically, distilling from SiT-XL/2+REPA, our method reaches an impressive FID of 1.45 on ImageNet 256x256, and 1.49 on ImageNet 512x512, both with only 1 sampling step. We hope our work establishes a more robust paradigm for accelerating generative models and motivates the broader adoption of flow map distillation without data.

