---
layout: default
title: Can LLMs Evaluate What They Cannot Annotate? Revisiting LLM Reliability in Hate Speech Detection
---

# Can LLMs Evaluate What They Cannot Annotate? Revisiting LLM Reliability in Hate Speech Detection

**arXiv**: [2512.09662v1](https://arxiv.org/abs/2512.09662) | [PDF](https://arxiv.org/pdf/2512.09662.pdf)

**作者**: Paloma Piot, David Otero, Patricia Martín-Rodilla, Javier Parapar

---

## 💡 一句话要点

**提出基于跨评分者可靠性的主观性感知框架，评估LLM在仇恨言论检测中的可靠性，发现其可作为代理评估者。**

**关键词**: `仇恨言论检测` `大型语言模型` `主观性评估` `跨评分者可靠性` `代理评估` `自然语言处理`

## 📋 核心要点

1. 核心问题：仇恨言论检测的主观性挑战，传统指标如Cohen's κ简化分歧，LLM无法完全替代人类判断。
2. 方法要点：使用跨评分者可靠性（xRR）重新评估LLM可靠性，分析LLM与人类在实例级和模式级的差异。
3. 实验或效果：LLM生成的标注能可靠反映分类模型性能趋势，与人类评估相关，可作为主观NLP任务的代理评估工具。

## 📄 摘要（原文）

> Hate speech spreads widely online, harming individuals and communities, making automatic detection essential for large-scale moderation, yet detecting it remains difficult. Part of the challenge lies in subjectivity: what one person flags as hate speech, another may see as benign. Traditional annotation agreement metrics, such as Cohen's $κ$, oversimplify this disagreement, treating it as an error rather than meaningful diversity. Meanwhile, Large Language Models (LLMs) promise scalable annotation, but prior studies demonstrate that they cannot fully replace human judgement, especially in subjective tasks. In this work, we reexamine LLM reliability using a subjectivity-aware framework, cross-Rater Reliability (xRR), revealing that even under fairer lens, LLMs still diverge from humans. Yet this limitation opens an opportunity: we find that LLM-generated annotations can reliably reflect performance trends across classification models, correlating with human evaluations. We test this by examining whether LLM-generated annotations preserve the relative ordering of model performance derived from human evaluation (i.e. whether models ranked as more reliable by human annotators preserve the same order when evaluated with LLM-generated labels). Our results show that, although LLMs differ from humans at the instance level, they reproduce similar ranking and classification patterns, suggesting their potential as proxy evaluators. While not a substitute for human annotators, they might serve as a scalable proxy for evaluation in subjective NLP tasks.

