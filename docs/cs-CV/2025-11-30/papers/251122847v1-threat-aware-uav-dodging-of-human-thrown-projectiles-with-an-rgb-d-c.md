---
layout: default
title: Threat-Aware UAV Dodging of Human-Thrown Projectiles with an RGB-D Camera
---

# Threat-Aware UAV Dodging of Human-Thrown Projectiles with an RGB-D Camera

**arXiv**: [2511.22847v1](https://arxiv.org/abs/2511.22847) | [PDF](https://arxiv.org/pdf/2511.22847.pdf)

**作者**: Yuying Zhang, Na Fan, Haowen Zheng, Junning Liang, Zongliang Pan, Qifeng Chen, Ximin Lyu

---

## 💡 一句话要点

**提出基于RGB-D相机的人类姿态估计与不确定性感知策略，实现无人机实时躲避投掷物攻击**

**关键词**: `无人机躲避` `RGB-D相机` `人类姿态估计` `轨迹预测` `不确定性感知` `实时系统`

## 📋 核心要点

1. 核心问题：无人机在运输等任务中易受人类投掷物攻击，需超低延迟响应和敏捷机动以躲避。
2. 方法要点：结合RGB-D相机，通过人类姿态估计和深度信息预测攻击者及投掷物轨迹，引入不确定性感知躲避策略。
3. 实验或效果：真实世界实验显示系统具有高预测精度、低延迟和强鲁棒性，有效确保无人机安全。

## 📄 摘要（原文）

> Uncrewed aerial vehicles (UAVs) performing tasks such as transportation and aerial photography are vulnerable to intentional projectile attacks from humans. Dodging such a sudden and fast projectile poses a significant challenge for UAVs, requiring ultra-low latency responses and agile maneuvers. Drawing inspiration from baseball, in which pitchers' body movements are analyzed to predict the ball's trajectory, we propose a novel real-time dodging system that leverages an RGB-D camera. Our approach integrates human pose estimation with depth information to predict the attacker's motion trajectory and the subsequent projectile trajectory. Additionally, we introduce an uncertainty-aware dodging strategy to enable the UAV to dodge incoming projectiles efficiently. Our perception system achieves high prediction accuracy and outperforms the baseline in effective distance and latency. The dodging strategy addresses temporal and spatial uncertainties to ensure UAV safety. Extensive real-world experiments demonstrate the framework's reliable dodging capabilities against sudden attacks and its outstanding robustness across diverse scenarios.

