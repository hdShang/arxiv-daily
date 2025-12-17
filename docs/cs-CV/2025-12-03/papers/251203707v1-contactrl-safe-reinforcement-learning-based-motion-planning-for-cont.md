---
layout: default
title: ContactRL: Safe Reinforcement Learning based Motion Planning for Contact based Human Robot Collaboration
---

# ContactRL: Safe Reinforcement Learning based Motion Planning for Contact based Human Robot Collaboration

**arXiv**: [2512.03707v1](https://arxiv.org/abs/2512.03707) | [PDF](https://arxiv.org/pdf/2512.03707.pdf)

**作者**: Sundas Rafat Mulkana, Ronyu Yu, Tanaya Guha, Emma Li

---

## 💡 一句话要点

**提出ContactRL框架，通过力反馈奖励实现人机协作中的安全接触运动规划。**

**关键词**: `人机协作` `强化学习` `运动规划` `接触安全` `控制屏障函数` `力反馈`

## 📋 核心要点

1. 核心问题：人机协作需确保安全物理接触，避免碰撞并最小化接触力。
2. 方法要点：基于强化学习，将接触安全融入奖励函数，结合控制屏障函数保障部署安全。
3. 实验或效果：仿真中安全违规率0.2%，任务成功率87.7%；真实实验接触力低于10N，验证安全高效协作。

## 📄 摘要（原文）

> In collaborative human-robot tasks, safety requires not only avoiding collisions but also ensuring safe, intentional physical contact. We present ContactRL, a reinforcement learning (RL) based framework that directly incorporates contact safety into the reward function through force feedback. This enables a robot to learn adaptive motion profiles that minimize human-robot contact forces while maintaining task efficiency. In simulation, ContactRL achieves a low safety violation rate of 0.2\% with a high task success rate of 87.7\%, outperforming state-of-the-art constrained RL baselines. In order to guarantee deployment safety, we augment the learned policy with a kinetic energy based Control Barrier Function (eCBF) shield. Real-world experiments on an UR3e robotic platform performing small object handovers from a human hand across 360 trials confirm safe contact, with measured normal forces consistently below 10N. These results demonstrate that ContactRL enables safe and efficient physical collaboration, thereby advancing the deployment of collaborative robots in contact-rich tasks.

