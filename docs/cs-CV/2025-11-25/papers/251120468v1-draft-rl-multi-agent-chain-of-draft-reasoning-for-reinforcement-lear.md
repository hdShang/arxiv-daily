---
layout: default
title: DRAFT-RL: Multi-Agent Chain-of-Draft Reasoning for Reinforcement Learning-Enhanced LLMs
---

# DRAFT-RL: Multi-Agent Chain-of-Draft Reasoning for Reinforcement Learning-Enhanced LLMs

**arXiv**: [2511.20468v1](https://arxiv.org/abs/2511.20468) | [PDF](https://arxiv.org/pdf/2511.20468.pdf)

**作者**: Yuanhao Li, Mingshan Liu, Hongbo Wang, Yiding Zhang, Yifei Ma, Wei Tan

---

## 💡 一句话要点

**提出DRAFT-RL框架，通过多代理草稿链推理增强LLMs在复杂任务中的性能**

**关键词**: `多代理强化学习` `草稿链推理` `大型语言模型` `复杂推理任务` `奖励模型优化`

## 📋 核心要点

1. 现有多代理反思框架依赖单次响应，推理探索缺乏结构多样性
2. DRAFT-RL集成草稿链推理，代理生成多草稿，通过同伴评估和奖励模型选择优化策略
3. 在代码合成、符号数学和知识问答任务中，准确性和收敛速度显著优于现有方法

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown impressive capabilities in multi-step reasoning and problem-solving.Recent works introduce multi-agent reflection frameworks where multiple LLM agents critique and refine each other's outputs using reinforcement learning (RL). However, these approaches often rely on single-shot responses and lack structural diversity in reasoning exploration. In this paper, we propose DRAFT-RL, a novel framework that integrates Chain-of-Draft (CoD) reasoning into multi-agent RL training. Instead of generating single responses, each agent produces multiple drafts per query, which are then evaluated by peer agents and a learned reward model to identify the most promising trajectory. These selected drafts are used to refine future reasoning strategies through actor-critic learning.DRAFT-RL enables explicit multi-path exploration, peer-guided reflection, and reward-aligned selection, resulting in more robust and interpretable LLM agent behavior. We evaluate our method on complex reasoning tasks including code synthesis, symbolic math, and knowledge-intensive QA,demonstrating that DRAFT-RL outperforms existing reflective and RL-based agents by significant margins in both accuracy and convergence speed

