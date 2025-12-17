---
layout: default
title: LODESTAR: Degeneracy-Aware LiDAR-Inertial Odometry with Adaptive Schmidt-Kalman Filter and Data Exploitation
---

# LODESTAR: Degeneracy-Aware LiDAR-Inertial Odometry with Adaptive Schmidt-Kalman Filter and Data Exploitation

**arXiv**: [2511.09142v1](https://arxiv.org/abs/2511.09142) | [PDF](https://arxiv.org/pdf/2511.09142.pdf)

**作者**: Eungchang Mason Lee, Kevin Christiansen Marsim, Hyun Myung

---

## 💡 一句话要点

**提出LODESTAR方法以解决LiDAR-惯性里程计在退化环境中的性能下降问题**

**关键词**: `LiDAR-惯性里程计` `退化环境` `Schmidt-Kalman滤波` `数据利用` `状态估计` `机器人导航`

## 📋 核心要点

1. 核心问题：LiDAR测量在退化环境（如长走廊）中不平衡或稀疏，导致状态估计病态
2. 方法要点：结合退化感知自适应Schmidt-Kalman滤波和数据利用，优化状态估计
3. 实验或效果：在多种退化条件下，精度和鲁棒性优于现有方法

## 📄 摘要（原文）

> LiDAR-inertial odometry (LIO) has been widely used in robotics due to its high accuracy. However, its performance degrades in degenerate environments, such as long corridors and high-altitude flights, where LiDAR measurements are imbalanced or sparse, leading to ill-posed state estimation. In this letter, we present LODESTAR, a novel LIO method that addresses these degeneracies through two key modules: degeneracy-aware adaptive Schmidt-Kalman filter (DA-ASKF) and degeneracy-aware data exploitation (DA-DE). DA-ASKF employs a sliding window to utilize past states and measurements as additional constraints. Specifically, it introduces degeneracy-aware sliding modes that adaptively classify states as active or fixed based on their degeneracy level. Using Schmidt-Kalman update, it partially optimizes active states while preserving fixed states. These fixed states influence the update of active states via their covariances, serving as reference anchors--akin to a lodestar. Additionally, DA-DE prunes less-informative measurements from active states and selectively exploits measurements from fixed states, based on their localizability contribution and the condition number of the Jacobian matrix. Consequently, DA-ASKF enables degeneracy-aware constrained optimization and mitigates measurement sparsity, while DA-DE addresses measurement imbalance. Experimental results show that LODESTAR outperforms existing LiDAR-based odometry methods and degeneracy-aware modules in terms of accuracy and robustness under various degenerate conditions.

