---
layout: default
title: RoboScape-R: Unified Reward-Observation World Models for Generalizable Robotics Training via RL
---

# RoboScape-R: Unified Reward-Observation World Models for Generalizable Robotics Training via RL

**arXiv**: [2512.03556v1](https://arxiv.org/abs/2512.03556) | [PDF](https://arxiv.org/pdf/2512.03556.pdf)

**作者**: Yinzhou Tang, Yu Shang, Yinuo Chen, Bingwen Wei, Xin Zhang, Shu'ang Yu, Liangzhi Shi, Chao Yu, Chen Gao, Wei Wu, Yong Li

---

## 💡 一句话要点

**提出RoboScape-R框架，利用世界模型作为通用环境代理以增强机器人策略的泛化能力。**

**关键词**: `世界模型` `强化学习` `机器人策略` `泛化训练` `内生奖励`

## 📋 核心要点

1. 核心问题：传统强化学习缺乏统一奖励信号，导致策略在多样化场景中泛化能力不足。
2. 方法要点：引入基于世界模型的内生奖励机制，从状态转移动态中生成通用奖励。
3. 实验或效果：在域外场景下平均性能提升37.5%，验证了框架的有效性和泛化优势。

## 📄 摘要（原文）

> Achieving generalizable embodied policies remains a key challenge. Traditional policy learning paradigms, including both Imitation Learning (IL) and Reinforcement Learning (RL), struggle to cultivate generalizability across diverse scenarios. While IL policies often overfit to specific expert trajectories, RL suffers from the inherent lack of a unified and general reward signal necessary for effective multi-scene generalization. We posit that the world model is uniquely capable of serving as a universal environment proxy to address this limitation. However, current world models primarily focus on their ability to predict observations and still rely on task-specific, handcrafted reward functions, thereby failing to provide a truly general training environment. Toward this problem, we propose RoboScape-R, a framework leveraging the world model to serve as a versatile, general-purpose proxy for the embodied environment within the RL paradigm. We introduce a novel world model-based general reward mechanism that generates ''endogenous'' rewards derived from the model's intrinsic understanding of real-world state transition dynamics. Extensive experiments demonstrate that RoboScape-R effectively addresses the limitations of traditional RL methods by providing an efficient and general training environment that substantially enhances the generalization capability of embodied policies. Our approach offers critical insights into utilizing the world model as an online training strategy and achieves an average 37.5% performance improvement over baselines under out-of-domain scenarios.

