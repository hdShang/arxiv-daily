---
layout: default
title: High-Altitude Balloon Station-Keeping with First Order Model Predictive Control
---

# High-Altitude Balloon Station-Keeping with First Order Model Predictive Control

**arXiv**: [2511.07761v1](https://arxiv.org/abs/2511.07761) | [PDF](https://arxiv.org/pdf/2511.07761.pdf)

**作者**: Myles Pasetsky, Jiawei Lin, Bradley Guo, Sarah Dean

---

## 💡 一句话要点

**提出一阶模型预测控制以解决高空气球定点保持问题**

**关键词**: `高空气球控制` `模型预测控制` `可微分优化` `在线规划` `风场建模`

## 📋 核心要点

1. 高空气球非线性、欠驱动且风场部分可观测，传统方法依赖无模型强化学习
2. 开发一阶模型预测控制，使用JAX实现可微分风与气球动力学，支持在线梯度优化
3. 实验显示优于强化学习策略，时间在半径内指标提升24%，但在线计算成本较高

## 📄 摘要（原文）

> High-altitude balloons (HABs) are common in scientific research due to their wide range of applications and low cost. Because of their nonlinear, underactuated dynamics and the partial observability of wind fields, prior work has largely relied on model-free reinforcement learning (RL) methods to design near-optimal control schemes for station-keeping. These methods often compare only against hand-crafted heuristics, dismissing model-based approaches as impractical given the system complexity and uncertain wind forecasts. We revisit this assumption about the efficacy of model-based control for station-keeping by developing First-Order Model Predictive Control (FOMPC). By implementing the wind and balloon dynamics as differentiable functions in JAX, we enable gradient-based trajectory optimization for online planning. FOMPC outperforms a state-of-the-art RL policy, achieving a 24% improvement in time-within-radius (TWR) without requiring offline training, though at the cost of greater online computation per control step. Through systematic ablations of modeling assumptions and control factors, we show that online planning is effective across many configurations, including under simplified wind and dynamics models.

