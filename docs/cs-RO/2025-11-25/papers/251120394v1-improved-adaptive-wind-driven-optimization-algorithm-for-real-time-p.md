---
layout: default
title: Improved adaptive wind driven optimization algorithm for real-time path planning
---

# Improved adaptive wind driven optimization algorithm for real-time path planning

**arXiv**: [2511.20394v1](https://arxiv.org/abs/2511.20394) | [PDF](https://arxiv.org/pdf/2511.20394.pdf)

**作者**: Shiqian Liu, Azlan Mohd Zain, Le-le Mao

---

## 💡 一句话要点

**提出多层级自适应风驱动优化算法以提升动态环境中实时路径规划的适应性和鲁棒性**

**关键词**: `路径规划` `风驱动优化` `自适应算法` `实时导航` `优化算法` `动态环境`

## 📋 核心要点

1. 动态环境中实时路径规划存在适应性和鲁棒性不足的核心问题
2. 基于风驱动优化框架引入多层级引导机制平衡探索与利用
3. 在基准函数和路径规划实验中显示优化精度和轨迹平滑度显著提升

## 📄 摘要（原文）

> Recently, path planning has achieved remarkable progress in enhancing global search capability and convergence accuracy through heuristic and learning-inspired optimization frameworks. However, real-time adaptability in dynamic environments remains a critical challenge for autonomous navigation, particularly when robots must generate collision-free, smooth, and efficient trajectories under complex constraints. By analyzing the difficulties in dynamic path planning, the Wind Driven Optimization (WDO) algorithm emerges as a promising framework owing to its physically interpretable search dynamics. Motivated by these observations, this work revisits the WDO principle and proposes a variant formulation, Multi-hierarchical adaptive wind driven optimization(MAWDO), that improves adaptability and robustness in time-varying environments. To mitigate instability and premature convergence, a hierarchical-guidance mechanism divides the population into multiple groups guided by individual, regional, and global leaders to balance exploration and exploitation. Extensive evaluations on sixteen benchmark functions show that MAWDO achieves superior optimization accuracy, convergence stability, and adaptability over state-of-the art metaheuristics. In dynamic path planning, MAWDO shortens the path length to 469.28 pixels, improving over Multi-strategy ensemble wind driven optimization(MEWDO), Adaptive wind driven optimization(AWDO) and WDO by 3.51\%, 11.63\% and 14.93\%, and achieves the smallest optimality gap (1.01) with smoothness 0.71 versus 13.50 and 15.67 for AWDO and WDO, leading to smoother, shorter, and collision-free trajectories that confirm its effectiveness for real-time path planning in complex environments.

