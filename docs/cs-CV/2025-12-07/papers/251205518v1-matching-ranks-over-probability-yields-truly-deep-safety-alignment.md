---
layout: default
title: Matching Ranks Over Probability Yields Truly Deep Safety Alignment
---

# Matching Ranks Over Probability Yields Truly Deep Safety Alignment

**arXiv**: [2512.05518v1](https://arxiv.org/abs/2512.05518) | [PDF](https://arxiv.org/pdf/2512.05518.pdf)

**作者**: Jason Vega, Gagandeep Singh

---

## 💡 一句话要点

**提出PRESTO方法以解决RAP攻击下LLM安全对齐的浅层漏洞**

**关键词**: `大语言模型安全对齐` `预填充攻击` `令牌排名匹配` `注意力正则化` `RAP攻击` `数据增强防御`

## 📋 核心要点

1. 核心问题：现有数据增强防御在RAP攻击下仍暴露浅层安全对齐，因SFT目标易被‘博弈’导致有害令牌排名高。
2. 方法要点：通过匹配目标分布的令牌排名而非概率，提出PRESTO方法，正则化有害预填充令牌的注意力。
3. 实验或效果：在三个开源LLM上，PRESTO使RAP攻击下的StrongREJECT分数平均提升高达4.7倍，对模型效用影响低。

## 📄 摘要（原文）

> A frustratingly easy technique known as the prefilling attack has been shown to effectively circumvent the safety alignment of frontier LLMs by simply prefilling the assistant response with an affirmative prefix before decoding. In response, recent work proposed a supervised fine-tuning (SFT) defense using data augmentation to achieve a \enquote{deep} safety alignment, allowing the model to generate natural language refusals immediately following harmful prefills. Unfortunately, we show in this work that the "deep" safety alignment produced by such an approach is in fact not very deep. A generalization of the prefilling attack, which we refer to as the Rank-Assisted Prefilling (RAP) attack, can effectively extract harmful content from models fine-tuned with the data augmentation defense by selecting low-probability "harmful" tokens from the top 20 predicted next tokens at each step (thus ignoring high-probability "refusal" tokens). We argue that this vulnerability is enabled due to the "gaming" of the SFT objective when the target distribution entropies are low, where low fine-tuning loss is achieved by shifting large probability mass to a small number of refusal tokens while neglecting the high ranks of harmful tokens. We then propose a new perspective on achieving deep safety alignment by matching the token ranks of the target distribution, rather than their probabilities. This perspective yields a surprisingly simple fix to the data augmentation defense based on regularizing the attention placed on harmful prefill tokens, an approach we call PRefill attEntion STOpping (PRESTO). Adding PRESTO yields up to a 4.7x improvement in the mean StrongREJECT score under RAP attacks across three popular open-source LLMs, with low impact to model utility.

