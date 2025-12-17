---
layout: default
title: Multistep Quasimetric Learning for Scalable Goal-conditioned Reinforcement Learning
---

# Multistep Quasimetric Learning for Scalable Goal-conditioned Reinforcement Learning

**arXiv**: [2511.07730v1](https://arxiv.org/abs/2511.07730) | [PDF](https://arxiv.org/pdf/2511.07730.pdf)

**作者**: Bill Chunyuan Zheng, Vivek Myers, Benjamin Eysenbach, Sergey Levine

---

## 💡 一句话要点

**提出多步拟度量学习以解决长视野目标条件强化学习中的距离估计问题**

**关键词**: `目标条件强化学习` `拟度量学习` `多步回报` `长视野任务` `机器人操作` `离线数据集`

## 📋 核心要点

1. 核心问题：长视野任务中估计观测对之间的时间距离，现有方法在最优性与性能间存在权衡
2. 方法要点：结合多步蒙特卡洛回报拟合拟度量距离，实现端到端目标条件强化学习
3. 实验或效果：在模拟任务中优于现有方法，并在真实机器人操作中实现多步拼接

## 📄 摘要（原文）

> Learning how to reach goals in an environment is a longstanding challenge in AI, yet reasoning over long horizons remains a challenge for modern methods. The key question is how to estimate the temporal distance between pairs of observations. While temporal difference methods leverage local updates to provide optimality guarantees, they often perform worse than Monte Carlo methods that perform global updates (e.g., with multi-step returns), which lack such guarantees. We show how these approaches can be integrated into a practical GCRL method that fits a quasimetric distance using a multistep Monte-Carlo return. We show our method outperforms existing GCRL methods on long-horizon simulated tasks with up to 4000 steps, even with visual observations. We also demonstrate that our method can enable stitching in the real-world robotic manipulation domain (Bridge setup). Our approach is the first end-to-end GCRL method that enables multistep stitching in this real-world manipulation domain from an unlabeled offline dataset of visual observations.

