---
layout: default
title: Subgoal Graph-Augmented Planning for LLM-Guided Open-World Reinforcement Learning
---

# Subgoal Graph-Augmented Planning for LLM-Guided Open-World Reinforcement Learning

**arXiv**: [2511.20993v1](https://arxiv.org/abs/2511.20993) | [PDF](https://arxiv.org/pdf/2511.20993.pdf)

**作者**: Shanwei Fan

---

## 💡 一句话要点

**提出SGA-ACR框架以解决LLM在开放世界强化学习中的规划-执行对齐问题**

**关键词**: `强化学习` `大语言模型` `子目标规划` `规划-执行对齐` `开放世界环境`

## 📋 核心要点

1. 核心问题：LLM生成的子目标语义合理但环境不可行，且规划过程缺乏自验证导致不可靠
2. 方法要点：集成环境特定子目标图和结构化知识，采用多LLM管道分离生成、批判和精炼
3. 实验或效果：在22个开放世界游戏任务中验证了方法的有效性

## 📄 摘要（原文）

> Large language models (LLMs) offer strong high-level planning capabilities for reinforcement learning (RL) by decomposing tasks into subgoals. However, their practical utility is limited by poor planning-execution alignment, which reflects a critical gap between abstract plans and actionable, environment-compatible behaviors. This misalignment arises from two interrelated limitations: (1) LLMs often produce subgoals that are semantically plausible but infeasible or irrelevant in the target environment due to insufficient grounding in environment-specific knowledge, and (2) single-LLM planning conflates generation with self-verification, resulting in overconfident yet unreliable subgoals that frequently fail during execution. To address these challenges, we propose Subgoal Graph-Augmented Actor-Critic-Refiner (SGA-ACR), a framework that integrates an environment-specific subgoal graph and structured entity knowledge with a multi-LLM planning pipeline that explicitly separates generation, critique, and refinement to produce executable and verifiable subgoals. A subgoal tracker further monitors execution progress, provides auxiliary rewards, and adaptively updates the subgoal graph to maintain alignment between plans and actions. Experimental results on 22 diverse tasks in the open-world game "Crafter" demonstrate the effectiveness of our proposed method.

