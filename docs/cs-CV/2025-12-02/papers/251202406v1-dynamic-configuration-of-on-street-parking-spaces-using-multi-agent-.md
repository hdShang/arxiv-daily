---
layout: default
title: Dynamic Configuration of On-Street Parking Spaces using Multi Agent Reinforcement Learning
---

# Dynamic Configuration of On-Street Parking Spaces using Multi Agent Reinforcement Learning

**arXiv**: [2512.02406v1](https://arxiv.org/abs/2512.02406) | [PDF](https://arxiv.org/pdf/2512.02406.pdf)

**作者**: Oshada Jayasinghe, Farhana Choudhury, Egemen Tanin, Shanika Karunasekera

---

## 💡 一句话要点

**提出基于多智能体强化学习的动态路边停车位配置框架以减少交通拥堵**

**关键词**: `多智能体强化学习` `动态停车配置` `交通拥堵缓解` `图注意力网络` `SUMO仿真`

## 📋 核心要点

1. 核心问题：路边停车占用道路宽度，加剧城市交通拥堵，需动态优化停车位配置。
2. 方法要点：采用双层多智能体强化学习框架，结合LSTM和图注意力网络捕捉时空相关性。
3. 实验或效果：在SUMO仿真中，平均旅行时间损失减少高达47%，步行距离增加可忽略。

## 📄 摘要（原文）

> With increased travelling needs more than ever, traffic congestion has become a major concern in most urban areas. Allocating spaces for on-street parking, further hinders traffic flow, by limiting the effective road width available for driving. With the advancement of vehicle-to-infrastructure connectivity technologies, we explore how the impact of on-street parking on traffic congestion could be minimized, by dynamically configuring on-street parking spaces. Towards that end, we formulate dynamic on-street parking space configuration as an optimization problem, and we follow a data driven approach, considering the nature of our problem. Our proposed solution comprises a two-layer multi agent reinforcement learning based framework, which is inherently scalable to large road networks. The lane level agents are responsible for deciding the optimal parking space configuration for each lane, and we introduce a novel Deep Q-learning architecture which effectively utilizes long short term memory networks and graph attention networks to capture the spatio-temporal correlations evident in the given problem. The block level agents control the actions of the lane level agents and maintain a sufficient level of parking around the block. We conduct a set of comprehensive experiments using SUMO, on both synthetic data as well as real-world data from the city of Melbourne. Our experiments show that the proposed framework could reduce the average travel time loss of vehicles significantly, reaching upto 47%, with a negligible increase in the walking distance for parking.

