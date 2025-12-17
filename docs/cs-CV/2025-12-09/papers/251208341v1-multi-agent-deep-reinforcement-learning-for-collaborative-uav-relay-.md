---
layout: default
title: Multi-Agent Deep Reinforcement Learning for Collaborative UAV Relay Networks under Jamming Atatcks
---

# Multi-Agent Deep Reinforcement Learning for Collaborative UAV Relay Networks under Jamming Atatcks

**arXiv**: [2512.08341v1](https://arxiv.org/abs/2512.08341) | [PDF](https://arxiv.org/pdf/2512.08341.pdf)

**作者**: Thai Duong Nguyen, Ngoc-Tan Nguyen, Thanh-Dao Nguyen, Nguyen Van Huynh, Dinh-Hieu Tran, Symeon Chatzinotas

---

## 💡 一句话要点

**提出基于多智能体深度强化学习的协作无人机中继网络抗干扰方法**

**关键词**: `多智能体强化学习` `无人机中继网络` `抗干扰策略` `集中训练分散执行` `协作通信`

## 📋 核心要点

1. 核心问题：无人机群在干扰环境下需平衡吞吐量最大化、防碰撞和抗干扰等多目标动态优化
2. 方法要点：采用集中训练分散执行框架，通过全局状态指导局部决策，实现协作抗干扰
3. 实验或效果：仿真显示系统吞吐量提升约50%，碰撞率接近零，智能体自发学习抗干扰策略

## 📄 摘要（原文）

> The deployment of Unmanned Aerial Vehicle (UAV) swarms as dynamic communication relays is critical for next-generation tactical networks. However, operating in contested environments requires solving a complex trade-off, including maximizing system throughput while ensuring collision avoidance and resilience against adversarial jamming. Existing heuristic-based approaches often struggle to find effective solutions due to the dynamic and multi-objective nature of this problem. This paper formulates this challenge as a cooperative Multi-Agent Reinforcement Learning (MARL) problem, solved using the Centralized Training with Decentralized Execution (CTDE) framework. Our approach employs a centralized critic that uses global state information to guide decentralized actors which operate using only local observations. Simulation results show that our proposed framework significantly outperforms heuristic baselines, increasing the total system throughput by approximately 50% while simultaneously achieving a near-zero collision rate. A key finding is that the agents develop an emergent anti-jamming strategy without explicit programming. They learn to intelligently position themselves to balance the trade-off between mitigating interference from jammers and maintaining effective communication links with ground users.

