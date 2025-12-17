---
layout: default
title: On Mobile Ad Hoc Networks for Coverage of Partially Observable Worlds
---

# On Mobile Ad Hoc Networks for Coverage of Partially Observable Worlds

**arXiv**: [2512.09495v1](https://arxiv.org/abs/2512.09495) | [PDF](https://arxiv.org/pdf/2512.09495.pdf)

**作者**: Edwin Meriaux, Shuo Wen, Louis-Roy Langevin, Doina Precup, Antonio Loría, Gregory Dudek

---

## 💡 一句话要点

**提出POCGAGP模型及CADENCE与DADENCE算法，以解决未知环境中移动代理的覆盖与连通网络构建问题。**

**关键词**: `移动自组织网络` `部分可观测覆盖` `计算几何模型` `分布式算法` `通信驱动探索`

## 📋 核心要点

1. 核心问题：在部分可观测的未知环境中，移动代理如何部署以实现空间覆盖和通信网络连通。
2. 方法要点：基于计算几何框架，引入POCGAGP模型，开发集中式CADENCE和分布式DADENCE算法。
3. 实验或效果：在1,500个模拟测试中，算法成功构建连通网络，覆盖未知空间，分布式方法性能接近集中式。

## 📄 摘要（原文）

> This paper addresses the movement and placement of mobile agents to establish a communication network in initially unknown environments. We cast the problem in a computational-geometric framework by relating the coverage problem and line-of-sight constraints to the Cooperative Guard Art Gallery Problem, and introduce its partially observable variant, the Partially Observable Cooperative Guard Art Gallery Problem (POCGAGP). We then present two algorithms that solve POCGAGP: CADENCE, a centralized planner that incrementally selects 270 degree corners at which to deploy agents, and DADENCE, a decentralized scheme that coordinates agents using local information and lightweight messaging. Both approaches operate under partial observability and target simultaneous coverage and connectivity. We evaluate the methods in simulation across 1,500 test cases of varied size and structure, demonstrating consistent success in forming connected networks while covering and exploring unknown space. These results highlight the value of geometric abstractions for communication-driven exploration and show that decentralized policies are competitive with centralized performance while retaining scalability.

