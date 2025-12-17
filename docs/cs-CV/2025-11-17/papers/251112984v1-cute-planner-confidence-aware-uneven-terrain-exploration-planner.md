---
layout: default
title: CUTE-Planner: Confidence-aware Uneven Terrain Exploration Planner
---

# CUTE-Planner: Confidence-aware Uneven Terrain Exploration Planner

**arXiv**: [2511.12984v1](https://arxiv.org/abs/2511.12984) | [PDF](https://arxiv.org/pdf/2511.12984.pdf)

**作者**: Miryeong Park, Dongjin Cho, Sanghyun Kim, Younggun Cho

---

## 💡 一句话要点

**提出CUTE-Planner框架以提升行星机器人在崎岖地形中的探索安全性和地图可靠性**

**关键词**: `行星探索机器人` `崎岖地形导航` `置信度感知规划` `卡尔曼滤波估计` `图基探索规划` `不确定性减少`

## 📋 核心要点

1. 核心问题：现有方法难以处理高程估计不确定性，影响导航安全和地图质量
2. 方法要点：集成安全路径生成、自适应置信度更新和置信感知探索策略
3. 实验或效果：在模拟月球实验中，不确定性降低69%，任务成功率从0%提升至100%

## 📄 摘要（原文）

> Planetary exploration robots must navigate uneven terrain while building reliable maps for space missions. However, most existing methods incorporate traversability constraints but may not handle high uncertainty in elevation estimates near complex features like craters, do not consider exploration strategies for uncertainty reduction, and typically fail to address how elevation uncertainty affects navigation safety and map quality. To address the problems, we propose a framework integrating safe path generation, adaptive confidence updates, and confidence-aware exploration strategies. Using Kalman-based elevation estimation, our approach generates terrain traversability and confidence scores, then incorporates them into Graph-Based exploration Planner (GBP) to prioritize exploration of traversable low-confidence regions. We evaluate our framework through simulated lunar experiments using a novel low-confidence region ratio metric, achieving 69% uncertainty reduction compared to baseline GBP. In terms of mission success rate, our method achieves 100% while baseline GBP achieves 0%, demonstrating improvements in exploration safety and map reliability.

