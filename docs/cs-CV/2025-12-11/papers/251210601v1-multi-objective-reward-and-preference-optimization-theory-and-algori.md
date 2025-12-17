---
layout: default
title: Multi-Objective Reward and Preference Optimization: Theory and Algorithms
---

# Multi-Objective Reward and Preference Optimization: Theory and Algorithms

**arXiv**: [2512.10601v1](https://arxiv.org/abs/2512.10601) | [PDF](https://arxiv.org/pdf/2512.10601.pdf)

**作者**: Akhil Agnihotri

---

## 💡 一句话要点

**提出多目标奖励与偏好优化理论及算法，以推进约束强化学习在控制、偏好学习和大模型对齐中的应用。**

**关键词**: `约束强化学习` `偏好学习` `大模型对齐` `平均成本优化` `后验采样` `多目标优化`

## 📋 核心要点

1. 核心问题：约束强化学习在平均成本、有限时域和人类偏好学习中的理论与算法挑战。
2. 方法要点：开发ACPO、e-COP、warmPref-PS、PSPL和MOPO算法，结合敏感性分析、信任域更新和后验采样。
3. 实验或效果：算法在安全关键环境中实现理论保证、高效数据收集和可扩展性，适用于数十亿参数模型。

## 📄 摘要（原文）

> This thesis develops theoretical frameworks and algorithms that advance constrained reinforcement learning (RL) across control, preference learning, and alignment of large language models. The first contribution addresses constrained Markov Decision Processes (CMDPs) under the average-cost criterion through the Average-Constrained Policy Optimization (ACPO) algorithm. ACPO integrates sensitivity analysis with trust-region updates to ensure stable constraint handling, achieving state-of-the-art empirical performance with theoretical guarantees. Constrained RL is then extended to finite-horizon settings via e-COP, the first policy optimization method for episodic CMDPs. Built on an episodic policy difference lemma, e-COP offers provable performance, simplicity, and scalability in safety-critical environments. The thesis then investigates reinforcement learning from human preferences. warmPref-PS introduces a posterior sampling strategy for linear bandits that integrates offline preference data from heterogeneous raters into online learning. Explicit modeling of rater competence yields substantial regret reduction and more efficient data collection for RLHF. The PSPL algorithm further advances preference-based RL by jointly sampling reward models and transition dynamics from pairwise trajectory comparisons, providing Bayesian simple-regret guarantees and robust empirical identification of optimal policies. The final contribution applies these methods to large-scale model alignment. A multi-objective constrained optimization view yields MOPO, an iterative algorithm with closed-form updates that scales to multi-billion-parameter language models and remains robust across alignment settings. Collectively, the thesis unifies constrained RL across average-cost, episodic, and preference-driven paradigms, delivering theoretical advances and practical tools for safe and aligned decision-making.

