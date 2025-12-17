---
layout: default
title: ASTRO: Adaptive Stitching via Dynamics-Guided Trajectory Rollouts
---

# ASTRO: Adaptive Stitching via Dynamics-Guided Trajectory Rollouts

**arXiv**: [2511.23442v1](https://arxiv.org/abs/2511.23442) | [PDF](https://arxiv.org/pdf/2511.23442.pdf)

**作者**: Hang Yu, Di Zhang, Qiwei Du, Yanping Zhao, Hai Zhang, Guang Chen, Eduardo E. Veas, Junqiao Zhao

---

## 💡 一句话要点

**提出ASTRO框架以解决离线强化学习中轨迹拼接的分布局限和动态不一致问题。**

**关键词**: `离线强化学习` `轨迹拼接` `数据增强` `动态一致性` `时序距离表示` `Rollout Deviation Feedback`

## 📋 核心要点

1. 核心问题：离线强化学习中，次优和碎片化轨迹导致奖励传播困难，影响价值估计和政策性能。
2. 方法要点：学习时序距离表示识别可到达拼接目标，通过动态引导的拼接规划器自适应生成连接动作序列。
3. 实验或效果：在OGBench和D4RL基准测试中优于现有离线强化学习增强方法，提升政策学习效果。

## 📄 摘要（原文）

> Offline reinforcement learning (RL) enables agents to learn optimal policies from pre-collected datasets. However, datasets containing suboptimal and fragmented trajectories present challenges for reward propagation, resulting in inaccurate value estimation and degraded policy performance. While trajectory stitching via generative models offers a promising solution, existing augmentation methods frequently produce trajectories that are either confined to the support of the behavior policy or violate the underlying dynamics, thereby limiting their effectiveness for policy improvement. We propose ASTRO, a data augmentation framework that generates distributionally novel and dynamics-consistent trajectories for offline RL. ASTRO first learns a temporal-distance representation to identify distinct and reachable stitch targets. We then employ a dynamics-guided stitch planner that adaptively generates connecting action sequences via Rollout Deviation Feedback, defined as the gap between target state sequence and the actual arrived state sequence by executing predicted actions, to improve trajectory stitching's feasibility and reachability. This approach facilitates effective augmentation through stitching and ultimately enhances policy learning. ASTRO outperforms prior offline RL augmentation methods across various algorithms, achieving notable performance gain on the challenging OGBench suite and demonstrating consistent improvements on standard offline RL benchmarks such as D4RL.

