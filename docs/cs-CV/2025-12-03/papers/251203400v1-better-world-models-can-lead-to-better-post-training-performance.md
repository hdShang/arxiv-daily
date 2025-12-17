---
layout: default
title: Better World Models Can Lead to Better Post-Training Performance
---

# Better World Models Can Lead to Better Post-Training Performance

**arXiv**: [2512.03400v1](https://arxiv.org/abs/2512.03400) | [PDF](https://arxiv.org/pdf/2512.03400.pdf)

**作者**: Prakhar Gupta, Henry Conklin, Sarah-Jane Leslie, Andrew Lee

---

## 💡 一句话要点

**研究显式世界建模目标对Transformer内部表示及下游能力的影响，发现其能提升强化学习后训练性能**

**关键词**: `世界建模` `Transformer表示` `强化学习后训练` `状态预测` `序列规划任务`

## 📋 核心要点

1. 核心问题：显式世界建模如何影响Transformer在不同训练阶段的内部表示和下游任务能力
2. 方法要点：比较标准下一词预测与两种显式世界建模策略，使用GRPO进行后训练
3. 实验或效果：显式世界建模产生更线性可解码和因果可操控的状态表示，提升GRPO在困难任务上的性能

## 📄 摘要（原文）

> In this work we study how explicit world-modeling objectives affect the internal representations and downstream capability of Transformers across different training stages. We use a controlled 2x2x2 Rubik's Cube and ask: (1) how does explicitly pretraining a world model affect the model's latent representations, and (2) how does world-model quality affect the model's performance after reinforcement learning post-training? We compare standard next-token prediction to two explicit world-modeling strategies -- (i) state-prediction pretraining and (ii) a joint state-prediction + next-token objective -- and assess task performance after Group Relative Policy Optimization (GRPO) is applied as post-training. We evaluate the representation quality with linear probes and causal interventions. We find that explicit world-modeling yields more linearly decodable and causally steerable state representations. More importantly, we find that improved state representations lead to higher gains for GRPO, especially on harder cube states. Our results indicate that sharpening state representations can improve the effectiveness of post-training for sequence-planning tasks.

