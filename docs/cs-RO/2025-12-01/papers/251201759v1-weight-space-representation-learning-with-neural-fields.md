---
layout: default
title: Weight Space Representation Learning with Neural Fields
---

# Weight Space Representation Learning with Neural Fields

**arXiv**: [2512.01759v1](https://arxiv.org/abs/2512.01759) | [PDF](https://arxiv.org/pdf/2512.01759.pdf)

**作者**: Zhuoqian Yang, Mathieu Salzmann, Sabine Süsstrunk

---

## 💡 一句话要点

**提出基于预训练模型和低秩适应的权重空间表示学习方法，提升神经场在重建、生成和分析任务中的性能。**

**关键词**: `权重空间表示` `神经场` `低秩适应` `潜在扩散模型` `生成任务` `重建任务`

## 📋 核心要点

1. 核心问题：探索权重作为有效表示的潜力，特别是在神经场中。
2. 方法要点：通过预训练基础模型和低秩适应约束优化空间，诱导权重空间结构。
3. 实验或效果：在2D和3D数据任务中，乘法LoRA权重实现高质量表示，与潜在扩散模型结合优于现有方法。

## 📄 摘要（原文）

> In this work, we investigate the potential of weights to serve as effective representations, focusing on neural fields. Our key insight is that constraining the optimization space through a pre-trained base model and low-rank adaptation (LoRA) can induce structure in weight space. Across reconstruction, generation, and analysis tasks on 2D and 3D data, we find that multiplicative LoRA weights achieve high representation quality while exhibiting distinctiveness and semantic structure. When used with latent diffusion models, multiplicative LoRA weights enable higher-quality generation than existing weight-space methods.

