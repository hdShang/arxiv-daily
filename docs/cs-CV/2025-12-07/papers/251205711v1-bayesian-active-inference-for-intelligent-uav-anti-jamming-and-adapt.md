---
layout: default
title: Bayesian Active Inference for Intelligent UAV Anti-Jamming and Adaptive Trajectory Planning
---

# Bayesian Active Inference for Intelligent UAV Anti-Jamming and Adaptive Trajectory Planning

**arXiv**: [2512.05711v1](https://arxiv.org/abs/2512.05711) | [PDF](https://arxiv.org/pdf/2512.05711.pdf)

**作者**: Ali Krayani, Seyedeh Fatemeh Sadati, Lucio Marcenaro, Carlo Regazzoni

---

## 💡 一句话要点

**提出基于贝叶斯主动推理的分层轨迹规划框架，以解决无人机在对抗性干扰下的自适应飞行问题。**

**关键词**: `无人机轨迹规划` `贝叶斯主动推理` `对抗性干扰` `分层控制` `在线自适应` `概率生成模型`

## 📋 核心要点

1. 核心问题：无人机在未知干扰源位置下，需在线适应轨迹以降低通信干扰和任务成本。
2. 方法要点：结合专家演示与概率生成模型，编码符号规划、运动策略和无线信号反馈，实现干扰预测和定位。
3. 实验或效果：仿真显示，相比无模型强化学习基线，该方法性能接近专家，显著减少干扰并保持动态环境中的鲁棒泛化。

## 📄 摘要（原文）

> This paper proposes a hierarchical trajectory planning framework for UAVs operating under adversarial jamming conditions. Leveraging Bayesian Active Inference, the approach combines expert-generated demonstrations with probabilistic generative modeling to encode high-level symbolic planning, low-level motion policies, and wireless signal feedback. During deployment, the UAV performs online inference to anticipate interference, localize jammers, and adapt its trajectory accordingly, without prior knowledge of jammer locations. Simulation results demonstrate that the proposed method achieves near-expert performance, significantly reducing communication interference and mission cost compared to model-free reinforcement learning baselines, while maintaining robust generalization in dynamic environments.

