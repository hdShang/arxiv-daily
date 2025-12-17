---
layout: default
title: The Agent Capability Problem: Predicting Solvability Through Information-Theoretic Bounds
---

# The Agent Capability Problem: Predicting Solvability Through Information-Theoretic Bounds

**arXiv**: [2512.07631v1](https://arxiv.org/abs/2512.07631) | [PDF](https://arxiv.org/pdf/2512.07631.pdf)

**作者**: Shahar Lutati

---

## 💡 一句话要点

**提出代理能力问题框架，通过信息论界限预测资源约束下任务可解性**

**关键词**: `代理能力问题` `信息论界限` `资源约束预测` `自主代理` `问题解决建模` `实验验证`

## 📋 核心要点

1. 核心问题：代理在资源约束下何时应投入资源以解决任务，避免无效搜索
2. 方法要点：将问题解决建模为信息获取，定义总信息需求与每步信息增益，推导有效成本界限
3. 实验或效果：验证预测与实际性能紧密匹配，优于贪婪和随机策略，泛化于LLM和代理工作流

## 📄 摘要（原文）

> When should an autonomous agent commit resources to a task? We introduce the Agent Capability Problem (ACP), a framework for predicting whether an agent can solve a problem under resource constraints. Rather than relying on empirical heuristics, ACP frames problem-solving as information acquisition: an agent requires $\Itotal$ bits to identify a solution and gains $\Istep$ bits per action at cost $\Cstep$, yielding an effective cost $\Ceff = (\Itotal/\Istep), \Cstep$ that predicts resource requirements before search. We prove that $\Ceff$ lower-bounds expected cost and provide tight probabilistic upper bounds. Experimental validation shows that ACP predictions closely track actual agent performance, consistently bounding search effort while improving efficiency over greedy and random strategies. The framework generalizes across LLM-based and agentic workflows, linking principles from active learning, Bayesian optimization, and reinforcement learning through a unified information-theoretic lens. \

