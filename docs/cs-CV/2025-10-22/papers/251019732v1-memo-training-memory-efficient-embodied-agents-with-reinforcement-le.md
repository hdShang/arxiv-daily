---
layout: default
title: Memo: Training Memory-Efficient Embodied Agents with Reinforcement Learning
---

# Memo: Training Memory-Efficient Embodied Agents with Reinforcement Learning

**arXiv**: [2510.19732v1](https://arxiv.org/abs/2510.19732) | [PDF](https://arxiv.org/pdf/2510.19732.pdf)

**作者**: Gunshi Gupta, Karmesh Yadav, Zsolt Kira, Yarin Gal, Rahaf Aljundi

---

## 💡 一句话要点

**提出Memo架构以解决长时程具身任务中transformer内存效率问题**

**关键词**: `具身智能` `强化学习` `transformer架构` `内存效率` `长时程任务`

## 📋 核心要点

1. 核心问题：transformer在具身决策中视觉输入易超上下文限制，需高效记忆机制
2. 方法要点：引入周期性摘要令牌，在训练中集成记忆创建与检索
3. 实验或效果：在网格世界和室内导航任务中优于基线，提升计算效率与泛化能力

## 📄 摘要（原文）

> To enable embodied agents to operate effectively over extended timeframes, it
> is crucial to develop models that form and access memories to stay
> contextualized in their environment. In the current paradigm of training
> transformer-based policies for embodied sequential decision-making tasks,
> visual inputs often overwhelm the context limits of transformers, while humans
> can maintain and utilize a lifetime of experience compressed as memories.
> Significant compression is possible in principle, as much of the input is
> irrelevant and can be abstracted. However, existing approaches predominantly
> focus on either recurrent models with fixed-size memory or transformers with
> full-context reliance. In this work, we propose Memo, a transformer-based
> architecture and training recipe for reinforcement learning (RL) on
> memory-intensive, long-horizon tasks. Memo incorporates the creation and
> retrieval of memory by interleaving periodic summarization tokens with the
> inputs of a model during training. We demonstrate Memo's effectiveness on a
> gridworld meta-RL benchmark and a multi-object navigation task in
> photo-realistic indoor settings. Memo outperforms naive long-context
> transformer baselines while being more compute and storage efficient.
> Additionally, Memo generalizes better to longer contexts at inference time and
> remains robust in streaming settings, where historical context must be
> truncated to fit inference constraints.

