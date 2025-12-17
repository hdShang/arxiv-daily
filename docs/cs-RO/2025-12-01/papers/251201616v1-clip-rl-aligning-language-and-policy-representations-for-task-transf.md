---
layout: default
title: CLIP-RL: Aligning Language and Policy Representations for Task Transfer in Reinforcement Learning
---

# CLIP-RL: Aligning Language and Policy Representations for Task Transfer in Reinforcement Learning

**arXiv**: [2512.01616v1](https://arxiv.org/abs/2512.01616) | [PDF](https://arxiv.org/pdf/2512.01616.pdf)

**作者**: Chainesh Gautam, Raghuram Bharadwaj Diddigi

---

## 💡 一句话要点

**提出CLIP-RL方法，通过对齐语言与策略表示实现强化学习中的任务迁移**

**关键词**: `强化学习` `任务迁移` `多模态对齐` `语言表示` `策略嵌入` `CLIP扩展`

## 📋 核心要点

1. 核心问题：强化学习代理需在同一环境中解决多任务，且任务与语言自然关联。
2. 方法要点：借鉴CLIP思想，对齐语言指令与策略嵌入，构建统一表示空间。
3. 实验或效果：实验显示算法能加速任务迁移，提升效率。

## 📄 摘要（原文）

> Recently, there has been an increasing need to develop agents capable of solving multiple tasks within the same environment, especially when these tasks are naturally associated with language. In this work, we propose a novel approach that leverages combinations of pre-trained (language, policy) pairs to establish an efficient transfer pipeline. Our algorithm is inspired by the principles of Contrastive Language-Image Pretraining (CLIP) in Computer Vision, which aligns representations across different modalities under the philosophy that ''two modalities representing the same concept should have similar representations.'' The central idea here is that the instruction and corresponding policy of a task represent the same concept, the task itself, in two different modalities. Therefore, by extending the idea of CLIP to RL, our method creates a unified representation space for natural language and policy embeddings. Experimental results demonstrate the utility of our algorithm in achieving faster transfer across tasks.

