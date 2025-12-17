---
layout: default
title: Samplability makes learning easier
---

# Samplability makes learning easier

**arXiv**: [2512.01276v1](https://arxiv.org/abs/2512.01276) | [PDF](https://arxiv.org/pdf/2512.01276.pdf)

**作者**: Guy Blanc, Caleb Koch, Jane Lange, Carmen Strassle, Li-Yang Tan

---

## 💡 一句话要点

**提出显式规避集以证明可采样PAC学习显著增强高效学习能力**

**关键词**: `PAC学习` `可采样分布` `显式规避集` `计算复杂度` `样本复杂度` `在线学习`

## 📋 核心要点

1. 核心问题：标准PAC学习要求所有分布，包括难采样分布，限制了高效学习
2. 方法要点：引入显式规避集作为复杂度原语，区分标准与可采样PAC学习
3. 实验或效果：构建概念类，在可采样PAC中多项式样本可学，标准PAC中需指数样本

## 📄 摘要（原文）

> The standard definition of PAC learning (Valiant 1984) requires learners to succeed under all distributions -- even ones that are intractable to sample from. This stands in contrast to samplable PAC learning (Blum, Furst, Kearns, and Lipton 1993), where learners only have to succeed under samplable distributions. We study this distinction and show that samplable PAC substantially expands the power of efficient learners.
>   We first construct a concept class that requires exponential sample complexity in standard PAC but is learnable with polynomial sample complexity in samplable PAC. We then lift this statistical separation to the computational setting and obtain a separation relative to a random oracle. Our proofs center around a new complexity primitive, explicit evasive sets, that we introduce and study. These are sets for which membership is easy to determine but are extremely hard to sample from.
>   Our results extend to the online setting to similarly show how its landscape changes when the adversary is assumed to be efficient instead of computationally unbounded.

