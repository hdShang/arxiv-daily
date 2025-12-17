---
layout: default
title: REASAN: Learning Reactive Safe Navigation for Legged Robots
---

# REASAN: Learning Reactive Safe Navigation for Legged Robots

**arXiv**: [2512.09537v1](https://arxiv.org/abs/2512.09537) | [PDF](https://arxiv.org/pdf/2512.09537.pdf)

**作者**: Qihao Yuan, Ziyu Cao, Ming Cao, Kailai Li

---

## 💡 一句话要点

**提出REASAN框架，用于足式机器人在复杂动态环境中的反应式安全导航。**

**关键词**: `足式机器人导航` `反应式安全导航` `强化学习策略` `模块化框架` `LiDAR传感器` `实时系统`

## 📋 核心要点

1. 核心问题：足式机器人在复杂动态环境中实现反应式安全导航的挑战。
2. 方法要点：采用模块化端到端框架，结合强化学习策略和基于Transformer的外部感知估计器。
3. 实验或效果：在单/多机器人设置中实现全机载实时导航，并通过消融实验验证鲁棒性提升。

## 📄 摘要（原文）

> We present a novel modularized end-to-end framework for legged reactive navigation in complex dynamic environments using a single light detection and ranging (LiDAR) sensor. The system comprises four simulation-trained modules: three reinforcement-learning (RL) policies for locomotion, safety shielding, and navigation, and a transformer-based exteroceptive estimator that processes raw point-cloud inputs. This modular decomposition of complex legged motor-control tasks enables lightweight neural networks with simple architectures, trained using standard RL practices with targeted reward shaping and curriculum design, without reliance on heuristics or sophisticated policy-switching mechanisms. We conduct comprehensive ablations to validate our design choices and demonstrate improved robustness compared to existing approaches in challenging navigation tasks. The resulting reactive safe navigation (REASAN) system achieves fully onboard and real-time reactive navigation across both single- and multi-robot settings in complex environments. We release our training and deployment code at https://github.com/ASIG-X/REASAN.

