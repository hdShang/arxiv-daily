---
layout: default
title: Simultaneous Genetic Evolution of Neural Networks for Optimal SFC Embedding
---

# Simultaneous Genetic Evolution of Neural Networks for Optimal SFC Embedding

**arXiv**: [2512.09318v1](https://arxiv.org/abs/2512.09318) | [PDF](https://arxiv.org/pdf/2512.09318.pdf)

**作者**: Theviyanthan Krishnamohan, Lauritz Thamsen, Paul Harvey

---

## 💡 一句话要点

**提出GENESIS遗传算法，通过进化三个神经网络同时优化SFC嵌入的三个子问题。**

**关键词**: `服务功能链嵌入` `遗传算法` `神经网络进化` `NP难优化` `数据中心网络`

## 📋 核心要点

1. 核心问题：SFC最优嵌入是NP难问题，需同时优化链组合、VNF嵌入和链路嵌入三个子问题。
2. 方法要点：GENESIS进化三个正弦激活神经网络，输出经高斯分布和A*算法处理，实现同时优化。
3. 实验或效果：在48个数据中心场景中，GENESIS实现100%最优解，且速度最快，平均15.84分钟。

## 📄 摘要（原文）

> The reliance of organisations on computer networks is enabled by network programmability, which is typically achieved through Service Function Chaining. These chains virtualise network functions, link them, and programmatically embed them on networking infrastructure. Optimal embedding of Service Function Chains is an NP-hard problem, with three sub-problems, chain composition, virtual network function embedding, and link embedding, that have to be optimised simultaneously, rather than sequentially, for optimal results. Genetic Algorithms have been employed for this, but existing approaches either do not optimise all three sub-problems or do not optimise all three sub-problems simultaneously. We propose a Genetic Algorithm-based approach called GENESIS, which evolves three sine-function-activated Neural Networks, and funnels their output to a Gaussian distribution and an A* algorithm to optimise all three sub-problems simultaneously. We evaluate GENESIS on an emulator across 48 different data centre scenarios and compare its performance to two state-of-the-art Genetic Algorithms and one greedy algorithm. GENESIS produces an optimal solution for 100% of the scenarios, whereas the second-best method optimises only 71% of the scenarios. Moreover, GENESIS is the fastest among all Genetic Algorithms, averaging 15.84 minutes, compared to an average of 38.62 minutes for the second-best Genetic Algorithm.

