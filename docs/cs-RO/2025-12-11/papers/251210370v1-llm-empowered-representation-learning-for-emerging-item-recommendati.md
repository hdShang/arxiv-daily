---
layout: default
title: LLM-Empowered Representation Learning for Emerging Item Recommendation
---

# LLM-Empowered Representation Learning for Emerging Item Recommendation

**arXiv**: [2512.10370v1](https://arxiv.org/abs/2512.10370) | [PDF](https://arxiv.org/pdf/2512.10370.pdf)

**作者**: Ziying Zhang, Quanming Yao, Yaqing Wang

---

## 💡 一句话要点

**提出EmerFlow框架，利用LLM增强表示学习以解决新兴物品推荐问题**

**关键词**: `新兴物品推荐` `表示学习` `LLM推理` `元学习` `嵌入对齐`

## 📋 核心要点

1. 核心问题：新兴物品交互随时间累积，现有方法常忽略动态过程，假设交互稀少或为零，需平衡独特性和共享模式
2. 方法要点：通过LLM推理丰富新兴物品原始特征，对齐现有推荐模型嵌入空间，结合元学习优化嵌入
3. 实验或效果：在电影和医药等多领域实验中，EmerFlow优于现有方法，能从有限交互中学习表达性嵌入

## 📄 摘要（原文）

> In this work, we tackle the challenge of recommending emerging items, whose interactions gradually accumulate over time. Existing methods often overlook this dynamic process, typically assuming that emerging items have few or even no historical interactions. Such an assumption oversimplifies the problem, as a good model must preserve the uniqueness of emerging items while leveraging their shared patterns with established ones. To address this challenge, we propose EmerFlow, a novel LLM-empowered representation learning framework that generates distinctive embeddings for emerging items. It first enriches the raw features of emerging items through LLM reasoning, then aligns these representations with the embedding space of the existing recommendation model. Finally, new interactions are incorporated through meta-learning to refine the embeddings. This enables EmerFlow to learn expressive embeddings for emerging items from only limited interactions. Extensive experiments across diverse domains, including movies and pharmaceuticals, show that EmerFlow consistently outperforms existing methods.

