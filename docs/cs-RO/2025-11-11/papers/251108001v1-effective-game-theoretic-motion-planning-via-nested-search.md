---
layout: default
title: Effective Game-Theoretic Motion Planning via Nested Search
---

# Effective Game-Theoretic Motion Planning via Nested Search

**arXiv**: [2511.08001v1](https://arxiv.org/abs/2511.08001) | [PDF](https://arxiv.org/pdf/2511.08001.pdf)

**作者**: Avishav Engle, Andrey Zhitnikov, Oren Salzman, Omer Ben-Porat, Kiril Solovey

---

## 💡 一句话要点

**提出GTNS方法以高效计算多智能体交互中的纳什均衡**

**关键词**: `博弈论规划` `纳什均衡计算` `多智能体交互` `嵌套搜索算法` `自动驾驶决策`

## 📋 核心要点

1. 现有方法因简化动力学或枚举轨迹而难以扩展和避免局部最优
2. GTNS通过嵌套搜索高效筛选动作空间，确保无单边偏离约束
3. 在自动驾驶场景中实现秒级求解，支持用户指定目标选择均衡

## 📄 摘要（原文）

> To facilitate effective, safe deployment in the real world, individual robots must reason about interactions with other agents, which often occur without explicit communication. Recent work has identified game theory, particularly the concept of Nash Equilibrium (NE), as a key enabler for behavior-aware decision-making. Yet, existing work falls short of fully unleashing the power of game-theoretic reasoning. Specifically, popular optimization-based methods require simplified robot dynamics and tend to get trapped in local minima due to convexification. Other works that rely on payoff matrices suffer from poor scalability due to the explicit enumeration of all possible trajectories. To bridge this gap, we introduce Game-Theoretic Nested Search (GTNS), a novel, scalable, and provably correct approach for computing NEs in general dynamical systems. GTNS efficiently searches the action space of all agents involved, while discarding trajectories that violate the NE constraint (no unilateral deviation) through an inner search over a lower-dimensional space. Our algorithm enables explicit selection among equilibria by utilizing a user-specified global objective, thereby capturing a rich set of realistic interactions. We demonstrate the approach on a variety of autonomous driving and racing scenarios where we achieve solutions in mere seconds on commodity hardware.

