---
layout: default
title: Implicit State Estimation via Video Replanning
---

# Implicit State Estimation via Video Replanning

**arXiv**: [2510.17315v1](https://arxiv.org/abs/2510.17315) | [PDF](https://arxiv.org/pdf/2510.17315.pdf)

**作者**: Po-Chen Ko, Jiayuan Mao, Yu-Hsiang Fu, Hsien-Jeng Yeh, Chu-Rong Chen, Wei-Chiu Ma, Yilun Du, Shao-Hua Sun

---

## 💡 一句话要点

**提出视频重规划框架以解决部分观测环境中的不确定性适应问题**

**关键词**: `视频规划` `隐式状态估计` `在线学习` `重规划` `模拟操作`

## 📋 核心要点

1. 核心问题：视频规划框架难以适应交互失败，因无法推理部分观测环境的不确定性
2. 方法要点：在线更新模型参数并过滤失败计划，实现隐式状态估计
3. 实验或效果：在模拟操作基准上验证，提升重规划性能和视频决策能力

## 📄 摘要（原文）

> Video-based representations have gained prominence in planning and
> decision-making due to their ability to encode rich spatiotemporal dynamics and
> geometric relationships. These representations enable flexible and
> generalizable solutions for complex tasks such as object manipulation and
> navigation. However, existing video planning frameworks often struggle to adapt
> to failures at interaction time due to their inability to reason about
> uncertainties in partially observed environments. To overcome these
> limitations, we introduce a novel framework that integrates interaction-time
> data into the planning process. Our approach updates model parameters online
> and filters out previously failed plans during generation. This enables
> implicit state estimation, allowing the system to adapt dynamically without
> explicitly modeling unknown state variables. We evaluate our framework through
> extensive experiments on a new simulated manipulation benchmark, demonstrating
> its ability to improve replanning performance and advance the field of
> video-based decision-making.

