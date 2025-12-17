---
layout: default
title: Idea-Gated Transformers: Enforcing Semantic Coherence via Differentiable Vocabulary Pruning
---

# Idea-Gated Transformers: Enforcing Semantic Coherence via Differentiable Vocabulary Pruning

**arXiv**: [2512.03343v1](https://arxiv.org/abs/2512.03343) | [PDF](https://arxiv.org/pdf/2512.03343.pdf)

**作者**: Darshan Fofadiya

---

## 💡 一句话要点

**提出Idea-Gated Transformer以解决自回归语言模型中的主题漂移问题**

**关键词**: `自回归语言模型` `主题漂移` `可微分门控` `语义规划` `词汇剪枝` `可控生成`

## 📋 核心要点

1. 核心问题：自回归语言模型基于下一词预测训练，易因局部关联导致生成内容偏离初始提示，称为主题漂移。
2. 方法要点：引入Idea-Gated Transformer，通过辅助Idea Head预测未来上下文词袋分布，生成概念向量实时门控主词汇，抑制语义无关词。
3. 实验或效果：在WikiText-103上验证，模型保持与GPT-2相当的困惑度，但显著提升领域保持能力，有效锁定语义聚类。

## 📄 摘要（原文）

> Autoregressive Language Models (LLMs) trained on Next-Token Prediction (NTP) often suffer from ``Topic Drift'' where the generation wanders away from the initial prompt due to a reliance on local associations rather than global planning \citep{holtzman2019curious}. While scaling model size mitigates this \citep{brown2020language}, the fundamental myopia of the NTP objective remains. In this work, we introduce the Idea-Gated Transformer, a novel architecture that separates semantic planning from syntactic generation. We introduce an auxiliary ``Idea Head'' trained to predict the bag-of-words distribution for a future context window, creating a latent ``Concept Vector'' that actively gates the main vocabulary during generation. We propose a differentiable gating mechanism that suppresses semantically irrelevant tokens, effectively pruning the search space in real-time. Experiments on WikiText-103 demonstrate that while the Idea-Gated model achieves comparable validation perplexity to a standard GPT-2 baseline, it exhibits significantly superior Domain Retention. Qualitative and quantitative analysis reveals that the gating mechanism successfully locks generation into specific semantic clusters (e.g., Finance, Science) and resists associative drift, offering a parameter-efficient path toward more controllable language modeling.

