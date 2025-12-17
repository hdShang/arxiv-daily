---
layout: default
title: Maxitive Donsker-Varadhan Formulation for Possibilistic Variational Inference
---

# Maxitive Donsker-Varadhan Formulation for Possibilistic Variational Inference

**arXiv**: [2511.21223v1](https://arxiv.org/abs/2511.21223) | [PDF](https://arxiv.org/pdf/2511.21223.pdf)

**作者**: Jasraj Singh, Shelvia Wongso, Jeremie Houssineau, Badr-Eddine Chérief-Abdellatif

---

## 💡 一句话要点

**提出可能性变分推断的Donsker-Varadhan公式，以处理稀疏或不精确信息下的不确定性建模。**

**关键词**: `可能性理论` `变分推断` `Donsker-Varadhan公式` `认知不确定性` `指数族函数`

## 📋 核心要点

1. 核心问题：传统变分推断依赖高维积分，难以解析处理，且基于概率论无法直接建模认知不确定性。
2. 方法要点：重新定义熵和散度等核心概念，适应可能性理论的非可加性，并应用于指数族函数。
3. 实验或效果：未知，但强调与概率对应物的相似性和可能性理论的独特数学结构。

## 📄 摘要（原文）

> Variational inference (VI) is a cornerstone of modern Bayesian learning, enabling approximate inference in complex models that would otherwise be intractable. However, its formulation depends on expectations and divergences defined through high-dimensional integrals, often rendering analytical treatment impossible and necessitating heavy reliance on approximate learning and inference techniques. Possibility theory, an imprecise probability framework, allows to directly model epistemic uncertainty instead of leveraging subjective probabilities. While this framework provides robustness and interpretability under sparse or imprecise information, adapting VI to the possibilistic setting requires rethinking core concepts such as entropy and divergence, which presuppose additivity. In this work, we develop a principled formulation of possibilistic variational inference and apply it to a special class of exponential-family functions, highlighting parallels with their probabilistic counterparts and revealing the distinctive mathematical structures of possibility theory.

