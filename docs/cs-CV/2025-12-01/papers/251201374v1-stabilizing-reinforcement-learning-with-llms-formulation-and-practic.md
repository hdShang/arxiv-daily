---
layout: default
title: Stabilizing Reinforcement Learning with LLMs: Formulation and Practices
---

# Stabilizing Reinforcement Learning with LLMs: Formulation and Practices

**arXiv**: [2512.01374v1](https://arxiv.org/abs/2512.01374) | [PDF](https://arxiv.org/pdf/2512.01374.pdf)

**作者**: Chujie Zheng, Kai Dang, Bowen Yu, Mingze Li, Huiqiang Jiang, Junrong Lin, Yuqiong Liu, An Yang, Jingren Zhou, Junyang Lin

---

## 💡 一句话要点

**提出基于大语言模型的强化学习稳定化公式，解释并实践优化策略梯度训练的方法。**

**关键词**: `强化学习` `大语言模型` `策略梯度` `训练稳定性` `混合专家模型` `路由重播`

## 📋 核心要点

1. 核心问题：强化学习中真实序列级奖励难以直接优化，需通过代理令牌级目标近似，但训练-推断差异和策略陈旧性导致不稳定。
2. 方法要点：通过一阶近似推导，最小化训练-推断差异和策略陈旧性时，代理目标有效，并解释重要性采样校正、裁剪和路由重播等稳定技术。
3. 实验或效果：在30B混合专家模型上实验，展示稳定化后训练性能一致，提供稳定训练配方。

## 📄 摘要（原文）

> This paper proposes a novel formulation for reinforcement learning (RL) with large language models, explaining why and under what conditions the true sequence-level reward can be optimized via a surrogate token-level objective in policy gradient methods such as REINFORCE. Specifically, through a first-order approximation, we show that this surrogate becomes increasingly valid only when both the training-inference discrepancy and policy staleness are minimized. This insight provides a principled explanation for the crucial role of several widely adopted techniques in stabilizing RL training, including importance sampling correction, clipping, and particularly Routing Replay for Mixture-of-Experts (MoE) models. Through extensive experiments with a 30B MoE model totaling hundreds of thousands of GPU hours, we show that for on-policy training, the basic policy gradient algorithm with importance sampling correction achieves the highest training stability. When off-policy updates are introduced to accelerate convergence, combining clipping and Routing Replay becomes essential to mitigate the instability caused by policy staleness. Notably, once training is stabilized, prolonged optimization consistently yields comparable final performance regardless of cold-start initialization. We hope that the shared insights and the developed recipes for stable RL training will facilitate future research.

