---
layout: default
title: Global-State-Free Obstacle Avoidance for Quadrotor Control in Air-Ground Cooperation
---

# Global-State-Free Obstacle Avoidance for Quadrotor Control in Air-Ground Cooperation

**arXiv**: [2510.24315v1](https://arxiv.org/abs/2510.24315) | [PDF](https://arxiv.org/pdf/2510.24315.pdf)

**作者**: Baozhe Zhang, Xinwei Chen, Qingcheng Chen, Chao Xu, Fei Gao, Yanjun Cao

---

## 💡 一句话要点

**提出CoNi-OA算法以解决无人机在空地协作中的无全局状态避障问题**

**关键词**: `无人机避障` `空地协作` `非惯性框架` `LiDAR调制` `实时轨迹生成`

## 📋 核心要点

1. 核心问题：CoNi-MPC框架缺乏环境信息，难以实现无人机在动态环境中的避障
2. 方法要点：利用单帧LiDAR数据生成调制矩阵，直接调整无人机速度实现实时避障
3. 实验或效果：计算时间低于5毫秒/迭代，适应静态和动态环境，提升安全性

## 📄 摘要（原文）

> CoNi-MPC provides an efficient framework for UAV control in air-ground
> cooperative tasks by relying exclusively on relative states, eliminating the
> need for global state estimation. However, its lack of environmental
> information poses significant challenges for obstacle avoidance. To address
> this issue, we propose a novel obstacle avoidance algorithm, Cooperative
> Non-inertial frame-based Obstacle Avoidance (CoNi-OA), designed explicitly for
> UAV-UGV cooperative scenarios without reliance on global state estimation or
> obstacle prediction. CoNi-OA uniquely utilizes a single frame of raw LiDAR data
> from the UAV to generate a modulation matrix, which directly adjusts the
> quadrotor's velocity to achieve obstacle avoidance. This modulation-based
> method enables real-time generation of collision-free trajectories within the
> UGV's non-inertial frame, significantly reducing computational demands (less
> than 5 ms per iteration) while maintaining safety in dynamic and unpredictable
> environments. The key contributions of this work include: (1) a
> modulation-based obstacle avoidance algorithm specifically tailored for UAV-UGV
> cooperation in non-inertial frames without global states; (2) rapid, real-time
> trajectory generation based solely on single-frame LiDAR data, removing the
> need for obstacle modeling or prediction; and (3) adaptability to both static
> and dynamic environments, thus extending applicability to featureless or
> unknown scenarios.

