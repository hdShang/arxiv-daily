---
layout: default
title: A Simple Generalisation of the Implicit Dynamics of In-Context Learning
---

# A Simple Generalisation of the Implicit Dynamics of In-Context Learning

**arXiv**: [2512.11255v1](https://arxiv.org/abs/2512.11255) | [PDF](https://arxiv.org/pdf/2512.11255.pdf)

**作者**: Francesco Innocenti, El Mehdi Achour

---

## 💡 一句话要点

**提出上下文学习隐式动态的简单泛化，扩展至所有序列位置、任意Transformer块及更现实的残差块。**

**关键词**: `上下文学习` `Transformer` `隐式动态` `线性回归` `残差块` `层归一化`

## 📋 核心要点

1. 核心问题：上下文学习（ICL）中模型如何从输入示例学习新任务，无需参数更新。
2. 方法要点：泛化Dherin等人（2025）的理论，涵盖所有序列位置、任意Transformer块和包含层归一化的残差块。
3. 实验或效果：在简单上下文线性回归任务上实证验证，并探究块内和块间不同令牌的隐式更新关系。

## 📄 摘要（原文）

> In-context learning (ICL) refers to the ability of a model to learn new tasks from examples in its input without any parameter updates. In contrast to previous theories of ICL relying on toy models and data settings, recently it has been shown that an abstraction of a transformer block can be seen as implicitly updating the weights of its feedforward network according to the context (Dherin et al., 2025). Here, we provide a simple generalisation of this result for (i) all sequence positions beyond the last, (ii) any transformer block beyond the first, and (iii) more realistic residual blocks including layer normalisation. We empirically verify our theory on simple in-context linear regression tasks and investigate the relationship between the implicit updates related to different tokens within and between blocks. These results help to bring the theory of Dherin et al. (2025) even closer to practice, with potential for validation on large-scale models.

