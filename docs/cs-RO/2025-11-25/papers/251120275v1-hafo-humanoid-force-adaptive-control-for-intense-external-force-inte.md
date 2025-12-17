---
layout: default
title: HAFO: Humanoid Force-Adaptive Control for Intense External Force Interaction Environments
---

# HAFO: Humanoid Force-Adaptive Control for Intense External Force Interaction Environments

**arXiv**: [2511.20275v1](https://arxiv.org/abs/2511.20275) | [PDF](https://arxiv.org/pdf/2511.20275.pdf)

**作者**: Chenhui Dong, Haozhe Xu, Wenhao Feng, Zhipeng Wang, Yanmin Zhou, Yifei Zhao, Bin He

---

## 💡 一句话要点

**提出HAFO双智能体强化学习框架以解决人形机器人在强外力交互环境中的鲁棒控制问题**

**关键词**: `人形机器人控制` `强化学习` `外力交互` `双智能体框架` `弹簧-阻尼系统`

## 📋 核心要点

1. 核心问题：强化学习控制器在强外力交互下难以实现鲁棒精确运动
2. 方法要点：使用双智能体框架耦合训练，通过弹簧-阻尼系统建模外力实现精细力控
3. 实验或效果：在多种强外力交互中实现稳定控制，负载任务表现优异

## 📄 摘要（原文）

> Reinforcement learning controllers have made impressive progress in humanoid locomotion and light load manipulation. However, achieving robust and precise motion with strong force interaction remains a significant challenge. Based on the above limitations, this paper proposes HAFO, a dual-agent reinforcement learning control framework that simultaneously optimizes both a robust locomotion strategy and a precise upper-body manipulation strategy through coupled training under external force interaction environments. Simultaneously, we explicitly model the external pulling disturbances through a spring-damper system and achieve fine-grained force control by manipulating the virtual spring. During this process, the reinforcement-learning policy spontaneously generates disturbance-rejection response by exploiting environmental feedback. Moreover, HAFO employs an asymmetric Actor-Critic framework in which the Critic-network access to privileged spring-damping forces guides the actor-network to learn a generalizable, robust policy for resisting external disturbances. The experimental results demonstrate that HAFO achieves stable control of humanoid robot under various strong force interactions, showing remarkable performance in load tasks and ensuring stable robot operation under rope tension disturbances. Project website: hafo-robot.github.io.

