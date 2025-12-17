---
layout: default
title: Provably Learning from Modern Language Models via Low Logit Rank
---

# Provably Learning from Modern Language Models via Low Logit Rank

**arXiv**: [2512.09892v1](https://arxiv.org/abs/2512.09892) | [PDF](https://arxiv.org/pdf/2512.09892.pdf)

**作者**: Noah Golowich, Allen Liu, Abhishek Shetty

---

## 💡 一句话要点

**提出基于低对数秩的高效查询学习算法，以从现代语言模型中获取可证明学习保证。**

**关键词**: `低对数秩` `查询学习` `可证明学习` `语言模型抽象` `生成模型学习`

## 📋 核心要点

1. 核心问题：现代语言模型复杂，但经验上对数秩低，如何利用此结构进行可证明学习。
2. 方法要点：在查询学习模型中，设计算法从低对数秩模型中高效学习，适用于API访问场景。
3. 实验或效果：算法能学习近似低对数秩模型，为生成模型提供首个端到端学习保证。

## 📄 摘要（原文）

> While modern language models and their inner workings are incredibly complex, recent work (Golowich, Liu & Shetty; 2025) has proposed a simple and potentially tractable abstraction for them through the observation that empirically, these language models all seem to have approximately low logit rank. Roughly, this means that a matrix formed by the model's log probabilities of various tokens conditioned on certain sequences of tokens is well approximated by a low rank matrix.
>   In this paper, our focus is on understanding how this structure can be exploited algorithmically for obtaining provable learning guarantees. Since low logit rank models can encode hard-to-learn distributions such as noisy parities, we study a query learning model with logit queries that reflects the access model for common APIs. Our main result is an efficient algorithm for learning any approximately low logit rank model from queries. We emphasize that our structural assumption closely reflects the behavior that is empirically observed in modern language models. Thus, our result gives what we believe is the first end-to-end learning guarantee for a generative model that plausibly captures modern language models.

