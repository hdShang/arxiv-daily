---
layout: default
title: SPIDER: Scalable Physics-Informed Dexterous Retargeting
---

# SPIDER: Scalable Physics-Informed Dexterous Retargeting

**arXiv**: [2511.09484v1](https://arxiv.org/abs/2511.09484) | [PDF](https://arxiv.org/pdf/2511.09484.pdf)

**作者**: Chaoyi Pan, Changhao Wang, Haozhi Qi, Zixi Liu, Homanga Bharadhwaj, Akash Sharma, Tingfan Wu, Guanya Shi, Jitendra Malik, Francois Hogan

---

## 💡 一句话要点

**提出SPIDER框架以将人类运动数据转化为机器人动态可行轨迹**

**关键词**: `物理信息重定向` `灵巧手控制` `运动数据转换` `动态可行性` `机器人学习`

## 📋 核心要点

1. 核心问题：人类运动数据因体现差异和缺失动态信息无法直接用于机器人控制
2. 方法要点：基于物理模拟和课程式虚拟接触指导，大规模采样优化轨迹
3. 实验或效果：在9种机器人上提升成功率18%，生成240万帧数据集

## 📄 摘要（原文）

> Learning dexterous and agile policy for humanoid and dexterous hand control requires large-scale demonstrations, but collecting robot-specific data is prohibitively expensive. In contrast, abundant human motion data is readily available from motion capture, videos, and virtual reality, which could help address the data scarcity problem. However, due to the embodiment gap and missing dynamic information like force and torque, these demonstrations cannot be directly executed on robots. To bridge this gap, we propose Scalable Physics-Informed DExterous Retargeting (SPIDER), a physics-based retargeting framework to transform and augment kinematic-only human demonstrations to dynamically feasible robot trajectories at scale. Our key insight is that human demonstrations should provide global task structure and objective, while large-scale physics-based sampling with curriculum-style virtual contact guidance should refine trajectories to ensure dynamical feasibility and correct contact sequences. SPIDER scales across diverse 9 humanoid/dexterous hand embodiments and 6 datasets, improving success rates by 18% compared to standard sampling, while being 10X faster than reinforcement learning (RL) baselines, and enabling the generation of a 2.4M frames dynamic-feasible robot dataset for policy learning. As a universal physics-based retargeting method, SPIDER can work with diverse quality data and generate diverse and high-quality data to enable efficient policy learning with methods like RL.

