---
layout: default
title: Fed-SE: Federated Self-Evolution for Privacy-Constrained Multi-Environment LLM Agents
---

# Fed-SE: Federated Self-Evolution for Privacy-Constrained Multi-Environment LLM Agents

**arXiv**: [2512.08870v1](https://arxiv.org/abs/2512.08870) | [PDF](https://arxiv.org/pdf/2512.08870.pdf)

**作者**: Xiang Chen, Yuling Shi, Qizhen Lan, Yuchao Qiu, Xiaodong Gu

---

## 💡 一句话要点

**提出Fed-SE联邦自进化框架，以解决隐私约束下多环境LLM代理的梯度冲突与负迁移问题。**

**关键词**: `联邦学习` `大语言模型代理` `自进化` `隐私保护` `梯度冲突` `负迁移`

## 📋 核心要点

1. 核心问题：隐私限制下，LLM代理在多环境中的异质任务和稀疏奖励导致梯度冲突，阻碍联邦优化。
2. 方法要点：本地基于高回报轨迹进行参数高效微调，全局在低秩子空间聚合更新以解耦环境动态。
3. 实验效果：在五个异质环境中，Fed-SE相比联邦基线平均任务成功率提升约18%。

## 📄 摘要（原文）

> LLM agents are widely deployed in complex interactive tasks, yet privacy constraints often preclude centralized optimization and co-evolution across dynamic environments. While Federated Learning (FL) has proven effective on static datasets, its extension to the open-ended self-evolution of agents remains underexplored. Directly applying standard FL is challenging: heterogeneous tasks and sparse, trajectory-level rewards introduce severe gradient conflicts, destabilizing the global optimization process. To bridge this gap, we propose Fed-SE, a Federated Self-Evolution framework for LLM agents. Fed-SE establishes a local evolution-global aggregation paradigm. Locally, agents employ parameter-efficient fine-tuning on filtered, high-return trajectories to achieve stable gradient updates. Globally, Fed-SE aggregates updates within a low-rank subspace that disentangles environment-specific dynamics, effectively reducing negative transfer across clients. Experiments across five heterogeneous environments demonstrate that Fed-SE improves average task success rates by approximately 18% over federated baselines, validating its effectiveness in robust cross-environment knowledge transfer in privacy-constrained deployments.

