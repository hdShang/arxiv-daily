---
layout: default
title: Feasibility of Embodied Dynamics Based Bayesian Learning for Continuous Pursuit Motion Control of Assistive Mobile Robots in the Built Environment
---

# Feasibility of Embodied Dynamics Based Bayesian Learning for Continuous Pursuit Motion Control of Assistive Mobile Robots in the Built Environment

**arXiv**: [2511.17401v1](https://arxiv.org/abs/2511.17401) | [PDF](https://arxiv.org/pdf/2511.17401.pdf)

**作者**: Xiaoshan Zhou, Carol C. Menassa, Vineet R. Kamat

---

## 💡 一句话要点

**提出基于体现动力学的贝叶斯学习框架，实现脑机接口辅助移动机器人的连续追踪运动控制。**

**关键词**: `脑机接口` `连续运动控制` `贝叶斯推理` `体现动力学` `在线学习` `辅助机器人`

## 📋 核心要点

1. 核心问题：现有脑机接口运动控制系统多限于离散命令，缺乏实时连续速度与方向调整能力。
2. 方法要点：利用体现动力学解码加速度级运动表征，结合贝叶斯推理和在线学习优化控制。
3. 实验或效果：在公开数据集上，相比基线方法，归一化均方误差降低72%，验证了方法的有效性。

## 📄 摘要（原文）

> Non-invasive electroencephalography (EEG)-based brain-computer interfaces (BCIs) offer an intuitive means for individuals with severe motor impairments to independently operate assistive robotic wheelchairs and navigate built environments. Despite considerable progress in BCI research, most current motion control systems are limited to discrete commands, rather than supporting continuous pursuit, where users can freely adjust speed and direction in real time. Such natural mobility control is, however, essential for wheelchair users to navigate complex public spaces, such as transit stations, airports, hospitals, and indoor corridors, to interact socially with the dynamic populations with agility, and to move flexibly and comfortably as autonomous driving is refined to allow movement at will. In this study, we address the gap of continuous pursuit motion control in BCIs by proposing and validating a brain-inspired Bayesian inference framework, where embodied dynamics in acceleration-based motor representations are decoded. This approach contrasts with conventional kinematics-level decoding and deep learning-based methods. Using a public dataset with sixteen hours of EEG from four subjects performing motor imagery-based target-following, we demonstrate that our method, utilizing Automatic Relevance Determination for feature selection and continual online learning, reduces the normalized mean squared error between predicted and true velocities by 72% compared to autoregressive and EEGNet-based methods in a session-accumulative transfer learning setting. Theoretically, these findings empirically support embodied cognition theory and reveal the brain's intrinsic motor control dynamics in an embodied and predictive nature. Practically, grounding EEG decoding in the same dynamical principles that govern biological motion offers a promising path toward more stable and intuitive BCI control.

