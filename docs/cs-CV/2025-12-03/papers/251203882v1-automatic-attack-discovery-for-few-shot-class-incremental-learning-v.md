---
layout: default
title: Automatic Attack Discovery for Few-Shot Class-Incremental Learning via Large Language Models
---

# Automatic Attack Discovery for Few-Shot Class-Incremental Learning via Large Language Models

**arXiv**: [2512.03882v1](https://arxiv.org/abs/2512.03882) | [PDF](https://arxiv.org/pdf/2512.03882.pdf)

**作者**: Haidong Kang, Wei Wu, Hanling Wang

---

## 💡 一句话要点

**提出ACraft方法，利用大语言模型自动发现针对少样本类增量学习的攻击方法**

**关键词**: `少样本类增量学习` `大语言模型` `自动攻击发现` `强化学习` `安全评估`

## 📋 核心要点

1. 核心问题：少样本类增量学习的安全问题未受充分关注，现有攻击方法效果有限或成本高
2. 方法要点：基于大语言模型自动生成攻击方法，结合PPO强化学习优化生成过程
3. 实验或效果：在主流基准上显著降低先进FSCIL方法性能，超越人工攻击方法且成本最低

## 📄 摘要（原文）

> Few-shot class incremental learning (FSCIL) is a more realistic and challenging paradigm in continual learning to incrementally learn unseen classes and overcome catastrophic forgetting on base classes with only a few training examples. Previous efforts have primarily centered around studying more effective FSCIL approaches. By contrast, less attention was devoted to thinking the security issues in contributing to FSCIL. This paper aims to provide a holistic study of the impact of attacks on FSCIL. We first derive insights by systematically exploring how human expert-designed attack methods (i.e., PGD, FGSM) affect FSCIL. We find that those methods either fail to attack base classes, or suffer from huge labor costs due to relying on huge expert knowledge. This highlights the need to craft a specialized attack method for FSCIL. Grounded in these insights, in this paper, we propose a simple yet effective ACraft method to automatically steer and discover optimal attack methods targeted at FSCIL by leveraging Large Language Models (LLMs) without human experts. Moreover, to improve the reasoning between LLMs and FSCIL, we introduce a novel Proximal Policy Optimization (PPO) based reinforcement learning to optimize learning, making LLMs generate better attack methods in the next generation by establishing positive feedback. Experiments on mainstream benchmarks show that our ACraft significantly degrades the performance of state-of-the-art FSCIL methods and dramatically beyond human expert-designed attack methods while maintaining the lowest costs of attack.

