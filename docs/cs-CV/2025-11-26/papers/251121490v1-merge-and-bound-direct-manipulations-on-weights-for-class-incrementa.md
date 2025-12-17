---
layout: default
title: Merge and Bound: Direct Manipulations on Weights for Class Incremental Learning
---

# Merge and Bound: Direct Manipulations on Weights for Class Incremental Learning

**arXiv**: [2511.21490v1](https://arxiv.org/abs/2511.21490) | [PDF](https://arxiv.org/pdf/2511.21490.pdf)

**作者**: Taehoon Kim, Donghwan Jang, Bohyung Han

---

## 💡 一句话要点

**提出Merge-and-Bound方法，通过直接操作权重解决类增量学习中的灾难性遗忘问题。**

**关键词**: `类增量学习` `权重合并` `有界更新` `灾难性遗忘` `模型优化`

## 📋 核心要点

1. 核心问题：类增量学习中模型易遗忘旧知识，即灾难性遗忘。
2. 方法要点：使用任务间和任务内权重合并，结合有界更新优化模型参数。
3. 实验或效果：在标准基准测试中表现优于现有方法，无需修改架构。

## 📄 摘要（原文）

> We present a novel training approach, named Merge-and-Bound (M&B) for Class Incremental Learning (CIL), which directly manipulates model weights in the parameter space for optimization. Our algorithm involves two types of weight merging: inter-task weight merging and intra-task weight merging. Inter-task weight merging unifies previous models by averaging the weights of models from all previous stages. On the other hand, intra-task weight merging facilitates the learning of current task by combining the model parameters within current stage. For reliable weight merging, we also propose a bounded update technique that aims to optimize the target model with minimal cumulative updates and preserve knowledge from previous tasks; this strategy reveals that it is possible to effectively obtain new models near old ones, reducing catastrophic forgetting. M&B is seamlessly integrated into existing CIL methods without modifying architecture components or revising learning objectives. We extensively evaluate our algorithm on standard CIL benchmarks and demonstrate superior performance compared to state-of-the-art methods.

