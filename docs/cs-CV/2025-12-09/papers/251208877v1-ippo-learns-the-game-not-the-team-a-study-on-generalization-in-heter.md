---
layout: default
title: IPPO Learns the Game, Not the Team: A Study on Generalization in Heterogeneous Agent Teams
---

# IPPO Learns the Game, Not the Team: A Study on Generalization in Heterogeneous Agent Teams

**arXiv**: [2512.08877v1](https://arxiv.org/abs/2512.08877) | [PDF](https://arxiv.org/pdf/2512.08877.pdf)

**作者**: Ryan LeRoy, Jack Kolb

---

## 💡 一句话要点

**提出旋转策略训练以研究异构多智能体团队中自学习PPO的泛化能力**

**关键词**: `多智能体强化学习` `异构智能体` `泛化能力` `自学习` `旋转策略训练` `PPO算法`

## 📋 核心要点

1. 核心问题：自学习PPO智能体是否学习基于游戏的通用协调策略，而非过拟合训练伙伴行为
2. 方法要点：引入旋转策略训练，在训练中轮换异构队友策略以暴露更广伙伴策略范围
3. 实验或效果：在HeMAC环境中，IPPO基线泛化至新队友算法，性能与RPT相似

## 📄 摘要（原文）

> Multi-Agent Reinforcement Learning (MARL) is commonly deployed in settings where agents are trained via self-play with homogeneous teammates, often using parameter sharing and a single policy architecture. This opens the question: to what extent do self-play PPO agents learn general coordination strategies grounded in the underlying game, compared to overfitting to their training partners' behaviors? This paper investigates the question using the Heterogeneous Multi-Agent Challenge (HeMAC) environment, which features distinct Observer and Drone agents with complementary capabilities. We introduce Rotating Policy Training (RPT), an approach that rotates heterogeneous teammate policies of different learning algorithms during training, to expose the agent to a broader range of partner strategies. When playing alongside a withheld teammate policy (DDQN), we find that RPT achieves similar performance to a standard self-play baseline, IPPO, where all agents were trained sharing a single PPO policy. This result indicates that in this heterogeneous multi-agent setting, the IPPO baseline generalizes to novel teammate algorithms despite not experiencing teammate diversity during training. This shows that a simple IPPO baseline may possess the level of generalization to novel teammates that a diverse training regimen was designed to achieve.

