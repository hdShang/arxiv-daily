---
layout: default
title: LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation
---

# LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation

**arXiv**: [2511.02239v1](https://arxiv.org/abs/2511.02239) | [PDF](https://arxiv.org/pdf/2511.02239.pdf)

**作者**: Youngjin Hong, Houjian Yu, Mingen Li, Changhyun Choi

---

## 💡 一句话要点

**提出LACY框架，通过双向语言-动作映射实现机器人操作的自我改进**

**关键词**: `机器人操作` `视觉语言模型` `双向映射` `自我监督学习` `语言-动作循环`

## 📋 核心要点

1. 核心问题：单向语言到动作映射缺乏上下文理解，限制机器人策略的泛化能力
2. 方法要点：联合训练语言到动作、动作到语言和语言一致性验证任务
3. 实验或效果：在拾取任务中平均提高成功率56.46%，增强语言-动作基础

## 📄 摘要（原文）

> Learning generalizable policies for robotic manipulation increasingly relies
> on large-scale models that map language instructions to actions (L2A). However,
> this one-way paradigm often produces policies that execute tasks without deeper
> contextual understanding, limiting their ability to generalize or explain their
> behavior. We argue that the complementary skill of mapping actions back to
> language (A2L) is essential for developing more holistic grounding. An agent
> capable of both acting and explaining its actions can form richer internal
> representations and unlock new paradigms for self-supervised learning. We
> introduce LACY (Language-Action Cycle), a unified framework that learns such
> bidirectional mappings within a single vision-language model. LACY is jointly
> trained on three synergistic tasks: generating parameterized actions from
> language (L2A), explaining observed actions in language (A2L), and verifying
> semantic consistency between two language descriptions (L2C). This enables a
> self-improving cycle that autonomously generates and filters new training data
> through an active augmentation strategy targeting low-confidence cases, thereby
> improving the model without additional human labels. Experiments on
> pick-and-place tasks in both simulation and the real world show that LACY
> improves task success rates by 56.46% on average and yields more robust
> language-action grounding for robotic manipulation. Project page:
> https://vla2026.github.io/LACY/

