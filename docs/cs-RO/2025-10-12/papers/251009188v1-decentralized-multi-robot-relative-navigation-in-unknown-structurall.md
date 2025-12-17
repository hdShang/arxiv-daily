---
layout: default
title: Decentralized Multi-Robot Relative Navigation in Unknown, Structurally Constrained Environments under Limited Communication
---

# Decentralized Multi-Robot Relative Navigation in Unknown, Structurally Constrained Environments under Limited Communication

**arXiv**: [2510.09188v1](https://arxiv.org/abs/2510.09188) | [PDF](https://arxiv.org/pdf/2510.09188.pdf)

**作者**: Zihao Mao, Yunheng Wang, Yunting Ji, Yi Yang, Wenjie Song

---

## 💡 一句话要点

**提出去中心化分层相对导航框架，解决未知结构约束环境中多机器人导航问题。**

**关键词**: `多机器人导航` `去中心化系统` `相对导航` `拓扑地图` `实时轨迹规划` `通信受限环境`

## 📋 核心要点

1. 核心问题：未知GPS缺失环境中多机器人导航，需平衡全局策略与局部敏捷性，通信受限。
2. 方法要点：分层框架，战略层交换拓扑地图，战术层实时生成可行轨迹。
3. 实验效果：仿真与真实实验显示，在通信受限复杂环境中成功率和效率显著提升。

## 📄 摘要（原文）

> Multi-robot navigation in unknown, structurally constrained, and GPS-denied
> environments presents a fundamental trade-off between global strategic
> foresight and local tactical agility, particularly under limited communication.
> Centralized methods achieve global optimality but suffer from high
> communication overhead, while distributed methods are efficient but lack the
> broader awareness to avoid deadlocks and topological traps. To address this, we
> propose a fully decentralized, hierarchical relative navigation framework that
> achieves both strategic foresight and tactical agility without a unified
> coordinate system. At the strategic layer, robots build and exchange
> lightweight topological maps upon opportunistic encounters. This process
> fosters an emergent global awareness, enabling the planning of efficient,
> trap-avoiding routes at an abstract level. This high-level plan then inspires
> the tactical layer, which operates on local metric information. Here, a
> sampling-based escape point strategy resolves dense spatio-temporal conflicts
> by generating dynamically feasible trajectories in real time, concurrently
> satisfying tight environmental and kinodynamic constraints. Extensive
> simulations and real-world experiments demonstrate that our system
> significantly outperforms in success rate and efficiency, especially in
> communication-limited environments with complex topological structures.

