---
layout: default
title: Unconsciously Forget: Mitigating Memorization; Without Knowing What is being Memorized
---

# Unconsciously Forget: Mitigating Memorization; Without Knowing What is being Memorized

**arXiv**: [2512.09687v1](https://arxiv.org/abs/2512.09687) | [PDF](https://arxiv.org/pdf/2512.09687.pdf)

**作者**: Er Jin, Yang Zhang, Yongli Mou, Yanfei Dong, Stefan Decker, Kenji Kawaguchi, Johannes Stegmaier

---

## 💡 一句话要点

**提出UniForget方法，通过模型剪枝缓解生成模型记忆训练数据问题，无需针对特定概念。**

**关键词**: `生成模型` `记忆缓解` `模型剪枝` `版权保护` `去记忆技术` `无监督学习`

## 📋 核心要点

1. 核心问题：生成模型易记忆训练数据，导致版权侵权等法律风险，现有方法计算开销大或可扩展性差。
2. 方法要点：识别模型中对受版权内容生成负责的部分，应用模型剪枝抑制生成概率，保持一般生成能力。
3. 实验或效果：有效降低受版权内容生成概率，与现有遗忘方法正交互补，提升去记忆技术。

## 📄 摘要（原文）

> Recent advances in generative models have demonstrated an exceptional ability to produce highly realistic images. However, previous studies show that generated images often resemble the training data, and this problem becomes more severe as the model size increases. Memorizing training data can lead to legal challenges, including copyright infringement, violations of portrait rights, and trademark violations. Existing approaches to mitigating memorization mainly focus on manipulating the denoising sampling process to steer image embeddings away from the memorized embedding space or employ unlearning methods that require training on datasets containing specific sets of memorized concepts. However, existing methods often incur substantial computational overhead during sampling, or focus narrowly on removing one or more groups of target concepts, imposing a significant limitation on their scalability. To understand and mitigate these problems, our work, UniForget, offers a new perspective on understanding the root cause of memorization. Our work demonstrates that specific parts of the model are responsible for copyrighted content generation. By applying model pruning, we can effectively suppress the probability of generating copyrighted content without targeting specific concepts while preserving the general generative capabilities of the model. Additionally, we show that our approach is both orthogonal and complementary to existing unlearning methods, thereby highlighting its potential to improve current unlearning and de-memorization techniques.

