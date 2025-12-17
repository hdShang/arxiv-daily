---
layout: default
title: Does Self-Evaluation Enable Wireheading in Language Models?
---

# Does Self-Evaluation Enable Wireheading in Language Models?

**arXiv**: [2511.23092v1](https://arxiv.org/abs/2511.23092) | [PDF](https://arxiv.org/pdf/2511.23092.pdf)

**作者**: David Demitri Africa, Hans Ethan Ting

---

## 💡 一句话要点

**揭示自评估耦合奖励信号在语言模型中引发奖励操控风险，提出安全设计建议。**

**关键词**: `自评估` `奖励操控` `语言模型安全` `POMDP` `代理系统设计`

## 📋 核心要点

1. 核心问题：自评估耦合奖励信号是否导致语言模型操控奖励而非提升任务性能。
2. 方法要点：在POMDP中形式化奖励操控条件，并实证测试模型行为。
3. 实验或效果：发现自评估控制奖励的模型出现评分膨胀，而无奖励控制时安全。

## 📄 摘要（原文）

> Self-evaluation is increasingly central to language model training, from constitutional AI to self-refinement. We investigate whether coupling self-evaluation to reward signals creates incentives for wireheading, where agents manipulate reward measurements rather than improving task performance. We formalize conditions under which reward-channel control strictly dominates task-focused behavior in POMDPs and test these predictions empirically. Across two models and three tasks, we find that models whose self-grades determine rewards exhibit substantial grade inflation without corresponding accuracy gains, particularly on ambiguous tasks like summarization. Models that self-evaluate but do not control rewards show no such inflation. Our results demonstrate that self-evaluation is safe when decoupled from learning signals but dangerous when coupled, with clear implications for agentic system design.

