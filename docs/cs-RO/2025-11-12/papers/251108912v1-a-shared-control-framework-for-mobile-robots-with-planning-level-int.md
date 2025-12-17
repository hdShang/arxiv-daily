---
layout: default
title: A Shared Control Framework for Mobile Robots with Planning-Level Intention Prediction
---

# A Shared Control Framework for Mobile Robots with Planning-Level Intention Prediction

**arXiv**: [2511.08912v1](https://arxiv.org/abs/2511.08912) | [PDF](https://arxiv.org/pdf/2511.08912.pdf)

**作者**: Jinyu Zhang, Lijun Han, Feng Jian, Lingxi Zhang, Hesheng Wang

---

## 💡 一句话要点

**提出基于规划级意图预测的共享控制框架，以提升移动机器人人机协作性能**

**关键词**: `共享控制` `意图预测` `路径重规划` `深度强化学习` `人机协作` `移动机器人`

## 📋 核心要点

1. 核心问题：移动机器人共享控制中，准确理解人类运动意图对协作至关重要
2. 方法要点：引入意图域概念，通过马尔可夫决策过程和深度强化学习联合优化意图预测与路径重规划
3. 实验或效果：仿真和真实用户研究表明，显著降低操作负荷并提高安全性，任务效率未受影响

## 📄 摘要（原文）

> In mobile robot shared control, effectively understanding human motion intention is critical for seamless human-robot collaboration. This paper presents a novel shared control framework featuring planning-level intention prediction. A path replanning algorithm is designed to adjust the robot's desired trajectory according to inferred human intentions. To represent future motion intentions, we introduce the concept of an intention domain, which serves as a constraint for path replanning. The intention-domain prediction and path replanning problems are jointly formulated as a Markov Decision Process and solved through deep reinforcement learning. In addition, a Voronoi-based human trajectory generation algorithm is developed, allowing the model to be trained entirely in simulation without human participation or demonstration data. Extensive simulations and real-world user studies demonstrate that the proposed method significantly reduces operator workload and enhances safety, without compromising task efficiency compared with existing assistive teleoperation approaches.

