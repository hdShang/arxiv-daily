---
layout: default
title: Agentic Policy Optimization via Instruction-Policy Co-Evolution
---

# Agentic Policy Optimization via Instruction-Policy Co-Evolution

**arXiv**: [2512.01945v1](https://arxiv.org/abs/2512.01945) | [PDF](https://arxiv.org/pdf/2512.01945.pdf)

**作者**: Han Zhou, Xingchen Wan, Ivan Vulić, Anna Korhonen

---

## 💡 一句话要点

**提出INSPO框架，通过指令-策略协同进化优化强化学习中的指令设计**

**关键词**: `强化学习` `指令优化` `协同进化` `多轮推理` `语言模型`

## 📋 核心要点

1. 核心问题：静态指令在强化学习中可能限制模型性能，需动态优化以适应策略改进
2. 方法要点：INSPO集成指令优化到RL循环，通过种群采样、奖励归因和反思机制生成新指令
3. 实验或效果：在多轮检索和推理任务中显著超越静态指令基线，性能提升显著且计算开销小

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the reasoning capability of large language models (LLMs), enabling autonomous agents that can conduct effective multi-turn and tool-integrated reasoning. While instructions serve as the primary protocol for defining agents, RLVR typically relies on static and manually designed instructions. However, those instructions may be suboptimal for the base model, and the optimal instruction may change as the agent's policy improves and explores the interaction with the environment. To bridge the gap, we introduce INSPO, a novel Instruction-Policy co-evolution framework that integrates instruction optimization as a dynamic component of the reinforcement learning (RL) loop. INSPO maintains a dynamic population of instruction candidates that are sampled with questions, where reward signals in RL loops are automatically attributed to each instruction, and low performers are periodically pruned. New instructions are generated and verified through an on-policy reflection mechanism, where an LLM-based optimizer analyzes past experience from a replay buffer and evolves more effective strategies given the current policy. We conduct extensive experiments on multi-turn retrieval and reasoning tasks, demonstrating that INSPO substantially outperforms strong baselines relying on static instructions. INSPO discovers innovative instructions that guide the agent toward more strategic reasoning paths, achieving substantial performance gains with only a marginal increase in computational overhead.

