---
layout: default
title: Multi-Objective Reinforcement Learning for Large-Scale Mixed Traffic Control
---

# Multi-Objective Reinforcement Learning for Large-Scale Mixed Traffic Control

**arXiv**: [2512.11247v1](https://arxiv.org/abs/2512.11247) | [PDF](https://arxiv.org/pdf/2512.11247.pdf)

**作者**: Iftekharul Islam, Weizi Li

---

## 💡 一句话要点

**提出多目标强化学习与战略路由的混合交通控制框架，以提升公平性、安全性和效率。**

**关键词**: `混合交通控制` `多目标强化学习` `战略路由` `公平性优化` `冲突避免`

## 📋 核心要点

1. 核心问题：现有方法缺乏公平性机制，导致低需求车辆服务不足。
2. 方法要点：结合多目标强化学习进行局部控制，引入冲突威胁向量和队列均等惩罚。
3. 实验或效果：在真实网络中显著减少等待时间、饥饿和冲突率，同时保持燃油效率。

## 📄 摘要（原文）

> Effective mixed traffic control requires balancing efficiency, fairness, and safety. Existing approaches excel at optimizing efficiency and enforcing safety constraints but lack mechanisms to ensure equitable service, resulting in systematic starvation of vehicles on low-demand approaches. We propose a hierarchical framework combining multi-objective reinforcement learning for local intersection control with strategic routing for network-level coordination. Our approach introduces a Conflict Threat Vector that provides agents with explicit risk signals for proactive conflict avoidance, and a queue parity penalty that ensures equitable service across all traffic streams. Extensive experiments on a real-world network across different robot vehicle (RV) penetration rates demonstrate substantial improvements: up to 53% reductions in average wait time, up to 86% reductions in maximum starvation, and up to 86\% reduction in conflict rate compared to baselines, while maintaining fuel efficiency. Our analysis reveals that strategic routing effectiveness scales with RV penetration, becoming increasingly valuable at higher autonomy levels. The results demonstrate that multi-objective optimization through well-curated reward functions paired with strategic RV routing yields significant benefits in fairness and safety metrics critical for equitable mixed-autonomy deployment.

