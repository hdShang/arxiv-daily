---
layout: default
title: Multi-Agent Reinforcement Learning with Communication-Constrained Priors
---

# Multi-Agent Reinforcement Learning with Communication-Constrained Priors

**arXiv**: [2512.03528v1](https://arxiv.org/abs/2512.03528) | [PDF](https://arxiv.org/pdf/2512.03528.pdf)

**作者**: Guang Yang, Tianpei Yang, Jingwen Qiao, Yanqing Wu, Jing Huo, Xingguo Chen, Yang Gao

---

## 💡 一句话要点

**提出通信约束先验模型以解决多智能体强化学习在损失通信场景下的鲁棒性问题**

**关键词**: `多智能体强化学习` `通信约束` `损失通信` `先验模型` `互信息估计` `分布式决策`

## 📋 核心要点

1. 核心问题：现实场景中损失通信普遍，现有方法在复杂动态环境中扩展性和鲁棒性不足
2. 方法要点：构建通用通信约束模型作为先验，区分损失与无损消息，并解耦其对决策的影响
3. 实验或效果：在多个通信约束基准上验证了方法的有效性，量化通信消息对全局奖励的影响

## 📄 摘要（原文）

> Communication is one of the effective means to improve the learning of cooperative policy in multi-agent systems. However, in most real-world scenarios, lossy communication is a prevalent issue. Existing multi-agent reinforcement learning with communication, due to their limited scalability and robustness, struggles to apply to complex and dynamic real-world environments. To address these challenges, we propose a generalized communication-constrained model to uniformly characterize communication conditions across different scenarios. Based on this, we utilize it as a learning prior to distinguish between lossy and lossless messages for specific scenarios. Additionally, we decouple the impact of lossy and lossless messages on distributed decision-making, drawing on a dual mutual information estimatior, and introduce a communication-constrained multi-agent reinforcement learning framework, quantifying the impact of communication messages into the global reward. Finally, we validate the effectiveness of our approach across several communication-constrained benchmarks.

