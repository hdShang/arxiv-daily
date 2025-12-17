---
layout: default
title: Flow-Aided Flight Through Dynamic Clutters From Point To Motion
---

# Flow-Aided Flight Through Dynamic Clutters From Point To Motion

**arXiv**: [2511.16372v1](https://arxiv.org/abs/2511.16372) | [PDF](https://arxiv.org/pdf/2511.16372.pdf)

**作者**: Bowen Xu, Zexuan Yan, Minghao Lu, Xiyu Fan, Yi Luo, Youshen Lin, Zhiqiang Chen, Yeke Chen, Qiyuan Qiao, Peng Lu

---

## 💡 一句话要点

**提出基于点流与强化学习的无人机动态障碍规避系统，实现从点云到动作的自主飞行。**

**关键词**: `动态障碍规避` `强化学习` `点云处理` `无人机控制` `环境感知`

## 📋 核心要点

1. 核心问题：动态环境中障碍物运动感知与规避行为生成效率低、不可靠。
2. 方法要点：使用LiDAR点云编码深度图与点流，结合强化学习隐式驱动规避策略。
3. 实验或效果：在仿真与真实四旋翼上展示高成功率与适应性，实现安全机动。

## 📄 摘要（原文）

> Challenges in traversing dynamic clutters lie mainly in the efficient perception of the environmental dynamics and the generation of evasive behaviors considering obstacle movement. Previous solutions have made progress in explicitly modeling the dynamic obstacle motion for avoidance, but this key dependency of decision-making is time-consuming and unreliable in highly dynamic scenarios with occlusions. On the contrary, without introducing object detection, tracking, and prediction, we empower the reinforcement learning (RL) with single LiDAR sensing to realize an autonomous flight system directly from point to motion. For exteroception, a depth sensing distance map achieving fixed-shape, low-resolution, and detail-safe is encoded from raw point clouds, and an environment change sensing point flow is adopted as motion features extracted from multi-frame observations. These two are integrated into a lightweight and easy-to-learn representation of complex dynamic environments. For action generation, the behavior of avoiding dynamic threats in advance is implicitly driven by the proposed change-aware sensing representation, where the policy optimization is indicated by the relative motion modulated distance field. With the deployment-friendly sensing simulation and dynamics model-free acceleration control, the proposed system shows a superior success rate and adaptability to alternatives, and the policy derived from the simulator can drive a real-world quadrotor with safe maneuvers.

