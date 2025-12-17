---
layout: default
title: Motion Planning for Safe Landing of a Human-Piloted Parafoil
---

# Motion Planning for Safe Landing of a Human-Piloted Parafoil

**arXiv**: [2512.10595v1](https://arxiv.org/abs/2512.10595) | [PDF](https://arxiv.org/pdf/2512.10595.pdf)

**作者**: Maximillian Fainkich, Kiril Solovey, Anna Clarke

---

## 💡 一句话要点

**提出基于采样运动规划的轨迹生成方法，以辅助人类飞行员安全降落滑翔伞。**

**关键词**: `运动规划` `滑翔伞降落` `安全轨迹` `采样算法` `训练模拟器`

## 📋 核心要点

1. 研究人类飞行员滑翔伞降落中的安全问题，缺乏有效训练模拟器。
2. 采用Stable Sparse RRT算法优化轨迹，最小化倾斜角以提升安全性。
3. 算法相比人类飞行数据，成本改善20%-80%，提供更平滑下降路径。

## 📄 摘要（原文）

> Most skydiving accidents occur during the parafoil-piloting and landing stages and result from human lapses in judgment while piloting the parafoil. Training of novice pilots is protracted due to the lack of functional and easily accessible training simulators. Moreover, work on parafoil trajectory planning suitable for aiding human training remains limited. To bridge this gap, we study the problem of computing safe trajectories for human-piloted parafoil flight and examine how such trajectories fare against human-generated solutions. For the algorithmic part, we adapt the sampling-based motion planner Stable Sparse RRT (SST) by Li et al., to cope with the problem constraints while minimizing the bank angle (control effort) as a proxy for safety. We then compare the computer-generated solutions with data from human-generated parafoil flight, where the algorithm offers a relative cost improvement of 20\%-80\% over the performance of the human pilot. We observe that human pilots tend to, first, close the horizontal distance to the landing area, and then address the vertical gap by spiraling down to the suitable altitude for starting a landing maneuver. The algorithm considered here makes smoother and more gradual descents, arriving at the landing area at the precise altitude necessary for the final approach while maintaining safety constraints. Overall, the study demonstrates the potential of computer-generated guidelines, rather than traditional rules of thumb, which can be integrated into future simulators to train pilots for safer and more cost-effective flights.

