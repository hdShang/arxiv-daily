---
layout: default
title: rSIM: Incentivizing Reasoning Capabilities of LLMs via Reinforced Strategy Injection
---

# rSIM: Incentivizing Reasoning Capabilities of LLMs via Reinforced Strategy Injection

**arXiv**: [2512.08300v1](https://arxiv.org/abs/2512.08300) | [PDF](https://arxiv.org/pdf/2512.08300.pdf)

**作者**: Sijia Chen, Baochun Li, Di Niu

---

## 💡 一句话要点

**提出强化策略注入机制，通过多智能体强化学习提升大语言模型推理能力。**

**关键词**: `强化学习` `推理语言模型` `多智能体系统` `策略注入` `链式思考` `通用规划器`

## 📋 核心要点

1. 核心问题：大语言模型在推理任务中缺乏策略性思考，如自我反思和深度思考。
2. 方法要点：使用小型规划器作为领导者智能体，通过强化学习自适应注入推理策略到链式思考中。
3. 实验或效果：rSIM使小模型性能超越大模型，规划器可通用化并支持持续学习。

## 📄 摘要（原文）

> Large language models (LLMs) are post-trained through reinforcement learning (RL) to evolve into Reasoning Language Models (RLMs), where the hallmark of this advanced reasoning is ``aha'' moments when they start to perform strategies, such as self-reflection and deep thinking, within chain of thoughts (CoTs). Motivated by this, this paper proposes a novel reinforced strategy injection mechanism (rSIM), that enables any LLM to become an RLM by employing a small planner to guide the LLM's CoT through the adaptive injection of reasoning strategies. To achieve this, the planner (leader agent) is jointly trained with an LLM (follower agent) using multi-agent RL (MARL), based on a leader-follower framework and straightforward rule-based rewards. Experimental results show that rSIM enables Qwen2.5-0.5B to become an RLM and significantly outperform Qwen2.5-14B. Moreover, the planner is generalizable: it only needs to be trained once and can be applied as a plug-in to substantially improve the reasoning capabilities of existing LLMs. In addition, the planner supports continual learning across various tasks, allowing its planning abilities to gradually improve and generalize to a wider range of problems.

