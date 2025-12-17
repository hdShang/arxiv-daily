---
layout: default
title: Learning-based Cooperative Robotic Paper Wrapping: A Unified Control Policy with Residual Force Control
---

# Learning-based Cooperative Robotic Paper Wrapping: A Unified Control Policy with Residual Force Control

**arXiv**: [2511.03181v1](https://arxiv.org/abs/2511.03181) | [PDF](https://arxiv.org/pdf/2511.03181.pdf)

**作者**: Rewida Ali, Cristian C. Beltran-Hernandez, Weiwei Wan, Kensuke Harada

---

## 💡 一句话要点

**提出基于学习的统一控制策略，结合残差力控制，解决人机协作包装变形物体问题。**

**关键词**: `人机协作` `变形物体操作` `统一控制策略` `残差力控制` `长时程任务` `基于学习框架`

## 📋 核心要点

1. 核心问题：变形物体动态不可预测，需自适应力控制，实现长时程包装任务。
2. 方法要点：集成LLM任务规划与IL/RL策略，使用START模型捕获长程时序依赖。
3. 实验效果：真实世界包装任务成功率97%，统一策略减少专用模型需求。

## 📄 摘要（原文）

> Human-robot cooperation is essential in environments such as warehouses and
> retail stores, where workers frequently handle deformable objects like paper,
> bags, and fabrics. Coordinating robotic actions with human assistance remains
> difficult due to the unpredictable dynamics of deformable materials and the
> need for adaptive force control. To explore this challenge, we focus on the
> task of gift wrapping, which exemplifies a long-horizon manipulation problem
> involving precise folding, controlled creasing, and secure fixation of paper.
> Success is achieved when the robot completes the sequence to produce a neatly
> wrapped package with clean folds and no tears.
>   We propose a learning-based framework that integrates a high-level task
> planner powered by a large language model (LLM) with a low-level hybrid
> imitation learning (IL) and reinforcement learning (RL) policy. At its core is
> a Sub-task Aware Robotic Transformer (START) that learns a unified policy from
> human demonstrations. The key novelty lies in capturing long-range temporal
> dependencies across the full wrapping sequence within a single model. Unlike
> vanilla Action Chunking with Transformer (ACT), typically applied to short
> tasks, our method introduces sub-task IDs that provide explicit temporal
> grounding. This enables robust performance across the entire wrapping process
> and supports flexible execution, as the policy learns sub-goals rather than
> merely replicating motion sequences.
>   Our framework achieves a 97% success rate on real-world wrapping tasks. We
> show that the unified transformer-based policy reduces the need for specialized
> models, allows controlled human supervision, and effectively bridges high-level
> intent with the fine-grained force control required for deformable object
> manipulation.

