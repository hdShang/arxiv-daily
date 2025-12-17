---
layout: default
title: AgentBalance: Backbone-then-Topology Design for Cost-Effective Multi-Agent Systems under Budget Constraints
---

# AgentBalance: Backbone-then-Topology Design for Cost-Effective Multi-Agent Systems under Budget Constraints

**arXiv**: [2512.11426v1](https://arxiv.org/abs/2512.11426) | [PDF](https://arxiv.org/pdf/2512.11426.pdf)

**作者**: Shuowei Cai, Yansong Ning, Hao Liu

---

## 💡 一句话要点

**提出AgentBalance框架，通过先骨干后拓扑设计，在预算约束下构建成本效益高的多智能体系统。**

**关键词**: `多智能体系统` `成本效益优化` `预算约束` `骨干选择` `拓扑设计` `延迟感知`

## 📋 核心要点

1. 核心问题：现有多智能体系统在显式令牌成本和延迟预算下设计不足，导致成本效益低。
2. 方法要点：先基于LLM池构建异构骨干智能体，再通过表示学习和延迟感知合成自适应通信拓扑。
3. 实验效果：在匹配预算下性能提升达10%和22%，并作为插件提升现有系统性能。

## 📄 摘要（原文）

> Large Language Model (LLM)-based multi-agent systems (MAS) are becoming indispensable building blocks for web-scale applications such as web search, social network analytics, and online customer support, where cost-effectiveness is increasingly the primary constraint for large-scale deployment. While recent work improves MAS cost-effectiveness by shaping inter-agent communication topologies and selecting agent backbones, it rarely models and optimizes under explicit token-cost and latency budgets that reflect deployment constraints. This often leads to topology-first designs and suboptimal cost-effectiveness when budgets are binding. We present AgentBalance, a framework for constructing cost-effective MAS under explicit token-cost and latency budgets via a backbone-then-topology design. AgentBalance first performs backbone-oriented agent generation, constructing agents with heterogeneous backbones through LLM pool construction, pool selection, and role-backbone matching. It then performs adaptive MAS topology generation, guiding inter-agent communication via agent representation learning, gating, and latency-aware topology synthesis. Experiments on benchmarks with 14 candidate LLM backbones show that AgentBalance achieves up to 10% and 22% performance gains under matched token-cost and latency budgets, respectively, and yields strong AUC on performance-versus-budget curves across benchmarks. AgentBalance also functions as a plug-in for existing MAS, improving performance under the same token-cost and latency constraints, and it generalizes well to unseen LLMs for practical, budget-aware deployment. Code: https://github.com/usail-hkust/AgentBalance

