---
layout: default
title: EgoExo-Con: Exploring View-Invariant Video Temporal Understanding
---

# EgoExo-Con: Exploring View-Invariant Video Temporal Understanding

**arXiv**: [2510.26113v1](https://arxiv.org/abs/2510.26113) | [PDF](https://arxiv.org/pdf/2510.26113.pdf)

**作者**: Minjoon Jung, Junbin Xiao, Junghyun Kim, Byoung-Tak Zhang, Angela Yao

---

## 💡 一句话要点

**提出View-GRPO框架以解决视频-LLMs在多视角下时间理解不一致问题**

**关键词**: `视频-LLMs` `多视角一致性` `时间理解` `强化学习` `基准数据集`

## 📋 核心要点

1. 核心问题：视频-LLMs在不同视角下时间理解不一致，性能远低于单视角
2. 方法要点：引入EgoExo-Con基准和View-GRPO强化学习框架，增强跨视角一致性
3. 实验或效果：View-GRPO优于简单微调和GRPO，显著提升跨视角一致性

## 📄 摘要（原文）

> Can Video-LLMs achieve consistent temporal understanding when videos capture
> the same event from different viewpoints? To study this, we introduce
> EgoExo-Con (Consistency), a benchmark of comprehensively synchronized
> egocentric and exocentric video pairs with human-refined queries in natural
> language. EgoExo-Con emphasizes two temporal understanding tasks: Temporal
> Verification and Temporal Grounding. It evaluates not only correctness but
> consistency across viewpoints. Our analysis reveals two critical limitations of
> existing Video-LLMs: (1) models often fail to maintain consistency, with
> results far worse than their single-view performances. (2) When naively
> finetuned with synchronized videos of both viewpoints, the models show improved
> consistency but often underperform those trained on a single view. For
> improvements, we propose View-GRPO, a novel reinforcement learning framework
> that effectively strengthens view-specific temporal reasoning while encouraging
> consistent comprehension across viewpoints. Our method demonstrates its
> superiority over naive SFT and GRPO, especially for improving cross-view
> consistency. All resources will be made publicly available.

