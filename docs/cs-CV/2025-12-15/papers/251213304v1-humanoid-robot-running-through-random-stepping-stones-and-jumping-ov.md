---
layout: default
title: Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories
---

# Humanoid Robot Running Through Random Stepping Stones and Jumping Over Obstacles: Step Adaptation Using Spring-Mass Trajectories

**arXiv**: [2512.13304v1](https://arxiv.org/abs/2512.13304) | [PDF](https://arxiv.org/pdf/2512.13304.pdf)

**作者**: Sait Sovukluk, Johannes Englsberger, Christian Ott

---

## 💡 一句话要点

**提出基于弹簧质量轨迹的步态适应框架，实现人形机器人随机踏石与跳跃障碍的敏捷运动。**

**关键词**: `人形机器人控制` `步态适应` `弹簧质量模型` `全身控制` `鲁棒性验证` `动态环境模拟`

## 📋 核心要点

1. 核心问题：人形机器人在动态环境中（如随机踏石、跳跃障碍）的步态适应与鲁棒控制。
2. 方法要点：自动生成弹簧质量轨迹库和死拍控制增益库，结合轨迹选择策略和全身控制框架映射。
3. 实验或效果：在MuJoCo模拟器中验证了多种敏捷行为的鲁棒性，包括抗干扰和不确定性，无需额外调参。

## 📄 摘要（原文）

> This study proposes a step adaptation framework for running through spring-mass trajectories and deadbeat control gain libraries. It includes four main parts: (1) Automatic spring-mass trajectory library generation; (2) Deadbeat control gain library generation through an actively controlled template model that resembles the whole-body dynamics well; (3) Trajectory selection policy development for step adaptation; (4) Mapping spring-mass trajectories to a humanoid model through a whole-body control (WBC) framework also accounting for closed-kinematic chain systems, self collisions, and reactive limb swinging. We show the inclusiveness and the robustness of the proposed framework through various challenging and agile behaviors such as running through randomly generated stepping stones, jumping over random obstacles, performing slalom motions, changing the running direction suddenly with a random leg, and rejecting significant disturbances and uncertainties through the MuJoCo physics simulator. We also perform additional simulations under a comprehensive set of uncertainties and noise to better justify the proposed method's robustness to real-world challenges, including signal noise, imprecision, modeling errors, and delays. All the aforementioned behaviors are performed with a single library and the same set of WBC control parameters without additional tuning. The spring-mass and the deadbeat control gain library are automatically computed in 4.5 seconds in total for 315 different trajectories.

