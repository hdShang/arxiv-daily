---
layout: default
title: Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning
---

# Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning

**arXiv**: [2511.11218v1](https://arxiv.org/abs/2511.11218) | [PDF](https://arxiv.org/pdf/2511.11218.pdf)

**作者**: Chenhao Liu, Leyun Jiang, Yibo Wang, Kairan Yao, Jinchen Fu, Xiaoyu Ren

---

## 💡 一句话要点

**提出多阶段强化学习框架，实现人形机器人全身羽毛球动态击球**

**关键词**: `人形机器人控制` `多阶段强化学习` `全身协调` `羽毛球任务` `轨迹预测` `实时部署`

## 📋 核心要点

1. 核心问题：人形机器人在动态环境中难以协调全身动作进行羽毛球击球
2. 方法要点：采用三阶段课程学习，无运动先验，集成EKF预测羽毛球轨迹
3. 实验或效果：仿真中连续21次击球，真实世界击球速度达10m/s，精度高

## 📄 摘要（原文）

> Humanoid robots have demonstrated strong capability for interacting with deterministic scenes across locomotion, manipulation, and more challenging loco-manipulation tasks. Yet the real world is dynamic, quasi-static interactions are insufficient to cope with the various environmental conditions. As a step toward more dynamic interaction scenario, we present a reinforcement-learning-based training pipeline that produces a unified whole-body controller for humanoid badminton, enabling coordinated lower-body footwork and upper-body striking without any motion priors or expert demonstrations. Training follows a three-stage curriculum: first footwork acquisition, then precision-guided racket swing generation, and finally task-focused refinement, yielding motions in which both legs and arms serve the hitting objective. For deployment, we incorporate an Extended Kalman Filter (EKF) to estimate and predict shuttlecock trajectories for target striking. We also introduce a prediction-free variant that dispenses with EKF and explicit trajectory prediction. To validate the framework, we conduct five sets of experiment in both simulation and the real world. In simulation, two robots sustain a rally of 21 consecutive hits. Moreover, the prediction-free variant achieves successful hits with comparable performance relative to the target-known policy. In real-world tests, both the prediction and controller module exhibit high accuracy, and on-court hitting achieves an outgoing shuttle speed up to 10 m/s with a mean return landing distance of 3.5 m. These experiment results show that our humanoid robot can deliver highly dynamic while precise goal striking in badminton, and can be adapted to more dynamism critical domains.

