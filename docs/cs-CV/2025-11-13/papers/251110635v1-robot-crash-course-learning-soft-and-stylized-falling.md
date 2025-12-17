---
layout: default
title: Robot Crash Course: Learning Soft and Stylized Falling
---

# Robot Crash Course: Learning Soft and Stylized Falling

**arXiv**: [2511.10635v1](https://arxiv.org/abs/2511.10635) | [PDF](https://arxiv.org/pdf/2511.10635.pdf)

**作者**: Pascal Strauch, David Müller, Sammy Christen, Agon Serifi, Ruben Grandia, Espen Knoop, Moritz Bächer

---

## 💡 一句话要点

**提出机器人无关奖励函数以实现受控软着陆，减少物理损伤并控制最终姿态。**

**关键词**: `机器人跌倒控制` `强化学习奖励函数` `姿态控制` `物理损伤减少` `模拟采样策略`

## 📋 核心要点

1. 核心问题：双足机器人在现实世界中易跌倒，现有研究多关注预防而非跌倒本身。
2. 方法要点：通过强化学习平衡目标姿态、冲击最小化和关键部件保护。
3. 实验或效果：模拟与真实实验验证双足机器人可实现受控软着陆。

## 📄 摘要（原文）

> Despite recent advances in robust locomotion, bipedal robots operating in the real world remain at risk of falling. While most research focuses on preventing such events, we instead concentrate on the phenomenon of falling itself. Specifically, we aim to reduce physical damage to the robot while providing users with control over a robot's end pose. To this end, we propose a robot agnostic reward function that balances the achievement of a desired end pose with impact minimization and the protection of critical robot parts during reinforcement learning. To make the policy robust to a broad range of initial falling conditions and to enable the specification of an arbitrary and unseen end pose at inference time, we introduce a simulation-based sampling strategy of initial and end poses. Through simulated and real-world experiments, our work demonstrates that even bipedal robots can perform controlled, soft falls.

