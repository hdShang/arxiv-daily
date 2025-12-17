---
layout: default
title: Delay-Aware Diffusion Policy: Bridging the Observation-Execution Gap in Dynamic Tasks
---

# Delay-Aware Diffusion Policy: Bridging the Observation-Execution Gap in Dynamic Tasks

**arXiv**: [2512.07697v1](https://arxiv.org/abs/2512.07697) | [PDF](https://arxiv.org/pdf/2512.07697.pdf)

**作者**: Aileen Liao, Dong-Ki Kim, Max Olan Smith, Ali-akbar Agha-mohammadi, Shayegan Omidshafiei

---

## 💡 一句话要点

**提出延迟感知扩散策略以解决机器人动态任务中的观测-执行延迟问题**

**关键词**: `延迟感知策略` `扩散模型` `模仿学习` `机器人控制` `动态任务`

## 📋 核心要点

1. 核心问题：机器人感知与动作选择间的延迟导致观测状态与执行状态不匹配，影响任务性能。
2. 方法要点：通过延迟补偿轨迹和延迟条件增强，将推理延迟显式纳入策略学习框架。
3. 实验或效果：在多种任务、机器人和延迟下验证，相比无延迟方法，成功率对延迟更鲁棒。

## 📄 摘要（原文）

> As a robot senses and selects actions, the world keeps changing. This inference delay creates a gap of tens to hundreds of milliseconds between the observed state and the state at execution. In this work, we take the natural generalization from zero delay to measured delay during training and inference. We introduce Delay-Aware Diffusion Policy (DA-DP), a framework for explicitly incorporating inference delays into policy learning. DA-DP corrects zero-delay trajectories to their delay-compensated counterparts, and augments the policy with delay conditioning. We empirically validate DA-DP on a variety of tasks, robots, and delays and find its success rate more robust to delay than delay-unaware methods. DA-DP is architecture agnostic and transfers beyond diffusion policies, offering a general pattern for delay-aware imitation learning. More broadly, DA-DP encourages evaluation protocols that report performance as a function of measured latency, not just task difficulty.

